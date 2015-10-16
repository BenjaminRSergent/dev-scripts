#!/bin/bash
mkdir tmp_glfw
cd tmp_glfw
wget https://github.com/glfw/glfw/releases/download/3.1.1/glfw-3.1.1.zip
if [ ! -e glfw-3.1.1.zip];
then
    echo "Failed to download. Stopping"
    exit 1
fi
unzip glfw-3.1.1.zip -d glfw_src
cd glfw_src/glfw-3.1.1
cmake .
make
sudo make install
cd ../../
cd ..
rm -r tmp_glfw
