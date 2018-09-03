#! /bin/bash
# https://superuser.com/a/1209701

sudo mkdir /mnt/e
sudo mount -t drvfs E: /mnt/e

./organize-photos.py

sudo umount /mnt/e
