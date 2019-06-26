import stf
import stfio
import wx as wx
import scipy.io as sio
import numpy as np


def load():

    # wx Widgets to create a file selection window
    fname = wx.FileSelector("Import Ephus file",
                            default_extension="Ephus XSG",
                            default_path=".",
                            wildcard="Matlab Ephus xsg. text import (*.xsg)|*.xsg",
                            flags=wx.OPEN | wx.FILE_MUST_EXIST)

    data_sio = sio.loadmat(fname, squeeze_me=True)
    data = data_sio.get('data')
    trace = data['ephys'].item().item()[0]
    header = data_sio.get('header')
    dt = header['ephys'].item().item()[0]['sampleRate'].item()

    stf.new_window(trace[1:])
    stf.set_sampling_interval(1000 / np.double(dt))
    stf.set_xunits('ms')
    stf.set_yunits('pA')


def get_amplitude_select(amplithresh):
    stf.unselect_all()
    stf.set_peak_direction('both')
    # total number of traces
    traces = stf.get_size_channel()
    selectedtraces, i = 0, 0

    while i < traces:
        stf.set_trace(i)
        amplitude = stf.get_peak() - stf.get_base()
        if amplitude > amplithresh and amplitude < 0:
            # print(i)
            stf.select_trace(i)
            i += 1
            selectedtraces += 1
        else:
            i += 1

    return selectedtraces


def save():
    stf.file_save("/Users/trose/Data/test.dat")
