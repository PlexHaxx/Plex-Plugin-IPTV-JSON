JSON IPTV Plug-in for Plex Media Center
---
Inspired by the M3U8 IPTV plug-in from Cigaras.

How to install the "KMTV beta" plugin for Plex Media Server?
--

Step 1:
	Locate the "Plug-ins" folder of Plex Media Server.
	
	The location of your Plex Plug-ins folder is likely as listed below:
	
		Windows
			%LOCALAPPDATA%\Plex Media Server\Plug-ins\
		
		OS X
			~/Library/Application Support/Plex Media Server/Plug-ins
		
		Linux (in general)
			$PLEX_HOME/Library/Application Support/Plex Media Server/Plug-ins
		
		QNAP
			/root/Library/Plex Media Server/Plug-ins
		
		ReadyNAS ROS6
			/apps/plexmediaserver/MediaLibrary/Plex Media Server/Plug-ins
		
		Seagate
			/data/plex_conf/Library/Application\ Support/Plex\ Media\ Server/Plug-ins
		
		Synology
			/Volume1/Plex/Library/Application Support/Plex Media Server/Plug-ins
		
		Western Digital
			/mnt/HD/HD_a2/plex_conf/Plex Media Server/Plug-ins
		
		Western Digital Wireless Pro
			.wdcache/.plexmediaserver/Plex Media Server/Plug-ins
	
	If you can't find your Plug-ins folder check out this article:
	https://support.plex.tv/hc/en-us/articles/201106098-How-do-I-find-the-Plug-Ins-folder-
	
Step 2:
	Copy the file "kmtvbeta.bundle" inside that folder.
	
Step 3:
	Open the "kmtvbeta.bundle" folder and edit the file Contents/Code/__init__.py
	Change the value of the variable on the first line (APIURL) to the URL you want to be your JSON back-end

Step 4:
	Open the Plex Media Center (usually at http://127.0.0.1:32400/web/index.html) and click in the left menu on "Channels"

Your plugin is now installed!