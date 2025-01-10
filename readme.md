This repo contains the sample codes required to create a virtual USB port on Ubuntu, send test data, and read the sent data.

#Setup
```
sudo apt-get install socat
socat -d -d pty,raw,echo=0 pty,raw,echo=0
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

#Starting
```
python reader.py
python writer.py
```