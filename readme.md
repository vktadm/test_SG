### 1. Проектирование БД
[ER-диаграмма:](https://github.com/vktadm)
| Критерий               |Вариант 1|Вариант 2|
|------------------------|---|---|
| Удобство использования |||
| Расширяемость          |||
| Целостность            |||
|Производительность|||
Моя оценка:
***
### 2. SQL запросы
#### Task 1
БД SQLite
```sql
SELECT strftime('%d', StartDateTime) AS day_month, count(*)
FROM Receptions
WHERE strftime('%Y', StartDateTime) = '2015'
GROUP BY day_month;"
```
#### Task 2
```
# Task 2 - 1
SELECT DISTINCT ID_Patient AS pt, ID_Doctor
FROM Receptions
WHERE StartDateTime = (
    SELECT max(StartDateTime)
    FROM Receptions
    WHERE ID_Patient = pt);

# Task 2 - 2
SELECT DISTINCT ID_Patient AS pt, ID_Doctor
FROM Receptions
WHERE StartDateTime = (
    SELECT StartDateTime
    FROM Receptions
    WHERE ID_Patient = pt
    ORDER BY StartDateTime DESC
    LIMIT 1);

# Task 2 - 3
SELECT DISTINCT ID_Patient, ID_Doctor
FROM Receptions
WHERE StartDateTime IN (
    SELECT max(StartDateTime)
    FROM Receptions
    GROUP BY ID_Patient);
```
Дублирование 
***
### 3.2 Web-приложение
[Web-app](https://github.com/vktadm)
