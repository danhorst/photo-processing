#! /bin/bash
# https://superuser.com/a/1209701

sudo mkdir /mnt/e
sudo mount -t drvfs E: /mnt/e

./organize-photos.py /mnt/e/DCIM/101CANON

sudo umount /mnt/e
