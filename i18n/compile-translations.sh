#!/bin/bash

echo "Processing: fi.ts"
./lrelease.exe fi.ts -qm ./fi.qm


echo "Processing: en.ts"
./lrelease.exe en.ts -qm ./en.qm
