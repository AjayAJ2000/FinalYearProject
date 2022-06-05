from django.shortcuts import render
from . import thingspeak,sendmsg
# Create your views here.
def home(request):
    data = thingspeak.getdata()
    temperature = data[0]
    temp_status = data[1]
    solar_voltage = data[2]
    wind_voltage = data[3]
    sys_connection = data[4]
    print(data)
    indicate = 0
    if(sys_connection == "Solarwind\r\n\r\n\r\n\r\n"):
        indicate = 11
    elif(sys_connection == "Grid"):
        indicate = 22
    print(indicate)
    '''
    image_link = ""
    if(sys_connection.lower() == 'solarwind'):
        image_link = "https://cdn.shortpixel.ai/spai/w_1003+q_glossy+ret_img+to_webp/https://balkangreenenergynews.com/wp-content/uploads/2022/03/Hybrid-power-plants-dominate-2-8-GW-in-new-grid-capacity-Turkey.jpg"
    elif(sys_connection == 'Grid'):
        image_link = "https://assets.terrapass.com/wp-content/uploads/2019/11/terrapass-blog-electricalgrid.jpg"
    else:
        image_link = "https://previews.123rf.com/images/gigisomplak/gigisomplak1808/gigisomplak180800032/107696886-sketchy-loading-sign-vector-illustration.jpg"
    '''
    if(temperature > 40):
        message  = "Temperature is Increased\n Temperature value = "+ str(temperature)+"\n"+"Voltage from Solar = "+str(solar_voltage)+"\n"+"Voltage from Wind = "+str(wind_voltage)
        sendmsg.send(message)
    return render(request,'home.html',{'temp':temperature,'status':temp_status,'solar':solar_voltage,'wind':wind_voltage,'sys':sys_connection,'indi':indicate})