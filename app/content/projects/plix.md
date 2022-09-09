title: Plix
keyword: plix
subtitle: Online community for location-based collaborative pixel art
date: 2018-02-01
context: MIT 6.148 Web Programming Competition
tags: [Web Development, Art, UI Design]
technologies: [Node, Express, SocketIO, Mongoose, Google Maps API, Handlebars, SASS, jQuery, Javascript, HTML, CSS]
categories: [code, interactive]
label: Web Development
thumbnail: /static/images/projects/plix/thumbnail.jpg
cover: /static/images/projects/plix/cover.jpg
color: 19158c
link: https://plix.onrender.com
github: https://github.com/shannonpeng/plix
collaborators: Jessica Tang
caption: Pixel art on the Next House board in Plix.
description: Online community for location-based collaborative pixel art, built with Node.js and Socket.IO
emoji: 🖌

I created Plix with my friend [Jessica Tang](http://jynnie.me/) in January 2018. It won 1st Place in MIT 6.148 (now [web.lab](http://weblab.mit.edu/)), a campus-wide web programming class and competition.

**Note:** Plix currently only has boards on MIT campus, so you'd need to be at MIT to draw on a board. However, you can always view boards other Plixers have created by logging in with username `test` and password `test`, and then clicking the <i class="fas fa-user"></i> icon.

<a href="https://plix.onrender.com" class="button">
	Open Plix <i class="fas fa-external-link-alt external-icon"></i>
</a>

## The Idea

Plix was inspired by public art and murals. At MIT, murals play a large role in dorm culture—students love to paint murals in the hallways, and often the art created by each living group reflects its unique community.

<div class="image-set image-set-two" markdown="1">

![Chalkboard mural in Next House](/static/images/projects/plix/art1.jpg "Chalkboard mural in Next House")
![Lego mural in East Campus](/static/images/projects/plix/art2.jpg "Lego mural in East Campus")

##### *left:* MIT Next House, *right:* MIT East Campus
	
</div>

<div class="image-set image-set-two" markdown="1">

![Building mural in Boston](/static/images/projects/plix/art3.jpg "Building mural in Boston")
![Subway train mural in NYC](/static/images/projects/plix/art4.jpg "Subway train mural in New York")

##### *left:* Boston, MA, *right:* New York, NY
	
</div>

There is art to be found in communities, and community to be found in art, in places all over the world. People love to make art together, but it's often difficult to secure physical spaces to do so. Plix's online platform enables artists to collaborate with others nearby to create pixel art and share it with the world.

> There is art to be found in communities, and community to be found in art, in places all over the world.

## Walkthrough

### Homescreen

When you visit Plix, you'll find the homescreen, which prompts you to login or sign up for an account. The parallax pixel clouds (and the occasional pixel pizza, watermelon, or coffee) are randomly generated each time you load the page.

<div class="image-set" markdown="1">

![Plix homescreen](/static/images/projects/plix/homescreen.gif "Plix homescreen")

##### Parallax pixel clouds, and the occasional pizza.
	
</div>

### Main Features

Plix's main features include location-based discovery, community leaderboards, and personalized history.

<div class="image-set" markdown="1">

![Plix's main features](/static/images/projects/plix/features.jpg "Plix's main features")
	
</div>

**Location-based discovery:** Plix's main screen is a map showing boards near you, represented by flags. As you move around, you can discover more boards and view the art Plixers are creating nearby.

**Community leaderboard:** If you're located within range of a board, you can draw on it by selecting a color and clicking a pixel on the board. You'll also see a leaderboard showing the users who currently own the most pixels on that board. As other Plixers draw, the pixel art and the leaderboard update in real-time.

<div class="image-set" markdown="1">

![Plix board](/static/images/projects/plix/board.jpg "Plix board")

##### Board interface and community leaderboard.
	
</div>

**Personalized history:** You can find a list of your contributions on your profile — this is a fun way to keep track of places you've visited and watch how the art there evolves. The color of each board is determined by the color of the pixel you last placed on it.

<div class="image-set" markdown="1">

![Plix profile](/static/images/projects/plix/profile.jpg "Plix profile")

##### Personalized history on profile.
	
</div>

## How It Works

Plix is built with Node.js and Express, and it interfaces with a MongoDB database using [Mongoose](https://mongoosejs.com/). The frontend uses jQuery, [Handlebars.js](https://handlebarsjs.com/) templating, and the [SASS](https://sass-lang.com/) CSS preprocessor.

We also brought in [Google Maps API](https://developers.google.com/maps/documentation/) to render a map and grab the user's location, [SocketIO](https://socket.io) to implement real-time updating boards and leaderboards, and the [jscolor](http://jscolor.com/) library to create a color picker.

## What I Learned

Jessica and I worked closely across all aspects of Plix, splitting the code at a fine-grain level. Through this project, I strengthened my web development skills across the full stack.

On the backend, I learned how to implement sessions and user authentication, and I became more familiar with Javascript callback functions, MongoDB schemas, and SocketIO. On the frontend, I gained experience with sending HTTP requests, templating with Handlebars, and writing SASS/CSS to create Plix's playful look.

## What's Next

There are many directions in which we could take Plix! Here are a few ideas we came up with:

- **Create a board:** To initialize Plix with boards, we manually looked up latitude and longitude values for every dorm on campus and wrote a script to add them to the database. Creating new boards seems like the next feature to add as Plix begins to reach users outside of MIT and Boston.
- **Plix in AR:** One current downside of Plix is that it lives inside your laptop screen. To make the experience more seamless, we imagine embedding Plix in AR, so that murals can be viewed in the physical world, and it's easier to discover more murals as you travel.
- **Brands and businesses:** Brands and businesses could create sponsored Plix boards at their locations as a way to attract more visitors.

One small thing we're proud of is Plix's name. It's a spin on the word *pixel*, and we think it makes for a pretty catchy verb. Maybe it'll catch on one day — for now, we'll Plix on!
