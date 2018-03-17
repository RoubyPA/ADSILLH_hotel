--
-- Contraint function
--
CREATE FUNCTION Hotel.Dates_Debut_Fin_Correctes(integer, integer, date, date) 
  RETURNS boolean AS $$ 
SELECT NOT EXISTS (
  SELECT * 
  FROM Hotel.Reservations
  WHERE $1 = etage
    AND $2 = numero 
    AND $3 <= date_fin
    AND $4 >= date_debut)
$$ LANGUAGE SQL;

--
-- Contraint reservation date
--
ALTER TABLE Hotel.Reservations ADD CONSTRAINT DatesPossibles
  CHECK(Hotel.Dates_Debut_Fin_Correctes(etage, numero, date_debut, date_fin));

--
-- Contraint function
--
CREATE FUNCTION Hotel.EtageNumeroCorrects(integer, integer) 
  RETURNS boolean AS $$ 
SELECT ($1 = 1 AND $2 = 1)
  OR EXISTS (
  SELECT * 
  FROM Hotel.Chambres
  WHERE ($1 = Etage AND $2 = (Numero + 1))
     OR ($1 = (Etage + 1) AND $2 = 1))
$$ LANGUAGE SQL;

--
-- Contraint chambre
--
ALTER TABLE Hotel.Chambres ADD CONSTRAINT NumeroPossible
  CHECK(Hotel.EtageNumeroCorrects(Etage, Numero));
