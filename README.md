# multi-led-board 
#Bus 003 Device 005: ID 0451:f432 Texas Instruments, Inc. eZ430 Development Tool
ACTION=="add", \
SUBSYSTEM=="tty", \
ATTRS{idVendor}=="0451", \
ATTRS{idProduct}=="f432", \
MODE="4666", \
GROUP="led", \
SYMLINK+="led-monitor"
