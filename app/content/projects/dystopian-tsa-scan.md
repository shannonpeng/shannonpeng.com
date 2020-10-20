title: Dystopian TSA Scan
keyword: dystopian-tsa-scan
subtitle: A Kinect-powered interactive security scan prototype
date: 2020-05-11
context: MIT 21M.737 Interactive Design and Projection for Live Performance
tags: [Experiential Storytelling, Motion Graphics, Interactive Design]
technologies: [Kinect, Isadora, NI mate, After Effects, Logic Pro X, OSC, Syphon]
categories: [interactive]
label: Interactive Design
thumbnail: /static/images/projects/dystopian-tsa-scan/thumbnail.jpg
cover: /static/images/projects/dystopian-tsa-scan/thumbnail.jpg
caption: A screencap from the demo video.
color: 006078
video: https://www.youtube.com/watch?v=H7CRr3wcwLQ&list=PL13VJHLPzcIlgi0ceXD7n-MnPk4wwMh6Z&index=4
description: A Kinect-powered interactive security scan prototype
emoji: 👁‍🗨

In the MIT theatre class Interactive Design and Projection for Live Performance (21M.737), our first assignment is to introduce ourselves through a short "self-portrait" performance.

I'm a huge fan of sci-fi and dystopias (catch me binge-watching *Black Mirror*). I wondered, how could I add a dystopian twist to sharing fun facts about myself? I landed on the idea of an airport security scan gone too far.

<center><iframe width="560" height="315" style="max-width:100%" src="https://www.youtube.com/embed/H7CRr3wcwLQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

##### Watch the full demo video. (1:52)

<a href="https://www.youtube.com/watch?v=H7CRr3wcwLQ&list=PL13VJHLPzcIlgi0ceXD7n-MnPk4wwMh6Z&index=4" class="button">
	Watch Demo on YouTube <i class="fas fa-external-link-alt external-icon"></i>
</a>

## Going Interactive

In the first iteration of this project, I created a video, projected it onto a blank wall in the classroom space, and stood in front of it during my performance. Because the video's content and timing were fixed, I needed to practice timing my actions — walking onstage and raising/lowering my arms — until I got it right.

Later in the class, I revisited the piece and made it interactive, with the help of a [Kinect](https://en.wikipedia.org/wiki/Kinect) sensor, [NI mate](https://www.ni-mate.com/), and [Isadora](https://troikatronix.com/). Now I don't need to follow the video; the video follows me! The project tracks and uses the positions of my hands to progress through a sequence of scenes. 

## Behind the Scenes

Creating this piece led me through a variety of skills, from motion graphics to sensor integration, which made it all the more fun.

I started by hand-animating the motion graphics in After Effects.

<div class="image-set" markdown="1">

![Motion graphics in After Effects](/static/images/projects/dystopian-tsa-scan/ae.png "Hand-animated motion graphics in After Effects")

##### Motion graphics in After Effects.

</div>

In Logic Pro X, I recorded the voiceover, added music and sound effects, and mixed the audio.

<div class="image-set" markdown="1">

![Sound design in Logic Pro X](/static/images/projects/dystopian-tsa-scan/logic.png "Sound design in Logic Pro X")

##### Sound design in Logic Pro X.

</div>

In NI mate, I configured the Kinect sensor and set up communication between NI mate and Isadora: NI mate transmits Kinect data over OSC and real-time video input via Syphon.

I set up OSC and Syphon listeners in Isadora, assembled the video and audio clips, and implemented transition logic to integrate everything into an interactive experience.

<div class="image-set" markdown="1">

![Interactive logic in Isadora](/static/images/projects/dystopian-tsa-scan/isadora.png "Interactive logic in Isadora")

##### Interactive logic in Isadora.

</div>


## What's Next

While the scan responds to arm movement, its content is still fixed — it would ID everyone as me. But what if it didn't? What if it could dynamically display any user's biographical data, hobbies and interests, and psychological profile? Would that even be possible?

From a technological standpoint, it totally is. Access to our Facebook data alone (our profiles, reacts, check-ins, groups, and liked pages) could potentially unlock all of the above information. During the 2016 presidential election, [Cambridge Analytica](https://www.vox.com/science-and-health/2018/3/23/17152564/cambridge-analytica-psychographic-microtargeting-what) infamously psychologically profiled American voters based on their online activity. If I took the scan in this direction, the very existence of such a project would speak volumes about how little control we have over our data and privacy in this tech-driven world.

With a growing level of government surveillance, it's also not too hard to imagine a future in which even airport security procedures would tap into the wealth of data surrounding our digital identities.

This short, fun self-portrait project doubles as a piece that raises serious questions about where our digital privacy is headed in the future.

