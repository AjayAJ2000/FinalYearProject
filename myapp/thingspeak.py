import json
import requests

def getdata():
    READ_API_KEY='N9R36SGK1B7BX8XT'
    CHANNEL_ID= '1749653'

    response = requests.get("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    todos = json.loads(response.text)
    output = todos['field1']
    output = output.split("_")
    print(output)
    temp = float(output[1])
    temp_status = output[2]
    solar_voltage = float(output[4])
    wind_voltage = float(output[6])
    power_mode = output[7]
    print("System Temperature: ",temp)
    print("Temperature Status: ",temp_status)
    print("Voltage from Solar: ",solar_voltage)
    print("Voltage from Wind : ",wind_voltage)
    print("System Connection :",power_mode)
    return [temp,temp_status,solar_voltage,wind_voltage,power_mode]
