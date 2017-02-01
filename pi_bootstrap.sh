#!/usr/bin/env bash

#go home
cd /home/pi

# general stuff
apt-get -y purge apt-listchanges
# apt-mark hold rpi-chromium-mods

#update
apt-get -y update
# apt-get -y -qq upgrade
DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical apt-get -qq -y -o "Dpkg::Options::=--force-confdef" -o "Dpkg::Options::=--force-confold" upgrade

# python stuff
apt-get -y install build-essential python-dev python-smbus python-imaging git
apt-get -y install ipython

# vim
apt-get -y install vim
wget https://gist.githubusercontent.com/scottpham/7b1f79b81fec1ee48bed3ddf07594315/raw/ -O ~/.vimrc

# rpi lib
pip install RPi.GPIO

# Adafruit DHT 22 stuff
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
python setup.py install
cd /home/pi

# download led test
wget https://gist.githubusercontent.com/scottpham/cac28c2ff09b9cdb493a032d3f147a3a/raw -O /home/pi/led.py

# start VNC
/etc/init.d/vncserver-x11-serviced start

# ensure that it boots to vnc next time
sed -i -e '$i \/etc/init.d/vncserver-x11-serviced start \n' /etc/rc.local

#### start localization code ####

filekill() {
  if [ -e "$1" ]; then
    rm "$1"
  fi
}

tzup() {
  # change this line for timezone
  cp /usr/share/zoneinfo/America/Phoenix /etc/localtime
  ntpd
}
tzup
#==================================================== Update the keyboard layout
kbd() {
  sed -i /etc/default/keyboard -e 's|pc101|pc105|'
  sed -i /etc/default/keyboard -e 's|gb|us|'
  #filekill "/etc/default/keyboard"
  #sudo mv /home/pi/openwinkrpi/keyboard /etc/default/keyboard
  service keyboard-setup restart
}
kbd
#======================================================= Update Locale(Language)
lcale() {
  locale-gen
  sh -c 'sed -i /etc/default/locale -e "s/en_GB.UTF-8/en_US.UTF-8/"'
  sh -c 'sed -i /etc/locale.gen -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/"'
  sh -c 'sed -i /etc/locale.gen -e "s/en_GB.UTF-8 UTF-8/# en_GB.UTF-8 UTF-8/"'
  LANG=en_US.UTF-8
  LANGUAGE=en_US.UTF-8
  LC_TIME=en_US.UTF-8
  LC_COLLATE=en_US.UTF-8
  LC_NUMERIC=en_US.UTF-8
  LC_DATE=en_US.UTF-8
  LC_MESSAGES=en_US.UTF-8
  locale-gen --purge en_US.UTF-8
}
lcale
