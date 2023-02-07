# This file is testing the functions of controller.py, all functions within this file should be tested. 
# Unit tests are not testing the entire app, just this single function
# When testing you should be using a TEST_DB, to easily do this modify the db.py so it is using a new DB
# When testing on a test_db you should automatically reset the DB after testing and populate it with some data before testing

from controller import *
from service import *

def test_createOrder(mocker):
    test_data = "Order received :)"
    # Arrange - Variables and values needed for the test
    test_customer_name = 'Dave'
    test_drink_type = 'Coffee'
    test_drink_size = 'Large'
    test_extras = 'No'
    test_price = 1.00
    mocker.patch("service.enterOrder", return_value=test_data)

    # Act - What you are testing 
    result = service.enterOrder(test_customer_name, test_drink_type, test_drink_size, test_extras, test_price)

    # Assert - Asserting whether what you assume happens, does happen
    assert result == test_data