ALTER TABLE t_budgets
ADD COLUMN notification BOOLEAN NULL DEFAULT 0 AFTER a_amount_spent;
