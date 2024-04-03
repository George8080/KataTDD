import pytest
import os
import datetime
from functions import greetings

def test_patched_greetingsMorning(monkeypatch):
    monkeypatch.setenv('MYDATE', '05-31-2018 07:30:12')
    assert greetings("Juan") ==  "¡Buenos días Juan!"

def test_patched_greetingsAfternoon(monkeypatch):
    monkeypatch.setenv('MYDATE', '08-27-2023 18:32:43')
    assert greetings("Mario") ==  "¡Buenas tardes Mario!"

def test_patched_greetingsNight_1(monkeypatch):
    monkeypatch.setenv('MYDATE', '08-27-2023 01:32:43')
    assert greetings("George") ==  "¡Buenas noches George!"