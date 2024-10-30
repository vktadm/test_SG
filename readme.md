### 1. Проектирование БД
1. [Реляционная модель](https://github.com/vktadm/test_SG/blob/master/ER.png)
2. NoSQL (документо-ориентированная)
```
// Сотрудники
{
  "id": ,
  "patientId": [],
  "firstname": "",
  "lastname": "",
  "surname": "",
  "date_birth": ,
  "phone": "",
  "inn_number": ""
}

// Пациенты
{
  "id": ,
  "workerId": [],
  "firstname": "",
  "lastname": "",
  "surname": "",
  "date_birth": ,
  "phone": "",
  "medical_card": ""
}
```
| Критерий               | Реляционная     | NoSQL                                        |
|------------------------|-----------------|----------------------------------------------|
| Удобство использования |                 | Более гибкая работа с данными                |
| Расширяемость          |                 | Приемущество в горизонтальном маштабировании |
| Целостность            | Требования ACID |                                              |
| Производительность     |                 | Выше                                         |


**Мое мнение:** довольно сложно оценить, какой подход будет
являться наиболее удачным, тк опыта работы с NoSQl БД я не имела. Но могу предположить, что для сети стомотологий
целесообразнее выбрать NoSQl из-за легкого горизонтального масштабирования.
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
***
### 3.2 Web-приложение
1. [Подготовка данных](https://github.com/vktadm/test_SG/blob/master/WebApp/webapp/main/prepare_data.py)
2. [Представления](https://github.com/vktadm/test_SG/blob/master/WebApp/webapp/main/views.py)
3. [Шаблоны](https://github.com/vktadm/test_SG/tree/master/WebApp/webapp/main/templates)
