from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

if __name__ == '__main__':
    print('Current date is:' + str(datetime.datetime.now()))
    get_employees()
    calculate_salary()