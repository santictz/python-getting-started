#Import everything from the module
import helpers
helpers.display('Sample message', True) 
#Only import the display function
from helpers import display
display('Sample message')