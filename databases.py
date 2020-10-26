import mysql.connector

import settings


def create_connection():
    """
    Create Database Connection
    :return: Database connection object
    """
    return mysql.connector.connect(
        host=settings.HOST,
        user=settings.USER,
        passwd=settings.PASSWORD,
        database=settings.DATABASE,
        port=3306
    )


def get_online_shops_data(cursor):
    """
    Return all online shops data
    :return: query string
    """
    query = f"""
        SELECT 
            t_shops.a_id, t_shops.a_name, t_shops.a_online, t_budgets.a_budget_amount,
            t_budgets.a_amount_spent, t_budgets.notification
        FROM 
            t_budgets
        INNER JOIN 
            t_shops 
        ON
            t_budgets.a_shop_id=t_shops.a_id
        WHERE 
            t_shops.a_online='1'
        """

    cursor.execute(query)
    return cursor.fetchall()


def update_shop_status(cursor, shop_id, online_status=0):
    """
    Update shop active status
    :param cursor: Database cursor
    :param shop_id: Id of shop to be updated
    :param online_status: Active status of the shop
    :return: None
    """
    query = "UPDATE t_shops SET a_online = %s WHERE a_id = %s"
    params = (online_status, shop_id)
    cursor.execute(query, params)


def update_notification_status(cursor, shop_id, notification=0):
    """
    Update shop budget notification status
    :param cursor: Database cursor
    :param shop_id: Id of shop to be updated
    :param notification: Notification status
    :return: None
    """
    query = "UPDATE t_budgets SET notification = %s WHERE a_shop_id = %s"
    params = (notification, shop_id)
    cursor.execute(query, params)
