
# Tell me baby, do you recognise me?

A brief solution of how to solve this challenge which was given in ISTE and MIST Aurora CTF.


## Solution
An image was provided with the challenge.


![HCCB](https://file.notion.so/f/f/07ddc1d2-0a10-4826-b971-c4945010857a/9453190d-c351-4a83-964f-10fac3b1c5b8/nice_pic.png?id=14241058-f3ec-42cf-83ed-15923dfb57c2&table=block&spaceId=07ddc1d2-0a10-4826-b971-c4945010857a&expirationTimestamp=1707523200000&signature=OiK69SOhTUvVGyvlOWm6Vss3oDeOhjd3pmbTYw_xqIE&downloadName=nice_pic.png)

This image is a **High Capacity Color Barcode**, proprietary technology made by Microsoft back in 2007(?). 

More information regarding the barcode can be found [here](https://www.microsoft.com/en-us/research/project/high-capacity-color-barcodes-hccb/).

From the same webpage, we can go to the patents section of the inventor where we can find one of his projects which goes by [System and method for encoding high density geometric symbol set](https://patents.google.com/patent/US7936901B2). The patent page generally talks about how geometric shapes and colours can be used to represent data. This page also consists of images among which there is a particular image that you might want to focus on.

![encoding](https://patentimages.storage.googleapis.com/4b/41/e7/4c3bbb3bb44777/US07936901-20110503-D00006.png)

In figure 12, you can see that a colour represents 3 bites, and 2.66 of colours represent a byte. The bits sequence are colour coded with respect to their RGB values. 

### Colour to bits conversion

| Bit sequence      | RGB Value                                                          |
| ----------------- | ------------------------------------------------------------------ |
| 000 | ![rgb(0, 0, 0)](https://via.placeholder.com/10/000000?text=+) rgb(0, 0, 0) |
| 001 | ![rgb(0, 0, 255)](https://via.placeholder.com/10/0000ff?text=+) rgb(0, 0, 255) |
| 010 | ![rgb(0, 255, 0)](https://via.placeholder.com/10/00ff00?text=+) rgb(0, 255, 0) |
| 011 | ![rgb(0, 255, 255)](https://via.placeholder.com/10/00ffff?text=+) rgb(0, 255, 255) |
| 100 | ![rgb(255, 0, 0)](https://via.placeholder.com/10/ff0000?text=+) rgb(255, 0, 0) |
| 101 | ![rgb(255, 0, 255)](https://via.placeholder.com/10/ff00ff?text=+) rgb(255, 0, 255) |
| 110 | ![rgb(255, 255, 0)](https://via.placeholder.com/10/ffff00?text=+) rgb(255, 255, 0) |
| 111 | ![rgb(255, 255, 255)](https://via.placeholder.com/10/ffffff?text=+) rgb(255, 255, 255)|

### Translation

Since we have the image and conversion table, we can start decoding.

The binary data of the first line would be `011 000 010 110 001 101 110 100`.
Similarly we can translate all the lines. At last, we would end up with this sequence:

    011 000 010 110 001 101 110 100 011 001 100 111 101 101 101 000 001 100 000 111 011 101 011 111 011 001 000 011 000 101 100 100 010 111 110 111 010 101 011 111 011 001 110 011 001 101 110 100 010 111 110 110 100 000 110 011 011 100 100 011 001 101 111 101

This can be written as:

    01100001 01100011 01110100 01100110 01111011 01101000 00110000 01110111 01011111 01100100 00110001 01100100 01011111 01110101 01011111 01100111 00110011 01110100 01011111 01101000 00110011 01110010 00110011 01111101


If you put this binary data in any binary-to-ascii translator online, you should be able to get the flag.

Flag: `actf{h0w_d1d_u_g3t_h3r3}`
