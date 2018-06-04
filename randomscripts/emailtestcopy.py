import smtplib

t = 80

content = 'Do not shut down your computer when you leave'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('incongnitoanonymous@gmail.com', 'thomas00')

while t > 0:
  
  mail.sendmail('incongnitoanonymous@gmail.com', 'alexander.errington@gmail.com', content)
  t -= 1
  print('email sent '+ str(t))
  
mail.close()
