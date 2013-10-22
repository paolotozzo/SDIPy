"""
sender.py

by Charles Fracchia, Copyright (c) 2013

Sender class module

This class defines data and methods for the sender in a packet
"""
import re, warnings

allowedAttributes = ["name","brand","model","modelNum"]       #In future, this could be loaded dynamically from a reference JSON

class Sender(object):
  """docstring for Packet"""
  
  def __init__(self, address, **kwargs):
    super(Sender, self).__init__()
    if (self._validateAddress(address) != False) :         #Validate submitted address
      self.addressType = self._validateAddress(address)
      self.address = address
      
    #For each extra attribute add it to the object to expose it
    for arg in kwargs:
      if arg not in allowedAttributes:                    #If it's not an allowed attribute according to OBMP
        allowedList = ""                                  #Used for nicely formatted warning
        for attribute in allowedAttributes:               #For each of the attributes in the list
          if allowedList != "": allowedList = allowedList + ", " + attribute    #Nicely formatted :)
          else: allowedList += attribute                  #Nicely formatted :)
        warnings.warn("Invalid sender attribute passed. Attribute will not be set. Allowed attributes are: %s" % allowedList)     #Warn the user
      else:
        setattr(self, arg, kwargs[arg])                   #This sets the attribute with dynamic name
      
  def _validateAddress(self, address):
    """
    Check that the [address] is a valid address and return its type
    Return destination address if correct, Nothing otherwise. If it is a MAC address it will return it as a byte field (xAAxBBxCCxDDxEExFFxGGxHH)
    Acceptable: 
        XBee MAC address formatted like AA:BB:CC:DD:EE:FF:GG:HH:GG:HH
        IP address formatted like 000.000.255.255, each block has to be 0 <= n < 256
    """
    pass
    addressType = []                                    #Used for storing regex matches
    mac = '^[a-fA-F0-9][aceACE02468][:|\-]?([a-fA-F0-9]{2}[:|\-]?){4}[a-fA-F0-9]{2}$'                 #For regular mac addresses
    beemac = '^[a-fA-F0-9][aceACE02468][:|\-]?([a-fA-F0-9]{2}[:|\-]?){6}[a-fA-F0-9]{2}$'              #For XBee mac addresses
    ip = '(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'  #For IP addresses
    
    regexes = {"mac":mac,"beemac":beemac,"ip":ip}
    
    for regex in regexes:
      regexFound = re.compile(regexes[regex]).search(address)    #Do the regex search
      if regexFound != None:                            #If it finds a match
        addressType.append("%s" % regex)                #append the type to an array, this way we can detect addresses that match multiple regexes
    
    if len(addressType) != 1:                           #If we matched too many regex
      raise ValueError("The provided address is not correctly formatted. The address can be an IP, regular MAC address or ZigBee MAC address")
      return False
    else:                                               #We correctly matched just 1 type
      return addressType[0]                             #Return the address type matched

#TESTING
#p = Sender("192.168.1.1",brand="Charles Corp", model="Omatic v1")
#print p.model
#print p.address
#print p.addressType
      