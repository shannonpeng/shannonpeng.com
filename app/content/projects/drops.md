hidden: true
title: Drops
keyword: drops
subtitle: Javascript game raising awareness about water pollution
date: 2017-06-25
context: ByteHacks 2017
tags: [Game Development, Graphic Design, UI Design]
technologies: [Javascript, PhaserIO, Illustrator]
categories: [games, interactive, design]
label: Game Development
thumbnail: /static/images/projects/drops/thumbnail.png
cover: /static/images/projects/drops/cover.png
color: 6e5a78
link: https://liliapoteat.github.io/drops/
github: https://github.com/shannonpeng/plix
collaborators: Claire Nord, Lilia Poteat, and Sarah Powazek
caption: Collecting polluted water drops in Drops Level 3.
description: Javascript game created to raise awareness about disparities in water quality around the United States
emoji: 💧

I built Drops with my friends [Claire](https://clairenord.com/), Lilia, and Sarah at [ByteHacks 2017](https://bytehacks2017.devpost.com/), where it won 1st Place and Best UX. Drops was inspired by [Scoops](https://itunes.apple.com/us/app/scoops-build-match-food-free/id291591378?mt=8), an iOS game I loved to play growing up. I worked on developing the gameplay with the Javascript game framework [Phaser.IO](http://phaser.io/) and creating the game's assets.

<a href="https://liliapoteat.github.io/drops/" class="button">
	Play Drops <i class="fas fa-external-link-alt external-icon"></i>
</a>

## Gameplay

In Drops, the player moves a bucket to collect clean water drops in **<span style="color:#74c5ef;">blue</span>** and **<span style="color:#66c89c">green</span>**, while avoiding the dirty ones in **<span style="color:#936e38">brown</span>**. To advance to the next level, the player must collect 15 drops.

<div class="image-set image-set-two" markdown="1">

![Gameplay: home](/static/images/projects/drops/home.png "Gameplay: home")
![Gameplay: instructions](/static/images/projects/drops/instructions.png "Gameplay: instructions")

##### The home and instruction screens at the beginning of Drops.

</div>

Drops has three levels: (1) Boston, Massachusetts, (2) Charleston, West Virginia, and (3) Sebring, Ohio. With each level, the ratio of dirty to clean water drops increases, raising the game difficulty while teaching the player about disparities in water quality between the three locations.

<div class="image-set image-set-three" markdown="1">

![Boston: introduction](/static/images/projects/drops/boston-intro.png "Boston: introduction")
![Boston: play](/static/images/projects/drops/boston-play.png "Boston: play")
![Boston: score](/static/images/projects/drops/boston-score.png "Boston: score")

##### Level 1: Boston, MA

</div>

**Level 1:** "Welcome to Boston! Cities like Boston have access to reservoirs and high quality treatment plants. In the last 5 years, 90% of water samples had safe levels of lead."

<div class="image-set image-set-three" markdown="1">

![Charleston: introduction](/static/images/projects/drops/charleston-intro.png "Charleston: introduction")
![Charleston: play](/static/images/projects/drops/charleston-play.png "Charleston: play")
![Charleston: score](/static/images/projects/drops/charleston-score.png "Charleston: score")

##### Level 2: Charleston, WV

</div>

**Level 2:** "Welcome to Charleston! Areas like this with many industrial plants are prone to chemical and coal ash leaks. These make the drinking water unsafe and cause short-term health problems."

<div class="image-set image-set-three" markdown="1">

![Sebring: introduction](/static/images/projects/drops/sebring-intro.png "Sebring: introduction")
![Sebring: play](/static/images/projects/drops/sebring-play.png "Sebring: play")
![Sebring: score](/static/images/projects/drops/sebring-score.png "Sebring: score")

##### Level 3: Sebring, OH

</div>

**Level 3:** "Welcome to Sebring! In the US, 6-8 million homes still get water from lead pipelines. These corrode and infect water toxins, leading to chronic health problems for families and children."

## Development

We spent a lot of time planning different aspects of Drops, including research, game mechanics, control flow, and assets.

<div class="image-set" markdown="1">

![Development: whiteboard](/static/images/projects/drops/whiteboard.jpg "Development: whiteboard")

##### We took over multiple whiteboards over the course of the hackathon.

</div>

### Creating Assets

I drew the game's drops, buckets, and backgrounds in Illustrator.

<div class="image-set" markdown="1">

![Assets: drops](/static/images/projects/drops/assets-drops.png "Assets: drops")

##### **Drops:** Blue, brown, and green drops.

</div>

<div class="image-set" markdown="1">

![Assets: buckets](/static/images/projects/drops/assets-buckets.png "Assets: buckets")

##### **Buckets:** Buckets filled with various levels of clean, polluted, and deadly water.

</div>

Only the empty bucket made it into the final game, but I thought it would've been a neat feature to have the water in the bucket respond to the player's progress in the game. The more drops collected, the higher the water level in the bucket, and the greater the percentage of polluted drops collected, the dirtier the water.

<div class="image-set" markdown="1">

![Assets: backgrounds](/static/images/projects/drops/assets-backgrounds.png "Assets: backgrounds")

##### **Backgrounds:** Background artwork for Boston, Charleston, and Sebring.

</div>

## What I Learned

Every hackathon project, I aim to learn something new. Through Drops, I learned basics of game development, including programming the game interface and working with sprites and collisions. I also learned more about the issue of water pollution and the different types of pollutants in tap water around the country.

## What's Next

Each level of Drops terminates after 15 drops are collected, which is great for a quick hackathon demo, but so short for real gameplay!

In [Scoops](https://itunes.apple.com/us/app/scoops-build-match-food-free/id291591378?mt=8), players could continue stacking scoops of ice cream indefinitely, unless they've acquired three "bad" scoops (onions or tomatoes). Perhaps Drops levels could go on until the player's pollution level has surpassed that of drinkable tap water.

Maybe the green drops could even act as "purifying" drops that help the player reduce the pollutants they've already collected. That'll be a project for next time!