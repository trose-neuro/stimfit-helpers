import stf

def loadtxt( freq=10000 ):
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
        default_extension = "Ratiometric" ,
        default_path = "." ,
        wildcard = "Matlab Ephus xsg. text expor (*.xsgtxt)|*.xsgtxt" ,
        flags = wx.OPEN | wx.FILE_MUST_EXIST)

    stf.new_window( np.loadtxt( fname ) )
    stf.set_xunits('ms')
    stf.set_yunits('pA')

    stf.set_sampling_interval(1.0/freq*1000) # acquision in ms
