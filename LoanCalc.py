import math
import argparse

parser = argparse.ArgumentParser( description="Loan calc.")

parser.add_argument( "--type", choices=['annuity', 'diff'], required=True )
parser.add_argument( "--principal", type=int, help="Provide loan amount" )
parser.add_argument( "--periods", type=int )
parser.add_argument( "--interest", type=float )
parser.add_argument( "--payment", type=int )

try:
    if interest is None:
        print("Incorrect parameters")
    elif len(sys.argv) != 5:
        print("Incorrect parameters")
    elif type == "diff" and payment is not None:
        print("Incorrect parameters")
    elif type != "diff" and type != "annuity":
        print("Incorrect parameters")
except(TypeError, ValueError, NameError):
    print("Incorrect parameters")

args = parser.parse_args()
type_choice = args.type
principal_amount = args.principal
annuity_pay = args.payment
interest_rate = args.interest
months_number = args.periods
months_counter = int( 1 )
interest_calc = 0


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil( n * multiplier ) / multiplier


def month_calc(n):
    years = n // 12
    months = n % 12

    if months == 1 and years == 0:
        print( f'''It will take {months} month to repay the loan''' )
    elif months < 12 and years < 1:
        print( f'''It will take {months} months to repay the loan''' )
    elif months == 0 and years == 1:
        print( f'''It will take {years} year to repay the loan''' )
    elif years == 1 and months == 1:
        print( f'''It will take {years} year and {months} month to repay the loan''' )
    elif years == 1 and months > 1:
        print( f'''It will take {years} year and {months} months to repay the loan''' )
    elif years == 2 and months == 0:
        print( f'''It will take {years} years to repay the loan''' )
    elif 2 < years >= 1 and months > 1:
        print( f'''It will take {years} years and {months} months to repay the loan''' )
    elif years <= 2 and months == 1:
        print( f'''It will take {years} years and {months} month to repay the loan''' )
    elif years >= 2 and months == 1:
        print( f'''It will take {years} years and {months} month to repay the loan''' )
    elif years >= 2 and months > 1:
        print( print( f'''It will take {years} years and {months} months to repay the loan''' ) )



try:



    if type_choice == 'diff':
        add_all = 0
        interest_calc = interest_rate / (12 * 100)
        for i in range( months_number ):
            ordinary_annuity_result = math.ceil( principal_amount * (
                        (interest_calc * (1 + interest_calc) ** months_number) / (
                            (1 + interest_calc) ** months_number - 1)) )

            principal_amount_result = ordinary_annuity_result / (
                        (interest_calc * (1 + interest_calc) ** months_number) / (
                            (1 + interest_calc) ** months_number - 1))
            principal_amount_result = math.floor( principal_amount_result )

            diff_pay = (int( round_up( (principal_amount / months_number) + interest_calc * (
                        principal_amount - (principal_amount * (months_counter - 1)) / months_number) ) ))
            print( f'''Month {months_counter}: payment is {diff_pay}''' )
            months_counter += 1
            add_all = add_all + diff_pay

        overpay = int( add_all - principal_amount )
        print()
        print( f'''Overpayment = {overpay}''' )

    if type_choice == 'annuity':

        if principal_amount is not None and months_number is not None and interest_calc is not None:

            interest_calc = interest_rate / (12 * 100)
            ordinary_ann_result = math.ceil( principal_amount * (
                        (interest_calc * (1 + interest_calc) ** months_number) / (
                            (1 + interest_calc) ** months_number - 1)) )
            print( f'''Your annuity payment = {ordinary_ann_result}!''' )
            overpayment = (ordinary_ann_result * months_number) - principal_amount
            print( f'''Overpayment = {overpayment}''' )

        elif annuity_pay is not None and months_number is not None and interest_calc is not None:

            interest_calc = interest_rate / (12 * 100)
            principal_amount_result = annuity_pay / ((interest_calc * (1 + interest_calc) ** months_number) / (
                        (1 + interest_calc) ** months_number - 1))
            principal_amount_result = math.floor( principal_amount_result )
            print( f'''Your loan principal = {principal_amount_result}!''' )

        elif principal_amount is not None and annuity_pay is not None and interest_calc is not None:

            interest_calc = interest_rate / (12 * 100)
            number_periods = math.log( (annuity_pay / (annuity_pay - interest_calc * principal_amount)),
                                       1 + interest_calc )
            number_periods = math.ceil( number_periods )
            overpayment = (annuity_pay * number_periods) - principal_amount
            print( f'''Overpayment = {overpayment}''' )
            month_calc( number_periods )


except (ValueError, TypeError, Exception, AttributeError, argparse.ArgumentError):
    print('Incorrect parameters')


