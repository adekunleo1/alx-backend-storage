-- script for trigger that decreases the quantity of an item after adding
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity -NEW.number WHERE name = NEW.item_name;
