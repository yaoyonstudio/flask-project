
建项目
mkdir flask-project

初始化环境
virtualenv venv
venv\Scripts\activate

安装依赖
pip install Flask
pip install flask-migrate flask-script
pip install flask-sqlalchemy flask-mysqldb

迁移
python db.py db init
python db.py db migrate
python db.py db upgrade


运行
python run.py

