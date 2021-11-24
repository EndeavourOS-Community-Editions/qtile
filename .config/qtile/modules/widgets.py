from libqtile import widget
from libqtile.widget.battery import Battery, BatteryState
from libqtile import qtile
import subprocess

# if THE WIDGET IS NOT HERE, IT'S IN screens_laptop or screens_desktop, depending
# on if your device is a laptop or a desktop.

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


            #########################
            # WIDGET AND BAR COLORS #
            #########################

colors = [
    ["#282a30"], #0 color of "arrow"
    ["#f28a8a"], #1 color of the layout widget/powermenu widget
    ["#af5ee6"], #2 color of the volume widget
    ["#7fb4ff"], #3 color of the connection widget
    ["#ff96dc"], #4 color of the clock widget
    ["#d65547"], #5 low foreground battery
    ["#2f3340"], #6 color of the bar
]


                ##################
                # BATTERY WIDGET #
                ##################

class MyBattery(Battery):
    def build_string(self, status):
        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground
        if status.state == BatteryState.DISCHARGING:
            if status.percent >= 0.75:
                char = '  '
            if status.percent >= 0.60:
                char = ' '
            elif status.percent >= 0.45:
                char = ' '
            else:
                char = ' '
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = '  '
        elif status.state == BatteryState.EMPTY or \
                (status.state == BatteryState.UNKNOWN and status.percent == 0):
            char = ' '
        else:
            char = ' '
        return self.format.format(char=char, percent=status.percent)

battery = MyBattery(
    format='{char}  {percent:2.0%}',
    low_foreground=colors[5],
    show_short_text=False,
    low_percentage=0.25,
    fontsize=15,
    font="RobotoCondensed Bold",
    #background=colors[0],
    foreground="#47d665"
)

                ##################
                # VOLUME WIDGET  #
                ##################

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '婢'
        elif self.volume <= 33:
            self.text = ''
        elif self.volume < 66:
            self.text = '墳'
        else:
            self.text = ' \t '

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '婢'
        elif self.volume <= 33:
            self.text = ''
        elif self.volume < 66:
            self.text = '墳'
        else:
            self.text = ' '
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")



                ##################
                #  LOGO WIDGET   #
                ##################

eoslogo = widget.Image(
    filename='~/.config/qtile/eos-logo.png', 
    margin=4, background=colors[6], 
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
)

                ######################
                #  SEPARATOR WIDGET  #
                ######################

separator = widget.Sep(
    padding=6,
    linewidth=0,
    background=colors[6],    
)
                #####################
                #   Systray widget  #
                #####################
                
systray = widget.Systray(
    padding=2,
)
           
                #########################
                #   Arrows decorations  #
                #########################
                
arrow_a = widget.TextBox(
    text="",
    padding=0,
    fontsize="28",
    foreground=colors[0],
)

arrow_b = widget.TextBox(                                                                    
    text = "",
    padding = 0,
    fontsize = 28,
    foreground=colors[6],
    background=colors[0],
)

