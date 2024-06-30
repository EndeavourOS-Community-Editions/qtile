#!/usr/bin/env bash
clear

create_backup() {
	echo -e "\e[32mCreating backups of your configuration files...\e[0m"
	cp -R ~/.config/dunst ~/.config/dunst.bak
	cp -R ~/.config/gtk-3.0 ~/.config/gtk-3.0.bak
	cp -R ~/.config/qtile ~/.config/qtile.bak
	cp -R ~/.config/rofi ~/.config/rofi.bak
	cp -R ~/.config/xfce4 ~/.config/xfce4.bak
	cp ~/.config/picom.conf ~/.config/picom.conf.bak
	cp ~/.Xresources ~/.Xresources.bak
	cp ~/.gtkrc-2.0 ~/.gtkrc-2.0.bak
}

copy_config() {
	echo -e "\e[32mCopying configuration files...\e[0m"
	username=$(whoami)
	cp -R .config/* ~/.config
	chmod +x ~/.config/qtile/autostart.sh
	chmod -R +x ~/.config/qtile/scripts/*.sh
	chmod -R +x ~/.config/qtile/scripts/i3lock-fancy/*.sh
	chmod +x ~/.config/rofi/powermenu.sh
	chown -R $username:$username ~/.config
	cp .Xresources ~/.Xresources 
	cp .gtkrc-2.0 ~/.gtkrc-2.0 
	chown $username:$username ~/.Xresources 
	chown $username:$username ~/.gtkrc-2.0 
}

echo -e """\e[35;1m
  ____ _______ _ _      ______ ____   _____        _____ ______ 
 / __ \__   __(_) |    |  ____/ __ \ / ____|      / ____|  ____|
| |  | | | |   _| | ___| |__ | |  | | (___ ______| |    | |__   
| |  | | | |  | | |/ _ \  __|| |  | |\___ \______| |    |  __|  
| |__| | | |  | | |  __/ |___| |__| |____) |     | |____| |____ 
 \___\_\ |_|  |_|_|\___|______\____/|_____/       \_____|______|                                                          
\e[0m"""
echo -e "\e[35mEndeavourOS Community Edition setup for QTile\e[0m"

echo -e -n "\n\n\e[34;1m:: \e[0mThis script will modify your configuration files. \e[1mDo you want to proceed? [y/N]\e[0m "
read confirm
confirm=$(echo "$confirm" | tr '[:upper:]' '[:lower:]')

if [[ "$confirm" = "yes" || "$confirm" = "y" ]]; then
	create_backup
	copy_config
	echo -e "\e[33mInstalling the required packages...\e[0m"
	sudo pacman -S --needed --noconfirm - <packages-repository.txt
	echo -e "\e[33mEnabling Login Manager (SDDM)\e[0m"
	sudo systemctl enable sddm.service
	sudo systemctl start sddm.service
	echo -e "\e[32mDone!\e[0m"
	exit 0
else
	echo -e "\e[31mAborting...\e[0m"
	exit 130
fi
