from SimConnect import *
from SimConnect.Enum import *
import logging
from time import sleep
#-----------------------------Imports-----------------------------
#-----------------------------Global VARS-------------------------

DEBUGMODE = True

#-----------------------------Global VARS-------------------------
#-----------------------------Logging-----------------------------

def loggingSetup():
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
        #TODO RAISE
    return

#-----------------------------Logging-----------------------------
#-----------------------------Main--------------------------------

def main():
    global sm, aq, ae
    #Give all the variables that you want in a list like this:
    #["PLANE_ALTITUDE", "ENGINE_CONTROL_SELECT", "RADIO_HEIGHT", "PARTIAL_PANEL_ADF", "HSI_SPEED", "HSI_DISTANCE"]
    input = ["MAGNETO_LEFT"]

    #Use the SimConnect() to connect to the the game
    sm = SimConnect()


    aq = AircraftRequests(sm)
    ae = AircraftEvents(sm)

    readInfo(input)
    return

#-----------------------------Main--------------------------------
#-----------------------------readInfo-----------------------------

def readInfo(input):
    global sm, aq

    #Make empty list and replace all the keywords with the locations to use the .get() on
    locations = []
    for x in input:
        locations.append(aq.find(x))

    #Infinite loop that fetches the requested info
    while True:       
        print("\n\n")
        for x in locations:
            print(x.get())
        sleep(1)

#-----------------------------readInfo-----------------------------
#-----------------------------__name__----------------------------

if __name__ == "__main__":
    loggingSetup()
    main()