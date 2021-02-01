#! /bin/bash
# https://superuser.com/a/1209701

echo "SD Card Setup"
if [[ -d "/mnt/d/DCIM" ]]; then
  echo "SD Card already mounted"
else
  sudo mkdir -p /mnt/d
  sudo mount -t drvfs D: /mnt/d
fi

echo "Drive Setup"
if [[ -d "/mnt/f/2020" ]]; then
  echo "Drive already mounted"
else
  sudo mkdir -p /mnt/f
  sudo mount -t drvfs F: /mnt/f
fi

sudo ./organize-photos.py /mnt/d/DCIM/100CANON
