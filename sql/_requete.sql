--
-- Disponibilité
--
SELECT *
FROM Hotel.Disponibilite
ORDER BY etage, libre_du, au, numero;

--
-- Chambre dispo
--
EXPLAIN SELECT *
FROM Hotel.Disponibilite
ORDER BY etage, libre_du, au, numero;

