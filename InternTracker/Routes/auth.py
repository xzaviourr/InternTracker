import psycopg2,bcrypt
from Database.connection import Database
from Logger.logger import db_logger
from flask import Flask,request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

try :
    obj = Database()
    conn = obj.connect()
    cur = conn.cursor()
    print("Connected to the database successfully")

except Exception as e:
    db_logger.error("Error in connection to database")
    print(e)


# For registering a user
@app.route("/register",methods=["GET","POST"])
def register():
    print(request.json)
    if request.method == "POST":
        name=request.json.get("name")
        password=request.json.get("password")
        email=request.json.get("email")
        phone=request.json.get("phone")
        year=request.json.get("year")

        # Check if phone number already registered
        cur.execute(f"""SELECT * FROM users WHERE phone='{phone}' OR email='{email}';""")
        if(cur.rowcount):
            return {"ok":"false","message":"User already registered"}
        else:
            #Hash the password before storing 
            # hashed_password=str(bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()))
            # print(hashed_password)
            # print(hashed_password.split("'"))
            # print(("''").join(hashed_password.split("'")))
            # hashed_password = ("''").join(hashed_password.split("'"))


            # Add user in database
            cur.execute(f"""INSERT into users(user_id,name,password,email,phone,year) values (1,'{name}','{password}','{email}','{phone}','{year}');commit;""")
            
            return {"ok":"true"}



#For logging in a user
@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        field = request.json.get("email")
        password = request.json.get("password")

        #Fetch credentials from database
        cur.execute(f"""SELECT * FROM users WHERE email='{field}' OR phone='{field}';""")
        print(f"""SELECT * FROM users WHERE email='{field}' OR phone='{field}';""")

        if cur.rowcount==0:
            #Check if user exists
            return {"ok":"false","message":"user does not exist"}
        else:
            #Compare password and send response
            db_password = cur.fetchone()[2]

            if password==db_password:
                return {"ok":"true"}
            else:
                return {"ok":"false","message":"invalid credentials"}




if __name__ == "__main__":
    app.run(debug=True,port=80)