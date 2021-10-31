#MADE BY SIDTHEMINER
#Twitter @SidTheMiner
#Youtube SIDTHEMINER 
#Hope you like the project
# I am a beginner so forgive me if I made some mistakes.
#Have a good day :)




####MODULES IMPORT####

from pyshorteners import Shortener
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pyperclip

#Screen
screen=Tk()
screen.title("URL-Shortener")
screen.geometry("1100x650")
screen.configure(background='#232323')
screen.resizable(width=False, height=False)


####VARIABLES####
link_get=StringVar()
Selected_api=StringVar()
link_Final_set=StringVar()


###########################FUNCTIONS########################################



####MAIN FUNCTION#####


def shortener_main():

    s = Shortener()
    
    if Selected_api.get()=='TinyURL':
        Short_link=s.tinyurl.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Chilp.it':
        Short_link=s.chilpit.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Da.gd':
        Short_link=s.dagd.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Git.io(Only Github urls)':
        Short_link=s.gitio.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Is.gd':
        Short_link=s.isgd.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Osdb.link':
        Short_link=s.osdb.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Qps.ru':
        Short_link=s.qpsru.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='NullPointer':
        Short_link=s.nullpointer.short(link_get.get())
        link_Final_set.set(Short_link)
		
    elif Selected_api.get()=='Clck.ru':
        Short_link=s.clckru.short(link_get.get())
        link_Final_set.set(Short_link)
	
    




####COPY FUNCTION####	

def Copy_Link():
    pyperclip.copy(link_Final_set.get())


####CONVERT BUTTON HOVER ANIMATION####

def on_enter_convert(e):
   Convert_btn.config(image=Con_btn_render1, bd=0,bg='#161616',activebackground="#161616",background='#232323')


def on_leave_convert(e):
   Convert_btn.config(image=Con_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323')


####COPY BUTTON HOVER ANIMATION#### 


def on_enter_copy(e):
   Copy_btn.config(image=Copy_btn_render1, bd=0,bg='#161616',activebackground="#161616",background='#232323')


def on_leave_copy(e):
   Copy_btn.config(image=Copy_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323')





########################WINDOW SETUP##################################







#inner frames

#frame1
frame1 = Frame(screen,bg="white")
frame1.pack(pady=150)

#frame2
frame2 = Frame(frame1,bg="#161616",width=850,height=650)
frame2.pack(pady=0.5,padx=0.5)


#heading

#heading image load
Heading_load= Image.open(r"Images\Heading.png")
Heading_render = ImageTk.PhotoImage(Heading_load)

#heading image display
img = Label(screen, image=Heading_render,background='#232323')
img.place(x="285",y="30")


#paste image load
Paste_link_load= Image.open(r"Images\button_paste-link.png")
Paste_link_render = ImageTk.PhotoImage(Paste_link_load)

#paste image display
img1 = Label(screen, image=Paste_link_render,background='#232323',bd=0)
img1.place(x="150",y="200")




####LINK ENTRY####
Link=Entry(screen,textvariable=link_get,font="Courier 10",fg="#FFD700",bg="#161616", ).place(x=265,y=207,width=670,height=30)


###COMBO BUTTON FOR URL SHORTENERS####

#Api Image load
Sel_API_load= Image.open(r"Images\button_select-url-shortener-leave-tinyurl-for-default-if-none.png")
Sel_API_render = ImageTk.PhotoImage(Sel_API_load)

#Api Image display
img2 = Label(screen, image=Sel_API_render,background='#232323',bd=0)
img2.place(x="150",y="250")


#Combo button
API=('TinyURL','Chilp.it','Da.gd','Git.io(Only Github urls)','Is.gd','Osdb.link','Qps.ru','NullPointer','Clck.ru')
API_CB=ttk.Combobox(screen, textvariable=Selected_api)
API_CB['values']=API
API_CB['state'] = 'readonly'
API_CB.current(0)
API_CB.place(x=650,y=255,width=280,height=30)


####CONVERT BUTTON####


#Button Image2 load
Con_btn_load1= Image.open(r"Images\button_convert (2).png")
Con_btn_render1 = ImageTk.PhotoImage(Con_btn_load1)

#Button Image1 load
Con_btn_load= Image.open(r"Images\button_convert (1).png")
Con_btn_render = ImageTk.PhotoImage(Con_btn_load)

#Button
Convert_btn = Button(screen, image=Con_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323',command=shortener_main)
Convert_btn.place(x=450,y=300)

#Bind
Convert_btn.bind('<Enter>', on_enter_convert)
Convert_btn.bind('<Leave>', on_leave_convert)



####FINAL RESULT DISPLAY####


Result_load= Image.open(r"Images\Final.png")
Result_render = ImageTk.PhotoImage(Result_load)
img3 = Label(screen, image=Result_render,background='#232323',bd=0)
img3.place(x="150",y="365")

#display entry
Final_Link=Entry(screen,textvariable=link_Final_set,font="Courier 15",fg="#FFD700",bg="#161616", ).place(x=160,y=369,width=670,height=30)




####COPY BUTTON####


#Copy Button Image 2 load
Copy_btn_load1= Image.open(r"Images\button_copy (2).png")
Copy_btn_render1 = ImageTk.PhotoImage(Copy_btn_load1)

#Copy Button image 1 load

Copy_btn_load= Image.open(r"Images\button_copy (1).png")
Copy_btn_render = ImageTk.PhotoImage(Copy_btn_load)

#Button
Copy_btn = Button(screen, image=Copy_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323', command=Copy_Link)
Copy_btn.place(x=837,y=369)

#Bind
Copy_btn.bind('<Enter>', on_enter_copy)
Copy_btn.bind('<Leave>', on_leave_copy)




####NAME DISPLAY####

Name_load= Image.open(r"Images\button_made-by-sidtheminer.png")
Name_render = ImageTk.PhotoImage(Name_load)
img4 = Label(screen, image=Name_render,background='#232323',bd=0)
img4.place(x=860,y=610)


####LOOP####
screen.mainloop()

####HOPE YOU LIKED IT :)

		

