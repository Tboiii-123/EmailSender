from tkinter import *
from tkinter import messagebox
#The meaning of smtplib is simple mail transfer protocol
import smtplib



#function
def reset():
    
        email_input.delete(0,END)
        password_input.delete(0,END)
        to_email_input.delete(0,END)
        subject_input.delete(0,END)
        content_input.delete("1.0",END)

        messagebox.showinfo('','DATA CLEARED SUCCESSFULLY')

def send():
    try:
        emailName=temp_email.get()
        passwordName=temp_password.get()
        to_emailName=temp_to_email.get()
        subjectName=temp_subject.get()
        contentName=temp_content.set(content_input.get("1.0",END))  
        if emailName=="" or passwordName =="" or to_emailName=="" or subjectName=="" or contentName=="":
            messagebox.showwarning('Warning',"ALL ENTRIES MUST BE FILLED")
        else:
            Message ='Subject : {}\n\n{}'.format(subjectName,contentName)

            #Server connecting to the SMTP server
            server =smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(emailName,passwordName)
            server.sendmail(emailName,to_emailName,Message)
            messagebox.showinfo('','MESSAGE HAS BEEN SENT SUCCESSFULLY')
    except :
        messagebox.showerror('','MESSAGES HAS NOT BEEN SENT DUE TO AN ERROR DETECTION')
        
#Main screen
root =Tk()
root.title("Email")
root.geometry('840x650')
root.configure(bg='black')
root.resizable(False,False)
#Graphics


label1 =Label(root,text="Use the form below to send message",font=('Calibri',27),fg='white',bg='black')
label1.place(x=130,y=0)



#storage

temp_email =StringVar()
temp_password=StringVar()
temp_to_email =StringVar()
temp_subject =StringVar()
temp_content=StringVar()

#Widget for Label
email =Label(root,text=" Your Email :",font=("Helvetica",14),fg='white',bg='black')
email.place(x=10,y=100)

password =Label(root,text="Your Password :",font=("Helvetica",14),fg='white',bg='black')
password.place(x=10,y=140)

to_email =Label(root,text="Recipient Email :",font=("Helvetica",14),fg='white',bg='black')
to_email.place(x=10,y=180)

subject =Label(root,text="Subject :",font=("Helvetica",14),fg='white',bg='black')
subject.place(x=10,y=220)

content =Label(root,text="Message :",font=("Helvetica",14),fg='white',bg='black')
content.place(x=10,y=260)


#Widget for Entry
email_input =Entry(root,bd=3,width=54,textvariable=temp_email,font=("Helvetica",12))
email_input.insert(0,'lawalhussein775@gmail.com')

email_input.place(x=190,y=100)

password_input =Entry(root,bd=3,width=54,show="*",textvariable=temp_password,font=("Helvetica",12))
password_input.insert(0,'kcgx gurr ejub gdwp')
password_input.place(x=190,y=140)

#The show is to make the entryshow the desired sign denoted 



to_email_input =Entry(root,bd=3,width=54,textvariable=temp_to_email,font=("Helvetica",12))
to_email_input.place(x=190,y=180)

subject_input =Entry(root,bd=3,width=54,textvariable=temp_subject,font=("Helvetica",12))
subject_input.place(x=190,y=220)

content_input =Text(root,width=79,height=18,wrap=WORD)
content_input.place(x=190,y=260)



Login=Button(root,text='SEND',width=15,height=2,bg='green',fg='white',relief='raised',command=send)
Login.place(x=180,y=570)

def Exit():
     root.quit()
button=Button(root,text="CANCEL",bg="red",fg='white',width=15,height=2,cursor="target",command=Exit)
button.place(x=380,y=570)

Reset=Button(root,text="RESET",bg="blue",fg='white',width=15,height=2,command=reset)
Reset.place(x=580,y=570)


status=Label(root,text='Mail in Process.....',bd=5,relief='raised')
status.pack(side=BOTTOM,fill=X)



root.mainloop()
