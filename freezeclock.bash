yosys -p "synth_ice40 -top drive1toclock -json blinky.json" freezeclock.v 
nextpnr-ice40 --json blinky.json --asc freezeclock.asc --pcf freezeclock.pcf --up5k --package sg48
icepack freezeclock.asc freezeclock.bin
sudo iceprog freezeclock.bin