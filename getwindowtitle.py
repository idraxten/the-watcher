from Xlib import *

# get the display and screen
dsp = display.Display()
scr = dsp.screen()

# get the active window ID
active_win = scr.root.get_full_property(
    dsp.intern_atom('_NET_ACTIVE_WINDOW'), 
    X.AnyPropertyType
).value[0]

# get the active window object
win_obj = dsp.create_resource_object('window', active_win)

# get the name of the process owning the window
process_id = win_obj.get_full_property(
    dsp.intern_atom('_NET_WM_PID'), 
    X.AnyPropertyType
).value[0]

# get the command line used to launch the process
with open(f'/proc/{process_id}/cmdline', 'rb') as f:
    cmdline = f.read().decode('utf-8')

# get the name of the executable
program_name = cmdline.split('\x00')[0]

print(program_name)
