import os
import sys
import pandas as pd
from Give_Me_Some_Credit.logger import logging
from Give_Me_Some_Credit.util.util import load_object
from Give_Me_Some_Credit.exception import CreditException


class DefaultData:
    def __init__(
        self,
        RevolvingUtilizationOfUnsecuredLines: int,
        age: int,
        NumberOfTime30_59DaysPastDueNotWorse: float,
        DebtRatio: float,
        MonthlyIncome: float,
        NumberOfOpenCreditLinesAndLoans: int,
        NumberOfTimes90DaysLate: int,
        NumberRealEstateLoansOrLines: int,
        NumberOfTime60_89DaysPastDueNotWorse: int,
        NumberOfDependents: float,
        SeriousDlqin2yrs: int = None,
    ):
        try:
            self.RevolvingUtilizationOfUnsecuredLines = (
                RevolvingUtilizationOfUnsecuredLines
            )
            self.age = age
            self.NumberOfTime30_59DaysPastDueNotWorse = (
                NumberOfTime30_59DaysPastDueNotWorse
            )
            self.DebtRatio = DebtRatio
            self.MonthlyIncome = MonthlyIncome
            self.NumberOfOpenCreditLinesAndLoans = NumberOfOpenCreditLinesAndLoans
            self.NumberOfTimes90DaysLate = NumberOfTimes90DaysLate
            self.NumberRealEstateLoansOrLines = NumberRealEstateLoansOrLines
            self.NumberOfTime60_89DaysPastDueNotWorse = (
                NumberOfTime60_89DaysPastDueNotWorse
            )
            self.NumberOfDependents = NumberOfDependents
            self.SeriousDlqin2yrs = SeriousDlqin2yrs
        except Exception as e:
            raise CreditException(e, sys) from e

    def get_credit_input_dataframe(self):
        try:
            credit_input_dict = self.get_credit_data_as_dict()
            return pd.DataFrame(credit_input_dict)
        except Exception as e:
            raise CreditException(e, sys) from e

    def get_credit_data_as_dict(self):
        try:
            input_data = {
                "RevolvingUtilizationOfUnsecuredLines": [
                    self.RevolvingUtilizationOfUnsecuredLines
                ],
                "age": [self.age],
                "NumberOfTime30_59DaysPastDueNotWorse": [
                    self.NumberOfTime30_59DaysPastDueNotWorse
                ],
                "DebtRatio": [self.DebtRatio],
                "MonthlyIncome": [self.MonthlyIncome],
                "NumberOfOpenCreditLinesAndLoans": [
                    self.NumberOfOpenCreditLinesAndLoans
                ],
                "NumberOfTimes90DaysLate": [self.NumberOfTimes90DaysLate],
                "NumberRealEstateLoansOrLines": [self.NumberRealEstateLoansOrLines],
                "NumberOfTime60_89DaysPastDueNotWorse": [
                    self.NumberOfTime60_89DaysPastDueNotWorse
                ],
                "NumberOfDependents": [self.NumberOfDependents],
            }
            return input_data
        except Exception as e:
            raise CreditException(e, sys) from e


class DefaultPredictor:
    def __init__(self, model_dir):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise CreditException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise CreditException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            default_probability = model.predict_proba(X)[:, 1]
            return default_probability
        except Exception as e:
            raise CreditException(e, sys) from e