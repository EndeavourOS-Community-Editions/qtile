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

volume = MyVolume(
    fontsize = 15,
    font="Nerd fonts",
    background=colors2[1],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

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
            output+="  "
            return output
    
        else:
            command = "nmcli | grep {}".format(output[0])    
            proc = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE)
            output = proc.stdout.read()
            output= output[21:39] + "  "
            return output
    
    else:
        output = "Not connected 睊"
        return output

screens = [
    Screen(
        top=bar.Bar(
        [   
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                    ),
                widget.Image(filename='~/.config/qtile/eos-logo.png', margin=3, background=colors[0], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")}),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.GroupBox(
                    disable_drag=True,
                    font="RobotoCondensed",
                    fontsize=16,
                    margin_y=5,
                    margin_x=3,
                    padding_x=4.3,
                    borderwidth=4,
                    active="#92c4de",
                    inactive=colors[3],
                    foreground="#00000",
                    highlight_color=colors[0],
                    highlight_method="line",
                    this_current_screen_border=colors[2],
                    block_highlight_text_color="#ffffff",
                    ),
                widget.Systray(),
                widget.Prompt(
                    background=colors[0],
                    font="RobotoCondensed",
                    fontsize=14,
                    foreground="#9fd8fb",
                    ignore_dups_history=True,
                ),
                widget.WindowName(
                    font="RobotoConsended",
                    fontsize=15,
                    format="{state}{name}",
                ),
                widget.TextBox(
                text="\ue0bc",
                font="Inconsolata for powerline",
                fontsize="33",
                padding=0,
                background=colors[1],
                foreground=colors[0],
                ),
                widget.CurrentLayout(
                    font="RobotoConsended",
                    fontsize=15,
                    background=colors[1],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[1],
                    foreground=colors[2],
                ),
                widget.Volume(
                    background=colors[2],
                    font="RobotoCondensed",
                ),
                volume,
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[2],
                ),
                widget.TextBox(
                    text="\ue0bc",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[3],
                    foreground=colors[2],
                    ),
                battery,
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[3],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[3],
                    foreground=colors[4],
                ),
                widget.GenPollText(
                    func=network,
                    background=colors[4],
                    update_interval=2,
                    fontsize=15,
                    font="RobotoCondensed"   
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[4],
                ),
                widget.TextBox(
                    text="\ue0bc",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[5],
                    foreground=colors[4],
                    ),
                widget.Clock(
                    font="RobotoCondensed",
                    foreground="#ffffff",
                    background=colors[5],
                    fontsize=15,
                    format="%d %b, %A  %I:%M %p",
                    fmt="  {}"
                    ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[5],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[5],
                    foreground=colors[6],
                    ),
                widget.TextBox(
                    text='',
                    fontsize=17,
                    mouse_callbacks= {'Button1':lambda:qtile.cmd_spawn(os.path.expanduser('~/.config/qtile/scripts/powermenu.sh'))},
                    background=colors[6]
                    ),
                widget.Sep(
                    padding=8,
                    linewidth=0,
                    background=colors[6],
                    ),
    ],
    28,
    background=colors[0],
    margin=[8,9,5,9],
    ), ),
]
