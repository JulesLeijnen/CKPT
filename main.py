from SimConnect import *
from SimConnect.Enum import *
import logging
from time import sleep
from copy import deepcopy
from pynput import keyboard
#-----------------------------Imports-----------------------------
#-----------------------------Global VARS-------------------------

DEBUGMODE = True

#-----------------------------Global VARS-------------------------
#-----------------------------Logging-----------------------------

def loggingSetup(): #Setup needed logging settings
    if DEBUGMODE:
        logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a", format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s')
        logging.critical("\n\n\nNew session, DEBUG=ON")
    elif not DEBUGMODE:
        logging.basicConfig(level=logging.WARNING, filename="log.log", filemode="a", format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s')
        logging.critical("\n\n\nNew session, DEBUG=OFF".format)
    else:
        logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a", format='%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s')
        logging.critical("\n\n\nNew session, DEBUG=ERROR")
        logging.warning("Logging not correctly initiated via DEBUGMODE variable... Somehow?")
        logging.warning("Restoring default level=DEBUG config")
    return

#-----------------------------Logging-----------------------------
#-----------------------------Main--------------------------------

def main():
    Usedconfig = loadConfig("Cessna152") #Fetches config file from the correct directory. Add the planename as a string as a argument to get the correct one
    CReadD, CWriteD, keymapping = fetchFromConfig(Usedconfig) #Currently a placeholder: Fetch needed data from the file givven bij loadConfig()
    ReadD = deepcopy(CReadD) #Create a exact non-dependent copy to keep the original in tact when editing this one

    listener = keyboard.Listener(on_press=onkeypress) #Setup listener to execute onkeypress() when a keyboard key is pressed
    listener.start() #Start listner
    listener.join() #Remove if main thread is polling self.keys



def onkeypress(Key):
    temp = {"9" : ["E", 1.0, "PARKING_BRAKES"],
            "8" : ["E", 0.0, "PARKING_BRAKES"]} #A copy of the testversion of keymapping
    
    print(Key)                                  #Print checks
    print(type(Key))                            #Print checks
    if hasattr(Key, "char"):                    #Prevent crash if key has no char element like in BACKSPACE
        if Key.char == "\x03":                  #ctrl-C to close escape if needed
            exit()
        if Key.char in temp:                    #Check to see if key in temp
            print("Ping!")
            print(temp.get(Key.char))           #Fetch key value
    


        

    #Init loop for reading and writing
        #Read from game to DB.
        #Check for Inputs
        #Write to game

#-----------------------------Main--------------------------------
#-----------------------------ConfigStuff-------------------------

def loadConfig(Name):
    with open("PlanesConfigs\{}\{}_Panel.cfg".format(Name, Name), encoding = 'utf-8') as file: #Open file from directory according to the given input
        config = file.read() #Load file to var
    return config #Return var to main thread

def fetchFromConfig(config):
    #Faking this to test the rest of the parts
    ReadData = {101 : "YOKE_X_POSITION", #Request Yoke X position (float range: -1.0 to 1.0)
                102 : "YOKE_Y_POSITION", #Request Yoke Y position (float range: -1.0 to 1.0)
                103 : "ELEVATOR_TRIM_POSITION", #Request Elevator Trim (float range: -0.34033920413889424 to 0.34033920413889424)
                
                201 : "GENERAL_ENG_THROTTLE_LEVER_POSITION:1", #Request Throttle1 position (float range: 0.0 to 100.0)
                202 : "BRAKE_PARKING_POSITION", #Request Park brake position (Bool: 0.0 or 1.0)
                
                301 : "RECIP_ENG_LEFT_MAGNETO:1", #Request Left1 Magneto state (Bool: 0.0 or 1.0)
                302 : "RECIP_ENG_RIGHT_MAGNETO:1", #Request Right1 Magneto state (Bool: 0.0 or 1.0)
                303 : "GENERAL_ENG_STARTER:1", #Request Starter1 state (Bool: 0.0 or 1.0)
                
                401 : "LIGHT_CABIN", #Request Cabin Lights state (Bool: 0.0 or 1.0)
                402 : "LIGHT_NAV", #Request Nav Lights state (Bool: 0.0 or 1.0)
                403 : "LIGHT_STROBE", #Request Strobe Lights state (Bool: 0.0 or 1.0)
                404 : "LIGHT_BEACON", #Request Beacon Lights state (Bool: 0.0 or 1.0)
                405 : "LIGHT_TAXI", #Request Taxi Lights state (Bool: 0.0 or 1.0) 
                406 : "LIGHT_LANDING", #Request Landing Lights state (Bool: 0.0 or 1.0)
                
                501 : "ELECTRICAL_MASTER_BATTERY", #Request Master Battery switch state (Bool: 0.0 or 1.0)
                502 : "GENERAL_ENG_MASTER_ALTERNATOR:1", #Request master Alternator1 switch state (Bool: 0.0 or 1.0)
                
                601 : "RECIP_ENG_PRIMER:1", #Request Primer1 state (float range: 0.0 to 1.0)
                602 : "GENERAL_ENG_FUEL_VALVE:1", #Request Fuel valve1 state (Bool: 0.0 or 1.0)
                
                701 : "PITOT_HEAT" #Request Pitot heat switch state (Bool: 0.0 or 1.0)
                }


    #!Array in WriteData works as follows:
    #["W"/"E", [type, lowerrange, upperrange], "EventOrRequestName"]
    #   "W"/"E" = Tells if you need to write data to the game ("W"), or toggle an event ("E") to get what you want
    #   [type, lowerrange, upperrange] = the type of accepted info followed by the upper and lower limit ("f" = float, "b" = bool)
    #   EventorRequestName = The name from the pysimconnect docu to target specific part, like "YOKE_X_POSITION" for the yoke
    #
    #   IF "E" then you can replace [type, lowerrange, upperrange] with None
    #
    #Example: ["W", ["f", -1.0, 1.0], "YOKE_X_POSITION"] will tell the program that you can Write to this var like a request with range -1.0 to 1.0
    #Example2: ["E", None, "PARKING_BRAKES"] will toggle the brakes to engaged if they're not, or vise versa

    WriteData = {101 : ["W", ["f", -1.0, 1.0], "YOKE_X_POSITION"],
                 102 : ["W", ["f", -1.0, 1.0], "YOKE_Y_POSITION"],
                 103 : ["W", ["f", -0.34033920413889424, 0.34033920413889424], "ELEVATOR_TRIM_POSITION"],
                
                 201 : ["W", ["f", 0.0, 100.0], "GENERAL_ENG_THROTTLE_LEVER_POSITION:1"],
                 202 : ["E", None, "PARKING_BRAKES"],
                
                 301 : ["E", None, "MAGNETO_OFF"],
                 302 : ["E", None, "MAGNETO_RIGHT"],
                 303 : ["E", None, "MAGNETO_LEFT"],
                 304 : ["E", None, "MAGNETO_BOTH"],
                 305 : ["E", None, "MAGNETO_START"],
                
                 401 : ["E", None, "TOGGLE_CABIN_LIGHTS"],
                 402 : ["E", None, "TOGGLE_NAV_LIGHTS"],
                 403 : ["E", None, "STROBES_TOGGLE"],
                 404 : ["E", None, "TOGGLE_BEACON_LIGHTS"],
                 405 : ["E", None, "TOGLE_TAXI_LIGHTS"],
                 406 : ["E", None, "LANDING_LIGHTS_TOGGLE"],
                
                 501 : ["E", None, "TOGGLE_MASTER_BATTERY"],
                 502 : ["E", None, "TOGGLE_MASTER_ALTERNATOR"],
                
                 601 : ["E", None, "ENGINE_PRIMER"],
                 602 : ["E", None, "TOGGLE_FUEL_VALVE"],
                
                 701 : ["E", None, "PITOT_HEAT_TOGGLE"]
                }
    
    keymapping = {9 : ["E", 1.0, "PARKING_BRAKES"],
                  8 : ["E", 0.0, "PARKING_BRAKES"]} #Keymapping to test the current parts. If key 'x' is pressed, then toggle [a, b, c]

    return ReadData, WriteData, keymapping #return three needed peaces of info

#----------------------------ConfigStuff--------------------------
#-----------------------------__name__----------------------------

if __name__ == "__main__": #Self explanatory
    loggingSetup()
    main()