# stimfit helpers

Modified from http://www.stimfit.org/doc/sphinx/manual/event_extraction.html

1. Import python module
    * /.../stimfit-helpers/xsg.py
    * https://github.com/trose-neuro/stimfit-helpers/blob/master/xsg.py
2. Import Scanimage *.xsg file with
    * xsg.load()
3. Press ‘F’ to fit trace to window
4. Zoom into one event
    * Press “Z"
    * Right click on window (expand)
5. Set baseline (‘B’), Latency (‘L’), Peak (‘P’) and Fit (‘D’) cursors (left / right click). 
6. Press ‘Return’ to get peak / rise time values etc
7. Fit Biexponential with delay (command + N)
8. Extract preliminary events / Generate ‘Bait’ template (threshold 10, template matching) 
    * Analysis”->”Event detection”->”Template matching… Template scaling”
9. Select “Extract selected events” from right-click event menu
10. RESET BASELINE (‘B’) AND PEAK (‘P’) IN RESULTING EVENT TRACE (also press ‘return’)
11. Run the event thresholder with reasonable threshold (e.g. -100pA)
    *  xsg.get_amplitude_select(-100)
    * This selects only traces with a peak >100pA and <0pA (hopefully excluding test-pulses)
12. Subtract baseline
    * Analyze > Subtract Baseline
13. Average trace
    * Push the ’sigma/n’ button
14. Reset baseline, peak, and fit cursors
15. Fit Biexponential with delay (command + N)
16. Go back to the window with the original full ephus trace
17. Final event detection (deconvolution)
    1. Analysis”->”Event detection”->”Template matching… Deconvolution”
    2. Use a std threshold of 4.5!
18. Select “Extract selected events” from right-click event menu
19. RESET BASELINE (‘B’) AND PEAK (‘P’) IN RESULTING EVENT TRACE (also press ‘return’)
20. Run the event thresholder with reasonable threshold (e.g. -100pA) Again
21. Reset baseline, peak, and fit cursors
22. Batch analyze all selected traces (incl. biexponential fit).
