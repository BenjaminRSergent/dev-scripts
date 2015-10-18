#!/bin/bash

#Repositories
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
sudo apt-get -y install clang-3.5
sudo apt-get -y install clang++-3.5
sudo apt-get -y install cmake cmake-gui

#Dev Other 
sudo apt-get -y install liblog4cxx10 liblog4cxx10-dev
sudo apt-get -y install gource

#Graphics and CV
sudo apt-get -y install libglfw-dev
sudo apt-get -y install libglew-dev
sudo apt-get -y install libopencv-dev
sudo apt-get -y install binutils-gold
sudo apt-get -y install freeglut3 freeglut3-dev
sudo sh install_glfw.sh
sudo sh install_png16.sh

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
