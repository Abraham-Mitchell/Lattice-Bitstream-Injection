yosys -p "synth_ice40 -top blinky -json blinky.json" blinky_ice40_RG.v 
nextpnr-ice40 --json blinky.json --asc blinky_alt.asc --pcf modified_Ice40_UP_LED.pcf --up5k --package sg48
icepack blinky_alt.asc blinky_alt.bin
//sudo iceprog blinky_alt.bin

#/bin/bash

#take the bin files and unpack them into asc
iceunpack blinky_RG.bin circuit1.asc
iceunpack blinky_alt.bin circuit2.asc

#extract the data from the asc files and store them in a json
python extractAsc.py circuit1.asc circuit1.json
python extractAsc.py circuit2.asc circuit2.json

# #now process the json files and update them
python processingascdata.py circuit1.json circuit1_processed.json
python processingascdata.py circuit2.json circuit2_processed.json

# #draw circuit images and save them as png files
python displaytiles.py circuit1_processed.json circuit1_tileusage.png
python displaytiles.py circuit2_processed.json circuit2_tileusage.png

# #now try to combine the two json descriptions
python combine_circuits.py circuit1_processed.json circuit2_processed.json combined_circuit.json

#use the json file to create a new asc file
python json2asc.py combined_circuit.json combined_circuit.asc

# #pack and program
echo combined both circuits. Now trying to pack and program
icepack combined_circuit.asc combined_circuit.bin
iceprog combined_circuit.bin