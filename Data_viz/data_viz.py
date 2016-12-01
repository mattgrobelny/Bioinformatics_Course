# Cairo drawing module
#
import cairocffi as cairo

###############################################################################
#
# The img dictionary will hold image-specific dimensions.
#
img = {}
img['height']     = 800
img['width']      = 800
img['center_x']   = img['width']  / 2.0
img['center_y']   = img['height'] / 2.0
img['font_size']  = 16;

###############################################################################
#
# Define the path our file
#
ps = cairo.PDFSurface(outpath, img['height'], img['width'])
cr = cairo.Context(ps)
# All of your computation goes here...
#
# Close the file
#
cr.show_page()

###############################################################################
#
# Convert a radius and a span of degrees into X, Y coordinates #
def get_x_y_coordinates(center_x, center_y, degree, radius):
    if degree <= 90:
theta
opp_side
adj_side
x
y
= float(degree)
= radius * math.sin(math.radians(theta))
= radius * math.cos(math.radians(theta))
= center_x + adj_side
= center_y + opp_side
elif degree <= 180:
theta
opp_side
adj_side
x
y
= float(degree - 90.0)
= radius * math.sin(math.radians(theta))
= radius * math.cos(math.radians(theta))
= center_x - opp_side
= center_y + adj_side
elif degree <= 270:
    theta
    opp_side
    adj_side
    x
y
else: theta
    opp_side
    adj_side
    x
    y
= float(degree - 180.0)
= radius * math.sin(math.radians(theta))
= radius * math.cos(math.radians(theta))
= center_x - adj_side
= centre_y - opp_side
= float(degree - 270.0)
= radius * math.sin(math.radians(theta))
= radius * math.cos(math.radians(theta))
= center_x + opp_side
= center_y - adj_side
return (x, y)

###############################################################################
#
# Choose a font
#
cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
# Set the font size
cr.set_font_size(font_size)
# Choose a font color
cr.set_source_rgb(red, green, blue)
#
# Get the size of the text we want to write, returns a tuple:
#   (x, y, width, height, dx, dy)
#
textents = cr.text_extents(text)
text_width  = textents[2]
text_height = textents[3]
#
# Where you want to draw text may need to be adjusted,
# depending on the size of the text.
#
cr.move_to(x, y)
#
# Finally draw the text.
#
cr.show_text(text)

###############################################################################

chr_size_dic = {
'groupI'    : 28185914, 'groupII'   : 23295652, 'groupIII'   : 16798506, 'groupIV'  : 32632948,
'groupIX'   : 20249479, 'groupV'    : 12251397, 'groupVI'    : 17083675, 'groupVII' : 27937443,
'groupVIII' : 19368704, 'groupX'    : 15657440, 'groupXI'    : 16706052, 'groupXII' : 18401067,
'groupXIII' : 20083130, 'groupXIV'  : 15246461, 'groupXIX'   : 20240660, 'groupXV'  : 16198764,
'groupXVI'  : 18115788, 'groupXVII' : 14603141, 'groupXVIII' : 16282716, 'groupXX'  : 19732071,
'groupXXI'  : 11717487}
