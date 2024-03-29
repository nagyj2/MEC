-- To run: mysql -u root -p mec < ~/path/to/folder/file.ddl

-- USE MEC;

DROP TABLE IF EXISTS Assigned;
DROP TABLE IF EXISTS FoodItems;
DROP TABLE IF EXISTS Ticket;

CREATE TABLE IF NOT EXISTS FoodItems(
  FoodID int NOT NULL AUTO_INCREMENT,
  Price int NOT NULL,
  PRIMARY KEY (FoodID)
);

CREATE TABLE IF NOT EXISTS Ticket(
  TicketID int NOT NULL AUTO_INCREMENT,
  Status int,
  Price int,
  PRIMARY KEY (TicketID)
);

CREATE TABLE IF NOT EXISTS Assigned(
  TicketID int NOT NULL,
  FoodID int NOT NULL,
  Num int NOT NULL,
  PRIMARY KEY (TicketID, FoodID),
  CONSTRAINT FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (FoodID) REFERENCES FoodItems(FoodID) ON DELETE CASCADE
);
