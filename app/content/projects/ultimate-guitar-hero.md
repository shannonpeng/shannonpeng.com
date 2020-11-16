title: Ultimate Guitar Hero
keyword: ultimate-guitar-hero
subtitle: Guitar Hero-inspired game for learning any Ultimate Guitar tab
date: 2019-05-13
context: MIT 6.809/21M.385 Interactive Music Systems
tags: [Game Development, UI Design, Music Technology]
technologies: [Kivy, Python, MIDI Guitar]
categories: [code, music, interactive, games, design]
label: Interactive Music Systems
thumbnail: /static/images/projects/ultimate-guitar-hero/thumbnail.jpg
cover: /static/images/projects/ultimate-guitar-hero/cover.png
color: 454997
collaborators: Stef Ren, TC Qin
caption: Ultimate Guitar Hero's game interface.
description: Guitar Hero-inspired game for learning any Ultimate Guitar tab, built with Python and the Kivy UI framework
emoji: 🎸

When guitar players learn new music, they typically turn to guitar tabs. Tabs for most songs are easily found on websites like [Ultimate Guitar](http://ultimate-guitar.com), but they're often very static in nature: essentially plain text on a web page.

<div class="image-set image-set-two" markdown="1">

![Photograph by Ed Sheeran tab](/static/images/projects/ultimate-guitar-hero/photograph-tab.jpg "Photograph by Ed Sheeran tab")

##### A guitar tab for [Photograph by Ed Sheeran](https://tabs.ultimate-guitar.com/tab/ed_sheeran/photograph_tabs_1499667).

</div>

Tabs serve their purpose — with time and practice, you'll be able to learn how to play a song from its tab. But in Spring 2019, my final project team in MIT's Interactive Music Systems class (21M.385/6.809) couldn't help but wonder if these tabs could offer something more.

How can we transform static guitar tabs into a more dynamic, fun, and interactive learning experience? Here's what we came up with.

## How It Works

<div class="image-set" markdown="1">

![High-level flowchart](/static/images/projects/ultimate-guitar-hero/flowchart.jpg "High-level flowchart")

##### A high-level flowchart.

</div>

To start, we select a tab on [Ultimate Guitar](http://ultimate-guitar.com). We scrape the web page as HTML text, and then parse out the strings, fret numbers, and relative timing of notes (indicated by dashes in between numbers).

Using this data, we automatically generate a game in the style of Guitar Hero. The notes in the tab are illustrated as "gems" that move across the screen toward a "now bar" on the left, which indicates the current note(s) to be played.

The game is controlled by input from a MIDI guitar, which detects where the player puts their fingers and which strings they pluck.

## Walkthrough

Upon launching the app, you're greeted with Ultimate Guitar Hero's homescreen. You can choose to learn one of the most popular tabs on Ultimate Guitar or paste in a URL to any other tab on the website.

<div class="image-set" markdown="1">

![Homescreen](/static/images/projects/ultimate-guitar-hero/homescreen.jpg "Homescreen")

##### Ultimate Guitar Hero's homescreen.

</div>

Once you hit `Play`, you enter the game screen. It's packed with features:

<div class="image-set" markdown="1">

![Game screen features](/static/images/projects/ultimate-guitar-hero/features.gif "Game screen features")

##### Game screen features.

</div>

**Score, Progress Bar, and Streak:** These help you track your accuracy and progress.

**Notes Move Across the Screen:** You'll never lose your place in the tab again, because you don't have to scroll down for more notes — the notes scroll to you as you play. You can't move on to the next note until you play the current one correctly.

**Live Fret Diagram:** One of the challenges of reading a guitar tab is translating a fret number into a physical position on the fretboard. In Ultimate Guitar Hero, you can toggle a live fret diagram, which helps you visually compare where your fingers currently are to where they should be.

**Game Feedback:** You'll know when you've played something right or wrong. When you play a note correctly, it'll "poof" away on the screen. If you pluck the wrong string, the string you plucked will bend and flash red. If you pluck the right string but have your finger in the wrong place, an arrow and number will pop up, indicating the number of frets you should move your finger up or down on that string.

## Contributions

On this project, I worked across UI/UX design and software development: I designed the game interface, programmed the animations, and wrote code to process user input from the MIDI guitar controller.

## What's Next

Ultimate Guitar Hero received lots of praise from our class and from the MIT community! Where could we take it next? Here are some features we had in mind:

- Right now, the game filters out special indicators on guitar tabs, like hammer ons, pull offs, slides, and string bends. A next move would be to add support for these indicators to more accurately represent the guitar tabs that players wish to learn.

- The game is currently designed to work with a MIDI guitar — could we extend it to work with *any* guitar, possibly through the use of microphone input and audio analysis?

- It's currently not possible to infer the exact timing of a song from its tab without any additional data or processing. Given that data, could we make Ultimate Guitar Hero run in real-time and evaluate the player on how their timing compares to the timing of the original song?

