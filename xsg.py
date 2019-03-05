import stf
import wx as wx
import scipy.io as sio
import numpy as np

def load():

    # wx Widgets to create a file selection window
    fname = wx.FileSelector("Import Ephus file" ,
    default_extension = "Ratiometric" ,
    default_path = "." ,
    wildcard = "Matlab Ephus xsg. text export (*.xsg)|*.xsg" ,
    flags = wx.OPEN | wx.FILE_MUST_EXIST)

    data_sio = sio.loadmat(fname, squeeze_me = True)
    data = data_sio.get('data');
    trace = data['ephys'].item().item()[0]
    header = data_sio.get('header')
    dt = header['ephys'].item().item()[0]['sampleRate']

    stf.new_window( trace[1:])
    stf.set_sampling_interval( dt )
    stf.set_xunits('ms')
    stf.set_yunits('pA')
