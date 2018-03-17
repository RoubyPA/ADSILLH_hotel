--
-- Diponibilite
--
CREATE VIEW Hotel.Disponibilite AS
SELECT Etage, LibreDu, Au, Numero
FROM (SELECT Etage, Numero, GREATEST(date_fin, current_date) AS LibreDu, Min(date_debut) As Au
      FROM   (SELECT Etage, Numero, date_debut
              FROM   Hotel.Reservations
                UNION
              SELECT Etage, Numero, current_date+3650
              FROM   Hotel.Chambres) AS DebutOccupation 
        NATURAL JOIN 
             (SELECT Etage, Numero, date_fin
              FROM   Hotel.Reservations
                UNION
              SELECT Etage, Numero, 'now'
              FROM   Hotel.Chambres) AS FinOccupation
      WHERE  date_debut > date_fin
      GROUP BY Etage, Numero, date_fin
      HAVING Min(date_debut) > current_date) AS NonOccupation
  NATURAL JOIN Hotel.Chambres;

