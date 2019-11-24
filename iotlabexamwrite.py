import time
import random
import urllib

import sqlite3
import time


def sensor_data():
  temp = random.randint(5,45)
  wind = random.randint(55,110)
  moisture = random.randint(5,35)
  rain= random.randint(125,255)
  return temp,wind,moisture,rain
while(1):
  temp,wind,moisture,rain= sensor_data()
  print("Temperature",temp, chr(176) + "C")
  print("windspeed",wind,"%kmh")
  print("Moisture",moisture,"%gmm3")
  print("Rainlevel",rain,"%cm2")
  time.sleep(1.0)


  
  baseURL = "https://api.thingspeak.com/update?api_key=FX55RNDMIBOY73F8&field1=0&field2=0&field3=0"  
  g = urllib.urlopen(baseURL + "&field1=%d, &field2=%d, &field3=%d,"%(temp,wind,moisture))  
  time.sleep(0.10)  
  con = sqlite3.connect("new_db.db" )  
  cursor = con.cursor()  
  #cursor.execute("DROP TABLE IF EXISTS SENSOR_DATA
  #cursor.execute("CREATE TABLE SENSOR_DATA (SENSOR_TYPE  CHAR(20) , VALUE1 CHAR(20))");  

  con.execute("INSERT INTO SENSOR_DATA(SENSOR_TYPE,VALUE1) VALUES (?,?)",("temperature",temp));
  con.execute("INSERT INTO SENSOR_DATA(SENSOR_TYPE,VALUE1) VALUES (?,?)",("Wind",wind));
  con.execute("INSERT INTO SENSOR_DATA(SENSOR_TYPE,VALUE1) VALUES (?,?)",("moisture",moisture));

  
  con.commit()
  con.close()
  time.sleep(5)


  





























  



  



