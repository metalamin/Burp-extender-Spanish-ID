from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IIntruderPayloadProcessor

#
# Based on example from https://github.com/PortSwigger/example-intruder-payloads/blob/master/python/IntruderPayloads.py
#

class BurpExtender(IBurpExtender, IIntruderPayloadProcessor):
    def registerExtenderCallbacks(self, callbacks):
    
        self._helpers = callbacks.getHelpers()
        
        callbacks.setExtensionName("Add check letter to the Spanish ID (DNI/NIF/NIE)")
        callbacks.registerIntruderPayloadProcessor(self)
        return

    def getProcessorName(self):
        return "Spanish ID Letter"

    def processPayload(self,currentPayload, originalPayload, baseValue):
 
        payload = self._helpers.bytesToString(currentPayload)

        # Check if payload is a digit
        if not payload.isdigit():
            print "Payload must be a number"
            return currentPayload
        try:
            payload = payload + nif_letter(int(payload))
            print "Generated payload: ", payload
            
        except:
            print "Unexpected error:", sys.exc_info()[0]
        return payload

#
# Spanish ID letter generator algorithm (DNI/NIF/NIE)
# https://es.wikibooks.org/wiki/Algoritmia/Algoritmo_para_obtener_la_letra_del_NIF#Python
#

def nif_letter(number):
        return "TRWAGMYFPDXBNJZSQVHLCKE"[number%23] 

        