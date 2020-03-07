# Plant_Lights
If you don't use it to control anything, you can just use it as a testing calculator to see how much the lights would cost. I've included some commented code for use with a raspberry pi. 



First you need a few things. This program uses the free Open Weather Map api found at https://openweathermap.org/api

1. You need to install pyowm. This can be done with:
    
   $ pip install pyowm

2. You need to get an API key from OWM. Sign up at https://home.openweathermap.org/users/sign_up

3. (optional) If you want to use a Raspberry Pi to control your lights you will need the RPi.GPIO library. 
    1. $ sudo pip install RPi.GPIO
    2. Set the pin to whatever you want. 
    3. Use the pin to control the lights. This can be done with a relay, or you can build a circut with a transistor.   
    4. Uncomment out the comments with '##'

4. Set up the program by:
    1. Input a string of your OWM key into the API_key variable. 
    2. Set the timeInterval to the time (in hours) between weather updates. 
    3. Set the localWattCost variable to the price per watt. If your cost is in Kilowatts, simply divide by 1000.
    4. Set the obs variable (inside the checkWeather function) to the location nearest you. 
       Find more info about setting location here: https://openweathermap.org/current
    5. Set the 'while True:' loop to the time you want the lights to run. It is in 24 hour time. First 'timeofday.hour'         
       inequality is the ON hour. Next is the OFF hour.  
            
       ex: if timeofday.hour >= 8 and timeofday.hour < 22:   (This will run from 8am until 10pm)
       
    6. This is important! Be sure to set the 'newDay()' hour to the same as starting hour of the 'while True:' loop. This
       logs the date at the start of each new day. 
       
    7. Your file will be called Plant_Lights.txt (You can change this if you want). It includes weather/light information 
       and cost of lights. 
       
 I will be adding more features soon. Thanks! 
