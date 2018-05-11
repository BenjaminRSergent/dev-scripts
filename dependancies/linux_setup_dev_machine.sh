#!/bin/bash

#Repositories
sudo apt -y autoclean

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

#Get list and update
sudo apt -y update
sudo apt -y upgrade

#dev tools
sudo apt -y install build-essential
sudo apt -y install software-properties-common
sudo apt -y install gcc g++ cpp
sudo apt -y install clang
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
sudo apt -y install ccache
sudo apt -y install valgrind
sudo apt -y install massif-visualizer
sudo apt -y install clang-format
sudo apt -y install clang-tidy

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

#The commented packages are for personal machines
#IDEs and Text Editors
sudo snap install pycharm-community --classic
sudo apt -y install sublime-text
sudo apt -y install netbeans

#Media Editing
#sudo apt -y install handbrake
#sudo apt -y install gimp gimp-data gimp-plugin-registry gimp-data-extras
#sudo apt -y install audacity

#Entertainment
#sudo apt -y install steam
#sudo apt -y install vlc browser-plugin-vlc
