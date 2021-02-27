#! /bin/bash
# https://superuser.com/a/1209701

echo "Drive Setup"
if [[ -d "/mnt/e/2021" ]]; then
  echo "Drive already mounted"
else
  sudo mkdir -p /mnt/e
  sudo mount -t drvfs E: /mnt/e
fi

sudo ./organize-photos.py /mnt/e/Queue
