# Stylight coding assessment - Budget notifications
The current feature request revolves around notifying shops when their monthly expenditure reaches certain thresholds. We want to notify shops when they reach 50% of the current month's budget. Once they reach 100% of the current month's budget, the shops should be notified again and set to _offline_.

## Schema Update
The given database schema consists of two tables: Shops and budgets.

### Shops
The table `t_shops` holds master data about all the shops in our system.

* No change made.

### Budgets
The table `t_budgets` holds all shops' monthly budgets. A new `notification` field added.

* `notification`: Signifies, 50% budget threshold notification is generated for shop.

## Setup

Executing `db.sql` followed by `migration.sql` should result your intended database schema.

Install requirements: `pip install -r requirements.txt`

To execute task use the following command:`python task.py`
