import pytest
import os
import datetime
from functions import greetings
from functions import reverse
from functions import palindrome
from functions import stop

# Test greetings in the morning
def test_patched_greetingsMorning(monkeypatch):
    monkeypatch.setenv('MYDATE', '05-31-2018 07:30:12')
    assert greetings("Juan") ==  "¡Buenos días Juan!"


# Test greetings in the afternoon
def test_patched_greetingsAfternoon(monkeypatch):
    monkeypatch.setenv('MYDATE', '08-27-2023 18:32:43')
    assert greetings("Mario") ==  "¡Buenas tardes Mario!"


# Test greetings in the night
def test_patched_greetingsNight(monkeypatch):
    monkeypatch.setenv('MYDATE', '08-27-2023 01:32:43')
    assert greetings("George") ==  "¡Buenas noches George!"


# Test reverse word
def test_reverse_1():
	assert reverse("patata") == "atatap" 
def test_reverse_2():
	assert reverse("") == "" 
def test_reverse_3():
	assert reverse("arañara") == "arañara" 


# Test verify palindrome
def test_palindrome_1():
	assert palindrome("patata") == "" 
def test_palindrome_2():
	assert palindrome("") == "¡Bonita palabra!" 
def test_palindrome_3():
	assert palindrome("arañara") == "¡Bonita palabra!" 

# Test stoping program
def test_stop():
	assert stop("Carlos") == "Adios Carlos"