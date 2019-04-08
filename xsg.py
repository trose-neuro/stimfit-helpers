import stf
import stfio
import wx as wx
import scipy.io as sio
import numpy as np

def load():

    # wx Widgets to create a file selection window
    fname = wx.FileSelector("Import Ephus file" ,
    default_extension = "Ephus XSG" ,
    default_path = "." ,
    wildcard = "Matlab Ephus xsg. text import (*.xsg)|*.xsg" ,
    flags = wx.OPEN | wx.FILE_MUST_EXIST)

    data_sio = sio.loadmat(fname, squeeze_me = True)
    data = data_sio.get('data');
    trace = data['ephys'].item().item()[0]
    header = data_sio.get('header')
    dt = header['ephys'].item().item()[0]['sampleRate'].item()

    stf.new_window( trace[1:])
    stf.set_sampling_interval(1000/np.double(dt))
    stf.set_xunits('ms')
    stf.set_yunits('pA')

# def get_amplitude(trace=None):
#     """ Calculates the amplitude deviation (peak-base) in units of the Y-axis
#
#     Arguments:
#     base        -- Starting point (in ms) of the baseline cursor.
#     peak        -- Starting point (in ms) of the peak cursor.
#     delta       -- Time interval to calculate baseline/find the peak.
#     trace       -- Zero-based index of the trace to be processed, if None then current
#                     trace is computed.
#
#
#     Returns:
#     A float with the variation of the amplitude. False if
#
#     Example:
#     get_amplitude(980,1005,10,i) returns the variation of the Y unit of the trace i between
#     peak value (10050+10) msec and baseline (980+10) msec
#     """
#
#     # sets the current trace or the one given in trace
#     if trace is None:
#         sweep = stf.get_trace_index()
#     else:
#         if typ(trace) != int:
#             print "trace argument admits only intergers"
#             return False
#         sweep = trace
#
#
#     # # set base cursors:
#     # if not(stf.set_base_start(base,True)): return False # out-of range
#     # if not(stf.set_base_end(base+delta,True)): return False
#     #
#     # # set peak cursors:
#     # if not(stf.set_peak_start(peak,True)): return False # out-of range
#     # if not(stf.set_peak_end(peak+delta,True)): return False
#
#     # update measurements
#     stf.set_trace(sweep)
#
#     amplitude = stf.get_peak()-stf.get_base()
#
#     return amplitude
# def save():
#     stf.file_save("/Users/trose/Data/test.dat")
