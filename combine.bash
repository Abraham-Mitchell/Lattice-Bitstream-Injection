#/bin/bash
iceunpack blinky_RG.bin circuit1.asc
iceunpack drive_blue.bin circuit2.asc

python extractAsc.py circuit1.asc circuit1.json
python extractAsc.py circuit2.asc circuit2.json

python combine_circuits.py circuit1.json circuit2.json combined.json

python json2asc.py combined.json combined.asc

icepack combined.asc combined.bin
sudo iceprog combined.bin