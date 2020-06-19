featured: true
title: Zooming Away
keyword: zooming-away
subtitle: An immersive space-themed escape room over Zoom call
date: 2020-05-11
context: 21M.737 Interactive Design and Projection for Live Performance
tags: [Experiential Storytelling, Escape Room, Interactive Design]
technologies: [Photoshop, Illustrator, Lens Studio, Snap Camera, Logic Pro X, SocketIO, Node.js, Javascript]
categories: [interactive]
label: Interactive Design
thumbnail: /static/images/projects/zooming-away/thumbnail.jpg
cover: /static/images/projects/zooming-away/cover.jpg
caption: Rachel Ride, an ASAN cosmonaut, is tumbling out of control and set to hit an asteroid in 10 minutes.
link: /static/images/projects/zooming-away/diagnostic-guide.pdf
github: https://github.com/dillzhang/space-console
color: 3c5ce2
collaborators: Dillon Zhang
description: An immersive space-themed escape room over Zoom video call

I created Zooming Away with my friend Dillon Zhang in May 2020. It was our final project for an MIT theatre class: 21M.737 Interactive Design and Projection for Live Performance.

## The Idea

Normally, the class would have us create interactive media for a physical space on campus. However, after the COVID-19 outbreak moved our classes online, we found ourselves with a new, unique challenge: creating an interactive live performance from the confines of our homes, to be shared with the class over video call.

Rather than create a traditional performance and "virtualize" it, we decided to embrace the format and build our project around a video call. Drawing inspiration from the game [Keep Talking and Nobody Explodes](https://keeptalkinggame.com/), we created a 15-minute, 2-4 player immersive escape room that takes place in a Zoom call and web browser.

## Walkthrough

### Email Invitation

The experience starts in your inbox: each member of your team has just completed ASAN space cadet training and receives an invite to a virtual commencement webcast, held over Zoom.

<div class="image-set image-set-two" markdown="1">

![Zooming Away email invitation](/static/images/projects/zooming-away/email.jpg "Zooming Away email invitation")

</div>

<div class="image-set image-set-two" markdown="1">

![Zooming Away cadet virtual background](/static/images/projects/zooming-away/cadet-bg.jpg "Zooming Away cadet virtual background")

##### Zooming Away email invitation and virtual background

</div>

### Virtual Commencement

When the time comes, you join the Zoom call, and the ceremony kicks off with a special congratulatory message from Jim Fredstine, Director of ASAN.

<div class="image-set" markdown="1">

![Congratulations from Jim Fredstine](/static/images/projects/zooming-away/jim.jpg "Congratulations from Jim Fredstine")

##### A special message from Jim Fredstine, Director of ASAN

</div>

A few minutes in, ASAN cosmonaut Rachel Ride dials in urgently and interrupts, "Mayday!" Her space capsule is tumbling out of control and set to hit an asteroid in 10 minutes. She needs your help down at ground control to stabilize it and get it back on course before it explodes.

<div class="image-set" markdown="1">

![Rachel Ride's emergency call](/static/images/projects/zooming-away/rachel.gif "Rachel Ride is in an emergency")

##### Rachel Ride interrupts the webcast with an emergency call for help.

</div>

### Diagnostic Guide and Control Console

As space cadets, you retrieve the ASAN diagnostic guide you received during training and remote dial into the control console in your browser.

<div class="image-set image-set-two" markdown="1">

![Diagnostic guide: cover](/static/images/projects/zooming-away/dg-cover.jpg "Diagnostic guide: cover")

</div>

<div class="image-set image-set-two" markdown="1">

![Diagnostic guide: page 1](/static/images/projects/zooming-away/dg-1.jpg "Diagnostic guide: page 1")
![Diagnostic guide: page 2](/static/images/projects/zooming-away/dg-2.jpg "Diagnostic guide: page 2")

</div>

<div class="image-set image-set-two" markdown="1">

![Diagnostic guide: page 3](/static/images/projects/zooming-away/dg-3.jpg "Diagnostic guide: page 3")

</div>

##### An excerpt of the ASAN diagnostic guide (full guide [here](/static/images/projects/zooming-away/diagnostic-guide.pdf))


<div class="image-set" markdown="1">

![Space cadet control console](/static/images/projects/zooming-away/console.png "Space cadet control console")

##### The space cadet control console

</div>

Through interacting with Rachel over video call and flipping through the guide to determine the correct console commands, you can stabilize Rachel's space capsule and help steer her back on course. But can you repair everything in under 10 minutes?

## How It Works

The space cadets (players) communicate with the cosmonaut (live actor) and her space capsule through two channels: the Zoom video call and the control console.

<div class="image-set" markdown="1">

![Flowchart of Zooming Away components](/static/images/projects/zooming-away/flowchart.jpg "Flowchart of Zooming Away components")

##### Flowchart of Zooming Away components

</div>

### Audio and Video FX

To sell the illusion that the live actor is dialing in from a space capsule, we process her microphone and webcam feeds before sending them to Zoom. We pass the audio through Logic Pro X, where we apply EQ, distortion, and other plugins to achieve a lo-fi, crackly sound. We run the video through [Snap Camera](https://snapcamera.snapchat.com/), where we add a head-tracking heads-up display, a shaking effect, a scanning effect, and color correction, using custom AR lenses made in [Lens Studio](https://lensstudio.snapchat.com/).

### Control Console, Actor's Panel, and Server

Hidden from the players is the actor's panel, which helps the live actor direct the game and locate relevant information.

<div class="image-set" markdown="1">

![Actor's panel](/static/images/projects/zooming-away/actors-panel.png "Actor's panel")

##### The actor's panel

</div>

**Game Controls:** The start, pause, and resume game buttons allow the live actor to control the clock.

**Line Prompter:** At the bottom, a line prompter gives the actor hints and starter lines for directing the players, though the majority of her dialogue is left to improvisation.

**Capsule Information:** The middle section of the actor's panel contains a range of information about the space capsule, which the actor can or cannot read depending on the capsule state. For example: in this screencap, we know that the number on the outside of the window is 21737, but in order to see what's inside the window, we'll need to close the window. If the players ask about the inside of the window, the actor could say, "The window's open. I can't see inside." The players should then figure out that they need to hit the "Close Window" command in their control console.

Both the actor's panel and space cadet control console are connected via web sockets (Socket.IO) and a web server (Node.js) that keeps track of the game state.

## Contributions

I designed all graphic assets, video FX, and audio FX, and played the role of the cosmonaut during our final presentation. Dillon wrote the puzzles; developed the control console, actor's panel, and server; and played the role of the Director of ASAN during the presentation. The two of us worked together to build the narrative and integrate all the parts into one cohesive experience.

## Reflections

Zooming Away received glowing reviews from our guest participants and class instructor! They praised its level of immersion and its use of a Zoom call as a storytelling medium.

My biggest takeaway from this project was that building interactive live experiences for our laptop screens opens more doors than it closes. We lost the chance to experiment with physical space, but we gained the opportunity to explore how AR lenses and web sockets can play a role in producing engaging experiences in our own homes.

Where could this take us in the future?
