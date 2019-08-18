#!/bin/bash

# 1. Delete files in the pareent directory: /pythainlp/tutorials/*.*

for f in `curl --list-only --ipv4 ftp://${FTP_USER}:${FTP_PASSWORD}@thainlp.org/public_html/pythainlp/tutorials/`; do
  # Delete each file individually
  echo "deleting: $f"
  curl --ipv4 ftp://${FTP_USER}:${FTP_PASSWORD}@thainlp.org -Q "DELE -r public_html/pythainlp/tutorials/$f"
done

# 2. Delete files in the sub directories: notebooks, _images, _sources, _static

SUB_DIRECTORIES=(notebooks _images _sources _static)

for directory in ${SUB_DIRECTORIES[*]}; do
  echo "delete files in: $directory"
  for f in `curl --list-only --ipv4 ftp://${FTP_USER}:${FTP_PASSWORD}@thainlp.org/public_html/pythainlp/tutorials/$directory/`; do
    echo "-- deleting: $f"
    curl --ipv4 ftp://${FTP_USER}:${FTP_PASSWORD}@thainlp.org -Q "DELE public_html/pythainlp/tutorials/$directory/$f"
  done
done