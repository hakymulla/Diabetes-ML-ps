# Dataset

## Link to Dataset: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset , More information about the dataset can be found in Kaggle.

## Link 2 : https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/discussion/295407?sort=published

## Link 3 : https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook

# Data Description (From Link 2 and Link 3)

## Response Variable / Dependent Variable:

    (Ever told) you have diabetes (If "Yes" and respondent is female, ask "Was this only when you were pregnant?". If Respondent says pre-diabetes or borderline diabetes, use response code 4.) --> DIABETE3

## Independent Variables:

## High Blood Pressure

    Adults who have been told they have high blood pressure by a doctor, nurse, or other health professional --> _RFHYPE5

## High Cholesterol

    Have you EVER been told by a doctor, nurse or other health professional that your blood cholesterol is high? --> TOLDHI2
    Cholesterol check within past five years --> _CHOLCHK

## BMI

    Body Mass Index (BMI) --> _BMI5

## Smoking

    Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] --> SMOKE100

## Other Chronic Health Conditions

    (Ever told) you had a stroke. --> CVDSTRK3
    Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI) --> _MICHD

## Physical Activity

    Adults who reported doing physical activity or exercise during the past 30 days other than their regular job --> _TOTINDA

## Diet

    Consume Fruit 1 or more times per day --> _FRTLT1
    Consume Vegetables 1 or more times per day --> _VEGLT1

## Alcohol Consumption

    Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) --> _RFDRHV5

## Health Care

    Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare, or Indian Health Service? --> HLTHPLN1
    Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? --> MEDCOST

## Health General and Mental Health

    Would you say that in general your health is: --> GENHLTH
    Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? --> MENTHLTH
    Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? --> PHYSHLTH
    Do you have serious difficulty walking or climbing stairs? --> DIFFWALK

## Demographics

    Indicate sex of respondent. --> SEX
    Fourteen-level age category --> _AGEG5YR
    What is the highest grade or year of school you completed? --> EDUCA
    Is your annual household income from all sources: (If respondent refuses at any income level, code "Refused.") --> INCOME2


## Age (Fourteen-level age category)

    1 Age 18 to 24
    2 Age 25 to 29
    3 Age 30 to 34
    4 Age 35 to 39
    5 Age 40 to 44
    6 Age 45 to 49
    7 Age 50 to 54
    8 Age 55 to 59
    9 Age 60 to 64
    10 Age 65 to 69
    11 Age 70 to 74
    12 Age 75 to 79
    13 Age 80 or older
    14 Don't Know / Refused to answer (I removed these as well)

## Education


    1 Never attended school or only kindergarten
    2 Grades 1 through 8 (Elementary)
    3 Grades 9 through 11 (Some high school)
    4 Grade 12 or GED (High school graduate)
    5 College 1 year to 3 years (Some college or technical school)
    6 College 4 years or more (College graduate)
    9 Refused (All these records were deleted from the dataset)


## Income


    1 Less than $10,000
    2 Less than $15,000 ($10,000 to less than $15,000)
    3 Less than $20,000 ($15,000 to less than $20,000)
    4 Less than $25,000 ($20,000 to less than $25,000)
    5 Less than $35,000 ($25,000 to less than $35,000)
    6 Less than $50,000 ($35,000 to less than $50,000)
    7 Less than $75,000 ($50,000 to less than $75,000)
    8 $75,000 or more
    77 Don’t know/Not sure (removed from dataset)
    99 Refused (removed from dataset)
    BLANK Not asked or Missing(removed from dataset)
