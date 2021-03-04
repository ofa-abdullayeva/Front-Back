from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(120))
    subject = db.Column(db.String(220))
    message = db.Column(db.String(255))



@app.route('/',methods=['GET','POST'])
def index():
   if request.method=='POST':
      ad=request.form['fullname']
      email=request.form['email']
      movzu=request.form['movzu']
      mesaj=request.form['mesaj']
      gonderilenmesaj=Message(fullname=ad,email=email,subject=movzu,message=mesaj)
      db.session.add(gonderilenmesaj)
      db.session.commit()
      return redirect('/admin')

   return render_template('index.html')



@app.route('/admin')
def admin():
   mesajlar=Message.query.all()
   return render_template('admin.html',data=mesajlar)


@app.route('/delete/<id>')
def delete(id):
   silinecekolanmesaj=Message.query.get(id)
   db.session.delete(silinecekolanmesaj)
   db.session.commit()
   return redirect('/admin')

@app.route('/goster/<id>') 
def goster(id):
   gosterilecekolanmesaj=Message.query.get(id)
   return render_template('mesaj.html',mesaj=gosterilecekolanmesaj)  


@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
   deyisdirilecekolanmesaj=Message.query.get(id)
   if request.method=='POST':
      ad=request.form['fullname']
      email=request.form['email']
      movzu=request.form['movzu']
      mesaj=request.form['mesaj']
      deyisdirilecekolanmesaj.fullname=ad
      deyisdirilecekolanmesaj.email=email
      deyisdirilecekolanmesaj.subject=movzu
      deyisdirilecekolanmesaj.message=mesaj
      db.session.add(deyisdirilecekolanmesaj)
      db.session.commit()
      return redirect('/admin')

   return render_template('update.html',mesaj=deyisdirilecekolanmesaj)
if __name__=='__main__':
    app.run(debug=True)   