import logging

from databases import update_shop_status, update_notification_status


def notify_shop(shop_name, percentage):
    """
    Notify the Shop about monthly expenditure threshold
    :param shop_name: Name of Shop to be notified
    :param percentage: Expense threshold percentage reached
    :return: None
    """
    logging.warning('{0}: Your monthly expenditure crossed {1}% thresholds'.format(shop_name, percentage))


def validate_expense_threshold(cursor, shop):
    """
    Validate expenses of Shop
    :param cursor: Database cursor
    :param shop: Shop data item
    :return: None
    """
    expense = round((shop['a_amount_spent'] / shop['a_budget_amount']) * 100, 1)

    if expense >= 100 and shop['notification'] == 0:
        update_shop_status(cursor, shop['a_id'], 1)
        update_notification_status(cursor, shop['a_id'], 0)
        notify_shop(shop['a_name'], 100)
    elif expense >= 50 and shop['notification'] == 0:
        update_notification_status(cursor, shop['a_id'], 1)
        notify_shop(shop['a_name'], 50)
