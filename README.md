# Lattice Bitstream Injection Guide

Install guide for the required tools (Yosys, nextpnr, all the IceStorm tools) can be found here: https://prjicestorm.readthedocs.io/en/latest/overview.html#what-is-project-icestorm

I did this on an Ubuntu VM. I ran into some problems during the install. If that happens, IDK just ask chatgpt.

One problem I do know how to (possibly) solve is if on VirtualBox VM the usb can't be recognized. With the Lattice board plugged in, go to Settings -> USB -> enable USB controller -> select USB 2.0 controller -> add new USB filter with all fields... -> Ok

Below are the instructions I used to flash blinky.v into the board. If everything works correctly you will see the LED loop through colors. 

---

## 1. Synthesize Verilog to JSON Netlist using Yosys

```bash
yosys -p "synth_ice40 -top blinky -json blinky.json" blinky.v other_module1.v other_module2.v
```

This command runs Yosys to synthesize your Verilog design into a gate-level netlist targeting iCE40 FPGAs.

- `-top blinky`: Specifies the top-level module.
- `blinky.json`: Output JSON-format netlist.
- **Important**: Include *all* Verilog files that define modules used in your design. Don't just list the top-level file if it instantiates other modules.

---

## 2. Place-and-Route the Design using nextpnr-ice40 (with GUI)

```bash
nextpnr-ice40 --json blinky.json --asc blinky.asc --pcf Ice40_UP_LED.pcf --up5k --package sg48 --gui
```

This maps the synthesized netlist to actual FPGA resources.

- `--json blinky.json`: Input synthesized design.
- `--asc blinky.asc`: Output ASCII-format FPGA config.
- `--pcf Ice40_UP_LED.pcf`: Pin constraints file (board-specific).
- `--up5k --package sg48`: Specifies the FPGA chip and package.
- `--gui`: Opens a visual layout viewer.

> **Note**: If the GUI opens but no `.asc` file is generated, try removing the `--gui` flag and rerun the command headless.

---

## 3. Convert ASCII Config to Binary Bitstream using icepack

```bash
icepack blinky.asc blinky.bin
```

This converts the `.asc` configuration into a `.bin` binary bitstream suitable for flashing onto the FPGA.

---

## 4. Program the FPGA using iceprog

```bash
sudo iceprog blinky.bin
```

This uploads the bitstream (`blinky.bin`) to the FPGA via USB through the SPI flash.

Only run this step if your FPGA board is connected and ready to be programmed.

---


