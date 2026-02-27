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
file_name = './CA1_hippo_data.csv'

soma_df = pd.read_csv(file_name,
                      sep=',', index_col=0)

for k, v in enumerate(soma_df.label.unique()):
    node = soma_df.loc[soma_df.label == v, ['soma_x', 'soma_y', 'soma_z']].values


    color = soma_df.loc[soma_df.label == v, 'color'].values[0]
    color = np.array(hex2rgb(color)) / 255

    polyPointSource1 = PolyPointSource(registrationName='PolyPointSource_bouton' + str(v))
    polyPointSource1.Points = node.reshape(-1)

    # set active source
    SetActiveSource(polyPointSource1)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    polyPointSource1Display = Show(polyPointSource1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    polyPointSource1Display.Representation = 'Points'
    # change solid color
    polyPointSource1Display.AmbientColor = color
    polyPointSource1Display.ColorArrayName = [None, '']
    polyPointSource1Display.DiffuseColor = color
    polyPointSource1Display.SelectTCoordArray = 'None'
    polyPointSource1Display.SelectNormalArray = 'None'
    polyPointSource1Display.SelectTangentArray = 'None'
    polyPointSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    polyPointSource1Display.SelectOrientationVectors = 'None'
    polyPointSource1Display.ScaleFactor = 0.1
    polyPointSource1Display.SelectScaleArray = 'None'
    polyPointSource1Display.GlyphType = 'Arrow'
    polyPointSource1Display.GlyphTableIndexArray = 'None'
    polyPointSource1Display.GaussianRadius = 0.005
    polyPointSource1Display.SetScaleArray = [None, '']
    polyPointSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
    polyPointSource1Display.OpacityArray = [None, '']
    polyPointSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
    polyPointSource1Display.DataAxesGrid = 'GridAxesRepresentation'
    polyPointSource1Display.PolarAxes = 'PolarAxesRepresentation'
    polyPointSource1Display.SelectInputVectors = [None, '']
    polyPointSource1Display.WriteLog = ''

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # reset view to fit data
    renderView1.ResetCamera(False)

    # Properties modified on polyPointSource1Display
    polyPointSource1Display.RenderPointsAsSpheres = 1

    # Properties modified on polyPointSource1Display
    polyPointSource1Display.PointSize = 8.0

    # Properties modified on polyPointSource1Display
    polyPointSource1Display.Opacity = 1.