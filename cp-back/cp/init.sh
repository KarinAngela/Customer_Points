python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt

sudo docker run -dit --rm -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 --name mysql-cp mysql:8
# EXECUTAR MANUALMENTE
# docker exec -it mysql-cp bash
# mysql -u root -p 1234
# CREATE DATABASE cp;
# CREATE USER 'cp'@'%' IDENTIFIED BY '1234';
# GRANT ALL PRIVILEGES ON cp.* TO 'cp'@'%';
# exit

# INICIAR BACKEND
#entrar no .venv -  source .venv/bin/activate 
# uvicorn main:app --reload
