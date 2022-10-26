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
    },
    "incorrect_col":
    {

        "fixed_acidity": 5,
        "volatile_acidity": 0.5,
        "citric_acid": 0.99,
        "residual_sugar": 14,
        "chlorides": 0.5,
        "free_sulphur_dioxide": 999,
        "total_suphur_dioxide": 75,
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


def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)


def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message


def test_form_response_incorrect_col(data=input_data["incorrect_col"]):
    with pytest.raises(prediction_service.prediction.NotInCol):
        res = form_response(data)


def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCol().message
