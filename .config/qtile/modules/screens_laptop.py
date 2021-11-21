from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

#It's declerad here and not in widgets, because laptops use bigger fonts.
volume = MyVolume(
    fontsize = 15,
    font="RobotoCondensed Bold",
    foreground=colors[2],
    background=colors[0],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

screens = [
    Screen(
        top=bar.Bar(
        [   
            separator,
            eoslogo,
            separator,
            widget.GroupBox(
                font="RobotoCondensed",
                fontsize=14,
                margin_y=5,
                margin_x=2,
                padding_x=4.3,
                borderwidth=3,
                active="#0ab5fa",
                inactive="615c8a",
                foreground="#00000",
                highlight_color=colors[6],
                highlight_method="line",
                this_current_screen_border=colors[1],
                block_highlight_text_color="#ffffff",
            ),
            systray, 
            widget.Prompt(
                background=colors[6],
                font="RobotoCondensed",
                fontsize=14,
                foreground="#9fd8fb",
                ignore_dups_history=True,
            ),
            widget.WindowName(
                font="RobotoConsended",
                fontsize=15,
                format="{state}{name}",
                #background=colors[2],
                #foreground=colors[6],
            ),
            widget.CurrentLayout(
                font="RobotoConsended Bold",
                fontsize=15,
                background=colors[6],
                foreground=colors[1],
            ),
            separator,
            arrow_a,
            widget.Volume(
                #background=colors[0],
                font="RobotoCondensed Bold",
                fontsize=15
                background=colors[0],
                foreground=colors[2],
            ),
            volume,
            arrow_b,
            separator,
            battery,
            separator,
            arrow_a,
            widget.GenPollText(
                func=network,
                background=colors[0],
                foreground=colors[3],
                update_interval=2,
                fontsize=14,
                font="RobotoCondensed Bold"   
            ),
            arrow_b,
            separator,
            widget.Clock(
                font="RobotoCondensed Bold",
                foreground=colors[4],
                #background=colors[5],
                fontsize=14,
                format="%d %b, %A  %I:%M %p",
                fmt="    {}"
            ),
            arrow_a,
            widget.TextBox(
                text=' ',
                font="RobotoCondensed Bold",
                fontsize=14,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(os.path.expanduser("~/.config/qtile/scripts/powermenu.sh"))},            
                foreground=colors[1],
                background=colors[0],
            ),
            widget.Sep(
                padding=8,
                linewidth=0,
                background=colors[0],
            ),
    ],
        28,
        background=colors[6],
    ), 
),
]

