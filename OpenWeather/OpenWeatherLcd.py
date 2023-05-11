from machine import I2C,Pin,RTC,ADC 
import network, socket       
import struct                
from secrets import *        
import utime
import urequests
from lcd1602 import LCD1602  #on importe la librairie qui permet d'utiliser le LCD


def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"): 
    NTP_QUERY = bytearray(48)                                     
    NTP_QUERY[0] = 0x1B 
    
    addr = socket.getaddrinfo(host, 123)[0][-1] 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP/IP
    
    try:
        s.settimeout(1)                 
        res = s.sendto(NTP_QUERY, addr) 
                                        
        msg = s.recv(48)                
    finally:
        s.close()                       
    
    val = struct.unpack("!I", msg[40:44])[0] 

    t = val - delta     
    tm = utime.gmtime(t+offset) 
    return tm  


#connexion au WiFi 
wlan = network.WLAN(network.STA_IF)  
wlan.active(True)                   
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])  
                                                          

print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()

# Attend pour la connexion ou quitte avec une erreur si la connexion échoue
retry = 10                    
while (retry > 0):
    wlan_stat=wlan.status()   
    if wlan_stat==3:                                
        print("Got IP")
        break
    if wlan_stat==-1:                               
        raise RuntimeError('WiFi connection failed')
    if wlan_stat==-2:                               
        raise RuntimeError('No AP found')    
    if wlan_stat==-3:                               
        raise RuntimeError('Wrong WiFi password')
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break                                       
    retry = retry-1                                 
    utime.sleep(1)

if wlan_stat!=3:                                    
    raise RuntimeError('WiFi connection failed')


print()
print('Connected to WiFi network: ',end="")
print(wlan.config("ssid"))
print()

# On peut maintenant utiliser la connexion pour avoir accès à internet.

t_now=get_time()

# ferme la connexion
#wlan.disconnect()

rtc = RTC()
rtc.datetime((t_now[0], t_now[1], t_now[2], t_now[6] , t_now[3], t_now[4], t_now[5]-2, 0))

# Base url for the openweathermap API
root_url = "http://api.openweathermap.org/data/2.5/weather?"

url=root_url+"lat="+my_secrets["lat"]+"&lon="+my_secrets["lon"]+"&appid="+my_secrets["OWM_API_key"]
r = urequests.get(url) # Query openweather in http

# Parsing and displaying some weather data returned by the API (in json format)
dict=r.json() # convert json data into a dictionnary

temp=float((dict["main"]["temp"]))
temp_min=float((dict["main"]["temp_min"]))
temp_max=float((dict["main"]["temp_max"]))
humidity=float((dict["main"]["humidity"]))


print("Weather forecast from openweathermap.org")
print("----------------------------------------")

print("Type of weather: ",dict["weather"][0]["main"])
print("Current temperature: ",round(temp-273.15,1),"°C")
print("Minimum temperature today: ",round(temp_min-273.15,1),"°C")
print("Maximum temperature today: ",round(temp_max-273.15,1),"°C")
print("Relative humidity: ",round(humidity),"%")

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)      #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne;
d.display()                  #active l'affichage du LCD
d.setCursor(0, 0) 
d.clear()                    #efface l'affichage du LCD
d.print(str(rtc.datetime()[2]) +"/" + str(rtc.datetime()[1]) + " ")     #Affiche la date             
d.print(str(rtc.datetime()[4]) +"h" + str(rtc.datetime()[5]) +"m" + str(rtc.datetime()[6])+"s") #Affiche l'heure les minutes et les secondes 
d.print("temp: " + str(round(temp-273.15,1)))
    
    
