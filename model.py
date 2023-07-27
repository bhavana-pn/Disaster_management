import http_request
import pandas
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="My@220402",
  database="forestfire"
)

mycursor = mydb.cursor()


def get_prediction():
    params = http_request.get_response()

    wind_speed=params['current']['wind_speed']
    temperature = params['current']['temperature']
    precip = params['current']['precip']
    humidity = params['current']['humidity']


    sample = [[temperature,humidity,wind_speed,precip]]
    df = pandas.read_csv("forestfirex.csv")
    df1 = pandas.read_csv("forestfirex1.csv")


    features = ['temp', 'RH', 'wind', 'rain']

    X = df[features]
    y = df1['area']


    extratree = ExtraTreesRegressor()
    extratree = extratree.fit(X,y)
    pred = extratree.predict(X)
    
    
    output = extratree.predict(sample)
    if (output[0]<=10):
        sql = "INSERT INTO forestinfo01 (temp, RH,wind,rain,area) VALUES (%s, %s,%s, %s,%s)"
        val = (temperature,humidity,wind_speed,precip,output[0])
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        return ("nil")


    elif(output[0]>10 and output<60):
        sql = "INSERT INTO forestinfo01 (temp, RH,wind,rain,area) VALUES (%s, %s,%s, %s,%s)"
        val = (temperature,humidity,wind_speed,precip,output[0])
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        return ("Mild")

    elif (output[0]>60 and output[0]<120):
        sql = "INSERT INTO forestinfo01 (temp, RH,wind,rain,area) VALUES (%s, %s,%s, %s,%s)"
        val = (temperature,humidity,wind_speed,precip,output[0])
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        return ("Good")

    else:
        sql = "INSERT INTO forestinfo01 (temp, RH,wind,rain,area) VALUES (%s, %s,%s, %s,%s)"
        val = (temperature,humidity,wind_speed,precip,output[0])
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        return ("high")

