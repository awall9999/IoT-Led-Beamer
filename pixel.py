#!/usr/bin/env python
import max7219.led as led
import time

CLOCKNUM = [
        [0x00,0xee,0xaa,0xaa,0xaa,0xee,0x00,0x00],  # '0'
        [0x00,0xe2,0xa2,0xa2,0xa2,0xe2,0x00,0x00],  # '1'
        [0x00,0xee,0xa2,0xae,0xa8,0xee,0x00,0x00],  # '2'
        [0x00,0xee,0xa2,0xae,0xa2,0xee,0x00,0x00],  # '3'
        [0x00,0xea,0xaa,0xae,0xa2,0xe2,0x00,0x00],  # '4'
        [0x00,0xee,0xa8,0xae,0xa2,0xee,0x00,0x00],  # '5'
        [0x00,0xee,0xa8,0xae,0xaa,0xee,0x00,0x00],  # '6'
        [0x00,0xee,0xa2,0xa2,0xa2,0xe2,0x00,0x00],  # '7'
        [0x00,0xee,0xaa,0xae,0xaa,0xee,0x00,0x00],  # '8'
        [0x00,0xee,0xaa,0xae,0xa2,0xee,0x00,0x00],  # '9'
        [0x00,0x2e,0x2a,0x2a,0x2a,0x2e,0x00,0x00],  # '10'
        [0x00,0x22,0x22,0x22,0x22,0x22,0x00,0x00],  # '11'
        [0x00,0x2e,0x22,0x2e,0x28,0x2e,0x00,0x00],  # '12'
        [0x00,0x2e,0x22,0x2e,0x22,0x2e,0x00,0x00],  # '13'
        [0x00,0x2a,0x2a,0x2e,0x22,0x22,0x00,0x00],  # '14'
        [0x00,0x2e,0x28,0x2e,0x22,0x2e,0x00,0x00],  # '15'
        [0x00,0x2e,0x28,0x2e,0x2a,0x2e,0x00,0x00],  # '16'
        [0x00,0x2e,0x22,0x22,0x22,0x22,0x00,0x00],  # '17'
        [0x00,0x2e,0x2a,0x2e,0x2a,0x2e,0x00,0x00],  # '18'
        [0x00,0x2e,0x2a,0x2e,0x22,0x2e,0x00,0x00],  # '19'
        [0x00,0xee,0x2a,0xea,0x8a,0xee,0x00,0x00],  # '20'
        [0x00,0xe2,0x22,0xe2,0x82,0xe2,0x00,0x00],  # '21'
        [0x00,0xee,0x22,0xee,0x88,0xee,0x00,0x00],  # '22'
        [0x00,0xee,0x22,0xee,0x82,0xee,0x00,0x00],  # '23'
        [0x00,0x88,0x88,0xf8,0x88,0x88,0x00,0x00],  # 'H'
        [0x00,0x88,0xd8,0xa8,0x88,0x88,0x00,0x00],  # 'M'
        [],  # 'H'
        [],  # 'H'
]  # end of CLOCKNUM

device = led.matrix(cascaded=1)
device.brightness(15)
while True:

     for u in range (0,26):
           for q in range (0,8):
       
                 a = (CLOCKNUM[u][q])
                 b= ('{0:08b}'.format(a))


                 for x in range (0,8):
             
                       t=(b[x])
                       if t == "1":
                           t=1
                       else:
                           t=0
                       print(x,q,t)
                       device.pixel((7-x), q, t, redraw=False)

           device.flush()
           time.sleep(0.5)

