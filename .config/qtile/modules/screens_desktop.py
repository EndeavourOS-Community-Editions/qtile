from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

#It's declerad here and not in widgets, because desktops use smaller fonts.
volume = MyVolume(
    fontsize = 15,
    font="RobotoCondensed Bold",
    foreground=colors[2],
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
                disable_drag=True,
                font="RobotoCondensed",
                fontsize=12,
                margin_y=5.4,
                margin_x=2,
                padding_x=4.3,
                borderwidth=3,
                active="#0ab5fa",
                inactive="#615c8a",
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
                fontsize=11.7,
                foreground="#9fd8fb",
                ignore_dups_history=True,
            ),
            widget.WindowName(
                font="RobotoCondensed",
                fontsize=12.4,
                format="{state}{name}",
                padding=2,
                background=colors[6],
                parse_text=truncate_text,
            ),
            arrow_a,
            widget.CurrentLayout(
                font="RobotoCondensed Bold",
                fontsize=12,
                background=colors[0],
                foreground=colors[1],
                ),
            arrow_b,
            widget.Volume(
                #background=colors[0],
                font="RobotoCondensed Bold",
                fontsize=12,
                foreground=colors[2],
            ),
            volume,
            separator,
            arrow_a,
            widget.GenPollText(
                func=network,
                background=colors[0],
                foreground=colors[3],
                update_interval=2,
                font="RobotoCondensed Bold",
                # Not working fine with xfce4, works fine with alacritty.
                #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("xfce4-terminal -e nmtui")} 
            ),
            arrow_b,
            separator,
            widget.Clock(
                foreground=colors[4],
                #background=colors[0],
                #fontsize=12,
                font="RobotoCondensed Bold",
                format="%d %b, %A  %I:%M %p",
                fmt="   {}"
            ),                
            separator,             
            arrow_a,
            widget.TextBox(
                text=' ',
                background=colors[0],
                foreground=colors[1],
                font="RobotoConsended Bold",
                fontsize=12.5,
                mouse_callbacks={'Button1':lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/qtile/scripts/powermenu.sh'))},
                #background=colors[4],
            ),
            widget.Sep(
                padding=8,
                linewidth=0,
                background=colors[0],
            ),
        ],
        28,
 
        background=colors[6],
    ), ),
]








