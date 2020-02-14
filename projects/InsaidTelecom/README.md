

# Project Description

It's always wonderful to see services customized
to your needs. Businesses try to understand your behavior and adjust
their offerings so as to ensure you feel attached to their services.


InsaidTelecom, one of the leading telecom players, understands that customizing offering
is very important for its business to stay competitive.
Currently, InsaidTelecom is seeking to leverage behavioral data from more than 60% of the 50 million mobile devices active daily in India
to help its clients better understand and interact with their audiences.

In this consulting assignment, Insaidians are expected to build a dashboard to understand
user's demographic characteristics based on their mobile usage, geolocation, and mobile device properties.
Doing so will help millions of developers and brand advertisers around the world pursue
data-driven marketing efforts which are relevant to their users and catered to their preferences.



# Consulting Goals

To help the customer the consultants are expected to have depth of clarity in the underlying data.
How much effort has been put into cleansing and purifying the data will decide how closely have you looked at the data.
How detailed is the observation stated in the submission report and finally how well a group presents their consulting journey.

Please remember this is an analytics consulting hence, your efforts in terms of
finding user behavior is going to directly impact the company's offerings.
Do help the company understand what is the
right way forward and suggest actionable insights from marketing and product terms.

# Data Description

In this assignment, you are going to study the demographics of a user (gender and age) based on their app download and usage behaviors.
The Data is collected from mobile apps that use InsaidTelecom services. Full recognition and consent from individual user of those apps have been obtained,
and appropriate anonymization have been performed to protect privacy. Due to confidentiality, we won't provide details on how the gender and age data was obtained.
Please treat them as accurate ground truth for prediction. The data schema can be represented in the following table:


## gender_age_train
Devices and their respective user gender, age and age_group

## phone_brand_device_model
device ids, brand, and models phone_brand: note that few brands are in
Chinese

Brand Name	Brand English Mapping
'华为'	'Huawei'
'小米'	'Xiaomi'
'三星'	'Samsung'
'vivo'	'vivo'
'OPPO'	'OPPO'
'魅族'	'Meizu'
'酷派'	'Coolpad'
'乐视'	'LeEco'
'联想 '	'Lenovo'
'HTC'	'HTC'

## events_data
when a user uses mobile on INSAID Telecom network, the event gets logged
in this data. Each event has an event id, location (lat/long), and the
event corresponds to frequency of mobile usage. timestamp: when the user
is using the mobile.


# Instructions
Download the DataSets onto Python by connecting to the below provided MySQL instance.
                           
host	'cpanel.insaid.co'
user	'student'
passwd	'student'
database	'Capstone1'

Use "mysql.connector" package in Python.

[Group Sheet](https://docs.google.com/spreadsheets/d/1fU8PU9tcJewA-J85Lnp1899BKa7Sw5aWOJ0tzdY1R3o/edit#gid=0)
[Capstone Website](https://projects.insaid.co/capstone1/login.php)