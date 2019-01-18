featured: true
title: Virtual Piano
keyword: virtual-piano
subtitle: Play real-time piano duets, inside your browser
date: 2017-02-05
context: Hack@Brown 2017
tags: [Software, Web Development, Music]
technologies: [Node, Express, Socket.IO, Audiosynth, jQuery, Javascript, HTML, CSS]
categories: [code]
label: Web Development
thumbnail: /static/images/projects/virtual-piano/thumbnail.png
cover: /static/images/projects/virtual-piano/cover.png
color: 1747af
link: https://pengs-piano.herokuapp.com/
github: https://github.com/shannonpeng/virtual-piano
caption: Two people playing a chord in Virtual Piano.
description: Real-time piano duets in the browser, powered by Socket.IO and Audiosynth

I created Virtual Piano at [Hack@Brown 2017](https://2017.hackatbrown.org/), drawing inspiration from the browser-based experiments in Google's [Chrome Music Lab](https://musiclab.chromeexperiments.com/).

<a href="https://pengs-piano.herokuapp.com/" class="button">
	Play Virtual Piano
</a>

## The Idea

The magic of the Internet is that it can connect people anywhere around the world, at any time. We're now capable of messaging and even video calling our friends online—what if we could also make music together?

I envisioned a browser-based app that lets musicians start jamming together, no matter where they're located. Just log on, join a session, and then start making music as if you were in the same room.

Over the 24-hour hackathon, I built a demo of a virtual piano that allows multiple people to play from separate devices. Try it with a friend!

## How It Works

Virtual Piano is built with Node.js and [Socket.IO](https://socket.io/), an engine for real-time communication. The frontend is written using jQuery and [Audiosynth](https://github.com/keithwhor/audiosynth), a Javascript library that synthesizes digital instrument sounds, and vanilla HTML and CSS.

### Playing Piano

When you log onto Virtual Piano, you're greeted with a simple HTML and CSS keyboard.

<div class="image-set" markdown="1">

![How it works: piano](/static/images/projects/virtual-piano/piano.png "How it works: piano")

##### Virtual Piano interface

</div>

Each key is an HTML `div` with an attribute called `data-key`, which stores the pitch and octave (e.g. `F#-2`).

```HTML
<div id="piano">
	<div class="keys">
		<div class="white-keys">
			<div class="key white-key" data-key="C-2"></div>
			<div class="key white-key" data-key="D-2"></div>
			<!-- through E6 -->
		</div>
		<div class="black-keys">
			<span class="cluster">
				<div class="key black-key" data-key="C#-2"></div>
				<div class="key black-key" data-key="D#-2"></div>
			</span>
			<span class="cluster">
				<div class="key black-key" data-key="F#-2"></div>
				<div class="key black-key" data-key="G#-2"></div>
				<div class="key black-key" data-key="A#-2"></div>
			</span>
			<!-- through D#6 -->
		</div>
	</div>
</div>
```
There are two ways to play a note—you can either click a key with your cursor or press keys on the keyboard. The keys in the middle row of a QWERTY keyboard, `A` through `'`, map to white keys from C3 to F4. Matching the piano layout, the keys in the top row, `W` through `P`, map to black keys from C#3 to D#4. (Make sure your caps lock is off!)

![How it works: keyboard mapping](/static/images/projects/virtual-piano/keys.png "How it works: keyboard mapping")

##### Mapping piano keys to keyboard keys.

When you press a key, jQuery triggers the following event handler:

```JS
// Initialize Audiosynth instrument
// var piano = Synth.createInstrument('piano');

// ...

$("#piano .key").click(function(event) {

	// Get pitch and octave of key played
	var note = $(this).attr('data-key').split('-');

	// Use Audiosynth to play the piano note
	piano.play(note[0], note[1], 2.5);

	// Briefly show a blue gradient on the key just played
	$(this).addClass('active').delay(100).removeClass('active');

	// Relay this note to all other devices through Socket.IO
	socket.emit('piano-key', { note: note });
});
```

This function retrieves the pitch and octave from `data-key`, tells the Audiosynth instrument to play that note, and then displays a blue gradient (in CSS class `.active`) over the key to indicate that it has just been played.

![How it works: active](/static/images/projects/virtual-piano/active.png "How it works: active")

##### A blue gradient indicates you've just played the key.

The last line then uses Socket.IO to tell other devices about the note—keep reading for more details.

### Connecting Multiple Players

Socket.IO's real-time communication is based on *events*. An *event* can represent anything you choose, like a message sent in a chat, an action made in a game, or in Virtual Piano's case, a key pressed on a piano.

When one device *emits* an event, the server pushes that event's information to all devices connected to the web socket. The devices can then respond to the event accordingly.

When you press a key, Virtual Piano calls `socket.emit()`:

```JS
// Relay this note to all other devices through Socket.IO
socket.emit('piano-key', { note: note });
```

This emits an event with the name `piano-key` and data `note`, which includes the pitch and octave of the key.

When other devices receive the `piano-key` event, they respond with the following handler:

```JS
socket.on('piano-key', function(data){

	// Use Audiosynth to play the piano note
    piano.play(data.note[0], data.note[1], 2.5);

    // Briefly show a green gradient on the key just played
    $("[data-key='"+ data.note[0] + '-' + data.note[1] + "']")
      .addClass('other-active');
    setTimeout(function() {
    	 $("[data-key='"+ data.note[0] + '-' + data.note[1] + "']")
    	   .removeClass('other-active');
    }, 100);
});
```

This function plays the note through Audiosynth and displays a green gradient (in CSS class `.other-active`) over the corresponding key to show that it has just been played by someone else!

![How it works: other-active](/static/images/projects/virtual-piano/other-active.png "How it works: other-active")

##### A green gradient indicates someone else has played the key.


## What I Learned

Every hackathon I attend, I challenge myself to learn a new skill and build something with it right away.

Virtual Piano was my first time working with Socket.IO! I got the chance to learn about web sockets and apply what I learned to develop a fun, musical application. 

## What's Next

There are so many features I had in mind for Virtual Piano but didn't get to implement in time. Here are some of them:

- **Note labels:** At first glance, it's hard to tell which octaves of the piano you're looking at. Adding at least a few labels would help.
- **Sustained notes:** Holding down a key currently registers as multiple presses.
- **Support for multiple rooms:** Right now, there's only one room, so if 100 people joined, the piano would get pretty crowded! With multiple rooms, players could limit their jam sessions to friends using a unique link or code.
- **Additional player colors:** It'd be useful to know who's playing when there are more than two people in the room.
- **More keys:** More octaves to play!
- **More instruments:** The ability to add a second piano, or maybe a guitar, bass, and drums?

It'd also be interesting to try connecting Socket.IO to MIDI controllers or musical instruments for a more seamless experience. A friend of mine said that in the future, an application like this could allow piano teachers to give students lessons remotely. That's an awesome thought.

Music and technology are some of my favorite areas to explore, and I'd love to work on more projects combining the two in the future!