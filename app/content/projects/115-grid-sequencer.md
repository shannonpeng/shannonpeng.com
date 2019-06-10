featured: true
title: Grid Sequencer
keyword: 115-grid-sequencer
subtitle: Compose and visualize musical patterns
date: 2019-05-16
context: 6.115 Microcomputer Project Laboratory
tags: [Electronics, Embedded Systems, Music Technology]
technologies: [PSoC, C, Button Pad, LEDs, Speaker]
categories: [code, make]
label: Embedded Systems
thumbnail: /static/images/projects/115-grid-sequencer/thumbnail.jpg
cover: /static/images/projects/115-grid-sequencer/cover.jpg
color: 89a4f8
github: https://gist.github.com/shannonpeng/1657018d92a1b81b7fcb56381519141a
video: https://youtu.be/TMPp4XCwnAg
caption: A demo of my finished grid sequencer.
description: A simple grid sequencer for composing and visualizing musical patterns, programmed in C

I built a simple grid sequencer as my final project for [6.115](http://web.mit.edu/6.115/www/page/home.html), a class on microcontrollers and embedded systems. The goal of my project was to bring an embedded software project from concept to working prototype (and also create something cool and creative!) Watch demos of my sequencer making drum patterns (percussion) or notes (melody) in the videos below.

<a href="https://youtu.be/TMPp4XCwnAg" class="button">
	Watch Percussion Demo
</a>

<a href="https://youtu.be/fCk_Kd_At4U" class="button">
	Watch Melody Demo
</a>

## The Idea

Grid instruments, like the [Novation Launchpad](https://novationmusic.com/launch/launchpad), are often used in electronic music production and live performance to create looping patterns of sounds. A simple one works like this:

<div class="image-set" markdown="1">

![The Idea: diagram](/static/images/projects/115-grid-sequencer/diagram.jpg "The Idea: diagram")

</div>

In the grid, rows represent different sounds, and columns represent different times. The user toggles buttons to indicate which sounds should be played and when.

The sequencer cycles through the columns in order, and it plays the correct combination of sounds when it arrives at each column.

## Setting Up the Button Pad

To assemble a grid with 4 rows and 8 columns, I bought 2 [SparkFun 4x4 button pads](https://www.sparkfun.com/products/7835), the corresponding breakout PCBs and bezels, and 3mm common anode RGB LEDs.

Setting up 32 buttons and LEDs, even in a matrix arrangement, involved a *lot* of soldering. At the end, my 4x8 button pad had 32 wires coming out of it! Managing them all was a fun time.

<div class="image-set" markdown="1">

<div class="image-set image-set-two" markdown="1">

![Breakout PCB: front](/static/images/projects/115-grid-sequencer/pcb-front.jpg "Breakout PCB: front")
![Breakout PCB: back](/static/images/projects/115-grid-sequencer/pcb-back.jpg "Breakout PCB: back")

##### The front and back of the button pad breakout PCB. (SparkFun)

</div>

<div class="image-set" markdown="1">

![So many wires](/static/images/projects/115-grid-sequencer/wires.jpg "So many wires")

##### It was hard to cut wires to the perfect length between the two boards.

</div>
</div>

## Grid Software Interface

After assembling my grid controller, I set up a software interface for it. 6.115 provided us with [PSoC boards](https://www.cypress.com/documentation/development-kitsboards/cy8ckit-050-psoc-5lp-development-kit), which are like an instant chip inventory. Inside PSoC Creator, I could configure pins on the board to act like a variety of chips.

The software interface involved (1) matrix scanning to detect button presses, and (2) updating the LED matrix to reflect grid state.

### Button Matrix Scanning
- When the buttons are pressed, conductive circles underneath them make contact with the circles on the breakout PCB.
- To detect a button press, I cycled through the rows one at a time, driving the row `HIGH` (and the other rows `LOW`) and read in the output of each column. If a column was also `HIGH`, then I know the button at that row and column is currently being pressed.

<div class="image-set image-set-two" markdown="1">

![Button press](/static/images/projects/115-grid-sequencer/button-press.jpg "Button press")

##### A scope screenshot of a button press.

</div>

- I maintained two 2D arrays, one reflecting transient button state, and one reflecting the persistent grid state. I used the first array to detect key-up events and toggle the corresponding value in the second array.

### LED Matrix
- To turn on a common anode LED, I would drive the anode `HIGH` then drive a combination of the R, G, and B lines `LOW`. If I connected all 32 wires to analog PSoC pins, I could set my LEDs to any RGB color, but:
	- Because the PSoC couldn't source enough current to drive all the LEDs, I brought in [LM293](http://web.mit.edu/6.115/www/document/lm18293n.pdf) push/pull drivers. These drivers work with digital inputs and outputs, so I needed to configure my RGB lines as digital, limiting myself to 8 possible colors.
	- The PSoC has limited I/O pins, and I wanted to save those for other functions.
- To keep things simple and compatible with the drivers, I designated one color per row: <span style="color:#70eafb;font-weight:bold">turquoise</span> (0% R 100% G 100% B), <span style="color:#e58bf6;font-weight:bold">pink</span> (100% R 0% G 100% B), <span style="color:#8ea5f2;font-weight:bold">blue</span>, and <span style="color:#69e0a7;font-weight:bold">green</span>. 
- For turquoise and pink, I connected two color wires to the same driver output so I could control them both at the same time. This setup ultimately saved me 9 PSoC pins.
- I made liberal use of C's shift and bitwise logic operators to match the LEDs to a 2D array representing the grid state.

Now, I have a grid controller that turns on an LED when I press the corresponding button!

## Playing Audio
The next step was to get my PSoC to play audio. Originally, I wanted to play 16-bit, 44.1 kHz WAV drum samples using an external RAM chip. After wiring up my RAM, however, I realized, *how am I supposed to transfer such a large amount of audio data onto the RAM every time the program starts up?*

Converting WAV files to C arrays and putting them into code memory didn't seem feasible, because the PSoC internal memory was very limited. I tried burning them onto a ROM chip, but I ran into unknown errors with lab chip burners. I looked into using serial, but it seemed unnecessarily complex.

Soon, I found a much simpler (though hackier) solution. I discovered that PSoC Creator's [WaveDAC](https://www.cypress.com/documentation/component-datasheets/8-bit-waveform-generator-wavedac8) component allows for custom user-defined tables. If I converted my WAV files to CSV files of 8-bit raw audio data, then WaveDAC could play them!

<div class="image-set image-set-two" markdown="1">

![WaveDAC](/static/images/projects/115-grid-sequencer/wavedac.jpg "WaveDAC")

##### WaveDAC configuration with a custom table loaded into Waveform 1.

</div>

WaveDAC takes a max of 4000 table values between 0 and 255, so I downsampled my WAV files to 8-bit, 16 kHz and trimmed and padded them to exactly 0.25 seconds. I also removed the WAV metadata and headers in Audacity. And then... my PSoC played drums! (And the 8-bit, 16 kHz samples didn't sound *that* bad, too!)

## Timing and Sequencer Logic

The driving force of a sequencer is a timer that determines which column is active. I implemented this with a PSoC [Timer](https://www.cypress.com/documentation/component-datasheets/timer) component and had it generate a software interrupt on overflow (with the max load value, the interrupt period was 2.731 ms).

Every `NUM_INTERRUPTS` interrupts, the interrupt handler increments the active column, starts the appropriate WaveDAC components, and turns on all LEDs in that column. The result is a "shifting" column of LEDs that shows the sequencer timing.

The tempo is set by the `NUM_INTERRUPTS` variable:

<center>**tempo** = 60  / (`NUM_INTERRUPTS` * 0.002731)</center>

The user can control the sequencer tempo by adjusting the PSoC's onboard potentiometer. I read the potentiometer value using an ADC, and then mapped that to the `NUM_INTERRUPTS` variable. Using a 12-bit ADC, `adcResult` ranges from `0x0000` to `0x0FFF`:

<center>**`NUM_INTERRUPTS`** = 400 - (`adcResult` * 300)  / `0x0FFF` </center>

This gives a `NUM_INTERRUPTS` range of 100-400, which yields tempos of approximately 220 to 55 columns per minute.

## Mixing Audio

One downside of using WaveDAC components is that it's difficult to manipulate their outputs in code — I couldn't sum the outputs of multiple WaveDAC components to play multiple sounds at once.

<div class="image-set image-set-two" markdown="1">

![Analog mixer](/static/images/projects/115-grid-sequencer/mixer.jpg "Analog mixer")

##### An analog mixer example. (Jacob Smith)

</div>

I decided to build an analog mixer instead, following [this tutorial](https://www.allaboutcircuits.com/projects/build-an-audio-mixer/) by Jacob Smith. This added the bonus feature of being able to adjust relative volumes using potentiometers.

## Additional Challenges

- An issue with the WaveDACs is that they don't stop after playing a sound once, or one iteration of the table — which I guess makes sense, because you normally wouldn't want a waveform generator to stop after one period. To work around this, I wrote interrupt handlers that stop a WaveDAC after one iteration of the table. This results in some blips in the audio when a WaveDAC stops, but it's necessary to keep the samples from playing more than once per column.
- Because WaveDACs can only play one sound at a time, if the tempo becomes too fast such that a column is active for less time than the duration of the sound, and there are two consecutive sounds in a row, the second sound would not play. I took the easy fix by lowering the tempo limit. Given more time, I would like to develop a more solid solution.
- I liked being able to play pitched notes, so I created an easy way to program the sequencer with either a [percussion](https://youtu.be/TMPp4XCwnAg) and [melody](https://youtu.be/fCk_Kd_At4U) mode!

## PSoC Creator Schematic

<div class="image-set" markdown="1">

![PSoC schematic](/static/images/projects/115-grid-sequencer/schematic.jpg "PSoC schematic")

##### My final PSoC Creator schematic. [View Code](https://gist.github.com/shannonpeng/1657018d92a1b81b7fcb56381519141a)

</div>

## Reflections

This project taught me the value of being flexible. Coming in, I had minimal experience with C programming or PSoC Creator, and I wasn't sure about how to implement most of my ideas. Many times, the implementation I'd guessed didn't work out, and I learned a lot through adapting and exploring alternative strategies.

Overall, this final project, and 6.115 in general, have helped me become more confident in my ability to envision and implement embedded software projects. In the many long hours I've invested into this class, I've become more fluent with design patterns, working with lab equipment, reading data sheets, and integrating various types of chips into a system. I also had fun playing around with my finished grid sequencer :)

I especially found working with audio — picking apart WAV files and manipulating them as data points — interesting, and I would like to explore that in more depth in the future, maybe in C next time!

<div class="image-set" markdown="1">

![Final demo](/static/images/projects/115-grid-sequencer/final.jpg "Final demo")

##### My finished sequencer.

</div>

