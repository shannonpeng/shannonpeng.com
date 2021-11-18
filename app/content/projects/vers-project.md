featured: true
title: The V.E.R.S. Project
keyword: vers-project
subtitle: An Area 51-themed live remote interactive adventure
date: 2021-02-07
tags: [Experiential Storytelling, Escape Room, Interactive Design, Game Design]
technologies: [Adobe Creative Suite, Logic Pro X, QLab, SocketIO, React, Node.js, Javascript, HTML, CSS, Zoom]
categories: [code, interactive]
label: Interactive Design
thumbnail: /static/images/projects/vers-project/thumbnail.jpg
cover: /static/images/projects/vers-project/cover.jpg
caption: "It's time to prove that aliens are real, once and for all. Can your team help @lex break into Area 51 without getting caught? (Cover Art: @lex's desk)"
color: 5CAF00
link: https://versproject.herokuapp.com
video: https://www.youtube.com/watch?v=R0-Npw_SJDs&list=PL13VJHLPzcIlgi0ceXD7n-MnPk4wwMh6Z&index=5
collaborators: Dillon Zhang, Anand Tyagi
mentors: Joshua Higgason, Kevin Fulton
role: Creative Director
sponsors: The Council for the Arts at MIT (CAMIT)
description: An Area 51-themed live remote interactive adventure over Zoom and web browser
emoji: 👽

## Overview

The V.E.R.S. Project is a 60-minute live remote interactive adventure following the journey of Alex ("@lex"), an eccentric alien conspiracy theorist who enlists the help of a team of computer hackers to break into Area 51. In a unique blend of immersive theater and escape rooms, teams of 2-3 players tackle a series of narrative-driven challenges to determine the fate of @lex’s mission — all from the comfort of their own rooms.

VERS began as a fun quarantine project in Summer 2020 and culminated in a student-led production in early 2021, funded by The Council for the Arts at MIT (CAMIT).

The **[student-led MIT production <i class="fas fa-external-link-alt external-icon"></i>](https://versproject.herokuapp.com/team)** of VERS (January 15 - February 7, 2021) featured a cast of 8 actors and ran 72 shows, reaching a total of 185 players.

<iframe width="560" height="315" style="max-width:100%" src="https://www.youtube.com/embed/R0-Npw_SJDs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<a href="https://www.youtube.com/watch?v=R0-Npw_SJDs&list=PL13VJHLPzcIlgi0ceXD7n-MnPk4wwMh6Z&index=5" class="button">
	Watch Video on YouTube<i class="fas fa-external-link-alt external-icon"></i>
</a>

## The Idea

The idea behind VERS first came to us in a Zoom-era MIT theater class. When COVID-19 sent the world into lockdown, and the class online, we wondered: how do we design a live interactive performance for a cast, crew, and audience that are entirely remote? Moreover, how can we design an experience *specifically for* our computer screens? Perhaps screen technologies open more doors than they close.

In May 2020, these questions drove Dillon Zhang (MIT '20) and I to build [Zooming Away](https://shannonpeng.com/projects/zooming-away), a mini 15-minute experience in which players stabilize a crashing spaceship by interacting with the astronaut via a Zoom call and web-based "control console" UI. We had a lot of fun making the project, and our classmates and instructors loved playing it. Weeks after the class ended, I couldn't stop thinking about this new, exciting format of remote entertainment that we'd come up with and what else we could do with it.

<div class="image-set image-set-two" markdown="1">

![Zooming Away - Zoom call](/static/images/projects/zooming-away/rachel.gif "Zooming Away - Zoom call")
![Zooming Away - Control console UI](/static/images/projects/zooming-away/console.png "Zooming Away - Control console UI")

</div>

##### *Zooming Away:* Live interactive performance via Zoom call and web-based UI

Eager to continue exploring, I called together Dillon and Anand Tyagi (NYU '21) to create a more complex, ambitious experience based on Zooming Away, which we called The V.E.R.S. ("Virtual Escape Room Summer") Project. In the 3 months that followed, we met remotely to ideate, design, and develop a 60-minute interactive adventure centered around breaking into Area 51.

VERS initially began as a fun way to explore a novel concept and gain experience with game design and development over lockdown. With encouragement from our friends and MIT theater instructors, we later applied for grant funding, and then launched VERS into a successful fully-remote theater production for the MIT community.

## Player Experience

The experience begins in your inbox: the day before your mission, @lex reaches out via email with a Zoom link and some important reminders.

<div class="image-set image-set-two" markdown="1">

![VERS: Pre-mission email](/static/images/projects/vers-project/email.png "VERS: Pre-mission email")

</div>

##### VERS pre-mission email

### Orientation

When the Big Day arrives, your team gathers on Zoom. @lex greets you from the hot, windy Nevada desert and fills you in on his plan. Hidden deep inside Area 51 is a high-clearance room called "The Vault", and your mission is to help him locate it and uncover the secrets that lie inside. He introduces the custom virtual desktops he developed for this mission and sets your team up with accounts.

<div class="image-set" markdown="1">

![VERS: Zoom call](/static/images/projects/vers-project/zoom.jpg "VERS: Zoom call")

</div>

##### @lex explains the mission plan over Zoom.

### Virtual Desktops

As @lex turns off his video, you redirect your attention to the virtual desktop in your web browser. It's an Ubuntu-inspired desktop simulator with two apps to start: a simple Calculator and Secure Chat, where your team can exchange messages and receive attachments from @lex.

<div class="image-set" markdown="1">

![VERS: Virtual Desktop - Secure Chat](/static/images/projects/vers-project/vd-securechat.png "VERS: Virtual Desktop - Secure Chat")

</div>

##### VERS's Ubuntu-inspired virtual desktop UI.

### Gameplay

Through dialogue, sound effects, and pictures, you follow @lex on his journey through multiple locations: from the desert into a dark, abandoned warehouse; into an old, cranky elevator; through winding industrial hallways; to the entrance to The Vault, and finally, into The Vault itself. Each location unlocks new apps to use, documents to examine, and interactive puzzles to solve with your team.

Will you make it out of The Vault before the FBI arrives?

<div class="image-set image-set-two" markdown="1">

![VERS: Gameplay - Warehouse](/static/images/projects/vers-project/gp-1warehouse.jpg "VERS: Gameplay - Warehouse")
![VERS: Gameplay - Elevator](/static/images/projects/vers-project/gp-2elevator.jpg "VERS: Gameplay - Elevator")

</div>

<div class="image-set image-set-two" markdown="1">

![VERS: Gameplay - Sensors](/static/images/projects/vers-project/gp-3sensors.jpg "VERS: Gameplay - Sensors")
![VERS: Gameplay - Hallways](/static/images/projects/vers-project/gp-4hallways.jpg "VERS: Gameplay - Hallways")

</div>

<div class="image-set image-set-two" markdown="1">

![VERS: Gameplay - Personnel](/static/images/projects/vers-project/gp-5personnel.jpg "VERS: Gameplay - Personnel")
![VERS: Gameplay - Vault](/static/images/projects/vers-project/gp-6vault.jpg "VERS: Gameplay - Vault")

</div>

<div class="image-set image-set-two" markdown="1">

![VERS: Gameplay - Translate](/static/images/projects/vers-project/gp-7translate.jpg "VERS: Gameplay - Translate")
![VERS: Gameplay - Success](/static/images/projects/vers-project/gp-8success.jpg "VERS: Gameplay - Success")

</div>

<div class="image-set image-set-two" markdown="1">

![VERS: Gameplay - Failure](/static/images/projects/vers-project/gp-9failure.jpg "VERS: Gameplay - Failure")

</div>


##### Screenshots from various scenes throughout the show.

### Team Photo

Whether your mission ends in success or failure, your VERS experience concludes with a mission debrief with your actor and a team photo.

<div class="image-set" markdown="1">

![VERS: Photo Op](/static/images/projects/vers-project/VERS_12_raul_yizhi.jpg "VERS: Photo Op")

</div>

##### Team photo with VERS virtual backgrounds.

<div class="callout" markdown="1">
**🎖 Special Instructions for Webby Awards**

Hello there!

We're excited for you to try out VERS. ☺️ VERS normally takes 3 people to run (1 live actor and 2 players), but with some window juggling you can walk through the experience on one computer. For individual evaluation, we recommend following these steps:

1. In a new window, go to **[versproject.net/newroom <i class="fas fa-external-link-alt external-icon"></i>](https://versproject.herokuapp.com/newroom)**. This creates a new show and opens its Actor Panel.
2. Hover over the volume icon <i class="fas fa-volume-up"></i> at the top and click the mute button <i class="fas fa-volume-mute"></i> to mute the Actor Panel's sound.
3. Locate the Player URL at the top right, and open that URL in a second window. Log in with any username you'd like.
4. If possible, position the two windows side by side so that you can easily see both. Follow the instructions in the Actor Panel, pressing the buttons accordingly to drive the player experience. The buttons are color coded: <span style="color:#a27ef5">purple</span> for sound cues, <span style="color:#5aa0f2">blue</span> for content, and <span style="color:#edb538">orange</span> and <span style="color:#2bc125">green</span> for advancing the game state.
5. In Scene 3 (Hiding in Hallways), you will need an additional player to complete the puzzle. You can achieve this by opening the Player URL in a third window.

We hope you enjoy VERS! If you have any questions, feel free to contact us at [versproject@mit.edu](mailto:versproject@mit.edu).

-The VERS Team 💚

</div>
