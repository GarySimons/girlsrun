# Girls On The Run

## Contents

* **Overview**
* **User Experience**
    - Project Goals
    - Site Owner Stories
    - User Stories
* **Design**
    - Fonts
    - Colours
    - Grid
    - Images
* **Wireframes**
* **Features**
    - Navgation Bar
    - Home
    - Her Stories
    - Upcoming Runs
    - Members' Login
    - Advice
    - Shop
    - Contact Us
    - Shopping Bag
* **Database Design**
    - The Product Model
    - The Story Model
    - The Event Model
* **Bugs and Problems**
    - Scroll Bar on Bottom of Site
    - Bootstrap Flexbox and Order
    - Active Nav Bar
    - Code Stuck in message_container
* **Technologies Used**
    - Languages
    - Frameworks and Libraries
    - Tools
    - Databases
* **Deployment**
    - Running Project Locally
    - Deploying to Heroku
* **Credits**

## Overview

This is my **fouth milestone project for the Code Institute Full Stack Web Developer course.** It is a website to **promote running to women.** I feel that there are many barriers that stop women and girls from taking up exercise. I wanted to do someting positive that would empower women and give them confidence to git it a go.

The project has been built using **HTML, CSS, JavaScript, Python and Django.** It uses **SQL databases** to store database information during development, and **Amazon Web Services (AWS)** for databases in production. Also **Stripe** to handle payments.

---

## User Experience

### Project Goals

This website is aimed at **women** and **encouraging** them to engage in running with the help and support of a running club designed around them. 

I wanted to build this website after seeing the **disengagement of the women** in my own family with sports and excercise. It's well know that lots of girls and women are put off excercise for many complex and varied reasons. I wanted to build a website that would **inspire and engage women of all ages and abilities** and show that that they can do anything they want. They just have to take that first step.

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
* As a user of the website, I want to **create an account** to track orders and purchases on the website.
* As a user of the website, I want to **log in and out of my account.**
* As a user of the website, I want to **gain information and advice** to help support my fitness goals.
* As a user of the website, I want to **shop for branded merchandise** to feel part of a team.
* As a user of the website, I want to **view individual product details.**
* As a user of the website, I want to **view a total cost of my purchases** to track my spending.
* As a user of the website, I want to **select quantity of products** to add to my shopping bag.
* As a user of the website, I want to **adjust quantity of products** in my shopping bag.
* As a user of the website, I want to **remove products** from my shopping bag.
* As a user of the website, I want to **select sizes of products** to add to my shopping bag.

---

## Design
I wanted the website to have a friendly and welcoming feel, to make it appeal to a female market. The use of images or 'real' women and not just athletic ones, helps to make women feel more included and at home.

### Fonts
For my headings and main text I have used the compressed font [Oswald](https://fonts.google.com/specimen/Oswald?query=osw) in the 300 weight, with some **sophisticated letter spacing** to add to the airy feel. I like the no-nonsense clean lines of the font, and feel it suits the website perfectly. The 300 light weight looks stylish without being too thin or thick. For any other text, I've used [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=open), also in the 300 weight. This font is very readable and compliments the more stylized Oswald.

### Colours
I created a **simple, complimentary, sophisticated colour scheme** that carries through the site. I cut the colour palette down to just two colours for a clean and consistant feel. I wanted a strong grey to carry the main text with a bright turquoise to balance it out. The turquoise is a colour that appears on many women's sports wear items. I felt this would appeal to a wider audience than the standard and possibly patronising pink that might usually be used. I have used an alternative lighter turquoise and a lighter grey for the hovers on the grey and blue button classes. The subtle change is very sophisticated and user friendly.


* ![#696969](https://placehold.it/15/696969/000000?text=+) **Dark Grey: #696969** - This is the main colour for most of the text on the website. It's strong enough to read, but less harsh thank standard black.
* ![#8b8b8b](https://placehold.it/15/8b8b8b/000000?text=+) **Light Grey: #8b8b8b** - This is only used as a subtle hover colour on the btn-grey class buttons. It creates a simple, elegant feel as the mouse glides over it.
* ![#2fbdb8](https://placehold.it/15/3297a8/000000?text=+) **Turquoise: #2fbdb8** - This colour is used as a contrast to the dark grey. It's bright fun and brings an energy that brings the pages to life.  
* ![#90d1da](https://placehold.it/15/90d1da/000000?text=+) **Light Turquoise: #90d1da** - This is only used as a subtle hover colour on the btn-grey class buttons. It creates a simple, elegant feel as the mouse glides over it.
* ![#ff0000](https://placehold.it/15/90d1da/ff0000?text=+) **Red: #ff0000** - This is used on the sign in page to highlight the text informing you of the extra content for members.

### Grid
I carried the **same basic grid through** the pages to add consistency and easy of navigation. A large **section header** quickly establishes the page you've landed on, and under that, is a panel holding the content for that page. A footer on each page hold **social media links.**

### Images

All images were sourced from the [iStock](https://www.istockphoto.com/gb) image library. I used images of many different shapes, sizes and ages of women to show the inclusive nature of the site. This will hopefully make women feel more represented and less intimidated. I want any woman or girl to feel like this is a space where the are accepted and not judged.

---

## Wireframes
I built my wireframes using **Balsamiq Wireframes**. This was a quick and easy way to work out the basic pages and element and how the would interact with each other. I then mocked up more detailed versions using **Adobe InDesign** to allow me to play with fonts, colours and images. The basic structure from my wireframes remained much the same, but colours, styling and some elements were adapted as I built the website and saw how it worked as a whole. The main change to the pages was the home page. It was felt that a user landing on the home page didn't have enough clues as to the purpose of the website. I reduced the height of the main image to introduced a **'What we do'** that would show just above the fold of the page to entice the user to scroll down. I also **moved the 'My Story' page** to the home page to further introduce the idea behind the website and give it a personality.

View my **Balsamiq** wireframes <a href="https://github.com/GarySimons/girlsrun/tree/master/wireframes/png">here.</a>

View my **Adobe InDesign** wireframes <a href="https://github.com/GarySimons/girlsrun/tree/master/wireframes/jpg">here.</a>


## Features

### Navigation bar
**This holds all the links to the sections of the site:** Logo (home button), home, about, projects and contact. This allows the user to navigate quickly to the relevant section. The **navigation bar** is always visible when you are on the site, allowing for easy navigation to any part, no matter where you first land. The **home button and logo** will take you right back to the **home page** where you can get your bearings and start your journey. The **advice** button only shows up once a user has registered and logged in. This active button contains **member only content** on various aspects of training, food and kit on a dropdown menu of four pages. A link on the far right is a link to the **shopping bag** and shows the current total.

### Home
This is the first page a user comes to and it has to make a big impact. It has the job of informing the user as to what sort of site this is and to entice them to move further and engage with it. It opens with **strong simple typography** with a friendly welcome message, on a background image of a woman about to start a run. Having these visuals announces very quickly what the website is about. Just above the fold of the page you can see the top of a section called **'What we do'**, which explains a bit about the ideas behind the website. Showing this just above the fold **entices the user to scroll down to see what it says**. Underneath is another panel called **'My Story'**. On this panel we are **introduced to the site owner** and the founder of the running club. The friendly image of her in running gear is very inviting and engaging, reasuring the user that this is a safe space. The inspirational personal story of the owner and how she overcame adversity and found happiness and friendship through running will inspire other women to follow in her foot steps. **A Get in touch button** links through to the Contact page. 

### Her Stories
With this page we are able to showcase many of the inspirational women who belong to the running club. An image of them enjoying running with a short inspiration paragraph about their lives and how running has helped them will encourage other women. The images show a wide range of ages and sizes of women to show the inclusiveness of the group. This will help to make women feel included and represented.

### Upcomimg Runs
This is the page where the site owner can advertise all the events that are coming up. Users can find the date, time, place and a indicator of run length. There is also a short description and a button to find out more and book yourself on the run.

### Members' login page
This allows users to **create** an account or **login** to an existing one. Once logged in the dropdown options change, allowing the logged in user to **edit their profile** and see their **order history**. If logged in as a **super user,** there is the option to **add, edit and delete** items on the shopping page.

### Advice
This is a members only section that is revealed only when the user is logged in. It contains a dropdown menu of four pages:
#### Getting Started
For women new to running. This page offers advive on the best was to ease yourself into running and getting motivated. link to pay for a personalised plan.
#### Gear
Giving advice on the best types of running kit needed from shoes and bras to playlists to get you set up right. link to pay for a personalised plan.
#### Nutrition 
With a breakdown of what to eat to get the best results. Broken down into the basic food types and how each group affects your performance. link to pay for a personalised plan. 
#### Coaching 
with some tips for helping your body to achive the best results. All these pages have a button on the bottom offering a chance to get a personalised plan.

### Shop
Here we have the e-commerce section of the website. Users can purchase branded merchandise from the club. Here items can be browsed and selected to be added to a shopping basket. **super users** have the ability to **edit and delete items** from the store.

### Contact Us
This is where users can **get in touch with site owner**. The background image shows a woman running through a puddle. This is to reflect the real life situations and conditions that runners often face. It shows determination and spirit as it's telling you that this isn't easy, but it will be worth it.

### Shopping bag
This page in **linked from the shopping bag total** shown on the far right of the nav bar. It show's the user the items in their bag with amounts, prices, sizes and the total. The user can also add or remove items from this page. The **secure checkout button** takes the user to a Stripe payment page where they can input their details.

---

## Database Design

**During development of this website, I worked with the standard <strong>sqlite3</strong> database that comes inbuilt with Django.**

#### The Product Model:

The **Product** model within the **products app** holds the following data for the items on the shopping page:

| Name          | Validation                                                | Field Type   |
| ------------- | --------------------------------------------------------- | ------------ |
| sku           | (max\_length=254, null=True, blank=True                   | CharField    |
| name          | (max\_length=254)                                         | CharField    |
| description   | default='some string'                                     | TextField    |
| has\_sizes    | (default=False, null=True, blank=True)                    | BooleanField |
| price         | (max\_digits=6, decimal\_places=2)                        | DecimalField |
| rating        | (max\_digits=6, decimal\_places=2, null=True, blank=True) | DecimalField |
| image\_url    | (max\_length=1024, null=True, blank=True)                 | URLField     |
| image         | (max\_length=50, null=False, blank=False)                 | ImageField   |


#### The Story Model:

The **Story** model within the **herstories app** holds the following data for the women who are part of the club:

| Name          | Validation                                                | Field Type   |
| ------------- | --------------------------------------------------------- | ------------ |
| full\_name    | (max\_length=50, null=False, blank=False)                 | CharField    |
| age           | (null=False, blank=False)                                 | IntegerField |
| occupation    | (max\_length=254, null=False, blank=False)                | CharField    |
| details       | default='some string'                                     | TextField    |
| image         | (null=True, blank=True)                                   | ImageField   |


#### The Event Model:

The **Event** model within the **events app** holds the following data for the upcoming running events:

| Name          | Validation                                                | Field Type   |
| ------------- | --------------------------------------------------------- | ------------ |
| date          | (max\_length=100, null=False, blank=False)                | CharField    |
| location      | (max\_length=200, null=False, blank=False)                | CharField    |
| distance      | (null=False, blank=False)                                 | IntegerField |
| description   | default='some string'                                     | TextField    |
| image         | (null=True, blank=True)                                   | ImageField   |

---

## Planning and Testing

Planning out how my finished project would work was very important as I had to understand how all the elements would work together.

Using wireframes enabled me to quickly build a basic idea of the pages needed and how they would interact with each other. I then designed more detailed wireframes using dummy text and real images in InDesign, to experiment with colours, fonts and grids. 

As the project uses database models, it was vital that these were mapped out early on. Changing database models or adding new ones in later in the project could cause problems, so I wanted to get them right before I moved on too much with the site pages and interaction.

I utilised Django's templating language to reuse code over mutiple pages to simplify my code. This allowed me to keep the basic page design and drop in the seperate code where needed. 


### head
xxxxx

---

## Bugs and Problems

### Scroll bar on bottom of website
had a problem with having a scroll bar on bottom of site. I made coloured backgrounds for all the panels and divs that it could be and made them all **90vw**. There was still a scroll bar. After looking for solutions online, i figured it was the body of that the was causing the problem. I gave it a width of **98vw and the scroll bar disappeared.** However I how had my home page image and the panels underneath with a white line down the right hand side because of the 98vw. After a bit of searching in discovered that adding **'overflow-x: hidden;’** to body on the CSS fixed the problem.

### Bootstrap Flex box and Order
I wanted the order of the columns on some of my pages to change from desktop to tablet and mobile on the **My Story panel** and **Advice pages**. On desktop I wanted the text column one the left and image column on the right as I felt this worked best visually. But when switching to smaller screens I needed the image to be at the top to draw in the eye and create visual clues and impact. After searching for a solution I came across using **Bootstrap flex box** to solve it. using **‘flex-column-reverse flex-md-row’** flipped my second column to the top on smaller screens. However, this didn’t seem to work so well on the Advice pages as it threw out the grid on tablets. So for these I used **Bootstrap’s order** class to tell each column it’s position at each breakpoint.

### Highlighting active nav bar button
I wanted to show the user which page they were currently on by highlighting the corresponding button in the nav bar. There were a few options offered up by various Google searches, but the one that worked for me and seemed to be the simplest was to add a **with statement** within the nav bar that matched up the url names **{% with url_name=request.resolver_match.url_name %}** which created an active button if they matched **{% if url_name == ‘xxxxx’ %}active{% endif %}**. With an **active** CSS style created, this makes it clear to the user where they are.

### Code stuck in ‘message-container’
I was having a problem with a couple of my grids when logged in as a SuperUser. Both my ‘order history’ and ‘edit product’ pages had grids that were behaving badly and not showing the nav bar. In the **Inspect** view I could see that it was telling me that they were inside the message-container div which is only a thin column down the right of the page. As it was in the messages I felt it must be to do with my toast files. After much trial and error and some advice, it was tracked down to **not closing the div** in my toast-info.html file. That fixed, the pages looked great.

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
* [Psycopg2](https://pypi.org/project/psycopg2/)
* [Gunicorn](https://pypi.org/project/gunicorn/)
* [Stripe](https://stripe.com/en-gb)
* [Amazon Web Services (AWS)](https://aws.amazon.com/)
* [TinyPNG](https://tinypng.com/)
* [Genfavicon](http://www.genfavicon.com/)

#### Databases
* [PostgreSQL - Production](https://www.postgresql.org/)
* [SQlite3 - Development](https://www.sqlite.org/index.html)

---

## Deployment

### Running this project locally

**Follow these steps to run this project locally**

You must have the folowing:
* An **IDE (Interactive Development Environment)** ie [Gitpod](https://www.gitpod.io/)
* The following installed on your machine: [PIP](https://pip.pypa.io/en/stable/installing/), [Git](https://git-scm.com/), [Python3](https://www.python.org/)
* You will need to set up an account with [Stripe](https://stripe.com/en-gb) for processing shopping transactions.

### Instructions

**You may need to follow a different guide depending on which Operating System you are using.**

* **1 Clone** the girlsrun repository by either downloading [here](https://github.com/GarySimons/girlsrun) or entering the following command into your terminal:
```bash
git clone https://github.com/GarySimons/girlsrun
```
* **2** Navigate to this folder in your terminal.

* **3** In your termainal, write the following command:
```bash
python3 -m .venv venv
```
* **4** Initialize the environment with the following commad:
```bash
.venv\bin\activate
```
* **5** Install the requirements and dependancies from the **requirements.txt** file:
```bash
pip3 -r requirements.txt
```
* **6** With your IDE, create an **eny.py** file to store any secret information that you don't want getting out into the public domain.

* 7 Enter this command into your terminal to migrate the models into your database.
```bash
python3 manage.py migrate
```
* 8 Create a Superuser with special access to the admin of the website by entering:
```bash
python3 manage.py createsuperuser
```
* 9 You can now run the website locally using:
```bash
python3 manage.py runserver
```

### Delpoying to Heroku

**You will need to set up an account with [Heroku](https://www.heroku.com/) to host your website.**

* **1** Create a **requirements.txt** file by inputting the following command to your terminal:
```bash
pip3 freeze > requirements.txt
```
* 2 Create a **Procfile** with this this command:
```bash
echo web: python3 app.py > Procfile
```
* **3** Save and Push these files to your **repository.**

* **4** Create a **new app** for your project on the Heroku dashboard.

* **5** Select your **deployment method** by clicking on the deploymeny menthod button and selecting GitHub.

* **6** On the dashboard, go to the **Config Variables** section and set it up:

| Key                | Value                        |
| ------------------ | ---------------------------- | 
| DATABASE_URL       | <your_database_url>          |
| SECRET_KEY         | <your_secret_key>            |
| STRIPE_PUBLISHABLE | <your_stripe_publishable_key>|
| STRIPE_SECRET      | <your_stripe_secret_key>     |

* **7** Click the deploy button.

* **8** Waiting for the project build to processing.

* **9** Open the app and check your site is working correctly.

---

## Credits

### Thanks

My mentor [Simen Daehlin](https://dehlin.dev/) for all the advice and pointers. And for always pushing me to go further.

All the **tutors** that helped me along the way on the **Tutor Support**. Special thanks to [Michael Park](https://www.linkedin.com/in/michael-park-a04a40114/?originalSubdomain=ie), who was always there in my early mornings to offer sage advice, solutions and chat.

### Images
All images were sourced from the [iStock](https://www.istockphoto.com/gb) image library. 

### Text
All text written by me. **Advice pages text** adapted from various websites. See **Credits** section.

### Shopping pages code
Much of the code for the **e-commerce section** of my website was achieved by following the **Django E-Commerce Mini Project** from the Code Institute lessons. I adapted it to suit my website.

#### Inspiration
I was very inspired by a few of websites I found, that made me want to do build this project. All these sites were very important in helping me understand what angle to approach the subject:
* One of the main things I had in my mind when I started this project was the [This Girl Can](https://www.thisgirlcan.co.uk/) campaign that was launched a few years ago. It was great as it wanted to show women of all ages and sizes that they could get involved. It had lovely stories about real women and didn't try and make it too glamorous. 
* I loved the beautiful feeling of community and support on the [These Girls Can Run](http://thesegirlscanrun.weebly.com/home.html) website. 
* I also got more professional ideas on what should be included on my site from [She Runs Outside](https://www.sherunsoutdoors.com/). 
* Another inspiring website I found was [Brighton and Hove Women's Running Club](https://bhwrc.org/) which had some great ideas. 

#### Advice
For the member only **advice pages**, I wanted to get some expert information, which I put it in my own words as much as possible. I found useful information on various sites including: 
* Nutrition [New York Times](https://www.nytimes.com/guides/well/healthy-eating-for-runners)
* Beginning to run [New York Times](https://www.nytimes.com/guides/well/how-to-start-running)
* General Advice [runningtrainingplan.com](https://runningtrainingplan.com/)

#### Technical help
As much as I could I tried to use find my own solutions to questions and problems that I had. Some of the sites I used to solve my problems included:
* To **create active links** in the nav bar [Master Code Online - Django Tutorial - Create An Active Link In Django](https://www.youtube.com/watch?v=0StdrQY8074)
* To create a **transparent box** for my contact us page [css-tricks.com](https://css-tricks.com/snippets/css/transparent-background-images/)
* For the **loading spinner** on my shopping page [mdbootstrap.com](https://mdbootstrap.com/docs/jquery/components/spinners/)
* Swapping order of columns at different sizes using **order** [Stack Overflow](https://stackoverflow.com/questions/37814508/order-columns-through-bootstrap4)
* Swapping order of columns at different sizes using **flex** [codeply.com](https://www.codeply.com/go/6vWQN2ocxe)
* Getting rid of **horizontal scroll** at the bottom of website [Stack Overflow](https://stackoverflow.com/questions/40418627/how-do-i-remove-horizontal-scroll-bar-at-the-bottom-of-my-page-css)


### Disclaimer

This website is a Milestone Project for the **Full Stack Web Development** course at [Code Institute](https://codeinstitute.net/). It is for educational purposes only.
