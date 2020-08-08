# Girls On The Run

## Overview

This is my fouth milestone project for the Code Institute Full Stack Web Developer course. It is a website to promote running to women. I feel that there are many barriers that stop women and girls from taking up exercise. I wanted to do someting positive that would empower women and give them confidence to git it a go.

The project has been built using HTML, CSS, JavaScript, Python and Django. It uses SQL databases to store information and Stripe to handle payments.

---

## User Experience

### Project Goals

This website is aimed at women and encouraging them to engage in running with the help and support of a running club designed around them. 

I wanted it to be able to **build a like-minded, supportive and inclusive network of women.** This will help them with achieving their exercise goals, making good friends and connecting with others in similar situations.

The project required that a user can **create an account,** log in and use that account to access their profile and to get extra member content. I achieved this with **Django's** useful features which quickly allow accounts to be created and tracked.

The project also needed an **e-commerce** element, using **Stripe** to control payment from users. I have set up an online shop selling branded merchandise. This allows users to browse, add to a shopping bag and purchase the items.

### Site Owner Stories
* As the website owner, I want to **build brand awareness** and **grow membership.**
* As the website owner, I want to **build a network of women** to help and support each other.
* As the website owner, I want to **sell group running sessions** as a revenue stream
* As the website owner, I want to **sell branded merchandise** on site as a revenue stream.
* As the website owner, I want to **collect user data** for market research and promtional purposes.
* As the website owner, I want to **sell extra services** such as personal nutrition and coaching advice.

### User Stories
* As a user of the website, I want to **navigate easily** and find the **information I need quickly.**
* As a user of the website, I want an **engaging design** that is visually appealing and stimulating.
* As a user of the website, I want **good user experience** to keep the me engaged.
* As a user of the website, I want to **view it on all devices** and it still to look good and work perfectly.
* As a user of the website, I want to be able to **contact the site owner.**
* As a user of the website, I want to find a **supportive group** to join to help with personal exercise goals.
* As a user of the website, I want to **build friendships** and **personal networks.**
* As a user of the website, I want to **get fit.**
* As a user of the website, I want to build **persoanal confidence.**
* As a user of the website, I want to **shop for branded merchandise** to feel part of a team.
* As a user of the website, I want to **create an account** to track orders and purchases on the website.
* As a user of the website, I want to **gain information and advice** to help support my fitness goals.

---

## design
I wanted the webiste to have a friendly and welcoming feel, to make it appeal to a female market. The use of images or 'real' women and not just athletic ones, helps to make women feel more included and at home.

### Fonts
I've used the serif font [Merriweather](https://fonts.google.com/specimen/Merriweather?query=mer) in two weights, (300 and 900) with some **sophisticated letter spacing** to add to the airy feel. I like the no-nonsense clean lines of the font, and feel it suits the website perfectly. The 300 light weight contrast well with bold 900 weight.

### Colours
I created a **simple, complimentary, sophisticated colour scheme** that carries through the site. I simplified the colour palette down to just two colours for a clean and consistant feel. I wanted a strong grey to carry the main text with a bright turquoise to balance it out. The turquoise is a colour that appears on many women's sports wear items. I felt this would appeal to a wider audience than the standard and possibly patronising pink that might usually be used.
* ![#696969](https://placehold.it/15/696969/000000?text=+) Dark Grey: #696969;
* ![#3297a8](https://placehold.it/15/3297a8/000000?text=+) Turquoise: #3297a8;

* ```dark-grey: #696969```
* ```turquoise: #3297a8```

### Grid
I carried the **same basic grid through** the pages to add consistency and easy of navigation. A large **section header** quickly establishes the page you've landed on, and under that, is a panel holding the content for that page. A footer on each page hold **social media links.**

### Images

All images were sourced from the [iStock](https://www.istockphoto.com/gb) image library. I used images of many different shapes, sizes and ages of women to show the inclusive nature of the site. This will hopefully make women feel more represented and less intimidated. I want any woman or girl to feel like this is a space where the are accepted and not judged.

---

## Wireframes
I built my wireframes using **Balsamiq Wireframes**. This was a quick and easy way to work out the basic pages and element and how the would interact with each other. I then mocked up more detailed versions using **Adobe InDesign** to allow me to play with fonts, colours and images. The basic structure from my wireframes remained much the same, but colours, styling and some elements were adapted as I built the website and saw how it worked as a whole.   

View my **Balsamiq** wireframes <a href="https://github.com/GarySimons/girlsrun/tree/master/wireframes/png">here.</a>

View my **Adobe InDesign** wireframes <a href="https://github.com/GarySimons/girlsrun/tree/master/wireframes/jpg">here.</a>


## Features

### Navigation bar
**This holds all the links to the sections of the site:** Logo (home button), home, about, projects and contact. This allows the user to navigate quickly to the relevant section. The **navigation bar** is always visible when you are on the site, allowing for easy navigation to any part, no matter where you first land. The **home button and logo** will take you right back to the **home page** where you can get your bearings and start your journey.

### Home
This is the first page a user comes to and it has to make a big impact. It has the job of informing the user as to what sort of site this is and to entice them to move further and engage with it. It opens with **strong simple typography** on a background image of a woman about to start a run. Having these visuals announces very quickly what the website is about. 

### My Story
On this page we are introduced to the site owner and the founder of the running club. The friendly image of her in running gear is very inviting and engaging, reasuring the user that this is a safe space. The inspirational personal story of the owner and how she overcame adversity and found happiness and friendship through running will inspire other women to follow in her foot steps. A Get in touch button links through to the Contact page. 

### Her Stories
With this page we are able to showcase many of the inspirational women who belong to the running club. An image of them enjoying running with a short inspiration paragraph about their lives and how running has helped them will encourage other women. The images show a wide range of ages and sizes of women to show the inclusiveness of the group. This will help to make women feel included and represented.

### Upcomimg Runs
This is the page where the site owner can advertise all the events that are coming up. Users can find the date, time, place and a indicator of run length. There is also a short description and a button to find out more and book yourself on the run.

### Members login page
This allows users to create an account of login to an existing one. The background image of running shoes together represents a club of women together.

### Coaching
This is a members only page which is accessible once logged in. This offers general advice, and a link to pay for a personalised fitness plan.

### Nutrition
This is a members only page which is accessible once logged in. This offers general advice, and a link to pay for a personalised nutrition plan.

### Shop
Here we have the e-commerce section of the website. Users can purchase branded merchandise from the club. Here items can be browsed and selected to be added to a shopping basket. 

### Contact Us
The final page is where users can get in touch with site owner. The background image shows a woman running through a puddle. This is to reflect the real life situations and conditions that runners often face. It shows determination and spirit as it's telling you that this isn't easy, but it will be worth it.

---

## Database Design

### Data Models
The user model used was the inbuilt one provide by Django.

---

## Technologies used

#### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [JavaScript](https://www.javascript.com/)
* [jQuery](https://jquery.com/)

#### Frameworks and libraries
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)
* [PopperJS](https://popper.js.org/)

#### Tools
* [Heroku](https://www.heroku.com/)
* [Balsamiq Wireframes](https://wireframestogo.com/)
* [TinyPNG](https://tinypng.com/)
* [Genfavicon](http://www.genfavicon.com/)

---

## Credits

### Thanks

My mentor [Simen Daehlin](https://dehlin.dev/) for all the advice and pointers. And for always pushing me to go further.

All the **tutors** that helped me along the way on the **Tutor Support**. 

### Images

All images were sourced from the [iStock](https://www.istockphoto.com/gb) image library. 

### Text

All text written by me.

### Disclaimer

This website is a Milestone Project for the **Full Stack Web Development** course at [Code Institute](https://codeinstitute.net/). It is for educational purposes only.
