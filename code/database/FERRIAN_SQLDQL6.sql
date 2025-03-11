-- A) Definizione delle chiavi primarie
ALTER TABLE proprietario ADD PRIMARY KEY (CodP);
ALTER TABLE assicurazione ADD PRIMARY KEY (CodAss);
ALTER TABLE sinistro ADD PRIMARY KEY (CodS);
ALTER TABLE auto ADD PRIMARY KEY (Targa);
ALTER TABLE autocoinvolte ADD PRIMARY KEY (CodS, Targa);

-- 1. Targa e Marca delle auto con cilindrata superiore a 1000 cc o potenza superiore a 50 CV
SELECT Targa, Marca
FROM auto
WHERE Cilindrata > 1000 OR Potenza > 50;

-- 2. Nome del proprietario e Targa delle auto con cilindrata superiore a 1600 cc oppure potenza superiore a 50 CV
SELECT p.Nome, a.Targa
FROM auto a
JOIN proprietario p ON a.CodP = p.CodP
WHERE a.Cilindrata > 1600 OR a.Potenza > 50;

-- 3. Prime 10 righe con Targa e Nome del proprietario delle auto con cilindrata > 1000 cc o potenza > 50 CV, assicurate presso Sara
SELECT a.Targa, p.Nome
FROM auto a
JOIN proprietario p ON a.CodP = p.CodP
JOIN assicurazione ass ON a.CodAss = ass.CodAss
WHERE (a.Cilindrata > 1000 OR a.Potenza > 50)
AND ass.NomeAss = 'Sara Assicurazioni'
ORDER BY p.Nome
LIMIT 10;

-- 4. Targa e Nome del proprietario delle auto assicurate presso SARA e coinvolte in sinistri dal 11/05/2019
SELECT DISTINCT a.Targa, p.Nome
FROM auto a
JOIN proprietario p ON a.CodP = p.CodP
JOIN assicurazione ass ON a.CodAss = ass.CodAss
JOIN autocoinvolte ac ON a.Targa = ac.Targa
JOIN sinistro s ON ac.CodS = s.CodS
WHERE ass.NomeAss = 'Sara Assicurazioni'
AND s.DataS >= '2019-05-11';

-- 5. Per ciascuna Assicurazione, il nome, la sede e il numero di auto assicurate
SELECT ass.NomeAss, ass.Sede, COUNT(a.Targa) AS NumeroAutoAssicurate
FROM assicurazione ass
LEFT JOIN auto a ON ass.CodAss = a.CodAss
GROUP BY ass.NomeAss, ass.Sede;

-- 6. Per ciascuna auto Fiat, la targa e il numero di sinistri in cui è stata coinvolta
SELECT a.Targa, COUNT(ac.CodS) AS NumeroSinistri
FROM auto a
LEFT JOIN autocoinvolte ac ON a.Targa = ac.Targa
WHERE a.Marca = 'Fiat'
GROUP BY a.Targa;

-- 7. Per ciascuna auto coinvolta in più di un sinistro, la targa, il nome dell’assicurazione e il totale dei danni
SELECT a.Targa, ass.NomeAss, SUM(ac.Importo) AS TotaleDanni
FROM auto a
JOIN assicurazione ass ON a.CodAss = ass.CodAss
JOIN autocoinvolte ac ON a.Targa = ac.Targa
GROUP BY a.Targa, ass.NomeAss
HAVING COUNT(ac.CodS) > 1;

-- 8. CodP e Nome dei proprietari con più di un'auto
SELECT p.CodP, p.Nome
FROM proprietario p
JOIN auto a ON p.CodP = a.CodP
GROUP BY p.CodP, p.Nome
HAVING COUNT(a.Targa) > 1;

-- 9. Targa delle auto che non sono state coinvolte in sinistri dopo il 12/05/2019
SELECT a.Targa
FROM auto a
LEFT JOIN autocoinvolte ac ON a.Targa = ac.Targa
LEFT JOIN sinistro s ON ac.CodS = s.CodS
WHERE a.Targa NOT IN (
    SELECT ac.Targa
    FROM autocoinvolte ac
    JOIN sinistro s ON ac.CodS = s.CodS
    WHERE s.DataS > '2019-05-12'
);

-- 10. CodS dei sinistri in cui non sono state coinvolte auto con cilindrata inferiore a 1300 cc
SELECT s.CodS
FROM sinistro s
WHERE NOT EXISTS (
    SELECT 1
    FROM autocoinvolte ac
    JOIN auto a ON ac.Targa = a.Targa
    WHERE a.Cilindrata < 1300 AND ac.CodS = s.CodS
);
