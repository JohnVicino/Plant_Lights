from pyowm import OWM
import time
from datetime import datetime



##import RPi.GPIO 

## for the raspberry pi
##GPIO.setmode(GPIO.BCM)
##GPIO.setwarnings(False)
##GPIO.setup(12,GPIO.OUT)


API_key = 'OWM key here' #insert your OWM api key here
owm = OWM(API_key)


timeofday = datetime.now()




# Sets time (in hours) between weather checks. Ex: 2 for 2 hours.
timeInterval = 1


# Hours lights have been on.
lightHrs= 0

def lightCost():
    
    # Approximation of Kilowatt/watt cost in $USD. Uses float, so be careful, it is only an approximation. Use your local cost. 
    localWattCost= .0001559
    
    # Insert the light's wattage here and multiply by the number of lights being used.
    lampWatt= 45*4
    
    # Calculates the total cost of electricty.
    lightCost = localWattCost*lampWatt*lightHrs
    
    # Logs the light use and cost.
    f= open('Plant_Lights.txt', 'a+')
    f.write('\nLight hours: {}\nLight cost: {}\n\n\n\n'.format(lightHrs, lightCost))
    f.flush()
    f.close()
    print (lightCost)



def checkWeather():
    global lightHrs
    
    # Looks up local weather.
    obs = owm.weather_at_place('Berkley,US')
    w = obs.get_weather()

    # Checks for clouds and if higher than set percentage turns on lights.
    clouds = w.get_clouds()
    if clouds > 60:
        ##turns on lights
        ##GPIO.output(12, GPIO.HIGH)
        
        print('Cloudy at {}:{}.\nLogging weather to Plant_Lights.txt'.format(timeofday.hour, timeofday.minute))
        
        # Logs the weather to file called 'Plant_Lights.txt'
        f = open('Plant_Lights.txt', 'a+')
        f.write('It was cloudy at {}:{}.\nThe lights are on.\n'.format(timeofday.hour, timeofday.minute))
        f.flush()
        f.close()
        
        print ('Lights are on')
        
        lightHrs += 1 * timeInterval

    
    else:
           ##turns off lights
           ##GPIO.output(12, GPIO.LOW)
          
        print('Clear skies at {}:{}.\nLogging weather to Plant_Lights.txt'.format(timeofday.hour, timeofday.minute))
        
        # Logs the weather to file called 'Plant_Lights.txt'
        f = open('Plant_Lights.txt', 'a+')
        f.write('It was clear at {}:{}.\nThe lights are off.\n'.format(timeofday.hour, timeofday.minute))
        f.flush()
        f.close()
        print('Lights are off')
     

# Prints date to log. Make sure to set hour within hours of the 'while True:' loop below this function!
def newDay():
    if timeofday.hour == 6 and timeofday.minute <= 1:
        print("It's a new day!")
        f = open('Plant_Lights.txt', 'a+')
        f.write ('\nDate: {}:{}:{}\n'.format(timeofday.month, timeofday.day, timeofday.year))
    else:
        print ('Date: {}:{}'.format(timeofday.month, timeofday.day))
        
        
        


try:
    
    # Sets the hours for the lights to run. Make sure to set newDay() timeofday.hour, == to the first timeofday.hour of this 'while True:' loop!
    while True: 
        if timeofday.hour >= 9 and timeofday.hour <= 23:
                newDay()
                checkWeather()
                lightCost()
                #sets time between weather checks
                time.sleep(timeInterval*3600)
                print ('\nLight hours: {}'.format(lightHrs))
                
# Stops and cleans up gpio for Raspberry Pi. Quits program
except KeyboardInterrupt:
        print ('Keyboard Interrupt. Quitting Program')
        ##GPIO.cleanup()
        quit()
        
        





