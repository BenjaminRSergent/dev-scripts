#!/bin/bash

#Repositories
sudo apt-get -y autoclean
sudo wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add -
DIST=`lsb_release -c | cut -f2`
sudo apt-add-repository -y "deb http://llvm.org/apt/$DIST/ llvm-toolchain-$DIST main"

sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo add-apt-repository -y ppa:george-edison55/cmake-3.x
sudo add-apt-repository -y ppa:mystic-mirage/pycharm
sudo add-apt-repository -y ppa:webupd8team/sublime-text-3

#Get list and update
sudo apt-get -y update
sudo apt-get -y upgrade

#dev tools
sudo apt-get -y install nautilus-open-terminal
sudo apt-get -y install build-essential
sudo apt-get -y install software-properties-common
sudo apt-get -y install gcc g++ cpp
sudo apt-get -y install clang
sudo apt-get -y install clang++
sudo apt-get -y install cmake cmake-gui

#Dev Other 
sudo apt-get -y install liblog4cxx10 liblog4cxx10-dev
sudo apt-get -y install libgoogle-glog-dev
sudo apt-get -y install gource

sudo apt-get -y install libc++1
sudo apt-get -y install multiarch-support
sudo apt-get -y install libc6
sudo apt-get -y install libc++-helpers
sudo apt-get -y install libc++abi1
sudo apt-get -y install cpp
sudo apt-get -y install libtbb2
sudo apt-get -y install zlib1g
sudo apt-get -y install libiomp5
sudo apt-get -y install libusb-1.0-0
sudo apt-get -y install cpp
sudo apt-get -y install libc++-helpers

#Graphics and CV
sudo apt-get -y install libglfw-dev
sudo apt-get -y install libglm-dev
sudo apt-get -y install qtdeclarative5-dev
sudo apt-get -y install libglew-dev
sudo apt-get -y install libopencv-dev
sudo apt-get -y install binutils-gold
sudo apt-get -y install freeglut3 freeglut3-dev
sudo apt-get -y install libassimp-dev
sudo apt-get -y install opencl-headers
sudo apt-get -y install libpng12-dev
sudo sh install_glfw.sh

#IDEs and Text Editors
sudo apt-get -y install netbeans
sudo apt-get -y install pycharm
sudo apt-get -y install sublime-text-installer

#Media Editing
sudo apt-get -y install handbrake
sudo apt-get -y install gimp gimp-data gimp-plugin-registry gimp-data-extras
sudo apt-get -y install audacity

#Entertainment
sudo apt-get -y install steam
sudo apt-get -y install vlc browser-plugin-vlc
