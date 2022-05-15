#!/bin/bash

rm -r ../space20/root/*
rm ../space20/package.json
rm ../space20/requirements.txt
cp -p requirements.txt package.json ../space20/
cp -pr * ../space20/root/
cd ..
cd space20
git add .
git commit -m "make it better"
heroku buildpacks:clear -a space20
git push heroku master
heroku run bash