
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Anamika's Price Tracker</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f8f9fa; }
            .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 20px 0; }
            h1 { color: #2563eb; text-align: center; }
            .price { font-size: 2em; color: #10b981; font-weight: bold; }
            .btn { background: #10b981; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>🛒 Anamika's E-Commerce Price Tracker</h1>
        
        <div class="card">
            <h2>iPhone 15 128GB</h2>
            <div class="price">₹69,900</div>
            <p><strong>Lowest:</strong> ₹65,900</p>
            <button class="btn">📱 Track Price</button>
        </div>
        
        <div class="card">
            <h2>Samsung S24 Ultra</h2>
            <div class="price">₹1,24,999</div>
            <p><strong>Lowest:</strong> ₹1,15,000</p>
            <button class="btn">📱 Track Price</button>
        </div>
        
        <p style="text-align: center; color: #6b7280; margin-top: 40px;">
            Built by Anamika | B.Tech CSE 2023 | Python/Flask Developer<br>
            <a href="https://github.com/Anamika-mishra1">GitHub Portfolio</a>
        </p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("🚀 Starting at http://localhost:5000")
    app.run(debug=True, port=5000)
