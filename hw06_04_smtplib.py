import smtplib
import json
# help(smtplib)


if __name__ == '__main__':
#
    with open(r"./tmp/mail_cred.json", encoding='utf-8') as cred_file:
        acc = cred_file.read()
        acc = json.loads(acc)
        # cred_file.close()
#
    # to_list = ["foumart@ukr.net"]
    to_list = ["foumart@ukr.net", "el.piankova@gmail.com", "smilly86@gmail.com"]
    smtp_server = 'smtp.gmail.com'  # smtp server
#
    with smtplib.SMTP(smtp_server, 587) as smtp_object:  # mail portal
        smtp_object.starttls()  # turn on encrypting
        smtp_object.login(acc['login'], acc['password'])
#    help(smtp_object.sendmail)
#
        msg = "From: %s\r\nTo: %s\r\nSubject: Homework_06_04\r\n It works!" % (acc['login'], ' ,'.join(to_list))
        smtp_object.sendmail(from_addr=acc['login'], to_addrs=to_list, msg=msg)
        smtp_object.quit()

