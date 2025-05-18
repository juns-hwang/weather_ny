import schedule
import time
import subprocess

def job():
    print("Run weekly data pipeline")
    subprocess.run(["python3", "scripts/fetch_and_store.py"])

schedule.every().sunday.at("12:00").do(job)

print("Weekly schedule started")
while True:
    schedule.run_pending()
    time.sleep(60)