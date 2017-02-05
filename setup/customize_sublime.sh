mkdir -p Preferences.sublime-settings ~/.config/sublime-text-3/Packages/User/
cp Preferences.sublime-settings ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings
sudo sed -i -- 's/gedit/sublime-text/g' /usr/share/applications/defaults.list

