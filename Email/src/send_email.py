import sys
import yaml
import pandas as pd

from getpass import getpass

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email import encoders


class Config():
    def __init__(self) -> None:
        pass
    
    def read_cfg(self, file_path):
        try:
            with open(file_path, "r") as f:
                cfg = yaml.safe_load(f)
                Header = cfg["Header"]
        except Exception as err:
            print(err)
        
        
        self.csv = cfg["csv"]
        
        self.From = cfg["From"] 
        self.CC = cfg["CC"]

        self.Subject = cfg["Subject"] 
        text = open(cfg["Body"], "r", encoding="utf-8")
        self.Body = text.read()


        self.Header_src = Header["src"]
        self.Header_width = Header["width"]
        self.Header_height = Header["height"]
        self.Header_id = Header["id"] 


    def read_csv(self):
        try:
            data = pd.read_csv(self.csv, encoding="utf-8")
        except:
            raise
        
        self.companies = data["会社名"]
        self.names = data["名前"]
        self.mails = data["メアド"]




class Mailer:
    """ メールを送信するクラス """

    # 初期化
    def __init__(self, cfg):        
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()

        self.addr_from = cfg.From

        login = False
        while not login:
            self.password = getpass()
            try:
                self.smtp.login(self.addr_from, self.password)            
                login = True
                # self.smtp.quit()
                print("[INFO] Successful.")
            except:
                print("[INFO] Incorrect password. Try again.")
                continue

            
        self.charset = "ISO-2022-JP"
        self.subject = cfg.Subject
        self.body = cfg.Body
        self.CC = cfg.CC
                
        # self.msg = MIMEText(self.body.encode(self.charset), 'plain', self.charset)
        self.msg = MIMEMultipart(self.charset)


    def attach(self, file_path):
        fname = open(file_path, "rb")
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload((fname).read())

        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('Content-Disposition', 'attachment; filename=  test.pdf')
        self.msg.attach(payload)
        
        
        embedImage = MIMEText('<img src="cid:image1" width="160" height="100"><br>', 'html')
        self.msg.attach(embedImage)
        msgText = MIMEText(self.body)
        self.msg.attach(msgText)
        
        #test images
        fp = open('../data/sample.PNG', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header("Content-ID", "<image1>")
        self.msg.attach(msgImage)

    def _send(self, email_to):
        # メールの設定
        # msg = MIMEText(self.body.encode(self.charset), 'plain', self.charset)
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.addr_from
        self.msg['To'] = email_to
        self.msg['CC'] = self.CC

        # gmailのsmtp経由で送信
        # self.smtp = smtplib.SMTP('smtp.gmail.com', 587)        
        # self.smtp.ehlo()
        # self.smtp.starttls()
        # self.smtp.ehlo()
        # self.smtp.login(self.addr_from, self.password)            

        self.smtp.send_message(self.msg)

        # self.smtp.close()

    def reset(self):        
        del self.msg 
        self.msg = MIMEMultipart(self.charset)
        msgText = MIMEText(self.body)
        self.msg.attach(msgText)

if __name__ == "__main__":

    yaml_path = sys.argv[1]


    cfg = Config()
    cfg.read_cfg(yaml_path)
    cfg.read_csv()

    mail_list = cfg.mails
    print(mail_list.values)

    Mail = Mailer(cfg)


    for tmp in mail_list:
        Mail._send(tmp)
        Mail.reset()

    
    # Mail._send("atam378@aucklanduni.ac.nz")
    
    
    
    # for name, company, email in zip(cfg.names, cfg.companies, mail_list):
    #     print(email)
        # Mail.reset()

    # for ttt in mail_list:

        # Mail._send(ttt)
