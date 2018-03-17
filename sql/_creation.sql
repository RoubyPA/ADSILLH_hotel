--
-- Create Hotel
--
CREATE SCHEMA Hotel;
SET search_path TO Hotel, public;

--
-- Chambres
--
CREATE TABLE Hotel.Chambres (
  etage integer NOT NULL CHECK(etage > 0),
  numero integer NOT NULL CHECK(numero > 0),
  tarif integer NOT NULL CHECK (tarif >= 0),
  PRIMARY KEY (etage, numero)
);

--
-- Connsommations
--
CREATE TABLE Hotel.Consommations (
  intitule text NOT NULL,
  prix real NOT NULL CHECK(prix > 0),
  PRIMARY KEY (intitule)
);

--
-- Clients
--
CREATE TABLE Hotel.Clients (
  num_client serial NOT NULL,
  nom text NOT NULL,
  prenom text NOT NULL,
  adresse text NOT NULL,
  PRIMARY KEY (num_client),
  UNIQUE (nom, prenom, adresse)
);

--
-- Consommation clients
--
CREATE TABLE Hotel.Consommations_Clients (
  num_client serial NOT NULL,
  jour date NOT NULL,
  intitule text NOT NULL,
  quantite integer NOT NULL CHECK (quantite > 0),
  PRIMARY KEY (num_client, jour, intitule),
  FOREIGN KEY (num_client) REFERENCES Hotel.Clients(num_client),
  FOREIGN KEY (intitule) REFERENCES Hotel.Consommations(intitule)
);

--
-- Reservations
--
CREATE TABLE Hotel.Reservations (
  etage integer NOT NULL,
  numero integer NOT NULL,
  date_debut date NOT NULL,
  date_fin date NOT NULL,
  num_client serial NOT NULL,
  PRIMARY KEY (etage, numero, date_debut),
  UNIQUE (etage, numero, date_fin),
  FOREIGN KEY (num_client) REFERENCES Hotel.Clients(num_client),
  FOREIGN KEY (etage, numero) REFERENCES Hotel.Chambres(etage, numero),
  CHECK (date_debut < date_fin)
);
