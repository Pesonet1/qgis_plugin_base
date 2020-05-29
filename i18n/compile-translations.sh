#!/bin/bash

echo "Compiling fi.ts into fi.qm"
./lrelease.exe fi.ts -qm ./fi.qm


echo "Compiling en.ts into en.qm"
./lrelease.exe en.ts -qm ./en.qm
