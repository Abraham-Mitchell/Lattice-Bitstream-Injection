yosys -p "synth_ice40 -top blinky -json blinky.json" blinky.v 
nextpnr-ice40 --json blinky.json --asc blinky.asc --pcf Ice40_UP_LED.pcf --up5k --package sg48
icepack blinky.asc blinky.bin
sudo iceprog blinky.bin