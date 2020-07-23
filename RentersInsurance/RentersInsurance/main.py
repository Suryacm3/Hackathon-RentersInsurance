from flask import Flask, render_template, jsonify, request, json
import pdfkit
from sql import SQL
import os

app=Flask(__name__, static_folder = os.path.abspath("static/"))
app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'sql12355908'
app.config['MYSQL_DATABASE_PASSWORD'] = 'UPmxNQXL2d'
app.config['MYSQL_DATABASE_DB'] = 'sql12355908'
mySql = SQL(app)

@app.route('/')
def create_quote_ui():
    return render_template("create_quote.html")

@app.route('/quotes',methods=['GET'])
def get_quote_list_ui():
    return render_template("quote_list.html")

@app.route('/quote/<quoteId>',methods=['GET'])
def get_quote_ui(quoteId):
    mySql.initialize_connection()
    quoteInfoJson = mySql.fetch_one_as_json(SQL.get_quote.format(quoteId))
    mySql.close()
    print(quoteInfoJson)
    return render_template("quote_detail.html", **quoteInfoJson)

@app.route('/quote/<id>/print', methods=["GET"])
def print_pdf(id):
    root_dir = os.path.dirname(os.getcwd())
    pdfkit.from_url('http://127.0.0.1:5000/quote/'+id, 'static\quote_{0}.pdf'.format(id))
    return app.send_static_file('quote_{0}.pdf'.format(id))

@app.route('/api/calculatepremium',methods=['POST'])
def calculate_premium():
    content = request.json
    print(content)
    totalPremium = 0;
    # Get renters form data
    insType = content['insuranceType']
    startingDate = content['startingDate']
    fname = content['fname']
    lname = content['lname']
    email = content['email']
    phone = int(content['phone'])
    address1 = content['address1']
    address2 = content['address2']
    cityTerritory = int(content['city'])
    state = content['state']
    zipCode = int(content['zip'])
    plan = content['plan']
    age = content['age']
    buildingType = content['buildingType']
    deductible = int(content['deductible'])
    lCoverageValue = int(content['lCoverageValue'])
    ppCoverageValue = int(content['ppCoverageValue'])

    try:
        mySql.initialize_connection()
        if(ppCoverageValue < 50000):
            raise Exception("Personal property coverage limit should not be less than 50000")
        if(lCoverageValue < 100000):
            raise Exception("Liability coverage limit should not be less than 100000")
        # Get Factors
        baseRate = mySql.fetch_one_from_db(SQL.get_base_rate.format(cityTerritory, buildingType))[0]
        ppLimitFactor = mySql.fetch_one_from_db(SQL.get_personal_property_factor.format(ppCoverageValue))[0]
        deductibleFactor = mySql.fetch_one_from_db(SQL.get_personal_property_deductible.format(deductible))[0]
        lBaseRate = mySql.fetch_one_from_db(SQL.get_liability_base_rate.format(age))[0]
        lLimit = mySql.fetch_one_from_db(SQL.get_liability_limit_factor.format(lCoverageValue))[0]
        ppfactor = mySql.fetch_one_from_db(SQL.get_policy_plan_factor.format(plan))[0]

        # Calculate Premium
        personalPremium = float(baseRate) * float(ppLimitFactor) * float(deductibleFactor)
        liabilityPremium = float(lBaseRate) * float(lLimit)
        totalpremium = (personalPremium + liabilityPremium) * float(ppfactor)
        tp = format(round(totalpremium, 2))
        totalPremium = str(tp)

        # Store in Quote History
        mySql.execute(SQL.insert_quote.format(insType, startingDate, fname, lname, email, int(phone), address1, address2, cityTerritory, state, int(zipCode),
                plan, int(ppCoverageValue), buildingType, int(deductible), int(lCoverageValue), int(age),
                float(personalPremium), float(liabilityPremium), float(totalpremium)))
        lastInsertId=mySql.fetch_one_from_db(SQL.get_last_inserted_id)
        id=lastInsertId[0]
        print("last inserted id:",id)
        mySql.commit()
    except Exception as e:
        return jsonify({
            "status": "failure",
            "message": e.args[0]
        })
    finally:
        mySql.close()

    return jsonify({
        "status": "success",
        "total_premium": totalPremium,
        "quoteId":id
    })

@app.route('/api/quote/<quoteId>',methods=['GET'])
def get_quote(quoteId):
    # Get supplied quote from quote history table
    mySql.initialize_connection()
    json_data = mySql.fetch_one_as_json(SQL.get_quote.format(quoteId))
    mySql.close()
    return app.response_class(
        response=json.dumps(json_data),
        mimetype='application/json'
    )

@app.route('/api/quotes',methods=['GET'])
def get_list_of_quotes():
    # Get All the created quotes
    mySql.initialize_connection()
    json_data = mySql.fetch_all_as_json(SQL.get_all_quotes)
    mySql.close()
    return app.response_class(
        response=json.dumps(json_data),
        mimetype='application/json'
    )

if __name__ =="__main__":
    app.debug=True
    app.run()
