from flask import Flask, render_template, request,redirect

from mysqlconnection import MySQLConnector

app= Flask(__name__)

mysql=MySQLConnector(app,"full_friends")

@app.route('/')
def index():
    query = "SELECT * FROM Friends"
    friends = mysql.query_db(query)
    return render_template("index.html",friends=friends)

@app.route('/friends', methods=["POST"])
def register():
    query= "INSERT INTO Friends (first_name,last_name,email, created_at, updated_at) VALUES (:first_name, :last_name ,:emailname, NOW(), NOW() )"
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'emailname': request.form['email']
    }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit',methods=['POST'])
def edit_friend(friend_id):
    x=friend_id
    return render_template("edit_friends.html",x=x)

@app.route('/friends/<friend_id>/delete',methods=['POST'])
def delete_friend(friend_id):
    query = """DELETE FROM Friends
            WHERE id=:id"""
    data= {
        'id':friend_id
    }
    mysql.query_db(query, data)
    return redirect('/')



@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = """UPDATE Friends
             SET first_name = :first_name, last_name = :last_name, email=:email,updated_at=NOW()
             WHERE id = :id"""
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)
