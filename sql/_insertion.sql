--
-- Chambre
--
INSERT INTO Hotel.Chambres VALUES(1,1,50);
INSERT INTO Hotel.Chambres VALUES(1,2,50);
INSERT INTO Hotel.Chambres VALUES(1,3,50);
INSERT INTO Hotel.Chambres VALUES(1,4,50);
INSERT INTO Hotel.Chambres VALUES(1,5,50);
INSERT INTO Hotel.Chambres VALUES(1,6,50);
INSERT INTO Hotel.Chambres VALUES(1,7,50);
INSERT INTO Hotel.Chambres VALUES(1,8,50);
INSERT INTO Hotel.Chambres VALUES(1,9,50);
INSERT INTO Hotel.Chambres VALUES(2,1,150);
INSERT INTO Hotel.Chambres VALUES(2,2,150);
INSERT INTO Hotel.Chambres VALUES(2,3,150);
INSERT INTO Hotel.Chambres VALUES(2,4,150);
INSERT INTO Hotel.Chambres VALUES(2,5,150);
INSERT INTO Hotel.Chambres VALUES(2,6,150);
INSERT INTO Hotel.Chambres VALUES(2,7,200);
INSERT INTO Hotel.Chambres VALUES(2,8,200);
INSERT INTO Hotel.Chambres VALUES(2,9,220);
INSERT INTO Hotel.Chambres VALUES(3,1,150);
INSERT INTO Hotel.Chambres VALUES(3,2,150);
INSERT INTO Hotel.Chambres VALUES(3,3,150);
INSERT INTO Hotel.Chambres VALUES(3,4,150);
INSERT INTO Hotel.Chambres VALUES(3,5,150);
INSERT INTO Hotel.Chambres VALUES(3,6,150);
INSERT INTO Hotel.Chambres VALUES(3,7,150);
INSERT INTO Hotel.Chambres VALUES(3,8,150);
INSERT INTO Hotel.Chambres VALUES(3,9,150);
INSERT INTO Hotel.Chambres VALUES(4,1,1500);

--
-- Consomation
--
INSERT INTO Hotel.Consommations VALUES('Pepsi-Cola',2);
INSERT INTO Hotel.Consommations VALUES('Sex on the beach',5);
INSERT INTO Hotel.Consommations VALUES('Whisky-baby',9);
INSERT INTO Hotel.Consommations VALUES('Sauna',11);

--
-- Clients
--
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Duchemin','Albert','10 rue des Jumeaux à Strasbourg', 'duchemin.albert@mail.com', '5f4dcc3b5aa765d61d8327deb882cf99');
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Duchemin','Albert','13 rue de la Paix à Saillans (33141)', 'duchemin.albert@gmail.com', '5f4dcc3b5aa765d61d8327deb882cf99');
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Dupont','Jean','13 rue de la Paix à Saillans (33141)', 'dupont.jean@gmail.com', '5f4dcc3b5aa765d61d8327deb882cf99');
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Dupond','Jean','13 rue de la Paix à Saillans (33141)', 'dupond.jean@gmail.com', '5f4dcc3b5aa765d61d8327deb882cf99');
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Martin','Albert','13 rue de la Paix à Saillans (33141)', 'martin.du.33@gmail.com', '5f4dcc3b5aa765d61d8327deb882cf99');
INSERT INTO Hotel.Clients
  VALUES(DEFAULT,'Smith','Winston','1984 rue de la Paix à Saillans (33141)', 'smith.winston@oseania.com', '5f4dcc3b5aa765d61d8327deb882cf99');

--
-- Reservations
--
INSERT INTO Hotel.Reservations
  VALUES(1,2,'2017-02-26','2017-03-03',2);
INSERT INTO Hotel.Reservations
  VALUES(1,2,'2017-03-16','2017-03-21',2);
INSERT INTO Hotel.Reservations
  VALUES(1,2,'2017-04-16','2017-04-21',2);
INSERT INTO Hotel.Reservations
  VALUES(1,2,'2017-05-16','2017-05-21',2);
INSERT INTO Hotel.Reservations
  VALUES(1,4,'2017-02-26','2017-03-03',3);
INSERT INTO Hotel.Reservations
  VALUES(2,1,'2017-03-16','2017-03-21',3);
INSERT INTO Hotel.Reservations
  VALUES(2,7,'2017-04-16','2017-04-21',3);
INSERT INTO Hotel.Reservations
  VALUES(3,2,'2017-05-16','2017-05-21',3);
