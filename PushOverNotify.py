#!/usr/bin/python3

'''
# Optional PushOver API vars.

   attachment - a binary image attachment to send with the message (documentation)
   attachment_base64 - a Base64-encoded image attachment to send with the message (documentation)
   attachment_type - the MIME type of the included attachment or attachment_base64 (documentation)
   device - the name of one of your devices to send just to that device instead of all devices (documentation)
   html - set to 1 to enable HTML parsing (documentation)
   priority - a value of -2, -1, 0 (default), 1, or 2 (documentation)
   sound - the name of a supported sound to override your default sound choice (documentation)
		pushover - Pushover (default)
		bike - Bike
		bugle - Bugle
		cashregister - Cash Register
		classical - Classical
		cosmic - Cosmic
		falling - Falling
		gamelan - Gamelan
		incoming - Incoming
		intermission - Intermission
		magic - Magic
		mechanical - Mechanical
		pianobar - Piano Bar
		siren - Siren
		spacealarm - Space Alarm
		tugboat - Tug Boat
		alien - Alien Alarm (long)
		climb - Climb (long)
		persistent - Persistent (long)
		echo - Pushover Echo (long)
		updown - Up Down (long)
		vibrate - Vibrate Only
		none - None (silent)
   timestamp - a Unix timestamp of a time to display instead of when our API received it (documentation)
   title - your message's title, otherwise your app's name is used
   ttl - a number of seconds that the message will live, before being deleted automatically (documentation)
   url - a supplementary URL to show with your message (documentation)
   url_title - a title for the URL specified as the url parameter, otherwise just the URL is shown (documentation)
'''

import http.client, urllib

POuser="DZIVGLX3AS7VF7CSDPPAX3BHCNLMVUMX"
POtokn="FYBZZIBJR62LL73SMJZMPWU33Z7YUGAR"
POhost="https://api.pushover.net"
POurl="/1/messages.json"

conn = http.client.HTTPSConnection(f"{POhost}:443")
conn.request(
	"POST", 
	POurl,
	urllib.parse.urlencode(
		{
			"token"		: POtokn,
			"user"		:  POuser,
			"message"	: "hello world",
		}
	), 
	{ "Content-type": "application/x-www-form-urlencoded" }
	)

conn.getresponse()

