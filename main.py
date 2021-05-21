from flask import Flask, render_template, request
#from database import storeLogin, checkLogin, storeAccount, getAccount, storeTrans, storeMobile, storeFunds, updatePassword
from database import *
app = Flask(__name__)

# Pages routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About_us')
def About_us():
    return render_template('About_us.html')

@app.route('/Services')
def Services():
    return render_template('Services.html')
@app.route('/Contact_us')
def Contact_us():
    return render_template('Contact_us.html')

@app.route('/myaccount')
def myaccount():
    return render_template('myaccount.html')

@app.route('/trans')
def trans():
    return render_template('trans.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

@app.route('/funds')
def funds():
    return render_template('funds.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

# action routes
@app.route('/storeUser',methods=['POST','GET'])
def storeUser():
    if request.method=='POST':
        email = request.form['temail1']
        pass1 = request.form['tpass1']
        pass2 = request.form['tpass2']

        if pass1 != pass2:
            message='Password does not match'
            return render_template('message.html',mess=message)
        else:
            if storeLogin(email,pass1) == True:
                message = "Signup Successful !!"
            else:
                message = "Signup Failed !!"
            return render_template('message.html',mess=message)

@app.route('/checkUser',methods=['POST','GET'])
def loginUser():
    if request.method=='POST':
        email = request.form['temail']
        passw = request.form['tpass']
        if checkLogin(email,passw) == True:
            return render_template('userhome.html',user=email)
        else:
            message = "Login Failed !!"
        return render_template('message.html',mess=message)

@app.route('/createAccount',methods=['POST','GET'])
def createAccount():
    if request.method=='POST':
        email = request.form['temail']
        acno = request.form['tacno']
        amt = request.form['tamt']
        if storeAccount(email,acno,amt) == True:
            message="Account created Successfully !!"
            return render_template('usermess.html',mess=message)
        else:
            message = "Login Failed !!"
        return render_template('message.html',mess=message)

@app.route('/createTrans',methods=['POST','GET'])
def createTrans():
    if request.method=='POST':
        email = request.form['temail']
        acno = request.form['tacno']
        amt = request.form['tamt']
        type = request.form['type']

        if storeTrans(email,acno,amt,type) == True:
            message="Transaction is Successful !!"
            return render_template('usermess.html',mess=message)
        else:
            message = "Tranasction Failed !!"
        return render_template('message.html',mess=message)

@app.route('/createFunds',methods=['POST','GET'])
def createFunds():
    if request.method=='POST':
        email = request.form['temail']
        acno1 = request.form['tacno1']
        acno2 = request.form['tacno2']
        amt = request.form['tamt']


        if storeFunds(email,acno1,acno2,amt) == True:
            message="Fund Transfer is Successful !!"
            return render_template('usermess.html',mess=message)
        else:
            message = "Tranasction Failed !!"
        return render_template('message.html',mess=message)

@app.route('/createMobile',methods=['POST','GET'])
def createMobile():
    if request.method=='POST':
        email = request.form['temail']
        acno = request.form['tacno']
        amt = request.form['tamt']
        type = request.form['type']

        if storeMobile(email,acno,amt,type) == True:
            message="Mobile Recharge is Successful !!"
            return render_template('usermess.html',mess=message)
        else:
            message = "Mobile Recharge Failed !!"
        return render_template('message.html',mess=message)

@app.route('/showAccount',methods=['POST','GET'])
def showAccount():
    if request.method=='POST':
        email = request.form['temail1']
        acno = request.form['tacno1']

        amount = getAccount(email,acno)
        message="Balance in your account is " + str(amount) +" !!"
        return render_template('usermess.html',mess=message)

@app.route('/changePassword',methods=['POST','GET'])
def changePassword():
    if request.method=='POST':
        email = request.form['temail']
        oldp = request.form['told']
        newp1 = request.form['tnew1']
        newp2 = request.form['tnew2']

        if newp1 != newp2:
            message="Password not matched !!"
            return render_template('usermess.html',mess=message)
        else:
            if updatePassword(email,oldp,newp1) == True:
                message="Password updated successfully !!"
                return render_template('usermess.html',mess=message)



if __name__ == '__main__':
    app.run(debug=True)
