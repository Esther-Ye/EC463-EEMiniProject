# Collection of general notes

### Collecting the data 
List of steps:

0. Optional: SSH into the Pi from your PC
Once the pi and your PC are on the same hotspot, type: 
```sh
ssh pi@raspberrypi.local
```
It will ask you for the password

1. On the pi, navigate to where the python files are stored if you haven't already. Then type:
```sh
sudo python3 wifi_scan.py ~/data -N 100
```

2. Immediately the path to the json file will be shown (i.e. ```/home/pi/data/wifi_2021-09-14T23_50_18.json``` ), along with many online devices in the area.

### Moving data onto your PC
3. From the terminal in a Linux/MAC OS, type the command:
```sh
scp pi@raspberrypi.local:<the path to the file you want> <what you want your copy to be named>
```
For example, mine is:
```sh
scp pi@raspberrypi.local:/home/pi/data/wifi_2021-09-14T23_50_18.json wifi_2021-09-14T23_50_18.json
```
Note: Make sure you are in the right directory on your PC (terminal).

### Analyzing the data
4. Download wifi_plot.py if it isn't already in the same directory.
5. Then type:
```sh
sudo python3 wifi_plot.py <name of json file>
```
For example, mine is:
```sh
sudo python3 wifi_plot.py wifi_2021-09-14T23_50_18.json
```
6. The plot should output automatically in a figure window and can be saved as a .png file
