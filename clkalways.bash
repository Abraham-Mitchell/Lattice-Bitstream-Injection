yosys -p "synth_ice40 -top drive1toclock -json blinky.json" clkalways1.v 
nextpnr-ice40 --json blinky.json --asc clkalways1.asc --pcf clkalways1.pcf --up5k --package sg48
icepack clkalways1.asc clkalways1.bin
sudo iceprog clkalways1.bin