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

### Direct Marketing and Campaign Management
Direct marketing involves reaching out to customers and potential customers through various channels like email, social media, and direct mail to promote products or services using campaign management. Campaign management involves planning, executing, and monitoring marketing campaigns to achieve specific objectives. It includes coordinating various elements such as strategy development, message creation, channel selection, budget allocation, and performance tracking. Effective campaign management ensures that marketing efforts are organized, targeted, and aligned with the overall marketing goals of the business.

### Targeting
Targeting in marketing is the practice of narrowing down a target market into specific segments of consumers with common attributes and directing personalized marketing efforts toward them. This approach ensures that marketing resources are focused on the audience most likely to engage with the brand, leading to greater efficiency and return on investment.

### Conversion Rates
The conversion rate is the percentage of subjects who complete a specific desired action, such as making a purchase. Conversion rate can be calculated by taking the total number of subjects who have completed an action and dividing it by the overall size of the audience exposed to that. High conversion rates indicate effective marketing efforts.

# Problem Statement
Based on the understanding described above, my objectives in solving the Starbucks Project are:

* Offer effectiveness: Comparison of the conversion rate and the (monetary) revenue of the various BOGO and discount offers.
* Customer value: Identification of customers with the highest conversion rates and highest average revenue.
* Prediction of conversion and revenue.

In order to have insights related to revenue related to customers and offers the event history in transcript has to processed including data in portfolio, especially duration and difficulty.

**N. B. As the offers of type "informational" cannot be related directly to purchase events, I have excluded these events from further analysis.**

# Data Analysis

## Available Data Files <a name="data"></a>

The data is provided separated into three files in JSON format:

### profile.json - Customers with Starbucks reward membership
Rewards program users (17000 users x 5 fields)

* gender: (categorical) M, F, O, or null
* age: (numeric) missing value encoded as 118
* id: (string/hash)
* became_member_on: (date) format YYYYMMDD
* income: (numeric)
* portfolio.json
* Offers sent during 30-day test period (10 offers x 6 fields)

### portfolio.json - Offers description
Offers sent during 30-day test period (10 offers x 6 fields)

* reward: (numeric) money awarded for the amount spent
* channels: (list) web, email, mobile, social
* difficulty: (numeric) money required to be spent to receive reward
* duration: (numeric) time for offer to be open, in days
* offer_type: (string) bogo, discount, informational
* id: (string/hash)
* transcript.json
* Event log (306648 events x 4 fields)

### transcript.json - Interaction history including offer communication, conversion and revenue data
Event log (306648 events x 4 fields)

* person: (string/hash)
* event: (string) offer received, offer viewed, transaction, offer completed
* value: (dictionary) different values depending on event type
* offer id: (string/hash) not associated with any "transaction"
* amount: (numeric) money spent in "transaction"
* reward: (numeric) money gained from "offer completed"
* time: (numeric) hours after start of test

## Data Quality Issues
### profile.json

In profile.json are 2175 cusotmer records with age equals to 118 years and having gender None values and income NaN values. 
For gender the None values will be replaced by NaN values.

As soon as analysis/models are used which are sensitive to NaN values the data related records to these customer records will be deleted.

![profile.json data quality issues](profile_NaN_values.png "profile.json data quality issues")

### transcript.json

#### Basic assumption for the relationship between offer completed events and transactions
For one specific customer (id) the transaction record(s) with the same time value as the offer completed event record are considered as one purchase event.

#### Multiple offers used per transaction
In some cases, there are multiple offers used at one transaction (assumption: same time value). This means, that the amount has to be split up. I assumed, that the amount can be split up according to the ratio of rewards of the offers invovled at the same time of offer completion. 

Example: Based on this assumption the amount 18,42 is split up the following way:
* offer_id 9b*: 18,42 * 5 / (5 + 2) = 13,16
* offer_id fa*: 18,42 * 2 / (5 + 2) =  5,26

![transcript.json multiple offers per transaction issues](multiple_offers_per_trx.png "transccipt.json data anomaly: multiple offers per transaction issues")

#### Offer completion events without prior offer view events
In some cases, there are offer completion events without prior offer view events (e. g. offer_id 29* in the example below). Probably the there are lock screen notification on mobile devices, which are not tracked as viewed. As the customer is benefiting anyhow from the the offer my assumption is, to accept this event as a normal completion (i. e. conversion event).

![transcript.json offer completion without prior offer view event](offer_completed_without_view.png "transcript.json data anomaly: offer completion without prior offer view event")

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


