module drive_blue(input clk, output led_blue);
    always @(clk)
    begin
        led_blue = clk;
    end
endmodule