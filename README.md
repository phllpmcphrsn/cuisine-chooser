# Introduction
This project is a simple, Flask application. The aim is not only to practice with Python, Flask, and Heroku, but also to help someone decide what to eat.

# Running the Application
```
git clone <project>
```
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt 
```

5. Finally start the web server:
```
$ (env) python app.py # OR
$ (env) flask run
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
