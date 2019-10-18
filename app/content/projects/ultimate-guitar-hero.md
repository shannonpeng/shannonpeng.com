featured: true
title: Ultimate Guitar Hero
keyword: ultimate-guitar-hero
subtitle: Guitar Hero-inspired game for learning guitar tabs
date: 2019-05-13
context: 6.809/21M.385 Interactive Music Systems
tags: [Software, Game Development, UI Design, Music Technology]
technologies: [Kivy, Python, MIDI Guitar]
categories: [code]
label: Interactive Music Systems
thumbnail: /static/images/projects/ultimate-guitar-hero/thumbnail.jpg
cover: /static/images/projects/ultimate-guitar-hero/cover.png
color: 454997
collaborators: Stef Ren, TC Qin
caption: Ultimate Guitar Hero's game interface.
description: Guitar Hero-inspired game for learning guitar tabs, based in Python and the Kivy UI framework

When guitar players learn new music, they'll usually turn to [guitar tabs](https://en.wikipedia.org/wiki/Tablature). While tabs for most songs can be found in digital form on websites like [Ultimate Guitar](http://ultimate-guitar.com), they're often very static in nature, essentially just plain text on a web page.

<div class="image-set image-set-two" markdown="1">

![Photograph tab](/static/images/projects/ultimate-guitar-hero/photograph-tab.jpg "Photograph tab")

</div>
##### A guitar tab for [Photograph by Ed Sheeran](https://tabs.ultimate-guitar.com/tab/ed_sheeran/photograph_tabs_1499667)

Tabs serve their purpose — with some time and practice, you'll be able to learn how to play a song from its tab. But last spring, in the class 21M.385/6.809 Interactive Music Systems, my final project team couldn't help but wonder if these tabs could offer something more.

How can we turn static guitar tabs into a more dynamic, fun, and interactive learning experience?

Here's what we came up with.

## How It Works

<div class="image-set" markdown="1">

![Flowchart](/static/images/projects/ultimate-guitar-hero/flowchart.jpg "Flowchart")

</div>
##### A high-level flowchart

To start, we select a tab on [Ultimate Guitar](http://ultimate-guitar.com). We scrape the web page as HTML text, and then parse out the strings, fret numbers, and relative timing of notes (indicated by the dashes in between numbers).

Using this data, we then automatically generate a game in the style of Guitar Hero. The notes in the tab are illustrated as "gems" that move across the screen toward a "now bar" on the left, which indicates the current note(s) to be played.

The game is controlled by input from a MIDI guitar, which senses where the player puts their fingers and which strings they pluck.

## Walkthrough

Upon launching the app, you're greeted with Ultimate Guitar Hero's homescreen. You can choose to learn one of the most popular tabs on Ultimate Guitar, or paste in a URL to any other tab on the website.

<div class="image-set" markdown="1">

![Homescreen](/static/images/projects/ultimate-guitar-hero/homescreen.jpg "Homescreen")

</div>
##### Ultimate Guitar Hero's homescreen

Once you hit `Play`, you enter the game screen. It's packed with features:

<div class="image-set" markdown="1">

![Features](/static/images/projects/ultimate-guitar-hero/features.gif "Features")

</div>
##### Game screen features

- **Score, Progress Bar, and Streak:** These help you keep track of your accuracy and progress.
- **Notes Move Across the Screen:** You'll never lose your place in the guitar tab, because instead of having to scroll down the page to see more notes, the notes will scroll to you as you play! You can't move on to the next note until you play the current one correctly.
- **Live Fret Diagram:** One of the challenges of reading a guitar tab is translating a fret number into a physical position on the fretboard. You can toggle a live fret diagram, which helps you visually compare where your fingers currently are to where they should be.
- **Game Feedback:** You'll know when you've played something right or wrong. When you play a note correctly, it will "poof" away on the screen. If you pluck the wrong string, the string you plucked will bend and flash red. If you pluck the right string but have your finger in the wrong place, an arrow and number will pop up, indicating the number of frets you should move your finger up or down on that string.


## Next Steps

Ultimate Guitar Hero received lots of positive and constructive feedback from members of our class and the larger MIT community. Where could we take it next?

- Right now, the game filters out special features of guitar tabs, like hammer ons, pull offs, slides, and string bends. The next move would be to add support for these features to more accurately represent the guitar tabs that players wish to learn.

- The game is currently designed to work with a MIDI guitar — could we extend it to work with *any* guitar, possibly through the use of microphone input and audio analysis?

- It's currently not possible to infer the exact timing of a song from its tab without any additional data or processing. Given that data, could we make Ultimate Guitar Hero run in real-time and evaluate the player on how their timing compares to the timing of the original song?

