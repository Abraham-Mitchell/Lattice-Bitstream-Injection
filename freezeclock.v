module drive1toclock(
    input wire btn,
    output wire clk
);
    (* keep *) wire clk;
    assign clk = btn ? 1'bz : 1'b1;

endmodule