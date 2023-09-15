SELECT COUNT(*) AS estudiantes_mayor30 FROM estudiantes
WHERE edad > 30;

SELECT * FROM estudiantes WHERE color preferido <> 'amarillo';

SELECT * FROM estudiantes WHERE edad >= 50 AND edad <= 60;

DELETE * FROM estudiantes where fecha <> '2023-01-10'

DROP TABLE estudiantes;
