import smtplib
from email.mime.text import MIMEText
from sms import PROVIDERS
username = "egclearance@gmail.com"
password = "fcormefybepkdoet"

vtext = "251902229324@vtext.com"
message = "this is the message to be sent"

msg = MIMEText("""From: %s
To: %s
Subject: text-message
%s""" % (username, vtext, message))

server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
server.login(username,password)
server.sendmail(username, vtext, msg.as_string())
server.quit()


 if total<=100 and total >=90:
           grade="A+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<90 and total >=85:  
           grade= "A"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<85 and total >=80:  
           grade= "A-"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<80 and total >=75:  
           grade= "B+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<75 and total >=70:  
           grade= "B"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<70 and total >=65:  
           grade= "B-"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<65 and total >=60:  
           grade= "C+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<60 and total >=50:  
           grade= "C"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<50 and total >=40:  
           grade= "D"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       elif total<40 and total >=0:  
           grade= "F"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('../')
       else:
           print("invalid mark my exed or less than o please check it")
           return redirect('../')
       
       
    else:
        