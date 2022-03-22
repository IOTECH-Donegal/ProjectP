# Autostart for RPi
Startup has moved on from rc.local to systemd and the files and instructions here allow this 
project's services to be started.

Copy the service files to /etc/systemd/system.
Change the permissions of each file using 

    cd /etc/systemd/system
    sudo chmod 644 nmeabase.service
    sudo chmod 644 nmeaheading.service
    sudo chmod 644 ubxheading.service
    sudo chmod 644 str2str.service

Now enable each service to load at startup

    sudo systemctl daemon-reload
    sudo systemctl enable nmeabase.service
    sudo systemctl enable nmeaheading.service
    sudo systemctl enable ubxheading.service
    sudo systemctl enable str2str.service

Now reboot and check if the services are running

    sudo systemctl status nmeabase.service
    sudo systemctl status nmeaheading.service
    sudo systemctl status ubxheading.service
    sudo systemctl status str2str.service
