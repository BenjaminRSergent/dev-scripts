mkdir tmp_png
cd tmp_png
wget  http://downloads.sourceforge.net/libpng/libpng-1.6.18.tar.xz
if [ ! -e libpng-1.6.18.tar.xz];
then
    echo "Failed to download. Stopping"
    exit 1
fi

tar -xvf libpng-1.6.18.tar.xz
cd libpng-1.6.18
./configure
make
sudo make install
cd ../..
rm -r tmp_png
