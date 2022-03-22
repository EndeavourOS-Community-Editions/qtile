#!/bin/sh

#start notifier script
~/.config/qtile/scripts/low_bat_notifier.sh

#low battery level, you can modify it
low_bat=26

#Do not modify these variables
charging="fully-charged"
not_charging="discharging"
bat_now=$(cat /sys/class/power_supply/BAT0/capacity)
check=2

#I check if the battery is not charging, the script is not running and the battery
#perchantage is higher than low battery or if the battery was charging before.
#In this way the user can receive notification each time the battery level is low
#without spamming notifications

while true
do
	check_running=$(pgrep -fl low_battery.sh)
	state=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep state | awk '{print $2}')
	if [ "$state" = "$charged" ]; then
		check=1
		sleep 30
	elif [ "$state" = "$not_charging" ] && [ -z "$check_running" ] && ( [ "$bat_now" -gt "$low_bat" ]  || [ "$check" -lt 2 ] );then
		~/.config/qtile/scripts/low_bat.sh
	else
		sleep 30
	fi
done
