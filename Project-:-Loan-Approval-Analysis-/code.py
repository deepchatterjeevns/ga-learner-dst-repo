# --------------
import pandas as pd
import numpy as np

bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

banks = bank.drop(['Loan_ID'], axis=1)
# Check for null values
print(banks.isnull().sum())

# Null Value treatment
bank_mode = banks.mode()
banks = banks.fillna(bank_mode)
print(banks.isnull().sum())

avg_loan_amount = pd.pivot_table(data=banks, index=['Gender', 'Married', 'Self_Employed'],values = 'LoanAmount', aggfunc='mean')

loan_approved_se = banks[(banks["Self_Employed"] == 'Yes') & (banks['Loan_Status'] == "Y")].count()[0]
loan_approved_nse = banks[(banks["Self_Employed"] == 'No') & (banks['Loan_Status'] == "Y")].count()[0]

# Loan_status = banks.shape[0]
Loan_Status = 614

percentage_se = (loan_approved_se / Loan_Status) * 100
percentage_nse = (loan_approved_nse / Loan_Status) * 100

loan_term = banks["Loan_Amount_Term"].apply( lambda months : months/12)

big_loan_term = len(loan_term[loan_term >= 25])

loan_groupby = banks.groupby(['Loan_Status'])

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()



































































