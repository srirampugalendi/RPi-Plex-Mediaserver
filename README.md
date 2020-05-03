# RPi-Plex-Mediaserver
This project aims at building a remotely managed media-server with a Raspberry Pi, Plex &amp; Deluge.

**Pre-requisites:**
**Hardware:**
* Raspberry Pi with Raspbian OS
* USB 3 128GB
* WiFi Adapter(Optional)

**Software:**
* Plex media server
* Deluge Bit Torrent engine
* Deluge web client
* VNC Server
* RPi Monitor(Optional)

**Step 1:** Install plex server.
Install Plex media server in RPi
https://thepi.io/how-to-set-up-a-raspberry-pi-plex-server/

**Step 2:** Add external drive as media storage.
Format a USB pendrive in NTFS format. Add the mounted NTFS external drive as library location in plex media server settings by following the below guide.
https://forums.plex.tv/t/using-ext-ntfs-or-other-format-drives-internal-or-external-on-linux/198544

**Step 3:** Install Deluge. Enable the web interface. Enable service to make persistent at reboot.
Follow the below guide to do the same.
https://pimylifeup.com/raspberry-pi-deluge/

**Step 4:** Configure deluge torrent download location.
Set the download location to the plex media library folder. So, once the download is completed, the plex creates the meta files and adds it to the library.

**Step 5:** Automate to personal need using deluge execute plugin.
If you want to run any automation task, like sending email when download is completed or renaming the downloaded file, deluge executre plugin is there to help. Deluge can invoke shell scripts for you based on events like torrent downloaded, removed , added etc.. This option can be found in Deluge Web UI -> Preferences -> Execute.

I have uploaded invoke.sh script that i used to rename torrent files downloaded from specific sites, so plex is easily able to match the name against the imdb database

**Step 6:** Enabling remote access.
You can enable remote access(Plex -> Settings -> Remote Access) to plex media server so your friends can also access your media from their home. However, if you want to remote access your RPi from outside your home for troubleshooting, you can do it by installing VNC Server and login to vnc account.
https://www.realvnc.com/en/connect/download/vnc/raspberrypi/
