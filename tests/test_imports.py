import pytest
import sys
import os

import models
import utils

def test_imports():
    module_list = ['models','utils']
    for module in module_list:
        assert module in sys.modules