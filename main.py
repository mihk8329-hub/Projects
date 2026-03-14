from agent import TradingAgent
from notifier import send_telegram
import schedule
import time

print("Running market analysis...")

def run_analysis():

    agent = TradingAgent()

    result = agent.analyze("CL=F")

    print(result)
    send_telegram(result)


run_analysis()

schedule.every(5).minutes.do(run_analysis)

while True:

    print("Waiting for next run...")

    schedule.run_pending()

    time.sleep(60)

