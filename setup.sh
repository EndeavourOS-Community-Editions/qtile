# NEEDS BETTER ERROR HANDLING
# AND BACKUP FILES

echo "Deletes some existing config. Are you sure you want to do this? (yes/no)"
read x
if [ "$x" = "yes" ]
then
  echo "Presuming that all dependencies already installed..."

  rm -f ~/.Xresources ~/.gtkrc-2.0 ~/.config/picom.conf
  cp .Xresources ~/
  cp .gtkrc-2.0 ~/
  cp .config/picom.conf ~/.config/picom.conf
  rm -rf ~/.config/gtk-3.0/
  cp -r .config/gtk-3.0 ~/.config/
  rm -rf ~/.config/qtile/
  cp -r .config/qtile ~/.config/
  rm -rf ~/.config/rofi/
  cp -r .config/rofi ~/.config/
  rm -rf ~/.config/dunst
  cp -r .config/dunst ~/.config
  #Just make the files executable by git update-index --chmod=+x low_bat_notifier.sh and then commit to the repo
  chmod +x ~/.config/qtile/scripts/low_bat_notifier.sh
  echo 'done'
fi

