import pytest
import sys
import os

from simuload import models, utils


def test_imports():
    module_list = ["simuload.models", "simuload.utils"]
    for module in module_list:
        assert module in sys.modules
