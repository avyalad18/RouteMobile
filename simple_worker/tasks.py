from celery import Celery
import sqlite3,time
import json,os
from dotenv import load_dotenv
load_dotenv()
CONFIGS=dict()

with open(os.getenv('config_path'),'r') as f:
    CONFIGS=json.loads(f.read())

CELERY_CONF = CONFIGS.get("celery_config")
DB_CONF = CONFIGS.get("db_config")

app = Celery('tasks', broker=CELERY_CONF.get("CELERY_BROKER_URL"),backend=CELERY_CONF.get("CELERY_RESULT_BACKEND"))


@app.task
def updateItem(data): 
    # ADDED SLLEP TO SIMULATE THE PROCESS TIME
    time.sleep(5000)
    updateToDb(data.get('item'))
    return  "COMPLETE"


def updateToDb(item):
    """UPDAING STATUS OF THE ITEM RECIVED IN SQLITE DB

    Args:
        item (string):  value contains name of the item added to db
    """
    conn = sqlite3.connect(DB_CONF.get("path"))
    cursor = conn.cursor()    
    try:       
        cursor.execute("UPDATE items SET status='completed' WHERE item=?", (item,))
        conn.commit()
    except sqlite3.Error as e:
        print("error:", e)
    finally:       
        conn.close()