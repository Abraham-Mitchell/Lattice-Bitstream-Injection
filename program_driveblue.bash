yosys -p "synth_ice40 -top drive_blue -json blinky.json" drive_blue.v 
nextpnr-ice40 --json blinky.json --asc drive_blue.asc --pcf drive_blue.pcf --up5k --package sg48
icepack drive_blue.asc drive_blue.bin
sudo iceprog drive_blue.bin