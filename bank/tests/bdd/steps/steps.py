from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from bank.account import Account
from bank_app import app, BANK


@step(u'I create account "([^"]*)" with balance of "([^*]*)"')
def i_create_account_with_balance_of_group1(step, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)

@step(u'I visit homepage')
def i_visit_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)
    #assert_equal(world.response.text, 'Hello World!')

@step(u'I enter the account number "([^"]*)"')
def when_i_enter_the_account_number_group1(step, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)

@step(u'I see a balance of "([^"]*)"')
def then_i_see_a_balance_of_group1(step, expected_balance):
    assert_in("Balance: {}".format(expected_balance), world.form_response.text)
