# NEEDS BETTER ERROR HANDLING
# AND BACKUP FILES

echo "Deletes some existing config. Are you sure you want to do this? (yes/no)"
read x
if [ "$x" = "yes" ]
then
  echo "Presuming that all dependencies already installed..."
  
  if  [[ -d ~/.config ]]; then
      echo "Directory .config found"
  else
      cp -r .config ~/
  fi
  
  if [[ -d ~/.local ]]; then
      echo "~/.local found\n"
      if [[ -d ~/.local/share ]]; then
          echo "~/.local/share found\n"
          
          if [[ -d ~/.local/share/endeavouros ]]; then
              cp -r .local/share/endeavouros/* ~/.local/share/endeavouros
              echo "copying wallpapers to .local/share/endeavouros\n"
          else
              mkdir .local/share/endeavouros
              cp -r .local/share/endeavouros/* ~/.local/share/endeavouros
              echo "copying wallpapers to .local/share/endeavouros\n"
          fi
          
          if [[ -d ~/.local/share/fonts ]]; then
              cp -r .local/share/fonts/* ~/.local/share/fonts
              echo "copying fonts to .local/share/fonts\n"
          else
              mkdir .local/share/fonts
              cp -r .local/share/fonts/* ~/.local/share/fonts
              echo "copying fonts to .local/share/fonts\n"
          fi
      else
          mkdir ~/.local/share
          cp -r .local/share/* ~/.local/share
          echo "Directory ~/.local/share created.\n
          you can find wallpapers at : ~/.local/share/endeavouros\n
          you can find fonts at : ~/.local/share/fonts"
      fi
  else
      cp -r .local/* ~/.local/
      echo "Directory ~/.local/share created.\n
      you can find wallpapers at : ~/.local/share/endeavouros\n
      you can find fonts at : ~/.local/share/fonts"
  fi
  
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

