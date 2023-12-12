import tkinter as tk
import csv
import readwritecsv as rw
import os

path = os.getcwd()


noteicon = os.path.join(path,'note.ico')


#functionwrtite csv file


#window
win = tk.Tk()
win.title('เก็บข้อมูล')
win.geometry('500x500')
win.iconbitmap(noteicon)

f1 = tk.Frame(win)
f1.place(x=20,y=50)

####### screen #####


string_value = tk.StringVar()

#label
label1 = tk.Label(f1,text='กรุณากรอกใส่ช่อง').pack(pady=20)


#entry
en1 = tk.Entry(f1,textvariable=string_value,bg='red').pack()

#label2
label2 = tk.Label(f1,text='กรุณากรอกช่อมูลตามความเปนจริงนะจ๊ะ').pack(pady=20)

#text
textt = tk.Text(f1,height=8,width=56)
textt.pack(pady=20)


def save():
    valu = string_value.get()
    text = textt.get(1.0,'end-1c')
    
    print(valu)
    print(text)
    data = [valu,text]
    rw.writecsv(data)

    #cleardata in entry
    string_value.set('')
    #cleardata in text
    textt.delete(1.0,'end-1c')

#button
b1 = tk.Button(f1,text='Okay',command=save)
b1.pack(pady=10)

#####note button#######

detaillist = rw.readcsv()

global countindex
countindex = 0


#2nd window
def Note():
    win2 = tk.Toplevel()
    win2.geometry('500x400')
    win2.title('รายละเอียด')

    topic = tk.StringVar()
    detail = tk.StringVar()

    #label
    la1 = tk.Label(win2,textvariable=topic)
    la1.pack()
    topic.set(detaillist[0][0])

    la2 = tk.Label(win2,textvariable=detail)
    la2.pack()
    detail.set(detaillist[0][1])

    def BPrev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex-1
        
        topic.set(detaillist[countindex][0])
        detail.set(detaillist[countindex][1])

    def BNext():
        global countindex
        if countindex == (len(detaillist)-1):
            countindex = len(detaillist)-1
        else:
            countindex = countindex+1
        
        topic.set(detaillist[countindex][0])
        detail.set(detaillist[countindex][1])

    
    bpre = tk.Button(win2,text='<',command=BPrev)
    bpre.place(x=60,y=350) 


    bnext = tk.Button(win2,text='>',command=BNext)
    bnext.place(x=400,y=350)

    


    win2.mainloop()

notebutton = os.path.join(path,'note.png')
noteicon = tk.PhotoImage(file=notebutton)
bflashcard = tk.Button(win,image=noteicon,command=Note)
bflashcard.place(x=400,y=20)







win.mainloop()

