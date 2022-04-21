# ExampleSQL
Requirements:
 * Pthon3
 * Flask
 * MySQL

To make the save, set safe (app.py) to True. When the value is set to False, the app is vulnerable to SQLin. Due to autoescape set to false, this app is also vulnerable to XSS attack.

To set up the database, run:
```
python3 create_db.py
```

To simulate sensors run in the background:
```
python3 update_db.py
```

Run app by:
```
python3 app.py
```