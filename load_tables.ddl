INSERT INTO FoodItems VALUES (001,1), (002,2), (003,3), (004,4), (005,5) ;

INSERT INTO Ticket VALUES (1001,0,NULL), (1002,0,NULL), (1003,0,NULL);

INSERT INTO Assigned VALUES
  (1001,005,1),
  (1002,001,2),
  (1002,002,1),
  (1003,004,1),
  (1003,001,2),
  (1003,002,1);

-- To find ticket price
-- SELECT SUM(F.PRICE * NUM)
-- FROM FoodItems F, (
--   SELECT FoodID, Num
--   FROM Assigned AT
--   WHERE AT.TicketID = [TicketID]
-- ) Purchases
-- WHERE F.FoodID = Purchases.FoodID

-- SELECT SUM(F.PRICE * NUM) FROM FoodItems F, ( SELECT FoodID, Num FROM Assigned AT WHERE AT.TicketID = 1001 ) Purchases WHERE F.FoodID = Purchases.FoodID;
