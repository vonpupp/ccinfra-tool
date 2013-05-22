#from __future__ import print_function
from tester import *
from model.model import ServerSetup

#import PIL
#import PIL.Image

# Make sure we have the binary extension
srv = ServerSetup()
srv.set_in_path('conf/')
srv.set_out_path('out/')
srv.isc_dhcpd_setup()


#assert PIL.Image.VERSION[:3] == '1.1'
#
## Create an image and do stuff with it.
#assert (im.mode, im.size) == ('1', (100, 100))
#assert len(im.tobytes()) == 1300
#
## Create images in all remaining major modes.
#im = PIL.Image.new("P", (100, 100))
#im = PIL.Image.new("RGB", (100, 100))
#im = PIL.Image.new("I", (100, 100))
#im = PIL.Image.new("F", (100, 100))

print("ok")
