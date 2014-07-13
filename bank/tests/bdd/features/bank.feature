Feature: Bank web application to retrieve
         and update customer accounts

         As a customer I wish to be able to view my balance
         and update my balance
         and withdraw from my balance

         Scenario: Retrieve customer balance
         Given I create the following account:
            |account_number|balance|
            |1111          |50     |
         And I visit homepage
         When I enter the account number "1111"
         Then I see a balance of "50"
