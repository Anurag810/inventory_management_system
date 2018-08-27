# Product Inventory Management System
### The product is being developed to track real time movement of products from one location to another.

## Prerequisites:
The following items should be installed in your system:

1. Pycharm IDE
2. MySql Database server

## Technologies Used:

    1. Python 2.7.10
    2. Flask 1.0.2
    3. jinja2 2.10
    4. mysql-connector-python 8.0.12
    5. Bootstrap 4.1.3
    6. HTML5
    7. JavaScript
    8. CSS

## Commands used:


    //for creating virtual venv
    pip install virtualenv
    pip virtualenv venv

    //for installing Flask
    pip install Flask

    //for installing jinja2 templates
    pip install jinja2-cli

    //for installing mysql connector
    pip install mysql-connector-python

## Steps
1. Download the whole project
2. Create database name as inventory and following tables

        //for creating database
        CREATE DATABASE inventory;

        //for creating tables
        CREATE TABLE user (
            uid int(10) NOT NULL AUTO_INCREMENT,
            u_name varchar(50) NOT NULL,
            pass varchar(50) NOT NULL,
            PRIMARY KEY (uid)
        );

        //for creating product tables
        CREATE TABLE product (
            pid int(10) NOT NULL AUTO_INCREMENT,
            p_name varchar(50) NOT NULL,
            P_type varchar(50) NOT NULL,
            P_weight int(10) NOT NULL,
            PRIMARY KEY (pid)
        );

        //for creating table location
        CREATE TABLE location (
            lid int(10) NOT NULL AUTO_INCREMENT,
            l_name varchar(50) NOT NULL,
            l_add varchar(50) NOT NULL,
            l_city varchar(50) NOT NULL,
            PRIMARY KEY (lid)
        );

        //for creating table movement 
        CREATE TABLE movement (
            mid int(10) NOT NULL AUTO_INCREMENT,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            l_from varchar(10) NOT NULL,
            l_to varchar(10) NOT NULL,
            pid int(10),
            qty int(10),
            PRIMARY KEY (mid)
        );

        CREATE TABLE quantity (
            lid int(10) NOT NULL,
            pid int(10) NOT NULL,
            qty int(10) NOT NULL,
        );

4. Create default user for login

        //create default user
        
        INSERT INTO  `user` (
        `u_name` ,
        `pass`
        )
        VALUES (
        'user',  'password'
        );

3. Import to pycharm IDE

        File --> import settings --> project folder


# PAGES
## 1. Login Page

<img src="product_inventory/images/Login_page.png">

## 2. Home Page

<img src="product_inventory/images/home.png">

## 3. Add Product modal

<img src="product_inventory/images/Add_productModal.png">

## 4. Add Location modal

<img src="product_inventory/images/Add_locationModal.png">

## 5. Move Product modal

<img src="product_inventory/images/move_productModal.png">

## 6. View and Update product details 

<img src="product_inventory/images/viewproduct.png">

## 7. View and Update location details 

<img src="product_inventory/images/viewlocation.png">

## 8. View and Update product Movements details 

<img src="product_inventory/images/viemove.png">

## 7. View final report 

<img src="product_inventory/images/repprt.png">

 #### GIT Commands:
 
    git pull
    git status
    git add .
    git commit -m "any message"
    git push
    git push  --set-upstream origin branch_name
