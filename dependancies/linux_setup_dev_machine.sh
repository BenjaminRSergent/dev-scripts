#!/bin/bash

#Repositories
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo add-apt-repository ppa:george-edison55/cmake-3.x
sudo add-apt-repository ppa:mystic-mirage/pycharm
sudo add-apt-repository ppa:webupd8team/sublime-text-3

#Get list and update
sudo apt-get update
sudo apt-get upgrade

#dev tools
sudo apt-get install nautilus-open-terminal
sudo apt-get install build-essential
sudo apt-get install software-properties-common
sudo apt-get install gcc g++ cpp
sudo apt-get install clang-3.5
sudo apt-get install clang++-3.5
sudo apt-get install cmake cmake-gui

#Dev Other 
sudo apt-get install liblog4cxx10 liblog4cxx10-dev
sudo apt-get install gource

#Graphics and CV
sudo apt-get install libglfw-dev
sudo apt-get install libglew-dev
sudo apt-get install libopencv-dev
sudo apt-get install nvidia-opencl-dev
sudo apt-get install binutils-gold
sudo apt-get install freeglut3 freeglut3-dev
sudo sh install_glfw.sh
sudo sh install_png16.sh

#IDEs and Text Editors
sudo apt-get install netbeans
sudo apt-get install pycharm
sudo apt-get install sublime-text-installer

#Media Editing
sudo apt-get install handbrake
sudo apt-get install gimp gimp-data gimp-plugin-registry gimp-data-extras
sudo apt-get install audacity

#Entertainment
sudo apt-get install steam
sudo apt-get install vlc browser-plugin-vlc
