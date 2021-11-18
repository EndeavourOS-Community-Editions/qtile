# NEEDS BETTER ERROR HANDLING
# AND BACKUP FILES

echo "This will not show good result if you do not have all the dependencies installed :\n
do you want to continue ? (yes/no)"
read x
if [ "$x" = "yes" ]
then
  echo "Presuming that all dependencies already installed..."
  
  if  [[ -d ~/.config ]]; then
      
      if [[ -d ~/.config/qtile ]]; then
          mv ~/.config/qtile ~/.config/qtile.old
          cp -r .config/qtile ~/.config/
          echo "Existing qtile configuration already found, moved to ~/.config/qtile.old\n"
          echo "New configuration of qtile at ~/.config/qtile\n"
      else
          cp -r .config/qtile ~/.config/
          echo "Qtile configuration at ~/.config/qtile\n"
      fi
      
      if [[ -d ~/.config/xfce4 ]]; then
          if [[ -d ~/.config/xfce4/terminal ]]; then      
              mv ~/.config/xfce4/terminal ~/.config/xfce4/terminal.old
              cp -r .config/xfce4/* ~/.config/xfce4/
              echo "Existing xfce4-terminal configuration already found, moved to ~/.config/xfce4/terminal.old\n"
              echo "New configuration at ~/.config/xfce4/terminal"
          else
              cp -r .config/xfce4/* ~/.config/xfce4/
              echo "New configuration of xfce4-terminal at ~/.config/xfce4/terminal\n"
          fi
      else
          cp -r .config/xfce4 ~/.config/
          echo "New configuration of xfce4-terminal at ~/.config/xfce4/terminal\n"
      fi
      
      if [[ -d ~/.config/rofi ]]; then
          mv ~/.config/rofi ~/.config/rofi.old
          cp -r .config/rofi ~/.config/
          echo "Existing rofi configuration already found, moved to ~/.config/rofi.old\n"
          echo "New configuration of qtile at ~/.config/rofi\n"
      else
          cp -r .config/rofi ~/.config/
          echo "Rofi configuration at ~/.config/rofi\n"
      fi
      
      if [[ -e ~/.config/picom.conf ]]; then
          mv ~/.config/picom.conf ~/.config/picom.old
          cp -r .config/picom.conf ~/.config/
          echo "Existing picom configuration already found, moved to ~/.config/picom.old\n"
          echo "New configuration of picom at ~/.config/picom.conf\n"
      else
          cp -r .config/picom ~/.config/
          echo "New picom configuration at ~/.config/qtile\n"
      fi
      
      if [[ -d ~/.config/dunst ]]; then
          mv ~/.config/dunst ~/.config/dunst.old
          cp -r .config/dunst ~/.config/
          echo "Existing dunst configuration already found, moved to ~/.config/dunst.old\n"
          echo "New configuration of dunst at ~/.config/dunst\n"
      else
          cp -r .config/dunst ~/.config/
          echo "Dunst configuration at ~/.config/dunst\n"
      fi
      
      if [[ -d ~/.config/gtk-3.0 ]]; then
          mv ~/.config/gtk-3.0 ~/.config/gtk-3.0.old
          cp -r .config/gtk-3.0 ~/.config/
          echo "Existing gtk-3.0 configuration already found, moved to ~/.config/gtk-3.0.old\n"
          echo "New configuration of gtk-3.0 at ~/.config/gtk-3.0\n"
      else
          cp -r .config/gtk-3.0 ~/.config/
          echo "Gtk-3.0 configuration at to ~/.config/qtile\n"
      fi
  else
      cp -r .config ~/
      echo "~/.config directory created with all configuration files in it.\n"
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
          you can find fonts at : ~/.local/share/fonts\n"
      fi
  else
      cp -r .local/* ~/.local/
      echo "Directory ~/.local/share created.\n
      you can find wallpapers at : ~/.local/share/endeavouros\n
      you can find fonts at : ~/.local/share/fonts\n"
  fi
  
  
  if [[ -d ~/.icons ]]; then
      tar xvf Bibata-Modern.tar.gz -C ~/.icons
      tar xvf Tela-purple.tar.xz -C ~/.icons
      echo "Installed icon theme and cursor theme\n"
      if [[ -d ~/.icons/default ]]; then
          if [[ -e ~/.icons/default/index.theme ]]; then
              mv ~/.icons/default/index.theme ~/.icons/default/index.theme.old
              cp index.theme ~/icons/default/
              echo "Found existing index.theme in ~/.icons/default, moved to ~/.icons/default/index.theme.old\n"
              echo "New index.theme at ~/.icons/default/\n"
          else
              cp index.theme ~/icons/default/
              echo "New index.theme at ~/.icons/default/\n"
          fi
      else
          mkdir ~/.icons/default
          cp index.theme ~/icons/default/
          echo "New index.theme at ~/.icons/default/\n"
      fi     
  else
      mkdir ~/.icons
      tar xvf Bibata-Modern.tar.gz -C ~/.icons
      tar xvf Tela-purple.tar.xz -C ~/.icons
      echo "Installed icon theme and cursor theme\n"
      mkdir ~/.icons/default
      cp index.theme ~/icons/default/
      echo "New index.theme at ~/.icons/default/\n"
  fi
  
  
  if [[ -d ~/.themes ]]; then
      tar xvf Sweet-Dark.tar.xz -C ~/.themes
      echo "GTK theme installed\n"
  else
      mkdir ~/.themes
      tar xvf Sweet-Dark.tar.xz -C ~/.themes
      echo "GTK theme installed\n"
  fi     
  
  
  if [[ -e ~/.Xresources ]]; then
      mv ~/.Xresources ~/.Xresources.old
      cp .Xresources ~/
      echo "Existing .Xresources found, moved to ~/.Xresources.old\n"
      echo "New .Xresources at ~/.Xresources"
  else
      cp .Xresources ~/
      echo "Copied .Xresources at ~/.Xresources"
  fi
  
  if [[ -e ~/.gtkrc2.0 ]]; then
      mv ~/.gtkrc2.0 ~/.gtkrc2.0.old
      cp .gtkrc2.0 ~/
      echo "Existing .gtkrc2.0 found, moved to ~/.gtkrc2.0.old\n"
      echo "New .gtkrc2.0 at ~/.gtkrc2.0"
  else
      cp .gtkrc2.0 ~/
      echo "Copied .gtkrc2.0 at ~/.gtkrc2.0"
  fi
  
  find ~/.config/qtile/scripts/ -type f -exec chmod +x {} \;
  echo 'Installation terminated.'

fi

