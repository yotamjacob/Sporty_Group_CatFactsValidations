# Sporty_Group_CatFactsValidations
A Short project to test the capabilities of the Cat Facts API by alexwohlbruck

To use it, simply copy the repository and run pytest main.py
The suite will execute 3 tests: 

## Data

| Test Name   | Validation Used | Motivation |
|--------|-----|--------|
| test_cat_fact_api_is_available  | Using assertion on the response code to make sure it is equal to 200 | I Use this test to make sure the API is alive and accesible |
| test_correct_amount_of_facts_is_returned | assertion on the response json's length when calling the url GET /facts/random?animal_type=cat&amount=? | When comparing the result of this API call to an expected number of items, i validate the integrity of the DB ad makre sure data items are not being deleted |
| test_get_fact_by_id_return_correct_fact| I Assert the received response text to the expected fact string | By asserting the received fact and comparing to an expected one, i make sure the data is neing corrupt on the API's database |
