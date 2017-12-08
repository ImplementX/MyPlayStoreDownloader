#!/bin/bash
cd /data/tools/nginx/html/PlaystoreDownloader-master/
python3 ./test.py >> /data/tools/nginx/html/PlaystoreDownloader-master/log/$(date -d "today" +"%Y%m%d_%H").log 2>&1 
