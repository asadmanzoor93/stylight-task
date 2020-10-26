# Stylight coding assessment - Budget notifications
The current feature request revolves around notifying shops when their monthly expenditure reaches certain thresholds. We want to notify shops when they reach 50% of the current month's budget. Once they reach 100% of the current month's budget, the shops should be notified again and set to _offline_.

## Schema Update
The given database schema consists of two tables: Shops and budgets.

## Schema
The given database schema consists of two tables: Shops and budgets.

### Shops
The table `t_shops` holds master data about all the shops in our system.

* `a_id` and `a_name` should be self-explanatory.

* `a_online`: Specifies, whether a shop's products are currently being listed on the Stylight website. `1` means they are listed, `0` means they aren't.

### Budgets
The table `t_budgets` holds all shops' monthly budgets.

* `a_shop_id`: Signifies, which shop the budget is associated with.

* `a_budget_amount`: Signifies the monetary value a shop is willing to spend with Stylight in a given month.

* `a_amount_spent`: Represents how much money the shop has spent in that month.

* `a_month`: Signifies the month a budget is valid for. The _day_ component of the date is irrelevant and by convention always set to 1.

* `notification`: Signifies, 50% budget threshold notification is generated for shop.

The amounts spent for the current month are continously updated until the month ends. Assume a part of the system is already doing that. You may assume all monetary values are in the same currency.


## Setup

Executing `db.sql` followed by `migration.sql` should result your intended database schema.

Install requirements: `pip install -r requirements.txt`

To execute task use the following command:`python task.py`
