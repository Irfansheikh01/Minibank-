import pymysql as pm

def storeLogin(email,passw):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query="insert into users values('%s','%s')" % (email,passw)
    cursor.execute(query)
    try:
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def storeAccount(email,acno,amt):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query="insert into account values('%s','%d','%f')" % (email,int(acno),float(amt))
    cursor.execute(query)
    try:
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def storeTrans(email,acno,amt,type):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    if type=='Deposit':
        query="update account set balance=balance+'%f' where acno='%d' and emailid='%s'" % (float(amt),int(acno),email)
    else:
        query = "update account set balance=balance-'%f' where acno='%d' and emailid='%s'" % (float(amt), int(acno), email)
    cursor.execute(query)
    try:
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def storeMobile(email,acno,amt,type):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query = "update account set balance=balance-'%f' where acno='%d' and emailid='%s'" % (float(amt), int(acno), email)
    cursor.execute(query)
    try:
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def storeFunds(email,acno1,acno2,amt):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query = "update account set balance=balance-'%f' where acno='%d' and emailid='%s'" % (float(amt), int(acno1), email)
    cursor.execute(query)
    try:
        con.commit()
        query="update account set balance=balance+'%f' where acno='%d' and emailid='%s'" % (float(amt), int(acno2), email)
        cursor.execute(query)
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def updatePassword(email,oldp,newp):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query = "update users set password='%s' where password='%s' and emailid='%s'" % (newp,oldp,email)
    cursor.execute(query)
    try:
        con.commit()
        status=True
    except:
        con.rollback()
        status=False
    con.close()
    return status

def getAccount(email,acno):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query="select * from account where emailid ='%s' and acno='%d'" % (email,int(acno))
    cursor.execute(query)
    data = cursor.fetchone()
    amount = data[2]
    return amount

def checkLogin(email,passw):
    con = pm.connect('localhost','root','admin','minibank')
    cursor = con.cursor()
    query="select * from users where emailid='%s' and password ='%s'" % (email,passw)
    cursor.execute(query)
    if cursor.rowcount == 1:
        status=True
    else:
        status=False
    con.close()
    return status

