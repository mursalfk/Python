import pytest
import row_to_list
def test_for_clean_row():
  assert row_to_list("2,081\t314,942\n") == \ ["2,081","314,942"]
