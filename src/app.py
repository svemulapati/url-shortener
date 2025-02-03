from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

url_mapping = {}

# Function to shorten the URL
def shorten_url(long_url):
    short_url = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_mapping[short_url] = long_url
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = ""
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)