#!/bin/sh

~/.config/qtile/low_battery.sh

charging="fully-charged"
not_charging="discharging"
bat_now=$(cat /sys/class/power_supply/BAT1/capacity)
low_bat=30

#I check if the battery is not charging, the script is not running and the battery
#perchantage is higher than low battery. Because otherwise is the perchantage < low_battery
#then we would spam notification to the end user

while true
do
	check_running=$(pgrep -fl low_battery.sh)
	state=$(upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep state | awk '{print $2}')

	if [ "$state" = "$charged" ]; then
		sleep 300
	elif [ "$state" = "$not_charging" ] && [ -z "$check_running" ] && [ "$bat_now" -gt "$low_bat" ];then
		~/.config/qtile/low_battery.sh
	fi
done
