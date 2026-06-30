# VS Code Terminal
pip install flask
py main.py

# ubuntu terminal
sudo docker build -t flask-docker-app .
docker run -d -p 5000:5000 --name flask-container flask-docker-app
sudo docker ps

# access url
http://localhost:5000