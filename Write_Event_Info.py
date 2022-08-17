from turtle import position
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
    #["PARKING_BRAKES"]
    input = ["MAGNETO_RIGHT"]

    #Use the SimConnect() to connect to the the game
    sm = SimConnect()


    aq = AircraftRequests(sm)
    ae = AircraftEvents(sm)

    writeInfo(input)
    return


#-----------------------------Main--------------------------------
#-----------------------------WriteInfo-----------------------------

def writeInfo(input):
    for x in input:
        ae.find(x)()
    
    
        
        



#-----------------------------WriteInfo-----------------------------
#-----------------------------__name__----------------------------

if __name__ == "__main__":
    loggingSetup()
    main()