from libqtile import widget
from libqtile.widget.battery import Battery, BatteryState
from libqtile import qtile

colors = [
	      ["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
] 


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)

class MyBattery(Battery):
    def build_string(self, status):
        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground
        if status.state == BatteryState.DISCHARGING:
            if status.percent > 0.75:
                char = ''
            elif status.percent > 0.45:
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
    low_foreground=colors[1],
    show_short_text=False,
    low_percentage=0.25,
    foreground=colors[6],
    notify_below=12,
)


class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize=18,
    font='Font Awesome 5 Free',
    foreground=colors[4],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
