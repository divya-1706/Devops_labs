from app import app 
@app.route('/') 
def home(): 
    return 'Hello from Docker! Flask app is running inside a container.' 
@app.route('/health') 
def health(): 
    return 'OK', 200 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)