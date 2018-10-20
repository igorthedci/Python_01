
import smtplib
help(smtplib)
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login('your_test_login@gmail.com'. '******')
help(smtp_object.sendmail)
smtp_object.sendmail(from_addr='', to_addr='', msg="it's work!")
smtp_object.sendmail(from_addr='', to_addr=['', ''], msg="it's work!")
smtp_object.quit()

