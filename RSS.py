#-------------------------------------------------------------------------------
# Name:        RSS Feed parser and notifier
# Purpose:	   To parse a .rss feed and notify the user of updates via email
#
# Author:      enarik
#
# Created:     05/19/2014
# License:     MIT
#-------------------------------------------------------------------------------

import feedparser
import time
from datetime import datetime
from codecs import encode
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

known_items = set()

fromaddr = "fromemail same as server.login"
toaddr = "to email"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject of Email"
body = "Body of Email"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtpserver', smtpport)
server.ehlo()
server.starttls()
server.ehlo()
server.login("email@host.com", "password")
text = msg.as_string()


while True:
	# Parse feed
    r = feedparser.parse('url of rss feed')

	# Place title of each entry into the matches set, then dictionary
    _matches = set(r.entries)
    matches = {}
    for match in _matches:
        matches[match.title] = match
    new_items = set(matches.keys())-known_items
    for post in new_items:
        toprint = '%s ->--->---> %s\n'%(post,datetime.now())
		# To ignore nonprintable characters
        print toprint.encode('ascii','ignore')
        server.sendmail(fromaddr, toaddr, text)

    known_items.update(new_items)
    
	# Sleep and restart script after x seconds
    time.sleep(300)
