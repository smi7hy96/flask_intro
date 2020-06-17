#FLASK


## To install
```
$ pip install Flask
```
When running the application. it will use a local host to display the webpages.
http://127.0.0.1:5000/

## Main Page

- There is a main page where the Flask code is written, this controls the methods that will redirect and control the connections between pages.

### Route

```python
@app.route("/")
```
- For the main index page. this route is used.
- What this does is tells the browser what to do when it is on this particular url (in this case the base :5000/ page)

- So when the browser is on that domain, Flash will execute the method below it:
```python
def home():
    return render_template("index.html")
```
- This means that it will load up the index.html page. render_template takes care of the loading.
- NOTE: ALL html pages should belong in a separate 'templates' directory.

### LINKS

- Now that the index page is loaded. It is only a template so normal href="newlocation.html" will not work
- This must now change to:

```html
href="{{ url_for('location') }}""
```
- It wil now be recognised as a legitimate link and will work as expected (assuming the linked file is in the same templates directory - or is an external live website)

### STYLES

- stylesheets (or css pages) are also not recognised immediately.
- They must be added to the file hierarchy under directories 'static' and then 'styles'

- They will still not be loaded by your html files though as the href once again needs to be changed.

```html
href="{{ url_for('static',filename='styles/button.css') }}"
```

- replacing the normal 'href="style.css"' with the above code will successfully import your css page and the html files will now be displayed as expected.