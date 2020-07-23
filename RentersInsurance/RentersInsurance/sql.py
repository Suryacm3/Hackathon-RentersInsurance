from flaskext.mysql import MySQL

class SQL:
    get_base_rate = "select BaseRate from PersonalPropertyBaseRate where Territory='{0}' and ConstructionType='{1}'"
    get_personal_property_factor = "select Factor from PersonalPropertyLimitFactor where LimitRange <= {0} ORDER BY LimitRange DESC LIMIT 1"
    get_personal_property_deductible = "select Factor from DeductibleFactor where Deductible='{0}'"
    get_liability_base_rate = "select BaseRate from LiabilityBaseRate where CustomerAgeRange <= {0} ORDER BY CustomerAgeRange DESC LIMIT 1"
    get_liability_limit_factor = "select Factor from LiabilityLimitFactor where LiabilityLimit='{0}'"
    get_policy_plan_factor = "select PolicyPlanFactor from PolicyPlan where PolicyPlan='{0}'"
    get_quote = "select * from QuoteHistory where Id={0}"
    get_all_quotes = "select * from QuoteHistory"
    get_last_inserted_id="select last_insert_id()"
    insert_quote = str("insert into QuoteHistory(InsuranceType,PolicyStartDate,FirstName,LastName,EmailAddress,PhoneNumber,AddressLine1,AddressLine2,City,State,Zip,Plan,PPCoveragevalue,BuildingType,Deductible,LCoverageValue,Age,PersonalPremium,LiabilityPremium,TotalPremium) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}')");

    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)

    def initialize_connection(self):
        self.cur = self.mysql.get_db().cursor()

    def fetch_one_from_db(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def fetch_one_as_json(self, sql):
        rv = self.fetch_all_from_db(sql)
        row_headers = [x[0] for x in self.cur.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data[0];

    def fetch_all_as_json(self, sql):
        rv = self.fetch_all_from_db(sql)
        row_headers = [x[0] for x in self.cur.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data;
        
    def fetch_all_from_db(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute(self, sql):
        self.cur.execute(sql)

    def commit(self):
        self.cur.connection.commit()

    def close(self):
        self.cur.connection.close()