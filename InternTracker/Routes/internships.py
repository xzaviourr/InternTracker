import psycopg2,bcrypt,json
from connection import Database
from logger import db_logger
from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from passlib.hash import sha256_crypt

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


# For brief data of all internships, with or without filters
@app.route("/internships/<page>",methods=["GET","POST"])
def internships(page):
    page=int(page)

    # To get all internships  
    if request.method == "GET":
        cur.execute(f"""SELECT internship_id,company_name,role,stipend_min,stipend_max FROM internships OFFSET {(page-1)*25} LIMIT 25""")
        data = cur.fetchall()
        return {"ok":"true","data":data}

    # To get filtered internships  
    elif request.method == "POST":
        query = f"""SELECT internship_id,company_name,role,stipend_min,stipend_max FROM internships"""
        
        #Sample request body
        '''{
            "category":"Web Development",
            "stipend":"10000"
            }'''

        #Applying filters
        category = request.json.get("category")
        stipends = request.json.get("deadline")
        if category and not stipends:
            query += f""" WHERE role='{category}'"""
        if stipends and not category:
            query += f""" WHERE stipend_min>{stipends}"""
        query += f""" OFFSET {(page-1)*25} LIMIT 25"""

        cur.execute(query)
        data = cur.fetchall()
        return {"ok":"true","data":data}



#For data of a selected internship
@app.route("/internship/about/<id>",methods=["GET","POST"])
def about_internship(id):
        query = f"""SELECT * FROM internships WHERE internship_id={id}"""
        cur.execute(query)
        if cur.rowcount==0:
            return {"ok":"false","message":"invalid id"}
        else:
            return {"ok":"true","data":cur.fetchall()}




if __name__ == "__main__":
    app.run(debug=True,port=80)