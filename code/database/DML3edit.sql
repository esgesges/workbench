CREATE TABLE Studente(
    ID_studente integer UNIQUE not null,
    Cognome varchar(32) not null,
    Nome varchar(32) not null,
    Sesso char not null,
    DataNascita date not null,
    Classe integer not null,
    Sezione varchar(32) not null,
    primary key (ID_studente)
);

CREATE TABLE Aula(
    CodAula integer not null,
    Classe integer not null,
    Sezione varchar(32),
    primary key (CodAula)
);

CREATE TABLE Materia (
    ID_Materia INT PRIMARY KEY,
    Materia VARCHAR(50) NOT NULL
);

CREATE TABLE Verifica (
    ID_Verifica INT PRIMARY KEY,
    DataVerifica DATE NOT NULL,
    ID_Materia INT NOT NULL,
);

CREATE TABLE Voto (
    ID_Verifica INT NOT NULL,
    ID_Studente INT NOT NULL,
    Voto INT NOT NULL,
    PRIMARY KEY (ID_Verifica, ID_Studente),
);

INSERT INTO Materia (IDMateria, Materia) VALUES
(1, 'Matematica'),
(2, 'Fisica'),
(3, 'Storia'),
(4, 'Informatica'),
(5, 'Chimica');

INSERT INTO Verifica (IdVerifica, DataVerifica, IdMateria) VALUES
(1, '2024-02-01', 1),
(2, '2024-02-05', 2),
(3, '2024-02-10', 3),
(4, '2024-02-15', 4),
(5, '2024-02-20', 5);

INSERT INTO Voto (IdVerifica, IdStudente, Voto) VALUES
(1, 101, 8.5),
(1, 102, 7.0),
(2, 103, 6.5),
(3, 104, 9.0),
(4, 105, 8.0);

SELECT count(*) AS numero_voti
FROM Voto v
JOIN Verifica ve ON v.IdVerifica = ve.IdVerifica
JOIN Studente st ON v.IdStudente = st.ID_studente
WHERE YEAR(ve.DataVerifica) = 2025 AND st.Classe = 5 AND st.Sezione = "AII"