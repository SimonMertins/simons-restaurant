# Simon-Restaurant

## Overview

Simon-Restaurant is a web application designed to showcase and manage a restaurant's menu, allowing users to explore available dishes, and get information about the restaurant and make a reservation for a table. Targeted towards food enthusiasts and potential customers, Simon-Restaurant aims to provide an interactive and user-friendly platform for a seamless dining experience.

[Link to the site](https://simon-restaurant-0c9a920b2074.herokuapp.com/)

## Features

* The Site is fully responsive, with a Navigation bar that changes in to a dropdown for smaller screens and the layout of thee site changes to adapt to your screen size.

### Existing Features

#### Navigation Bar

Featured on all pages, the responsive navigation bar ensures easy navigation between Home, Menu, Reservations, and Contact sections. The consistent design across pages enhances user experience.

#### Reservation

Simon-Restaurant allows users to make a reservation.

#### Contact Information

The Contact section provides essential information about the restaurant, including address, phone number. This ensures users can easily reach out or plan a visit.

### Features Left to Implement

- Online ordering system
- User accounts for personalized experiences
- Integration with a payment gateway for online transactions

## Deployment

The project is deployd using heroku.

using the following steps:

* Create a project on Heroku and open settings.

* In Config Vars add 'DISABLE_COLLECTSTATIC' as a key and add '1' as value.

* In Config Vars add 'SECRET_KEY' as a key and add 'YourSecretKey (you can find your secret key settings.py)' as value.

* Open the deploy tab in heroku

* select connect to github and then you search for your repo and connect it.

* In settings.py, in the ALLOWED_HOSTS list, copy your ‘... .herokuapp.com’ string.

* And then you scroll down on the deploy tab tab in heroku and press deploy.



## Testing
* No waring on [w3 validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsimon-restaurant-0c9a920b2074.herokuapp.com%2F) 

* No warning on [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsimon-restaurant-0c9a920b2074.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
### Unfixed Bugs
* I have bug in the Navbar where 'Menu' look diffrent then Home, Reservations and Contact. And I have not been able to figure out how to fix it.
## Credits

- Code institute
- stackoverflow.com
- w3schools.com
- google
- chatGPT

### Content

- Text content on the website was crafted by Me (Simon Mertins,with some help from ChatGPT)

