# multi-led-board 
#Bus 003 Device 005: ID 0451:f432 Texas Instruments, Inc. eZ430 Development Tool <br>
ACTION=="add", \ <br>
SUBSYSTEM=="tty", \ <br>
ATTRS{idVendor}=="0451", \ <br>
ATTRS{idProduct}=="f432", \ <br>
MODE="4666", \ <br>
GROUP="led", \ <br>
SYMLINK+="led-monitor" <br>
