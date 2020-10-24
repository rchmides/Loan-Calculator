import math
import sys
import argparse


def diff_monthly(loan_principal, periods_number, loan_interest):
    loan_interest = loan_interest / 12 / 100
    overpayment = 0

    for month in range(1, periods_number + 1):
        monthly_payment = math.ceil(loan_principal / periods_number + loan_interest * (loan_principal - loan_principal *
                                                                                       (month - 1) / periods_number))
        print("Month {}: payment is {}".format(month, monthly_payment))
        overpayment += monthly_payment
    print("Overpayment =", overpayment - loan_principal)


def annuity_months(loan_principal, monthly_payment, loan_interest):
    loan_interest = loan_interest / 12 / 100

    months_number_1 = math.ceil(
        math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest))

    months_number = divmod(months_number_1, 12)

    if int(months_number[0]) != 0 and math.ceil(months_number[1]) != 0:
        if int(months_number[0]) != 1 and math.ceil(months_number[1]) != 1:
            print("It will take {} years and {} months to repay this loan!".format(int(months_number[0]),
                                                                                   math.ceil(months_number[1])))
        elif int(months_number[0]) == 1 and math.ceil(months_number[1]) == 1:
            print("It will take 1 year and 1 month to repay this loan!".format(int(months_number[0]),
                                                                               math.ceil(months_number[1])))
        elif int(months_number[0]) != 1 and math.ceil(math.ceil(months_number[1])) == 1:
            print("It will take {} years and 1 month to repay this loan!".format(int(months_number[0])))
        elif int(months_number[0]) == 1 and math.ceil(math.ceil(months_number[1])) != 1:
            print("It will take 1 year and {} months to repay this loan!".format(int(months_number[0])))
    elif math.ceil(months_number[0]) == 0:
        if math.ceil(months_number[1]) != 1:
            print("It will take {} months to repay this loan!".format(math.ceil(months_number[1])))
        else:
            print("It will take 1 month to repay this loan!")
    elif math.ceil(months_number[1]) == 0:
        if int(months_number[0]) != 1:
            print("It will take {} years to repay this loan!".format(int(months_number[0])))
        else:
            print("It will take 1 year to repay this loan!")

    overpayment = monthly_payment * months_number_1 - loan_principal
    print("Overpayment =", math.ceil(overpayment))


def annuity_monthly(loan_principal, periods_number, loan_interest):
    loan_interest = loan_interest / 12 / 100

    a = math.ceil(loan_principal * (loan_interest * pow(1 + loan_interest, periods_number)) / (
            pow(1 + loan_interest, periods_number) - 1))

    print("Your monthly payment = {}!".format(a))

    overpayment = a * periods_number - loan_principal
    print("Overpayment =", math.ceil(overpayment))


def annuity_loan(annuity_payment, periods_number, loan_interest):
    loan_interest = loan_interest / 12 / 100

    loan_principal = annuity_payment / (
            (loan_interest * pow(1 + loan_interest, periods_number)) / (pow(1 + loan_interest, periods_number) - 1))

    print("Your loan principal = {}!".format(int(loan_principal)))

    overpayment = annuity_payment * periods_number - loan_principal
    print("Overpayment =", math.ceil(overpayment))


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest
type = args.type

if len(sys.argv) < 4 or (type != "annuity" and type != "diff") or interest is None:
    print("Incorrect parameters")
elif type == "annuity":
    if payment is None:
        annuity_monthly(principal, periods, interest)
    elif principal is None:
        annuity_loan(payment, periods, interest)
    elif periods is None:
        annuity_months(principal, payment, interest)
elif type == "diff":
    if payment is not None:
        print("Incorrect parameters")
    else:
        diff_monthly(principal, periods, interest)

