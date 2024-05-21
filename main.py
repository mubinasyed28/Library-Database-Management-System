from tkinter import *
import tkinter.messagebox
import LibBksDatabase

class library():

    def __init__(self,root):
        self.root=root
        self.root.title("Library Database Management System")
        self.root.geometry("1920x1080+15+15")

        Mty = StringVar()
        Ref_id = StringVar()
        fna = StringVar()
        sna = StringVar()
        Adr = StringVar()
        pc = StringVar()
        MNo = StringVar()
        BkID = StringVar()
        BkTit= StringVar()
        Author = StringVar()
        Db = StringVar()
        Dd= StringVar()
        LRF= StringVar()
        DOD= StringVar()

        ############################### Function Declaration #########################################

        def iExit ():
            iExit=tkinter.messagebox.askyesno("Library Database Management Systems","Confirm if you want to exit?")
            if iExit >0:
                root.destroy()
                return

        def ClearData():
            self.txtMtype.delete(0,END)
            self.txtBkID.delete(0,END)
            self.txtRef_id.delete(0,END)
            self.txtBkTit.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtpc.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDb.delete(0,END)
            self.txtDOD.delete(0,END)
            self.txtMNo.delete(0,END)
            self.txtLRF.delete(0,END)
            self.txtDd.delete(0,END)
            self.txtAuthor.delete(0,END)

        def addData():
            if(len(Mty.get())!=0):
                LibBksDatabase.addDataRec (Mty.get(), Ref_id.get(), fna.get(), sna.get(), Adr.get(), pc.get(),
                                           MNo.get(), BkID.get(), BkTit.get(), Author.get(), Db.get(), Dd.get(),
                                           LRF.get(), DOD.get())

                booklist.delete(0,END)
                booklist.insert(END, (Mty.get(), Ref_id.get(), fna.get(), sna.get(), Adr.get(), pc.get(),
                                      MNo.get(), BkID.get(), BkTit.get(), Author.get(), Db.get(), Dd.get(),
                                      LRF.get(), DOD.get()))

        def DisplayData():
            booklist.delete(0,END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END,row)

        def SelectedBook(event):
            global sb
            searchBk = booklist.curselection()
            sb = booklist.get(searchBk)

            self.txtMtype.delete(0, END)
            self.txtMtype.insert(END,sb[1])

            self.txtRef_id.delete(0, END)
            self.txtRef_id.insert(END, sb[2])

            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sb[3])

            self.txtsna.delete(0, END)
            self.txtsna.insert(END, sb[4])

            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sb[5])

            self.txtpc.delete(0, END)
            self.txtpc.insert(END, sb[6])

            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END, sb[7])

            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END, sb[8])

            self.txtBkTit.delete(0, END)
            self.txtBkTit.insert(END, sb[9])

            self.txtAuthor.delete(0, END)
            self.txtAuthor.insert(END, sb[10])

            self.txtDb.delete(0, END)
            self.txtDb.insert(END, sb[11])

            self.txtDd.delete(0, END)
            self.txtDd.insert(END, sb[12])

            self.txtLRF.delete(0, END)
            self.txtLRF.insert(END, sb[13])

            self.txtDOD.delete(0, END)
            self.txtDOD.insert(END, sb[14])

        def DeleteData():
            if(len(Mty.get()) !=0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            booklist.delete(0, END)
            for row in LibBksDatabase.searchData(Mty.get(), Ref_id.get(), fna.get(), sna.get(), Adr.get(), pc.get(), \
                                                 MNo.get(), BkID.get(), BkTit.get(), Author.get(), Db.get(), Dd.get(), \
                                                 LRF.get(), DOD.get()):
                booklist.insert(END, row)

        def update():
            if(len(Mty.get()) != 0):
                LibBksDatabase.dataUpdate(sb[0], Mty.get(), Ref_id.get(), fna.get(), sna.get(), Adr.get(), pc.get(), \
                                                 MNo.get(), BkID.get(), BkTit.get(), Author.get(), Db.get(), Dd.get(), \
                                                 LRF.get(), DOD.get())

        ################################### Frames ####################################################

        MainFrame= Frame(self.root)
        MainFrame.grid()

        #Tittle frame
        TitFrame= Frame(MainFrame, bd=2, padx=375, pady=6, bg='dark slate gray', relief=FLAT)
        TitFrame.pack(side=TOP)
        #TitFrame.place(relx=0.05, rely=0.05)

        self.lblTit = Label(TitFrame, font=('times new roman', 28, 'bold'), width=35 , text="Library Database Management Systems", anchor='center', justify='center')
        self.lblTit.grid(sticky=W)

        #bottom data sectior
        ButtonFrame = Frame(MainFrame, bd=2, width=1920, height=1080, padx=20, pady=20, bg="gray", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        #ButtonFrame.place(relx=0.5, rely=1, anchor='se')

        FrameDetail= Frame(MainFrame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame= Frame(MainFrame, bd=1, width=1350, height=400, padx=20, pady=50, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT= LabelFrame(DataFrame, bd=1, width=1500, height=1000, padx=21, pady=21 , relief=RIDGE
                                  , font=('arial black', 13, 'bold'), text="Library Membership Info:", bg="gray42")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT= LabelFrame(DataFrame, bd=1, width=1500, height=1000, padx=20, pady=21, relief=RIDGE
                                   , font=('arial black', 12, 'bold'), bg="gray42", text="Book Details:")
        DataFrameRIGHT.pack(side=RIGHT)

        ################################### Entry ####################################################

        self.lblMemberType = Label(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), text="Member Type:", padx=12, pady=12,
                                   bg="gray42")
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.txtMtype= Entry(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), textvariable=Mty, width=25)
        self.txtMtype.grid(row=0, column=1)

        self.lblBkID= Label(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), text="Book ID:", padx=12, pady=12, bg="gray42")
        self.lblBkID.grid(row=0, column=2, sticky=W)
        self.txtBkID= Entry(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), textvariable= BkID, width=25)
        self.txtBkID.grid(row=0, column=3)

        self.lblRef_id = Label(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), text= 'Reference/Roll no:', pady=12, padx=12,
                               bg="gray42")
        self.lblRef_id.grid(row=1, column=0, sticky=W)
        self.txtRef_id = Entry(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), textvariable= Ref_id, width=25)
        self.txtRef_id.grid(row=1, column=1)

        self.lblBkTit = Label(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), text= 'Book Tittle:', padx=12, pady=12,
                              bg= 'gray42')
        self.lblBkTit.grid(row=1, column=2, sticky=W)
        self.txtBkTit = Entry(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), textvariable=BkTit, width=25)
        self.txtBkTit.grid(row=1, column=3)

        self.lblfna = Label(DataFrameLEFT, font=('dutch801 rm bt', 13, 'bold'), text='First Name:', padx=12, pady=12,
                            bg= 'gray42')
        self.lblfna.grid(row=2,column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable=fna, width=25)
        self.txtfna.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Author:', padx=12, pady=12,
                               bg= 'gray42')
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable=Author, width=25)
        self.txtAuthor.grid(row=2, column=3)

        self.lblsna = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Surname:', padx=12, pady=12,
                            bg= 'gray42')
        self.lblsna.grid(row=3, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable=sna, width=25)
        self.txtsna.grid(row=3, column=1)

        self.lblDb = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Data Borrowed:', padx=12, pady=12,
                           bg='gray42')
        self.lblDb.grid(row=3,column=2, sticky=W)
        self.txtDb = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'),textvariable= Db, width=25)
        self.txtDb.grid(row=3, column=3)

        self.lblAdr = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text="Address:", padx=12, pady=12,
                            bg='gray42')
        self.lblAdr.grid(row=4, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= Adr, width=25)
        self.txtAdr.grid(row=4, column=1)

        self.lblDd = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Date Due:', padx=12, pady=12,
                           bg='gray42')
        self.lblDd.grid(row=4, column=2, sticky=W)
        self.txtDd = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= Dd, width=25)
        self.txtDd.grid(row=4, column=3)

        self.lblpc = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Pin Code:', padx=12, pady=12,
                           bg='gray42')
        self.lblpc.grid(row=5, column=0, sticky=W)
        self.txtpc = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= pc, width=25)
        self.txtpc.grid(row=5, column=1)

        self.lblLRF = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Late Return Fine:', padx=12, pady=12,
                            bg='gray42')
        self.lblLRF.grid(row=5, column=2, sticky=W)
        self.txtLRF = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= LRF, width=25)
        self.txtLRF.grid(row=5, column=3)

        self.lblMNo = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Mobile Number:', padx=15, pady=15,
                            bg='gray42')
        self.lblMNo.grid(row=6, column=0, sticky=W)
        self.txtMNo = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= MNo, width=25)
        self.txtMNo.grid(row=6, column=1)

        self.lblDOD = Label(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), text='Date Over Due:', padx=15, pady=15,
                            bg='gray42')
        self.lblDOD.grid(row=6, column=2, sticky=W)
        self.txtDOD = Entry(DataFrameLEFT,  font=('dutch801 rm bt', 13, 'bold'), textvariable= DOD, width=25)
        self.txtDOD.grid(row=6, column=3)

        ########################### Listbox and Scrollbox ###############################

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = Listbox(DataFrameRIGHT, width=45, height=17, font=('dutch801 rm bt', 12, 'bold'), yscrollcommand= scrollbar.set)
        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        ########################### Bottom Widget ################################

        self.btnAddDate= Button(ButtonFrame, text= 'Add Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=18, bd=4,
                                command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text='Display Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)


        self.btnClearData = Button(ButtonFrame, text='Clear Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=ClearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Delete Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdateData = Button(ButtonFrame, text='Update Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, text='Search Data', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('AngsanaUPC', 14, 'bold'), height=2, width=16,
                                 bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__=='__main__':
    root=Tk()
    application= library(root)
    root.mainloop()
