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
    return

#-----------------------------Main--------------------------------
#-----------------------------__name__----------------------------

if __name__ == "__main__":
    loggingSetup()
    main()