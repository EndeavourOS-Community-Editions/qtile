#!/usr/bin/env bash

username="$1"
git clone https://github.com/parham-dev27/qtile-eos-mine --branch rewrite

cd qtile-eos-mine
cp -R .config /home/$username/
chmod +x /home/$username/.config/qtile/autostart.sh
chmod +x /home/$username/.config/rofi/powermenu.sh
chmod +x /home/$username/.config/rofi/powermenu.sh
chmod -R +x /home/$username/.config/qtile/scripts/*.sh
chmod -R +x /home/$username/.config/qtile/scripts/i3lock-fancy/*.sh
cp .Xresources /home/$username/
cp .gtkrc-2.0 /home/$username
chown -R $username:$username /home/$username/.config

pacman -S --needed --noconfirm - <packages-repository.txt

cd ..
rm -rf qtile-eos-mine
systemctl enable sddm
