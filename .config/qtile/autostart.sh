#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
