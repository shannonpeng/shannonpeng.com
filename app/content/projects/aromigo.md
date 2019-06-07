title: Aromigo
keyword: aromigo
subtitle: Connecting long-distance partners through familiar aromas
date: 2018-10-31
context: MAS.834 Tangible Interfaces
tags: [Tangible Interfaces, Interation Design, Electronics, Prototyping, Bluetooth]
technologies: [Arduino Uno, XBee, Peltiers, LEDs]
materials: [Lampshade, Essential Oils, Wooden Bowl, Copper Wire]
categories: [design, make]
label: Tangible Interfaces
thumbnail: /static/images/projects/aromigo/thumbnail.jpg
cover: /static/images/projects/aromigo/cover.jpg
color: b99bea
collaborators: Je Sung Lee and Joanne Leong
description: Connecting long-distance partners through Bluetooth-enabled oil warmers

I created Aromigo with my team in Tangible Interfaces, an interaction design class taught by the [Tangible Media](https://tangible.media.mit.edu/) group at the MIT Media Lab. For this project, I focused on Arduino programming, working with the sensors and XBee, and learning about principles of interaction design.

## Inspiration

It’s said that of the five senses (sight, hearing, smell, touch, and taste), smell is most powerfully linked to memory. We associate smells with many people and places around us. What if we used smell as means of communication, as a way to show that we’re thinking of one another?

Aromigos are paired devices that enable long-distance communication through aroma. Each partner sets a personalized aroma and color, and through touch, they can concurrently control the emission of their aroma and light color, in their device and their partner’s. In turn, the presence of the partner’s aroma and light color represent the partner’s way of saying, "I'm here and thinking of you."

## Narrative

Alex and Bailey are in a long-distance relationship and own a pair of Aromigos. Back when they lived closer together, Bailey would always use lavender-scented lotion, and whenever Alex made hot chocolate, he would add some peppermint.

Every time Alex smells lavender, he would think of Bailey—and every time Bailey smells peppermint, she would think of Alex. They configured their Aromigos so that Bailey’s color is pink and her aroma is lavender, and Alex’s color is blue and her aroma is peppermint.

<div class="image-set" markdown="1">

![Alex and Bailey's Aromigos](/static/images/projects/aromigo/narrative.jpg "Alex and Bailey's Aromigos")

##### Aromigo changes color and emits different aromas<br> based on who is currently interacting with the device.

</div>

One day, Bailey gets home from work and notices that her Aromigo is pulsing blue, and the room smells like peppermint—Alex is thinking of her! She puts her stuff down and walks over to touch her Aromigo. As soon as she touches it, the light begins to pulse purple, and the smell of lavender slowly enters the air, mingling with the peppermint.

On the other side of the country, Alex sees his Aromigo turn purple, and starts to smell some lavender in the air. He knows this means that Bailey is also thinking of him, and he is warmed by the knowledge that both of them are touching their Aromigos at the same time.

## Design Process

First, we met for multiple ideation sessions - brainstorming, selecting our idea, and then sketching and discussing possible interactions with an aroma-based interpersonal communication device.

<div class="image-set" markdown="1">
	
![Process: chalk one](/static/images/projects/aromigo/process-chalk1.jpg "Process: chalk one")
![Process: chalk two](/static/images/projects/aromigo/process-chalk2.jpg "Process: chalk two")

##### Our team brainstormed by listing, sketching out, and organizing our ideas on a chalkboard throughout multiple meetings.

</div>

<div class="image-set image-set-two" markdown="1">
	
![Process: sketch one](/static/images/projects/aromigo/process-sketch1.jpg "Process: sketch one")
![Process: sketch two](/static/images/projects/aromigo/process-sketch2.jpg "Process: sketch two")

##### After narrowing down our ideas, Joanne created some refined, labeled sketches to develop the ideas further. Here are the sketches for Aromigo, originally titled “connected oil warmers.”


</div>

We then began prototyping, gathering hardware components and writing code for the Arduino. In parallel, we rapidly explored multiple variations of the physical design using a variety of household objects.

<div class="image-set" markdown="1">

<div class="image-set image-set-three" markdown="1">
	
![Process: form one](/static/images/projects/aromigo/process-form1.jpg "Process: form one")
![Process: form two](/static/images/projects/aromigo/process-form2.jpg "Process: form two")
![Process: form three](/static/images/projects/aromigo/process-form3.jpg "Process: form three")

</div>

<div class="image-set image-set-two" markdown="1">
	
![Process: model one](/static/images/projects/aromigo/process-model1.jpg "Process: model one")
![Process: model two](/static/images/projects/aromigo/process-model2.jpg "Process: model two")

</div>

##### Je Sung began exploration on the physical form of Aromigo by experimenting with household objects.

</div>

We decided on the materials, constructed the final housing, and secured the electronics inside. After several iterations, we arrived at the final configuration.

<div class="image-set" markdown="1">

<div class="image-set image-set-two" markdown="1">
	
![Process: prototype two](/static/images/projects/aromigo/process-prototype2.jpg "Process: prototype two")
![Process: prototype three](/static/images/projects/aromigo/process-prototype3.jpg "Process: prototype three")

</div>

![Process: prototype one](/static/images/projects/aromigo/process-prototype1.jpg "Process: prototype one")

##### Later stages of prototyping the interaction with Aromigo using the capacitive sensor and LEDs.

</div>

## Affordances

An essential step in interaction design is thinking critically about the affordances of the design. Here are the perceived and intended affordances we compiled in our analysis.

### Perceived Affordances
- The round, curved shape of the Aromigo invites the user to rest their hands on the device.
- The chimney-like shape and presence of a spout and dish create an expectation that something can be released from the opening.
- The presence of the dish also suggests that it should be filled.

### Intended Affordances
- The user can rest their hands on the sides of the device.
- The larger, weighted bottom discourages the user from picking the device up.
- The user can smell aromas emitted from the opening.

### Aesthetics and Interactions

- The pulsing lights can help bring a user’s attention to their breath. This creates a meditative feel when interacting with the Aromigo.
- Aromigo can be both in the user’s center of attention or in the ambience; it can play a role in both the foreground and the background.
- The refined aesthetic induces respect for the device, which helps it embody the significance of other person.

## What's Inside

Each Aromigo device consists of a white, semi-translucent polycarbonate lampshade with a small rim at the top and a larger rim at the bottom. The lampshade sits on top of a wooden bowl.

<div class="image-set image-set-two" markdown="1">
	
![Inside Aromigo](/static/images/projects/aromigo/inside.jpg "Inside Aromigo")

##### The inner workings of Aromigo.

</div>

The electronics are tucked away from sight, attached to the inside of the bowl using tape. A hole drilled into the top of the bowl allows for the bolt, which supports a peltier, and several LED wires to come through.

Inside the bowl, the components are driven by the Arduino Uno microcontroller. The Uno takes inputs from the capacitive sensor on this device, as well as through the XBee (receiving information from the partner device), and uses that information to control the LEDs and the peltiers (through the motor driver).

### Inputs (Sensors)
- Touch sensing data from this device (capacitive touch sensor / copper wire)
- Touch sensing data from the partner device (through XBee communication)

### Outputs (Actuators)
- Peltiers, which heat up the essential oils
- LEDs, which indicate current interaction through color 

### Components Per Device

- 1 Arduino Uno
- 2 peltiers
- 1 TB6612FNG motor driver
- 1 red silicone adhesive sealant
- 4 ft copper wire (capacitive touch sensor)
- 1 10 MOhm resistor
- 1 12V power adapter, for peltiers
- 2 NeoPixel LEDs
- 1 breadboard
- 1 XBee
- 1 polycarbonate lampshade
- 1 wooden bowl
- 1 ¼ inch stud
- 2 ¼ inch nuts
- 1 stainless steel tray

### State Table

![State table](/static/images/projects/aromigo/state-table.jpg "State table")

### Software Features
- **Safety Timers** The code ensures that no peltier is heating for more than 5 seconds — after 5 seconds, the code forces the peltier to cool for a minimum of 5 seconds.
- **LED Pulsing** The code increases and decreases the LED brightness by a factor of 5 for each interval. This creates a subtle “pulsing” effect.
- **Moving Average Smoothing** The signal coming in through the capacitive touch sensor is smoothed using a moving average method.
- **Communication via XBee** Each device emits and receives touch sensing data through XBee.

## Final Presentation and Demo

<div class="image-set image-set-two" markdown="1">
	
![Presentation: slides](/static/images/projects/aromigo/present1.jpg "Presentation: slides")
![Presentation: demo](/static/images/projects/aromigo/present2.jpg "Presentation: demo")

##### Our final presentation and demo in class.

</div>

## Reflections

Through Aromigo, I learned about analyzing affordances and illustrating interactions with narratives, as well as working with new hardware components (controlling peltiers and networking via XBee) and smoothing sensor signals. 

Aromigo also gave me a venue to explore new questions and areas of design. While most products seek to make our lives more convenient now, Aromigo addresses our emotional needs and envisions how technology might connect us many years into the future.
