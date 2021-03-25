# light-control
Controls my LPD8806 LED strip.

The whoshome.py script uses python3 which itself will run party.py using python2.7 since it makes
use of the now deprecated RPi-LPD8806 library written for Python 2.

Formerly interacted closely with my home-control repository. This latest re-write ignore the
home-control library for now.

# Setup

```
sudo apt-get install git python3-dev python3-venv
git clone https://github.com/TechnoConserve/light-control
cd light-control
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python whoshome.py
```
