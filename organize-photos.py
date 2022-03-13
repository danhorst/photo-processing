#!/usr/bin/python

import sys
import os, shutil
import subprocess
import os.path
from datetime import datetime

######################## Functions #########################

def photoDate(f):
  "Return the date/time on which the given photo was taken."

  exifOutput = subprocess.check_output(['exiftool', '-args', '-CreateDate', f])
  exifString = exifOutput.rstrip().decode('UTF-8')
  cDate = exifString.split('=')[1]
  sys.stdout.write('\nDate photo was taken: %s' % cDate)
  return datetime.strptime(cDate, "%Y:%m:%d %H:%M:%S")


###################### Main program ########################

# Where the photos are and where they're going.
destDir = 'D:\\'

if len(sys.argv) == 2:
  sourceDir = sys.argv[1]
else:
  sourceDir = os.path.join(destDir, '/Queue')

errorDir = os.path.join(destDir, '/Unsorted')

sys.stdout.write('\nProcessing photos from %s' % sourceDir)

# The format for the new file names.
fmt = "%Y-%m-%d--%H-%M-%S-"

# The problem files.
problems = []

# Get all the photos in the source folder.
photos = os.listdir(sourceDir)
photos = [ x for x in photos if x[-4:] == '.jpg' or x[-4:] == '.JPG' or x[-4:] == '.cr2' or x[-4:] == '.CR2' or x[-4:] == '.raf' or x[-4:] == '.RAF']
sys.stdout.write('\nFiles found: %d' % len(photos))

# Prepare to output as processing occurs
lastMonth = 0
lastYear = 0

# Create the destination folder if necessary
if not os.path.exists(destDir):
  os.makedirs(destDir)
if not os.path.exists(errorDir):
  os.makedirs(errorDir)

# Copy photos into year and month subfolders. Name the copies according to
# their timestamps and the original filename.
for photo in photos:
  sys.stdout.write('\nProcessing %s...' % photo)
  original = os.path.join(sourceDir, photo)
  sys.stdout.write('\nOriginal file: %s' % original)
  try:
    pDate = photoDate(original)
    yr = pDate.year
    mo = pDate.month

    if not lastYear == yr or not lastMonth == mo:
      sys.stdout.write('\nProcessing %04d-%02d...' % (yr, mo))
      lastMonth = mo
      lastYear = yr
    else:
      sys.stdout.write('.')

    newname = pDate.strftime(fmt) + photo
    thisDestDir = os.path.join(destDir, '%04d' % yr, '%02d' % mo)
    sys.stdout.write('\nDestination directory: %s' % thisDestDir)
    if not os.path.exists(thisDestDir):
      os.makedirs(thisDestDir)

    duplicate = os.path.join(thisDestDir, '%s' % (newname))
    if os.path.isfile(duplicate):
      sys.stdout.write('\nSkipping %s file already exists\n' % (duplicate))
    else:
      shutil.copy2(original, duplicate)
  except Exception as e:
    sys.stdout.write('\nError processing %s\n' % original)
    sys.stdout.write(getattr(e, 'message', repr(e)))
    shutil.copy2(original, os.path.join(errorDir, photo))
    problems.append(photo)
  except:
    sys.exit("Execution stopped.")

# Report the problem files, if any.
if len(problems) > 0:
  sys.stdout.write('\nProblem files:')
  sys.stdout.write('\n'.join(problems))
  sys.stdout.write('These can be found in: %s' % errorDir)
