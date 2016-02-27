#!/usr/bin/env python3
from pushbullet import Pushbullet
from time import strftime

#Set all variables here
pb = Pushbullet("o.YZqCGqReW0YkjrA7iPJCenRJUIpUPAMM")
time = strftime ("%a %I:%M%p")
title = "Mailbox Alert"
msg = "You have received a package on %s" %(time)

#Clear any previous push notifications
#Pushbullet will resend if not done
pushes = pb.get_pushes()
if pushes:
	latest = pushes[0]
	pb.dismiss_push(latest.get("iden"))
	pb.delete_push(latest.get("iden"))

#Push notification to all devices connected to key
push = pb.push_note(title, msg)
