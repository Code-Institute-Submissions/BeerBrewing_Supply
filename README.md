# Beer Brewing Supply
Checkout on heroku [https://beerbrewing-supply.herokuapp.com/](https://beerbrewing-supply.herokuapp.com/)
![https://github.com/jourm/BeerBrewing_Supply/blob/master/media/homepage.PNG](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/homepage.PNG)
My local Home Brewing shop has been forced to close in the wake of the coronavirus.
The purpose of this project is to create a prototype for a new website with a online shop from them.
The Shop also sells equipment and ingredients for wine and cider making,
but initially the project will only cover the beer brewing side of the business. 
A beer brewing shop has many forms of products and most of these have more sub categories,
there can for exaple be over  20 subcategoreis to Equipment. The goal of this project is not to create
all of these categories but more of a base that a full store could be built upon.


## Business goals of the site:

* Sell Equipment, ingredients, etc that are used for beer brewing.
* Promote the beerbrewing hobby

## User stories:
There are three main kinds of users.
1. Site Owner
2. Experienced Homebrewer
3. Beginner Homebrewer
1. As the site owner I want to …. So that I can ….
    * Display the products I have for sale. -- Make money
    * Post information About upcoming sales, new products, Brewing news etc -- Keep my customers informed and drive up sales 
    * Add new Products -- Sell them
2. As a Experienced Homebrewer I want to …. So that I can ….
    * Buy Ingredients for my next beer -- Brew beer
    * Advance my knowledge -- brew better beer
    * Keep track of my previous purchases. -- Know what ingredients i used last time.
    * Buy New equipment. -- Test a new method, improve my setup.
    * Buy consumables. -- Keep my equipment clean and up to date
3. As a beginner Homebrewer I  want to …. So that I can ….
    * Find relevant information easily. -- Get into the hobby
    * Find a beginner kit. -- Brew my first beer

## Wireframes
[Products](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/Products.PNG)
[Product Details](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/productdetails.PNG)
[Cart](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/cart.PNG)



## Features
### Navbar
* Avliable on all pages and features links for veiwing the diferent categories of products, The shopping cart, account creation and management.

### Products
The Project features a polymorfic product model with several sub classes, this was done due to the fact that a beer brewing shop
features many diferent kinds of products and the diferent products can have very different attributes. By having a Concrete Base Model with some common fields, 
the basic information such as name, Price and image, for all products can be found in the product table. The issue with this database model is that there is no simple way to know 
what sub table to look in if one only has the date from the base table. This was solved by creating a utillity function get_product() that from an id finds the product in its table.
Information and inspiration for this product model was found on [RealPython.com](https://realpython.com/modeling-polymorphism-django-python/)
Product creation is managed through the default django admin panel. When a Product is created from its sub model, records in the base and child tables are created simultaneously with 
a shared ID.
![Product Database Model](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/ProductModel.PNG)

#### Hops, Malts, Equipment, Yeast and Books
Hops, Malts, Equipment, Yeast and Books are the categories fro the beta version of this site. For a fully populated beer Brewing shop more product categories would be added and these
categories would have sub categories of their own. 

### Shopping cart
The shopping cart for this project is stored in the session cookie as a dictionary of product ids and quantity. 
This is made possible due to the polimorfic nature of the Product database where no ids of different sub products can be the same.
To improve the infromation avaliable about the car a custom context processor collects aditional information based on the cart dictionary in the session.
This context processor makes a list of cart items, containing the item id, quantity, subtotal and the product itself,
as well as the cart total products count and the cart total cost avaliable in every template.
The Cart app comes with views for uppdating the amount of a product in the cat, adding products to the cart and removing products from the cart.

### Blog
This project features a blog where the store owner can post about new products, uppcoming enents and even more detail how to brew beer segments for beginners.
The blog app features views for adding, uppdating and deleting blogs avaliable only to the admin of the site. As well as a view blog view with acts as the landing page for the products.
Here a snippet of infromation about the site, and the four newest products are avaliable to the right of the blog on screens medium or larger.

### Checkout
This Project features checkout using Klarna API. Klarna is one of the largest providers of webshop payment systems in Sweden and they also offer a fully fledged order management system.
Klarna can aslo offer shipping managment, financing and there are features coing soon for managing returns as well.
These are all features that would be well suited for a beer brewing supply shop. Currently The site is set to only handle customers with adresses in sweden but this can easily be changed.
Currently the chain of events that take place is like this.
1. Customer klicks link to secure checkout.
2. The checkout view assebles a request containing the items from the cart, total cost and some urls for future interaction between klarna and this site. And then sends it to Klarna.
3. Klarna creates the Order in their system and resonds with a json object containing a Html snippet that checkout view renders to the page.
4. The customer then fills out thier shipping information, selects a shipping method and enters their credit card information.
5. Once the customer submits, the customer is then redirected to one of the urls supplied in step 2. The view calls Klarna api to recive the uppdated order information and creates 
a New oreder record in th database, as well as clears the cart and renders a checkout completed snippet recived from klarna.
6. Klarna sends a confirmation email to the customers specified email.
7. Two minutes after the purchase has been made Klarna sends a post request containing the order id to dubble check that the order has been created in the databse.
 If it has, A request validating the order in klarnas sytem is made,and if not the order is created and the validated.
8. The validated order will now be avalible in a ready to ship panel for the store owner to pack and pres ship once the order has been shipped.
 This changes the orders status to shipped and sends a request to klarna to capture the outstanding amount of money. 

### Orders
The order app is manily for containing the Order model as well as reveiving the priviously mentioned post request from klarna.
This app features a order panel mentioned above in step 8, where warehouse personel can se what to pack in an order and ship it out.
This app could stand to recive some futher developement. The order model should be uppdated to match Klarnas model more closesly and
 further Order management could be Implemented via Klarna api. 

## Further developement
* Uppdate Ui, The UI is currently very basic due to the fact that time has ben limited and more time was spent on a working backend.
* Implement klarna Shipping. To do this some uppdates to the product models would have to be made such as produc weight and dimensions.
* Implement a Stock, where before allowing a order to be created the stock is checked to make sure the products are in stock. There are Klarna method to integrate this into the checkout process.
* Implement a User profile where the user can see their orderhistory and and save thier shipping preferences.
* Extend Product models to feature A multitude of more sub categories.
* Create a FAQ section.

## Technologies used
This project uses HTML, CSS, JavaScript and Python programming languages.
#### [Gitpod online IDE](https://www.gitpod.io/)
This project was developed in Gitpod Online IDE
#### [Google fonts](https://fonts.google.com/)
This Project uses fonts from Google fonts.
#### [JQuery](https://jquery.com/)
This project uses jquery for DOM manipulation.
#### [Bootstrap](https://getbootstrap.com/)
This project uses bootstrap  for its grid system and premade classes.
#### [Pexels](https://www.pexels.com)
This project uses Pexels as a free source of images.
#### [balsamiq Mockups](https://balsamiq.com/wireframes/)
This project uses balsamiq mockups 3 for creating wireframes.
#### [Django](https://www.djangoproject.com/)
This project uses the Flask web framework.
#### [Heroku](https://www.heroku.com/)
This project is hosted on Heroku.
#### [AWS S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_st_s3)
This project uses AWS S3 to store upploaded files.
#### [Heroku](http://http://whitenoise.evans.io/en/stable/#)
This project uses whitenoise to serve staticfiles on heroku.
#### [Klarna](https://developers.klarna.com/)
This project uses Klarna chekout API for order managment, checkout, and payments.
#### [Gunicorn](https://gunicorn.org/)
This project uses Gunicorn to run the server on Heroku.



## Testing 
### Testing of User stories
1. Site Owner
2. Experienced Homebrewer
3. Beginner Homebrewer
1. As the site owner I want to …. So that I can ….
    1. Display the products I have for sale. -- Make money
    2. Post information About upcoming sales, new products, Brewing news etc -- Keep my customers informed and drive up sales 
    3. Add new Products -- Sell them
    1. **Fulfilled** The site features a store where the site owner can Add their products to sell.
    2. **Fulfilled** The site features a blog where the storowner can post the information they want to share.
    3. **Fulfilled** The site features a store where the site owner can Add their products to sell.
2. As a Experienced Homebrewer I want to …. So that I can ….
    1. Buy Ingredients for my next beer -- Brew beer
    2. Advance my knowledge -- brew better beer
    3. Keep track of my previous purchases. -- Know what ingredients i used last time.
    4. Buy New equipment. -- Test a new method, improve my setup.
    5. Buy consumables. -- Keep my equipment clean and up to date
    1. **Half Fulfilled** The site features a store where ingredients can be bought, but no shipping is implemented and the store currently only feature a small saple set of products. Tho fully achive this goal shipping wuld ne t be set up and the store fully populated.
    2. **Not Fulfilled** There is currently no way to fullfill this goal. Adding some books for sale would help to fulfill this goal.
    3. **Not Fulfilled** No orderhistory is avliable for custors. this would need to be implemented for this goal to be achived,
    4. **Half Fulfilled** The site features a store where equipment can be bought, but no shipping is implemented and the store currently only feature a small saple set of products. Tho fully achive this goal shipping wuld ne t be set up and the store fully populated.
    5. **Half Fulfilled** The site features a store where equipment can be bought, but no shipping is implemented and the store currently only feature a small saple set of products. Tho fully achive this goal shipping wuld ne t be set up and the store fully populated.
3. As a beginner Homebrewer I  want to …. So that I can ….
    1. Find relevant information easily. -- Get into the hobby
    2. Find a beginner kit. -- Brew my first beer
    1. **Not Fulfilled** But this goal could be fulfilled by the storowner writing a series of blogs on hown to brew beer amied at beginners.
    2. **Not Fulfilled** No kits are currently avaliable on the site.


### Automated testing
This Project uses Automated testing in python. Test were created in each apps tests.py and tests the functionality of the app.
Some views require a superuser to be logged in, the tests were ran with logged in required and if if request.user.is_superuser: commented out
since the setUp for testing dosnt support creating a superuser.

Coverage vas used to generate a report on the coverage of the tests.
The following coverage was achived
* Products: 94%
* Cart: 95%
* Checkout: 29%
* Blog: 64%
* Orders: 68%

Checkout and orders require interaction with Klarna Api and it is beyond the scope of this project to test automatically therefore the
coverage of these apps is low. But this will instead be tested manually.

#### Manual testing
**Test:** Visit site.  
**Expected Outcome:** Landingpage displays.  
**Outcome:** Landingpage displays.  
**Passed:** Yes 

**Test:** Add item to cart and visit cart.  
**Expected Outcome:** Item is added to the cart, the total under the cart sign is uppdated and the item that was added is visible on the cart page.  
**Outcome:** Item is added to the cart, the total under the cart sign is uppdated and the item that was added is visible on the cart page.  
**Passed:** Yes 

**Test:** Checkout using testing creditcard details from Klarna.  
**Expected Outcome:** Checkout forms renders correctly, the amount to be paid remains the same and once checkout is completed the checkout completed page is rendered. The order is then avaliable in the Ready to ship section for the site owner.  
**Outcome:** Checkout forms renders correctly, the amount to be paid remains the same and once checkout is completed the checkout completed page is rendered. The order is then avaliable in the Ready to ship section for the site owner.
**Passed:** Yes 

**Test:** Visit Orders to ship, click ship order.  
**Expected Outcome:** Order dissapears from the display and is Captured In Klarnas system.  
**Outcome:** Order dissapears from the display and is Captured In Klarnas system. 
**Passed:** Yes 

## Deployment 
## How to run this project locally.
* Make sure you have a IDE with a virtual enviroment running python3. Preferably gitpod online IDE.
This description will be based on you using Gitpod online IDE. 
* Go to [https://github.com/jourm/BeerBrewing_Supply](https://github.com/jourm/BeerBrewing_Supply) if you have Gitpod extension installed in you browser, a button with Gitpod will be visible next to clone/download press Gitpod.
* This will open the project in gitpod Online IDE. 
* Use pip to install all the required packages in requirements.txt  with : pip -r requirements.txt.
* In checkout.views you need to uppdate the urls in merchanturls to the url you are running your project from.
* Signup for Klarna testing envirioment [Klarna](https://developers.klarna.com/)
* Signup For AWS and create S3 bucket with public access And set up accsess keys. 
* In gitpod settings add the follwoing AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID, KLARNA_PW, KLARNA_PW
* Run python3 manage.py migrate in the terminal to migrate models to you database
* Run python3 manage.py createsuperuser in the terminal to create a superuser
* Run python3 manage.py runserver in the terminal to host the program locally.


## Deploy on heroku.
* First follow steps to run project locally.
* Commit and push project to your github account.
* Create Heroku account.
* Create new app.
* On heroku, go to resources, seach for postgress, click it and selecth the Hobby dev - Free plan, click provision
* On heroku, go to deploy > connect to github repo and connect heroku to you github repo.
* Settings > set config vars AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID, KLARNA_PW, KLARNA_PW
* On heroku go to more -> run console in the console run python3 manage.py migrate and python3 manage.py createsuperuser
* Go to deploy, scroll down and click "enable automatic deploys"