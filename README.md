# raspi-camera-twitter
Shoot a photo and post in Twitter

## Requirements

* Raspberry Pi 3B(+)
* Camera Mobule
* Python 3

## Download Models

```bash
cd /home/pi
wget https://github.com/chuanqi305/MobileNet-SSD/raw/master/MobileNetSSD_deploy.caffemodel
wget https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.prototxt
```

## Script Services

### pre-install script

user: root
timeout: 0

```bash
apt update
apt -y upgrade
apt update
apt install -y build-essential cmake pkg-config
apt install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
apt install -y libxvidcore-dev libx264-dev
apt install -y libgtk2.0-dev libgtk-3-dev
apt install -y libatlas-base-dev gfortran
apt install -y libqtgui4 libqt4-test
apt install -y libilmbase12 libopenexr22 libgstreamer1.0-dev
apt install -y python3-dev python3-pip
pip3 install numpy opencv-python picamera[array] flask imutils pyzbar
```

### post-update script

user: root
timeout: 0

```bash
pip3 install -r requirements.txt
```
