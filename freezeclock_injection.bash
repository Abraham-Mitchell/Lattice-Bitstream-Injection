#/bin/bash
yosys -p "synth_ice40 -top drive1toclock -json blinky.json" freezeclock.v 
nextpnr-ice40 --json blinky.json --asc freezeclock.asc --pcf freezeclock.pcf --up5k --package sg48
icepack freezeclock.asc freezeclock.bin
# sudo iceprog freezeclock.bin

#take the bin files and unpack them into asc
iceunpack freezeclock.bin circuit1.asc
iceunpack blinky.bin circuit2.asc

#extract the data from the asc files and store them in a json
python extractAsc.py circuit1.asc circuit1.json
python extractAsc.py circuit2.asc circuit2.json

#now process the json files and update them
python processingascdata.py circuit1.json circuit1_processed.json
python processingascdata.py circuit2.json circuit2_processed.json

#draw circuit images and save them as png files
python displaytiles.py circuit1_processed.json circuit1_tileusage.png
python displaytiles.py circuit2_processed.json circuit2_tileusage.png

#now try to combine the two json descriptions
python combine_circuits.py circuit1_processed.json circuit2_processed.json combined_circuit.json

#use the json file to create a new asc file
python json2asc.py combined_circuit.json combined_circuit.asc

#pack and program
echo combined both circuits. Now trying to pack and program
icepack combined_circuit.asc combined_circuit.bin
iceprog combined_circuit.bin