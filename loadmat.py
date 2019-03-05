import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

filename = '/users/trose/data/SW0003/SW0003AAAA0051.xsg'

data_sio = sio.loadmat(filename, squeeze_me = True)
data = data_sio.get('data');
trace = data['ephys'].item().item()[0]
header = data_sio.get('header')
dt = header['ephys'].item().item()[0]['sampleRate']

times=np.arange(len(trace))/dt
plt.plot(times,trace);

def loadxsgtxt():
    """
    Loads and ASCII file with extension *.GoR.
    This file contains ratiometric fluorescent measurementes
    (i.e Green over Red fluorescence)
    saved in one column. This function opens a new Stimfit window and
    sets the x-units to ms and y-units "Delta G over R".
    Arguments:

    freq -- (float) the sampling rate (in Hz) for the acquistion.
    the default value is 400 Hz.
    """

    # wx Widgets to create a file selection window
    fname = wx.FileSelector("Import Ca transients" ,
    default_extension = "EphusTxt" ,
    default_path = "." ,
    wildcard = "Matlab Ephus xsg. text export (*.dat)|*.dat" ,
    flags = wx.OPEN | wx.FILE_MUST_EXIST)



    trace = np.loadtxt(fname = file, skiprows = 0, unpack= True )

    dt = trace[0] # the second temporal sampling point is the sampling
    stf.new_window( trace[1:])
    stf.set_sampling_interval( dt )
    stf.set_xunits('ms')
    stf.set_yunits('pA')
