from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import subprocess
import os

#Function to truncate super long text in firefox.

def truncate_text(text):
    index = text.find('-')
    if index != -1:
        return text[index+1:]
    else:
        return text

#Instead of qtile Net widget I use the widget GenPollText calling
#to the function test_connection.

def network():
    command = "nmcli | grep interface | awk '{print $2}'"
    proc = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    
    if output != '':
        output = output.split()
        output = list(dict.fromkeys(output))
    
        if output[0] == "wlan0":
            proc=subprocess.Popen(["iwgetid", "-r"], universal_newlines=True, stdout=subprocess.PIPE)
            output = proc.stdout.read()
            output=output.rstrip("\n")
            output+="   "
            return output
    
        else:
            command = "nmcli | grep {}".format(output[0])    
            proc = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE)
            output = proc.stdout.read()
            output= output[21:39] + "  "
            return output
    
    else:
        output = "Not connected  睊 "
        return output


volume = MyVolume(
    fontsize = 15,
    font="RobotoCondensed",
    background=colors2[1],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

screens = [
    Screen(
        top=bar.Bar(
        [   
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Image(filename='~/.config/qtile/eos-logo.png', margin=4, background=colors[0], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")}),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.GroupBox(
                    disable_drag=True,
                    font="RobotoCondensed",
                    fontsize=12,
                    margin_y=5.4,
                    margin_x=2,
                    padding_x=4.3,
                    borderwidth=3,
                    active="#ccedff",
                    inactive=colors2[2],
                    foreground="#00000",
                    highlight_color=colors[0],
                    highlight_method="line",
                    this_current_screen_border=colors[2],
                    block_highlight_text_color="#ffffff",
                ),
                widget.Systray(
                    padding=2
                ),
                widget.Prompt(
                    background=colors[0],
                    font="RobotoCondensed",
                    fontsize=11.7,
                    foreground="#9fd8fb",
                    ignore_dups_history=True,
                ),
                widget.WindowName(
                    font="RobotoCondensed",
                    fontsize=12.4,
                    format="{state}{name}",
                    padding=2,
                    background=colors[0],
                    parse_text=truncate_text,
                ),
                widget.TextBox(
                text="\ue0bc",
                font="Inconsolata for powerline",
                fontsize="30",
                padding=0,
                background=colors2[0],
                foreground=colors[0],
                ),
                widget.CurrentLayout(
                    font="RobotoCondensed",
                    fontsize=12,
                    background=colors2[0],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="30",
                    padding=0,
                    background=colors2[0],
                    foreground=colors2[1],
                ),
                widget.Volume(
                    background=colors2[1],
                    font="RobotoCondensed",
                    fontsize=12,
                ),
                volume,
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors2[1],
                ),
                widget.TextBox(
                    text="\ue0bc",
                    font="Inconsolata for powerline",
                    fontsize="30",
                    padding=0,
                    background=colors2[2],
                    foreground=colors2[1],
                    ),
                widget.GenPollText(
                    func=network,
                    background=colors2[2],
                    update_interval=2,
                    font="RobotoCondensed",
                    # Not working fine with xfce4, works fine with alacritty.
                    #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("xfce4-terminal -e nmtui")} 
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors2[2],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="30",
                    padding=0,
                    background=colors2[2],
                    foreground=colors2[3],
                    ),
                widget.Clock(
                    foreground="#ffffff",
                    background=colors2[3],
                    font="RobotoCondensed",
                    format="%d %b, %A  %I:%M %p",
                    fmt="   {}"
                    ),
                widget.TextBox(
                    text="\ue0bc",
                    font="Inconsolata for powerline",
                    fontsize="30",
                    padding=0,
                    background=colors2[4],
                    foreground=colors2[3],
                ),
                widget.TextBox(
                    text=' ',
                    fontsize=13,
                    mouse_callbacks= {'Button1':lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/qtile/scripts/powermenu.sh'))},
                    background=colors2[4],
                ),
                widget.Sep(
                    padding=8,
                    linewidth=0,
                    background=colors2[4],
                    ),
    ],
    26,
    background=colors[0],
    margin=[8,9,5,9],
    ), ),
]
