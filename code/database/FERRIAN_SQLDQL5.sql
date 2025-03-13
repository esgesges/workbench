-- Elencare tutti i pazienti che hanno effetuato una visita
select p.Cognome, p.Nome
from Paziente p
join Visita v on p.Id = v.IdPaziente

-- Elencare tutti i pazienti che NON hanno effetuato una visita
select p.Cognome, p.Nome
from Paziente p
inner join Visita v on p.Id = v.IdPaziente
where v.IdPaziente is null

-- Elencare le città di provenienza dei pazienti (citarle una sola volta)
select distinct p.Prov
from Paziente p

-- Elencare cognome, nome e sesso dei pazienti con differenza di pressione inferiore ai 40 mmHg
select p.Nome, p.Cognome, p.Sesso
from Paziente p
join Visita v on p.Id = v.IdPaziente
where (v.PressioneMax - v.PressioneMin) < 40

-- Elencare cognome, sesso e peso dei pazienti con peso compreso tra 60 e 80 Kg di Verona
select p.Nome, p.Cognome, p.Sesso, v.Peso
from Paziente p
join Visita v on p.Id = v.IdPaziente
where v.Peso < 80 and v.peso > 60

-- Elencare cognome, Sesso, anno di nascita, glicemia dei pazienti con problemi di diabete (glicemia > 110) nell'anno 2024
select p.Cognome, p.Sesso, year(p.DataNascita), v.Glicemia
from Paziente p
join Visita v on p.Id = v.IdPaziente
where v.Glicemia > 110 and year(v.Data) = 2024
-- Fornire il peso medio per genere di paziente
SELECT P.Sesso, AVG(V.Peso) AS PesoMedio
FROM Paziente P
JOIN Visita V ON P.Id = V.IdPaziente
GROUP BY P.Sesso;
-- Fornire il numero di pazienti visitati in nelle varie Asl ciascun anno 
SELECT P.CodASL, YEAR(V.Data) AS Anno, COUNT(DISTINCT P.Id) AS NumeroPazienti
FROM Paziente P
JOIN Visita V ON P.Id = V.IdPaziente
GROUP BY P.CodASL, YEAR(V.Data);
-- Elencare, per ogni provincia, il numero dei pazienti trovati con differenza di pressione maggiore ai 40 mmHg
SELECT P.Prov, COUNT(DISTINCT P.Id) AS NumeroPazienti
FROM Paziente P
JOIN Visita V ON P.Id = V.IdPaziente
WHERE (V.PressioneMax - V.PressioneMin) > 40
GROUP BY P.Prov;

ALTER TABLE Paziente
ADD CONSTRAINT Paziente