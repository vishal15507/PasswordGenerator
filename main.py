from tkinter import Tk,Entry,Button,Label,Canvas,PhotoImage
from tkinter import messagebox
import pyperclip


windows=Tk()
windows.title("password manager")
windows.config(padx=20,pady=20,bg="#9bdeac")
canvas=Canvas(height=250,width=200,bg="#9bdeac",highlightthickness=0)
logo_img=PhotoImage(file="sun.gif")
pass_img=PhotoImage(file="pass.png")
canvas.create_image(100,100,image=logo_img)
canvas.create_image(100,200,image=pass_img)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website",width=15,font=("arial",10,"bold"),bg="#9bdeac",highlightthickness=1)
website_label.grid(row=2,column=0)
email_label=Label(text="Email/Username",width=15,font=("arial",10,"bold"),bg="#9bdeac",highlightthickness=1)
email_label.grid(row=3,column=0)
password_label=Label(text="password",width=15,font=("arial",10,"bold"),bg="#9bdeac",highlightthickness=1)
password_label.grid(row=4,column=0)

text=Label(text="",bg="#9bdeac")
text.grid(column=1,row=1,)
#entries
website_entry=Entry(width=35,font=("arial",12))
website_entry.grid(row=2,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35,font=("arial",12))
email_entry.grid(row=3,column=1,columnspan=2)
email_entry.insert(0,"vishalthool15507@gmail.com")
password_entry=Entry(width=22,font=("arial",12))
password_entry.grid(row=4,column=1)

def generatePassword():
    password = password_entry.get()
    if len(password)!=0:
        password_entry.delete(0,len(password))



    import random
    small_letters=["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap_letter=[letter.upper() for letter in small_letters]
    number=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')']

    password_sletter=[(random.choice(small_letters)) for i in range(random.randint(3,7))]
    password_cletter=[(random.choice(cap_letter)) for i in range(random.randint(2,4))]
    password_num=[(random.choice(number)) for i in range(random.randint(2,4))]
    password_symbol=[(random.choice(symbols)) for i in range(random.randint(2,4))]

    password_list=password_symbol+password_num+password_cletter+password_sletter
    random.shuffle(password_list)

    p="".join(password_list)
    print(f"password={p}")
    password_entry.insert(0,p)
    pyperclip.copy(p)

def generate_file():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="message",message="you have left some fields empty")

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are the details entered:\nEmail={email}"
                                                     f"\nPassword:{password}\nis it ok to save")
        if is_ok:

            with open("data.txt","a") as file:
                file.write(f"{website}  ||  {email}   ||  {password}\n")
                website_entry.delete(0, len(website))
                password_entry.delete(0, len(password))


    #messagebox.showinfo(title="Message",message="password saved")





#buttons
generate_password_button=Button(text="Generate Password",command=generatePassword)
generate_password_button.grid(column=2,row=4)
add_button=Button(text="Add",bg="#f7f5dd",width=16,command=generate_file)
add_button.grid(row=5,column=1,columnspan=2)



windows.mainloop()