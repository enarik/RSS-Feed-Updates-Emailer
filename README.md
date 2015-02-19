# RSS-Feed-Updates-Emailer
This will parse an rss feed and email you updates as they become available.

fromaddr = "fromemail same as server.login"      ~~~ The email that will be the "send from" email\

toaddr = "to email"                              ~~~ The email that it will be sent to

msg['Subject'] = "Subject of Email"              ~~~ = Subject of Email

body = "Body of Email"                           ~~~ = Body of email

server = smtplib.SMTP('smtpserver', smtpport)    ~~~ = your smtp server and port (Gmail is smtp.gmail.com and port 587)

server.login("email@host.com", "password")       ~~~ = from email address and password



r = feedparser.parse('url of rss feed')          ~~~ = link to RSS feed

time.sleep(300)                                  ~~~ = time to refresh



I do not recommend using the email feature for a very frequently refreshed page unless you up the sleep time... unless you want a ton of emails.

Thanks!
