import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = '1928999500@qq.com'
receiver_email = '2748824570@qq.com'
password = 'nqsyvmkrdzzceegb'

# 创建邮件对象
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Test Email 测试邮件'

# 添加邮件正文
msg.attach(MIMEText('This is a test email.', 'plain'))

# 添加附件
filename = 'test.jpg'
with open(filename, 'rb') as file:
    attachment = file.read()
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

# 连接到SMTP服务器

try:
  with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('邮件发送成功')
except Exception as e:
  print(f'邮件发送失败: {e}')
