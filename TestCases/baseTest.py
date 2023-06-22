"""
this will hold the fixtures we are using in our tests
"""

import pytest

@pytest.mark.usefixtures("log_on_failure","get_browser")
class baseTest:
    pass