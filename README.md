# auto_email
a python tool that sends a message to multiple gmails at the same time without getting blocked as spam,you can chose the gmail that you want to send with and also you can chose the message you want to sent, and you can choose your targets.

# usage :

#1- APPS PASSWORD : you need to set an app password for your gmail so you can login to the
<br>
tool, and you can do that by simply go to https://myaccount.google.com/  > login with your 
<br>
gmail > two-step verifaction > apps paasword > create new app password 
<br>

#2- INSTALL LIBRARIES : open terminal or cmd and print this code :
<br>
#for windows :
<br>
_ open cmd (windows+R print cmd then enter)
<br>
_ paste : winget install python.python.3.11
<br>
_ paste : pip install smrplib MIMEText MIMEMultipart time
<br>
#for linux(Ubuntu/Debian/Mint) :
<br>
_ open terminal
<br>
_paste : 
  <br>
  sudo apt update
  <br>
  sudo apt install python3 python3-pip
  <br>
  python3-venv
 <br> 
  pip3(or pip) install smrplib MIMEText MIMEMultipart time
<br>
#(Arch linux) :
<br>
_ open terminal
<br>
_paste : 
<br>
  sudo pacman -s python python-pip
<br>  
  pip3 install smrplib MIMEText MIMEMultipart time
<br>
#(Fedora):
<br>
_ open terminal
<br>
_paste : 
<br>
  sudo dnf install python3 python3-pip
  <br> 
  pip3 install smrplib MIMEText MIMEMultipart time
<br>
#3_ CHOSING TARGETS:
<br>
in the same folder with the tool there's a file with the name "targets.txt" open that file and fill it with the gmails that you want to send to 
<br>
#4_ RUN TOOL:
<br>
just use the command : python3 auto_emails.py 
notice : make sure that you are at the same path as the tool before printing this command and you can do that by printing : cd path_to_tool
<br>
 if you needed any help text me:
<br>
   insta : @u.cb0
   <br>
   gmail : adibbouache@gmail.com
