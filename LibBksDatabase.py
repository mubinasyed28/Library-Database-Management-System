import sqlite3

def ConnectData():
    con=sqlite3.connect("libbooks.db")
    cur= con.cursor()
    #cur.execute("drop table libbooks;")
    #cur.execute("Create table if not exists libbooks (id INTEGER PRIMARY KEY, MTy text, Ref_id text,fna text, sna text,\
              #  Adr text, pc text, MNo text, BkID text, BkTit text, Author text, Db text, Dd text, LRF text, DOD text)")
    cur.execute("Create table if not exists libbooks (id INTEGER PRIMARY KEY, MTy text, BkID text,Ref_id text, BkTit text,\
                    fna text, Author text, sna text, Db text, Adr text, Dd text, pc text, LRF text, MNo text, DOD text)")
    con.commit()
    con.close()

def addDataRec(Mty,Ref_id,fna, sna,Adr, pc,MNo,BkID, BkTit, Author,Db,Dd, LRF, DOD):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (Mty,Ref_id,fna, sna,Adr, pc,MNo,BkID, BkTit, Author,Db,Dd, LRF, DOD))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("Select * from libbooks")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("Delete from libbooks where id=?", (id,))
    con.commit()
    con.close()

def searchData (Mty="",  Ref_id="",fna="",sna="",Adr="",pc="",MNo="",BkID="", BkTit="",  Author="",  Db="",  Dd="", \
                LRF="", DOD=""):
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("Select * from libbooks where MTY=? or Ref_id=? or fna=? or sna=? or Adr=?or pc=? or Author=? or BkID=? or BkTit=? or Db=? \
                or Dd=?  or LRF=? or MNo=? or DOD=?", \
                (Mty,Ref_id,fna, sna,Adr, pc,MNo,BkID, BkTit, Author,Db,Dd, LRF, DOD))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id, Mty="", Ref_id="", fna="", sna="", Adr="", pc="", MNo="", BkID="", BkTit="", Author="", Db="",\
                Dd="", LRF="", DOD=""):
    con= sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("Update libbooks set MTY=?, BkID=?, Ref_id=?, BkTit=?, fna=?, Author=?, sna=?, Db=?, \
                Adr=?, Dd=?, pc=?, LRF=?, MNo=?, DOD=?", \
                (Mty,Ref_id,fna, sna,Adr, pc,MNo,BkID, BkTit, Author,Db,Dd, LRF, DOD))
    con.commit()
    con.close()

ConnectData()
