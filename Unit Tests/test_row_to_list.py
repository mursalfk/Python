import pytest
import row_to_list
def test_for_clean_row():
  # assert Statement only takes a boolean expression
  # If the boolean is True, it passes, if False, it failes and shows an error
  assert row_to_list("2,081\t314,942\n") == \ ["2,081","314,942"]

 
def test_for_missing_area():
  assert row_to_list("\293,410\n") is None
