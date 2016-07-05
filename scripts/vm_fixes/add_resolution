WIDTH=$1
HEIGHT=$2
MODE_NAME="${WIDTH}x${HEIGHT}_60.00"
MODE_LINE=`cvt $WIDTH $HEIGHT 60 | sed -n 2p | sed 's/Modeline\ / /g'`
sudo xrandr --newmode $MODE_LINE
sudo xrandr --addmode Virtual1 $MODE_NAME
xrandr -s $MODE_NAME