# RoobetStats
This system provides the odds of a round of roobet crash having an under or over 2x gain.
roobet.py
This file listens to live games and generates a "output.json" file that holds the statistics of each rounds "score" which is determined by the past 3 games.
roobetlive.py
This script will provide a real time percentage chance of an under or over 2x gain on the next round of crash based on the contents of output.json

output.json included here is only based on 1000 datapoints, a more accurate file will have around 10,000 datapoints. To generate this change line 21, which contains the value 1000. Each iteration takes 5 seconds to get the data as it collects data from live games. So generating this amount of data takes a fair bit of time.

A VPN is not required for theses scripts to work.
