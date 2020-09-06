import pytest
import row_to_list
def test_for_clean_row():
  # assert Statement only takes a boolean expression
  # If the boolean is True, it passes, if False, it failes and shows an error
  assert row_to_list("2,081\t314,942\n") == \ ["2,081","314,942"]

 
def test_for_missing_area():
    #Missing Area
    #Correct way is "assert var is None"
    # don't do like "assert var == None"
  assert row_to_list("\293,410\n") is None


def test_for_missing_tab():
    #For Missing a Tab Stace
  assert row_to_list("1,463238,765\n") is None

#To run it
# pytest test_row_to_list.py
