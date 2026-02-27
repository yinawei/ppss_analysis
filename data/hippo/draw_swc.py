# trace generated using paraview version 5.11.0-RC1
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 11

#### import the simple module from the paraview
import os
import pandas as pd
import numpy as np
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


def hex2rgb(hexcolor):
    if type(hexcolor) is str:
        hexcolor = hexcolor.replace('#', '0x')
        hexcolor = (int(hexcolor, base=16))
    rgb = [(hexcolor >> 16) & 0xff,
           (hexcolor >> 8) & 0xff,
           hexcolor & 0xff
           ]
    return rgb

# replace it by your abs path
file_name = './selected_obj_200perCluster.csv'
obj_folder = './hippo/obj'

swc_df = pd.read_csv(file_name,
                      sep=',',
                      index_col=0
                      )

# cluster_1 or cluster_2
for j in ['cluster_2']:
    swc_df = swc_df[swc_df['folder'] == j].copy()
    print(swc_df)

    print('load')

    for i in swc_df.index:
        obj = swc_df.loc[i, 'swc_id']
        color = swc_df.loc[i, 'color']
        folder = swc_df.loc[i, 'folder']
        # print(obj_folder + '\\'+ str(folder) + '\\' + obj)
        # create a new 'Wavefront OBJ Reader'
        a17545_00064obj = WavefrontOBJReader(registrationName=obj,
                                             FileName=obj_folder + '\\'+ folder + '\\' + obj+'.obj')
        color = np.array(hex2rgb(color)) / 255

        # set active source
        SetActiveSource(a17545_00064obj)

        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')

        # show data in view
        a17545_00064objDisplay = Show(a17545_00064obj, renderView1, 'GeometryRepresentation')

        # trace defaults for the display properties.
        a17545_00064objDisplay.Representation = 'Wireframe'

        # get the material library
        materialLibrary1 = GetMaterialLibrary()

        # reset view to fit data
        renderView1.ResetCamera(False)

        # change representation type
        # a17545_00064objDisplay.SetRepresentationType('Wireframe')

        # change solid color
        a17545_00064objDisplay.AmbientColor = color
        a17545_00064objDisplay.DiffuseColor = color

        # Properties modified on a17545_00064objDisplay
        a17545_00064objDisplay.LineWidth = 2.0
        a17545_00064objDisplay.Opacity = 1

        # show data in view
        a17545_00064objDisplay = Show(a17545_00064obj, renderView1, 'GeometryRepresentation')

        # reset view to fit data
        renderView1.ResetCamera(False)

        # update the view to ensure updated data information
        renderView1.Update()

# ================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
# ================================================================

# get layout
layout1 = GetLayout()

# --------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2162, 1094)

# -----------------------------------
# saving camera placements for views

# current camera placement for renderView1


# --------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).