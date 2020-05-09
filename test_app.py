import pytest
import tornado.web
from weatherapi import weather

airport= 'Williams Ag Airport'
def test_case1():
    assert weather(airport) == 'The Williams Ag Airport is a small_airport, which is belongs to Biggs. The current weather of the airport is clear sky, and the temperature is 299.04.              The pressure is 1014 meanwhile the humidity is 31.              In addition, the wind speed is 1.49              with 253 degrees.'
