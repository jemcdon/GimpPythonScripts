#!/usr/bin/env python

# Scrolling_wrapped_layer Rel 1
# Created by Tin Tran http://bakon.ca/gimplearn/
# Comments directed to http://gimplearn.com or http://gimp-forum.net or http://gimpchat.com or http://gimpscripts.com
#
# License: GPLv3
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# To view a copy of the GNU General Public License
# visit: http://www.gnu.org/licenses/gpl.html
#
#
# ------------
#| Change Log |
# ------------
# Rel 1: Initial release.
import math
import string
#import Image
from gimpfu import *
from array import array
import sys
def python_yscrolling_wrapped_layer(image, layer, scrolly) :
	pdb.gimp_image_undo_group_start(image)
	pdb.gimp_context_push()

	if (scrolly != 0):
		startyfactor = scrolly/abs(scrolly)
		ystep = abs((layer.height)/scrolly)
	else:
		startyfactor = 0
		ystep = 100000

	steps = int(ystep)

	layerposition = pdb.gimp_image_get_item_position(image,layer)
	#second copy to fill seamlessly
	temp = pdb.gimp_layer_new_from_drawable(layer,image)
	pdb.gimp_image_insert_layer(image,temp,None,layerposition)
	pdb.gimp_layer_translate(temp,0,(layer.height*startyfactor))
	new_layer = pdb.gimp_image_merge_down(image,temp,EXPAND_AS_NECESSARY)


	newimage = pdb.gimp_image_new(image.width,image.height,RGB)
	newdisplay = pdb.gimp_display_new(newimage)

	#this seemed to create an extra frame.
	#anilayer = pdb.gimp_layer_new_from_visible(image,newimage,"animation frame")
	#pdb.gimp_image_insert_layer(newimage,anilayer,None,0)

	for i in range(0,steps):
		pdb.gimp_layer_translate(new_layer,0,scrolly)
		anilayer = pdb.gimp_layer_new_from_visible(image,newimage,"animation frame")
		pdb.gimp_image_insert_layer(newimage,anilayer,None,0)

	pdb.gimp_context_pop()
	pdb.gimp_image_undo_group_end(image)
	pdb.gimp_displays_flush()
    #return

register(
	"python_fu_yscrolling_wrapped_layer",
	"Scrolling a y single layer wrapped animation",
	"Scrolling a y single layer wrapped animation",
	"Tin Tran",
	"Tin Tran",
	"2017",
	"<Image>/Python-Fu/Scrolling layer wrapped animation ...",             #Menu path
	"RGB*, GRAY*",
	[
	(PF_SPINNER, "scrolly", "Scroll y:", 10, (-500, 500, 1)),
	],
	[],
	python_yscrolling_wrapped_layer)

main()
