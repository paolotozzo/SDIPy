"""
packet.py

by Charles Fracchia, Copyright (c) 2013

Packet class module

This class defines data and methods common to all classes.
"""
import warnings
from obmpy.sender import Sender
from obmpy.data import Data

class Packet(object):
  """docstring for Packet"""
  
  def __init__(self, **kwargs):
    super(Packet, self).__init__()
    if "address" in kwargs:
      if "startTime" in kwargs:                                    #Forward startTime if it's present in the kwargs
        sender = Sender(kwargs['address'],kwargs['timeFormat'],kwargs['startTime'])
      else:
        sender = Sender(kwargs['address'],kwargs['timeFormat'])    #Instanciate the Sender object with the correct properties
      
      dataPresent = False                   #Check for presence of the Data in the packet
      for kwarg in kwargs:                  #Check arguments for data objects
        #print "Types %s" % type(kwargs[kwarg])
        if type(kwargs[kwarg]) == Data:
          data = kwargs[kwarg]              #We assume the data packet is valid because it was correctly instanciated. This may be a problem
          dataPresent = True
        elif type(kwargs[kwarg]) == list:   ###THIS IS NOT SUPPORTED YET! NEEDS WORK ON THE DATA INSTANCIATION TO WORK
          try:
            data = Data.__init__(kwargs[kwarg])        #Initialize the Data object using the array that was passed in
            dataPresent = True
          except KeyError:
            warnings.warn("The data packet you provided is malformed. It needs to be a dictionnary with the following structure: {'name':nameval, 'vals':['time':timeval, 'val':val]}")
          
      if not dataPresent:
        raise KeyError("You have not passed any data in, or all the data passed is invalid.")
      
    else:
      raise NameError("You need to provide at least the following values for packets: %s" % ("address","name","vals"))
      
    self.sender = sender
    self.data = data
    
    #Check if formatDetails are being set
  def exportJSON(self):
    """docstring for exportJSON"""
    pass
  
  def _flattenData(self, data):
    """
    It takes all the values and flattens them in the order they were passed into the object, makes retrieval and data handling by the user easier
    Takes in the data object
    Returns a dictionnary of this form: {'name':DataStreamName, 'x':[x,values], 'y':[y,values]}
    """
    pass
    