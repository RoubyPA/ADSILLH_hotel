--
-- Disponibilité
--
SELECT *
FROM Hotel.Disponibilite
ORDER BY etage, libredu, au, numero;

--
-- Chambre dispo
--
EXPLAIN SELECT *
FROM Hotel.Disponibilite
ORDER BY etage, libredu, au, numero;
