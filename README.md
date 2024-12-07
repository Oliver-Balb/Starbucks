# Starbuck's Capstone Challenge - Customer Segmentation and Offer Targeting


This is a GITHUB Repository **just for educational purposes.** All data was provided by [Udacity](https://www.udacity.com/dashboard) and Starbucks.

## Table of Contents

[Project Summary](#overview)
[Available Data and Features Included](#data)
[Installation](#installation)
[Execution](#execution)

## Overview<a name="overview"></a>

The dataset provided by starbucks simulates purchasing decisions influenced by promotional offers. Each person has hidden traits affecting their buying patterns, linked to observable traits. Events include receiving, opening offers, and making purchases, with only transaction amounts recorded. There are three offer types:

BOGO (Buy-One-Get-One): Spend a certain amount to get an equal reward.
Discount: Get a reward equal to a fraction of the amount spent.
Informational: No reward or spending requirement.

### Campaign Management
Campaign management involves planning, executing, and monitoring marketing campaigns to achieve specific objectives. It includes coordinating various elements such as strategy development, message creation, channel selection, budget allocation, and performance tracking. Effective campaign management ensures that marketing efforts are organized, targeted, and aligned with the overall marketing goals of the business.

### Targeting
Targeting in marketing is the practice of narrowing down a target market into specific segments of consumers with common attributes and directing personalized marketing efforts toward them. This approach ensures that marketing resources are focused on the audience most likely to engage with the brand, leading to greater efficiency and return on investment.

### Conversion Rates
The conversion rate is the percentage of subjects who complete a specific desired action, such as making a purchase. Conversion rate can be calculated by taking the total number of subjects who have completed an action and dividing it by the overall size of the audience exposed to that. High conversion rates indicate effective marketing efforts.


## Available Data and Features Included <a name="data"></a>

### Data Files
The data is provided separated into three files in JSON format:

#### profile.json - Customers with Starbucks reward membership
Rewards program users (17000 users x 5 fields)

* gender: (categorical) M, F, O, or null
* age: (numeric) missing value encoded as 118
* id: (string/hash)
* became_member_on: (date) format YYYYMMDD
* income: (numeric)
* portfolio.json
* Offers sent during 30-day test period (10 offers x 6 fields)

#### portfolio.json - Offers description
Offers sent during 30-day test period (10 offers x 6 fields)

* reward: (numeric) money awarded for the amount spent
* channels: (list) web, email, mobile, social
* difficulty: (numeric) money required to be spent to receive reward
* duration: (numeric) time for offer to be open, in days
* offer_type: (string) bogo, discount, informational
* id: (string/hash)
* transcript.json
* Event log (306648 events x 4 fields)

#### transcript.json - Interaction history including offer communication, conversion and revenue data
Event log (306648 events x 4 fields)

* person: (string/hash)
* event: (string) offer received, offer viewed, transaction, offer completed
* value: (dictionary) different values depending on event type
* offer id: (string/hash) not associated with any "transaction"
* amount: (numeric) money spent in "transaction"
* reward: (numeric) money gained from "offer completed"
* time: (numeric) hours after start of test

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.


### Program Files
* process_data.py - Extraction, transformation, and load of CSV above files into SQLITE DB including data cleansing.
* train_classifier.py - Definition and training of a supervised machine learning model based on labeled message data.
* Files required for the web app are stored within the udacity workspace.

## Execution <a name="files"></a>

**(1) ETL**`

Start of execution using command line with for mandatory arguments:

`python process_data.py [messages_filepath] [categories_filepath] [database_filepath]`

Provide the filepaths of the messages and categories datasets as the first and second argument respectively, as well as the filepath of the database to save the cleaned data to as the third argument. 

Example: python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

**(2) Model definition and training**
Start of execution using command line with two mandatory arguments:

`python train_classifier.py [database_filepath] [model_filepath]`

Provide the filepath of the disaster messages database as the first argument and the filepath of the pickle  file to save the model to as the second argument. 

Example: python train_classifier.py ../data/DisasterResponse.db classifier.pkl

**(3) Web Front End**

a. In Udacity Project Workspace go to `app` directory: `cd app`

b. Run your web app: `python run.py`

c. Click the `PREVIEW` button to open the homepage


