import pytest
import os
import datetime
from functions import greetings

def test_patched_greetingsMorning(monkeypatch):
    monkeypatch.setenv('MYDATE', '05-31-2018 07:30:12')
    assert greetings("Juan") ==  "¡Buenos días Juan!"