from libqtile import widget
from libqtile.widget.battery import Battery, BatteryState
from libqtile import qtile

# These are the colors if you're using a laptop.
colors = [
    ["#27173b"], #0 color of the bar
    ["#a05ae6"], #1 color of layout widget
    ["#FF7F7F"], #2 color of volume widget
    ["#7F3FBF"], #3 color of battery widget
    ["#7f7fff"], # 4 color of wifi widget 
    ["#d87aeb"], # 5 color of clock widget
    ["#FFBEBE"], # 6 color or powermenu widget
    ["#ff0000"], # 7color of low foreground battery
]

#These are the colors if you're using a desktop. The color of the bar is common.
colors2 = [
    ["#a286db"], # 0 color of the layout widget
    ["#f28a8a"], # 1 color of the volume widget
    ["#8166b0"], #2 color of the connection widget
    ["#9d9de3"], #3 color of the clock widget
    ["#f1b1fc"], #4 color of the powermenu wwidget
]

class MyBattery(Battery):
    def build_string(self, status):
        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground
        if status.state == BatteryState.DISCHARGING:
            if status.percent >= 0.75:
                char = ''
            if status.percent >= 0.60:
                char = ''
            elif status.percent >= 0.45:
                char = ''
            else:
                char = ''
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = ''
        elif status.state == BatteryState.EMPTY or \
                (status.state == BatteryState.UNKNOWN and status.percent == 0):
            char = ''
        else:
            char = ' '
        return self.format.format(char=char, percent=status.percent)

battery = MyBattery(
    format='{char}  {percent:2.0%}',
    low_foreground=colors[7],
    show_short_text=False,
    low_percentage=0.25,
    font="RobotoCondensed",
    background=colors[3],
)


class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '婢 '
        elif self.volume <= 33:
            self.text = ' '
        elif self.volume < 66:
            self.text = '墳 '
        else:
            self.text = '  '

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '婢 '
        elif self.volume <= 33:
            self.text = ' '
        elif self.volume < 66:
            self.text = '墳 '
        else:
            self.text = '  '
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")


