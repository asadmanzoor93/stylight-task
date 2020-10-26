from mysql.connector import Error

import databases
from utilities import validate_expense_threshold


def run():
    """
    Execute Budget Notification Process
    :return: None
    """
    try:
        conn = databases.create_connection()
        cursor = conn.cursor(buffered=True, dictionary=True)
        shops_data = databases.get_online_shops_data(cursor)

        for shop in shops_data:
            validate_expense_threshold(cursor, shop)

        conn.commit()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
