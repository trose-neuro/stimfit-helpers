# Stimfit protocol (incl. python module to import Ephus xsg files) to perform event extraction

(update September 2019 - TR)

Also see
http://www.stimfit.org/doc/sphinx/manual/event_extraction.html
https://github.com/neurodroid/stimfit

Install StimFit
https://github.com/neurodroid/stimfit/releases

This should give you pxthon 2.7 as well. To install the necessary Scipy for pyton 2.7 cd into your ```C:\Python27\Scripts``` folder. Then do ```pip install scipy```. Works for every python 2.7 module like this.

Download python module
/.../stimfit-helpers/xsg.py
https://github.com/trose-neuro/stimfit-helpers/blob/master/xsg.py
For PC it is easiest to copy xsg.py to the stimfit root folder.

---
1. **import xsg** with `import xsg`
  - Import Scanimage *.xsg file with `xsg.load()`
---  
2. Press ‘F’ to fit trace to window  
3. Zoom into one event
  - Press “Z"
  - Right click on window (expand)
4. Set baseline (‘B’), Peak (‘P’) and Fit (‘D’) cursors (left / right click).
5. Press ‘Return’ to get peak / rise time values etc.
6. Fit Biexponential with delay (command or control  + N) - fit function 5
---
7. Extract **preliminary events** / Generate ‘Bait’ template (threshold 10, template matching)
   - `Analysis”->”Event detection”->”Template matching… Template scaling`
8. press 'E' for event selection tool
9. Select “Extract selected events” from right-click event menu
10. RESET BASELINE (‘B’) AND PEAK (‘P’) IN RESULTING EVENT TRACE (also press ‘return’)
11. Run the event thresholder with reasonable threshold (e.g. -100pA)
 - `xsg.get_amplitude_select(-100)` This selects only traces with a peak >100pA and <0pA (hopefully excluding test-pulses)
12. Subtract baseline
  - `Analyze > Subtract Baseline`
13. select all resulting traces (ctr + a)
14. Average trace
   - Push the ’sigma/n’ button
15. Reset baseline, peak, and fit cursors
16. Fit Biexponential with delay (command + N)
17. Go back to the window with the original full ephus trace
---
18. **Final event detection** (deconvolution)
  - `Analysis”->”Event detection”->”Template matching… Deconvolution”`.
  - *Use a std threshold of 4*!
19. Select “Extract selected events” from right-click event menu
20. Copy resulting "extracted events" table to *new excel sheet*
21. RESET BASELINE (‘B’) AND PEAK (‘P’) IN RESULTING EVENT TRACE (also press ‘return’)
22. Run the event thresholder with reasonable threshold (e.g. -100pA - `xsg.get_amplitude_select(-100)`) Again
23. get indices of selected traces manually (no idea how to extract otherwise)
  - `stf.get_selected_indices()`
22. copy resulting numbers into excel sheet (pls use same col and row for this across sheets)
23. Reset baseline, peak, and fit cursors (can also be done on average event - save / note cursor positions ant vopy to here)
24. Batch analyze all selected traces (incl. biexponential fit).
  - check all boxes except "threshold crossing"
25. Copy results to new page in same excel sheet.
26. Save excel sheet in data folder under `xsg filename . xls`
