# Lattice Bitstream Injection Guide

This guide walks through the process of synthesizing, placing-and-routing, converting, and programming a bitstream for the iCE40 FPGA using open-source tools.

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


