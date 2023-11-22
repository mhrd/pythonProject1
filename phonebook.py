from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# اتصال به دیتابیس MySQL
db = mysql.connector.connect(
   host="localhost",
   user="your_username",
   password="your_password",
   database="phonebook"
)

# Cursor برای اجرای کوئری ها
cursor = db.cursor()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
   name = request.form['name']
   phone_number = request.form['phone_number']

   # اضافه کردن اطلاعات به جدول
   cursor.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone_number))
   db.commit()

   return redirect('/')

@app.route('/show_contacts')
def show_contacts():
   # دریافت تمام اطلاعات از جدول
   cursor.execute("SELECT * FROM contacts")
   contacts = cursor.fetchall()

   return render_template('show_contacts.html', contacts=contacts)

if __name__ == '__main__':
   app.run(debug=True)
