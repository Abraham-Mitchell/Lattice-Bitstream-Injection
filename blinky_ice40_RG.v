module blinky (
    input wire clock_12mhz,
    output reg led_red,
    output reg led_green,
    output reg led_blue
);

    reg [23:0] counter = 0;         // 24-bit counter for ~1 second delay at 12 MHz
    reg [1:0] led_state = 0;        // LED state machine: 0 = red, 1 = green, 2 = blue

    always @(posedge clock_12mhz) begin
        counter <= counter + 1;

        if (counter == 24'd12_000_000) begin  // 1 second = 12 million clock cycles at 12 MHz
            counter <= 0;
            led_state <= led_state ^ 1;
        end
    end

    always @(*) begin
        // Turn on only one LED at a time based on led_state
        led_red   = (led_state == 2'd0);
        led_green = (led_state == 2'd1);
        //led_blue  = (led_state == 2'd2);
   
    end

endmodule

