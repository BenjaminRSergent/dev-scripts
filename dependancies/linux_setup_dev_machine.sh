#!/bin/bash

#Repositories
sudo apt -y autoclean
sudo wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add -
DIST=`lsb_release -c | cut -f2`
sudo apt-add-repository -y "deb http://llvm.org/apt/$DIST/ llvm-toolchain-$DIST main"

sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo add-apt-repository -y ppa:george-edison55/cmake-3.x
sudo add-apt-repository -y ppa:mystic-mirage/pycharm
sudo add-apt-repository -y ppa:webupd8team/sublime-text-3

#Get list and update
sudo apt -y update
sudo apt -y upgrade

#dev tools
sudo apt -y install nautilus-open-terminal
sudo apt -y install build-essential
sudo apt -y install software-properties-common
sudo apt -y install gcc g++ cpp
sudo apt -y install clang-3.8 clang++-3.8 libclang1-3.8 libllvm3.8 lldb-3.8 llvm-3.8 llvm-3.8-runtime 
sudo apt -y install cmake cmake-gui
sudo apt -y install libc++1
sudo apt -y install multiarch-support
sudo apt -y install libc6
sudo apt -y install libc++-helpers
sudo apt -y install libc++abi1
sudo apt -y install libtbb2
sudo apt -y install libiomp5
sudo apt -y install libc++-helpers
sudo apt -y install openssh-server 

#Dev Other 
sudo apt -y install liblog4cxx10 liblog4cxx10-dev
sudo apt -y install libgoogle-glog-dev
sudo apt -y install gource
sudo apt -y install zlib1g
sudo apt -y install libusb-1.0-0
sudo apt -y install lm-sensors
sudo apt -y install rapidjson-dev

#Graphics and CV
sudo apt -y install libglfw3-dev
sudo apt -y install libglm-dev
sudo apt -y install qtdeclarative5-dev
sudo apt -y install libglew-dev
sudo apt -y install libopencv-dev
sudo apt -y install binutils-gold
sudo apt -y install freeglut3 freeglut3-dev
sudo apt -y install libassimp-dev
sudo apt -y install opencl-headers
sudo apt -y install libpng12-dev
sudo apt -y install libavcodec-dev 
sudo apt -y install libavformat-dev 
sudo apt -y install libswscale-dev

#Python libs
sudo apt -y install python-pip
sudo apt -y install python-numpy
sudo apt -y install python-scipy
sudo apt -y install python-pandas
sudo apt -y install python-matplotlib
sudo apt -y install python-pygraph 
sudo apt -y install python-pygraphviz
sudo apt -y install python-pygame

#IDEs and Text Editors
sudo apt -y install netbeans
sudo apt -y install pycharm
sudo apt -y install sublime-text-installer

#Media Editing
sudo apt -y install handbrake
sudo apt -y install gimp gimp-data gimp-plugin-registry gimp-data-extras
sudo apt -y install audacity

#Entertainment
sudo apt -y install steam
sudo apt -y install vlc browser-plugin-vlc
