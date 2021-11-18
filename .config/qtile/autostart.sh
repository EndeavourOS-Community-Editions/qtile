#!/bin/sh

#start script to autolock screen and autosuspend when the computer is inactive.
~/.config/qtile/scripts/locker &

#dunst notifications
/usr/bin/dunst &

#setting the wallpaper
feh --bg-scale ~/.local/share/endeavouros/eos-wallpaper.png

#check if battery is present, if so runs the script to send notifications when battery is low.
# couldn't make it work the notify built-in in qtile
if [ "$(ls -A /sys/class/power_supply)" ]; then
	~/.config/qtile/scripts/check_battery.sh &
fi

#start compositor
picom --experimental-backends &

# Start welcome
eos-welcome & disown
