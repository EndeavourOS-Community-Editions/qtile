#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
picom --experimental-backends --vsync & disown # should prevent screen tearing on most setups
