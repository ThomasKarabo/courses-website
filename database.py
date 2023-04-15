from sqlalchemy import create_engine, text
import os

db_connect = "mysql+pymysql://m51uxkam7cvz21myv65h:pscale_pw_8esCrQAM0grMtggwHqbWMQuFOHz2V7bgQXIHJ1JniSo@aws.connect.psdb.cloud/coursesdata?charset=utf8mb4"

engine = create_engine(
  db_connect, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM courses"))
  print(result.all())
