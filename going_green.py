# going_green.py
# Exercises selected: Lab 9.5 - Going Green
# Name of program: Going Green
# Description of program: This program has the user enter energy bills for
#   each month of the year prior to going green and the year after going
#   green.  It then reports the entered values and calculated savings.
#
# Ivan Boatwright
# March 24, 2016

def main(debug=False):
    # Declare local variables/constants
    endProgram = 'no'
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')
    HEADERS = ('SAVINGS', 'NOT GREEN', 'GONE GREEN', '  MONTH')


    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    # The program will continue looping until the user sets
    #   endProgram == 'yes' when prompted.
    while endProgram.lower() in ['no', 'n', '']:
        notGreenCost = []
        goneGreenCost = []
        savings = []
        report = ''
        headDesign = '{0:^4}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
                     '{0:^6}{{3:<8}}\n'.format('')
        reportDesign = '{0:^3}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
                       '{0:^8}{{3:<8}}\n'.format('')

        if not debug:
            # Function calls.
            get_not_green(notGreenCost, MONTHS)
            get_gone_green(goneGreenCost, MONTHS)
        else:
            notGreenCost = generate_numbers()
            goneGreenCost = generate_numbers()

        energy_saved(notGreenCost, goneGreenCost, savings)

        # Generate a printable report.
        report = get_report(HEADERS[0], HEADERS, headDesign, reportDesign,
                            savings, notGreenCost, goneGreenCost, MONTHS)

        # Display the report.
        display_results(report)

        # User is given the option to end the program loop by entering 'yes'.
        #   The user can enter 'no' or press enter to start a new loop.
        endProgram = input("Do you want to end program? yes or (n)o\n    >>>")

        # If the user enters anything other than 'yes', 'no' or enter this
        #   loop requests new/valid input.
        while endProgram.lower() not in ['yes', 'y', 'no', 'n', '']:
            print('Error: Invalid entry.')
            endProgram = input("Do you want to end program? yes or "
                               "(n)o\n    >>> ")
    # End main and say good-bye.
    print('{:>64}'.format('fin.'))
    return None

# todo: add welcome message for fluffy()
# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Going Green program.\n'
          '.\n')
    return None


# Requests the user input the notGreenCosts.
def get_not_green(ngc, months):
    monthly_values(months, 'NOT GREEN energy costs', ngc)
    return None


# Requests the user input the notGreenCosts.
def get_gone_green(ggc, months):
    monthly_values(months, 'GONE GREEN energy costs', ggc)
    return None


# Calculate the savings per month. explain
def energy_saved(ngc, ggc, sav):
    [sav.append(x[0] - x[1]) for x in zip(ngc, ggc)]
    return None


# Iterates through the list of months.  Each iteration has the user input
#   a value for that month.  The value is assigned to the reference array
#   with the same index as that month.
def monthly_values(months, name, vArray):
    print('{}\nPlease enter the {} for each month.\n'.format('_' * 79, name))
    for month in months:
        vArray.append(int(input('{}:  '.format(month))))
    return None


# comments
def moneyfy(*vArs):
    for vA in vArs:
        vA[:] = ['${}'.format(v) if v>0 else '-${}'.format(abs(v)) for v in vA]
    return None


# Takes a title, a set of headers, a merged parallel array and
#   a format string and returns a print friendly string.
def tablefy(title, headers, hdesign, design, data):
    title = '{0:-<62}\n\n{1:^67}\n{0:_<62}\n'.format('    ', title)
    head = hdesign.format(*headers)
    division = '{0:4}{0:_<58}\n'.format('')
    body = ''.join([design.format(j[0], j[1], j[2], j[3]) for j in data])
    return '{}{}{}{}'.format(title, head, division, body)


# comments
def get_report(title, headers, hdesign, design, *data):
    # Using moneyfy to turn all the integer values into strings with
    #   dollar signs.
    moneyfy(*data[:-1])

    # comments
    return tablefy(title, headers, hdesign, design, zip(*data))


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(report):
    print(report)
    return None

################DEBUG CODE##################
def generate_numbers(rMin=1, rMax=999, xNums=12):
    from random import sample
    # Uses the sample function from the random module to generate a list of
    #   integers.  The range function is used with the min and max variables
    #   to set the possible integer values generated.
    return sample(range(rMin, rMax), xNums)

main(True)