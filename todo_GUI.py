from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



class cust_win:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("800x550+0+0")#(1530x790)
        self.root.title("Hotel Management System ")
        
        #=================Title ================
        self.label=Label(self.root,text="To-Do-List",font=("time new ronin ",30,"bold"),width=10,bd=5,bg="burlywood",fg="black")
        self.label.place(x=0,y=0,width=800,height=60)
        
        # Background Image ======
        img1=Image.open(r"F:\Python Project\Hotel Management System\hotel images\back.jpg")
        img1=img1.resize((800,550),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        f_lbl.place(x=0,y=60,width=800,height=550)

        # ============
        self.label_1=Label(self.root,text="Create Task",font=("time new ronin ",20,"bold"),width=10,bd=5,bg="cadetblue2",fg="black")
        self.label_1.place(x=40,y=63,width=200,height=40)
        #============
        self.label_2=Label(self.root,text="Task List",font=("time new ronin ",20,"bold"),width=10,bd=5,bg="cadetblue2",fg="black")
        self.label_2.place(x=450,y=63,width=200,height=40)
        #===========================output Box =========================
        self.main_txt=Listbox(self.root,height=9,bd=4,width=23,font=("time new ronin",20,"bold"),bg="green")
        self.main_txt.place(x=380,y=110,width=400,height=400)
        
        
        
        
        #================ input box================
        self.text=Text(self.root,bd=5,height=2,width=30,font="ariel,10,bold")
        self.text.place(x=10,y=110)
        
        
        #================================ add function ===========================b 
        
        
        def add(): 
            contant=self.text.get(1.0,END)
            self.main_txt.insert(END,contant)
            with open('data.txt','a')as file:
                file.write(contant)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)
            
     
        
     #==========Delete Function ========================================       
        def delete():
            delete_=self.main_txt.curselection()
            look=self.main_txt.get(delete_)
            with open('data.txt','r+')as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_txt.delete(delete_)
        
        '''with open('data.txt','r')as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_txt.insert(END,ready)
            file.close()'''
            
        #==== Add Button==================================
        self.button=Button(self.root,text="Add",font="sarif,20  ",width=10 ,bd=5,bg="red",fg="black",command=add)
        self.button.place(x=30,y=200)
        #==== Delete Button ==================
        self.button_1=Button(self.root,text="Delete",font="sarif,20  ",width=10 ,bd=5,bg="red",fg="black",command=delete)
        self.button_1.place(x=30,y=250)
        #====Update=======
        self.button_1=Button(self.root,text="Update",font="sarif,20  ",width=10 ,bd=5,bg="red",fg="black",command=delete)
        self.button_1.place(x=150,y=200)
        
        # ====Trake ============
        self.button_1=Button(self.root,text="Trake",font="sarif,20  ",width=10 ,bd=5,bg="red",fg="black",command=delete)
        self.button_1.place(x=150,y=250)
    
    
        
        
            
        
        
        
        




__name__== "_main_"
root=Tk()
obj=cust_win(root)
root.mainloop()