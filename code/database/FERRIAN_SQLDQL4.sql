CREATE TABLE Materia(
    ID_Materia INTEGER not null PRIMARY KEY,
    Materia varchar(50) not null,
)
CREATE TABLE Verifica(
    ID_Verifica INTEGER not null PRIMARY KEY,
    Data_verifica date not null,
    ID_Materia INTEGER not null,
)
CREATE TABLE Voto(
    ID_Verifica INTEGER not null,
    ID_Studente INTEGER not null,
    Voto INTEGER not null,
)
INSERT INTO Materia (ID_Vateria, Materia)
VALUES 
    (1, 'Matematica'),
    (2, 'Italiano'),
    (3, 'Storia'),
    (4, 'Inglese'),
    (5, 'Scienze');

INSERT INTO Verifica (ID_Verifica, Data_verifica, ID_Materia)
VALUES 
    (1, '2025-01-20', 1),
    (2, '2025-01-22', 2),
    (3, '2025-01-24', 3),
    (4, '2025-01-26', 4),
    (5, '2025-01-28', 5);

INSERT INTO Voto (ID_Verifica, ID_Studente, Voto)
VALUES 
    (1, 1, 8),
    (1, 2, 7),
    (2, 1, 6),
    (2, 3, 9),
    (3, 2, 8),
    (4, 3, 7),
    (5, 1, 10),
    (5, 2, 9);


SELECT DISTINCT ID_Studente
FROM Voto v
JOIN Verifica ve ON v.ID_Verifica = ve.ID_Verifica
JOIN Materia m ON ve.ID_Materia = m.ID_Vateria
WHERE m.Materia = 'Italiano' AND YEAR(ve.Data_verifica) = 2025;

SELECT COUNT(*) AS Numero_Voti
FROM Voto v
JOIN Studente s ON v.ID_Studente = s.ID_Studente
WHERE s.Classe = '5Aii';

SELECT v.Voto, m.Materia, ve.Data_verifica
FROM Voto v
JOIN Verifica ve ON v.ID_Verifica = ve.ID_Verifica
JOIN Materia m ON ve.ID_Materia = m.ID_Vateria
JOIN Studente s ON v.ID_Studente = s.ID_Studente
WHERE s.Cognome = 'A%' AND s.Classe = '5%';

SELECT COUNT(*) AS Numero_Voti
FROM Voto v
JOIN Verifica ve ON v.ID_Verifica = ve.ID_Verifica
WHERE YEAR(ve.Data_verifica) = YEAR(CURRENT_DATE);

SELECT m.Materia
FROM Materia m
LEFT JOIN Verifica ve ON m.ID_Vateria = ve.ID_Materia
LEFT JOIN Voto v ON ve.ID_Verifica = v.ID_Verifica
WHERE v.ID_Verifica IS NULL;

SELECT AVG(v.Voto) AS Media_Voti
FROM Voto v
JOIN Verifica ve ON v.ID_Verifica = ve.ID_Verifica
JOIN Studente s ON v.ID_Studente = s.ID_Studente
WHERE s.Cognome = 'Bianchi' AND YEAR(ve.Data_verifica) = 2025;


ALTER TABLE Verifica
ADD CONSTRAINT ID_Materia
FOREIGN KEY (ID_Materia)
REFERENCES Materia(ID_Materia)

ALTER TABLE Voto
ADD CONSTRAINT ID_Verifica
FOREIGN KEY (ID_Verifica)
REFERENCES Verifica(ID_Verifica)
