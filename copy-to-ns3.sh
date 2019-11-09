#!/bin/bash

# Configure the following values
RAPIDJSON_FOLDER=~/codes/rapidjson
NS3_FOLDER=~/codes/ns-allinone-3.30.1/ns-3.30.1

# Do not change
rm -r $NS3_FOLDER/rapidjson
mkdir $NS3_FOLDER/rapidjson
cp  -r $RAPIDJSON_FOLDER/include/rapidjson/* $NS3_FOLDER/rapidjson/
cp  -f src/applications/model/* $NS3_FOLDER/src/applications/model/
cp  -f src/applications/helper/* $NS3_FOLDER/src/applications/helper/
cp  -f src/internet/helper/* $NS3_FOLDER/src/internet/helper/
cp  -f scratch/* $NS3_FOLDER/scratch/
