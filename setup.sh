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
  check_chassis
  rm -rf ~/.config/rofi/
  cp -r .config/rofi ~/.config/
  rm -rf ~/.config/dunst
  cp -r .config/dunst ~/.config
  #Just make the files executable by git update-index --chmod=+x low_bat_notifier.sh and then commit to the repo
  chmod +x ~/.config/qtile/scripts/low_bat_notifier.sh
  echo 'done'
fi

check_chassis(){
	line="widget.Battery(battery=1, discharge_char='    ', low_percentage=0.25, charge_char='   ', foreground='5bc236', format='{char} {percent:2.0%}', update_interval=30),"
	commented_line="#"
	commented_line+=$line
	chassis_type=$(cat /sys/class/dmi/id/chassis_type)
	#chassis numbers go from 1 to 11, from 8 to 11 there are all devices with a battery
	if [ "$chassis_type" -lt 8 ]; then
  		sed -i "s/$line/$commented_line/" ~/.config/qtile/config.py
	fi
}
