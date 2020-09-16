### Задание

Написать Web API которое позволит класть в СУБД Postgres SQL данные по следующим параметрам. 
Параметры: 
1. Номер билета (***формат 000***)
2. Дата (***формат dd.mm.yyyy***)
3. Время (***Формат MM:HH***)
Для демонстрации будет достаточно веб формы которая будет собирать вышеописанные данные.

Для демонстрации записи в СУБД достаточно отображения таблицы любым удобным способом.

Исключить дублирование данных.

### Результат
Реализована web-форма и api для создания записей о билетах.
Переменные окружения необходимые для запуска:  
**DATABASE_URL** в формате 'posgresql://login:password@host/dbname' ***ИЛИ***:
1. **PSQL_LOGIN** - логин пользователя postgresql
2. **PSQL_PASS** - пароль пользователя postgresql
3. **PSQL_HOST** - хост пользователя postgresql (по умолчанию localhost)
4. **TICKET_DB** - имя базы данных для хранения информации о билетах

Скрипт для быстрого развертывания и запуска:  
```
git clone https://github.com/gwindblaids/DRONESELFIE.git
cd first_task
*задаем значение переменным окружения. К примеру:*
export PSQL_LOGIN='ed'
python3 -m venv ed-tickets
source ed-tickets/bin/activate
pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

flask run
```
 
Пример запроса для тестов api:  
`http://localhost:5000/?number=11&date=22.03.1992&time=22:15`
