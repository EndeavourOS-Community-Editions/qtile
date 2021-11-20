#!/bin/sh

#dunst notifications
/usr/bin/dunst &

#setting the wallpaper
feh --bg-scale ~/.local/share/endeavouros/eos-wallpaper.png

#start compositor
picom --experimental-backends &

# Low battery notifier
if [ "$(ls -A /sys/class/power_supply)" ]; then
	~/.config/qtile/scripts/check_battery.sh &
fi

# Start welcome application
eos-welcome & disown
