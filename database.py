from sqlalchemy import create_engine, text
import os

db_connect = os.environ['DB_CONNECT']


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
