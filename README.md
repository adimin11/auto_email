# auto_email
a python tool that sends a message to multiple gmails at the same time without getting blocked as spam,you can chose the gmail that you want to send with and also you can chose the message you want to sent, and you can choose your targets.

# usage :

#1- APPS PASSWORD : you need to set an app password for your gmail so you can login to tha tool, and you can do that by simply go to https://myaccount.google.com/  > login with your gmail > two-step verifaction > apps paasword > create new app password 


#2- INSTALL LIBRARIES : open terminal or cmd and print this code :
#for windows :
_ open cmd (windows+R print cmd then enter)
_ paste : winget install python.python.3.11
_ paste : pip install smrplib MIMEText MIMEMultipart time
#for linux(Ubuntu/Debian/Mint) :
_ open terminal
_paste : 
  sudo apt update
  sudo apt install python3 python3-pip
  python3-venv
  pip3(or pip) install smrplib MIMEText MIMEMultipart time
#(Arch linux) :
_ open terminal
_paste : 
  sudo pacman -s python python-pip
  pip3 install smrplib MIMEText MIMEMultipart time
#(Fedora):
_ open terminal
_paste : 
  sudo dnf install python3 python3-pip
  pip3 install smrplib MIMEText MIMEMultipart time
#3_ CHOSING TARGETS:
in the same folder with the tool there's a file with the name "targets.txt" open that file and fill it with the gmails that you want to send to 
#4_ RUN TOOL:
just use the command : python3 auto_emails.py 
notice : make sure that you are at the same path as the tool before printing this command and you can do that by printing : cd path_to_tool
 if you needed any help text me:
   insta : @u.cb0
   gmail : adibbouache@gmail.com
