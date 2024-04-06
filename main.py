import requests
import pytest

@pytest.fixture
def cat_fact_api_url():
    return "https://cat-fact.herokuapp.com/facts/"

def test_cat_fact_api_is_available(cat_fact_api_url):
    response = requests.get(cat_fact_api_url + "random")
    assert response.status_code == 200

def test_correct_amount_of_facts_is_returned(cat_fact_api_url):
    amount_of_facts = "3"
    response = requests.get(cat_fact_api_url + "random?animal_type=cat&amount=" + amount_of_facts)
    assert len(response.json()) == int(amount_of_facts)

def test_get_fact_by_id_return_correct_fact(cat_fact_api_url):
    response = requests.get(cat_fact_api_url + "591f98803b90f7150a19c229")
    fact_text = response.json()["text"]
    assert fact_text == "In an average year, cat owners in the United States spend over $2 billion on cat food."