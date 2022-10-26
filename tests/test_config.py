import pytest
import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

TARGET_range = {
    "min": 3.0,
    "max": 8.0
}
input_data = {
    "correct_range":
    {

        "fixed_acidity": 5,
        "volatile_acidity": 0.5,
        "citric_acid": 0.99,
        "residual_sugar": 14,
        "chlorides": 0.5,
        "free_sulfur_dioxide": 5,
        "total_sulfur_dioxide": 75,
        "density": 1,
        "pH": 3,
        "sulphates": 1,
        "alcohol": 9

    },
    "incorrect_range":
    {

        "fixed_acidity": 5,
        "volatile_acidity": 0.5,
        "citric_acid": 0.99,
        "residual_sugar": 14,
        "chlorides": 0.5,
        "free_sulfur_dioxide": 999,
        "total_sulfur_dioxide": 75,
        "density": 1,
        "pH": 3,
        "sulphates": 1,
        "alcohol": 9
    }
}


def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert TARGET_range["min"] <= res <= TARGET_range["max"]


def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert TARGET_range["min"] <= res["response"] <= TARGET_range["max"]
