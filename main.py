from agent import TradingAgent
from notifier import send_telegram, get_updates
import time

agent = TradingAgent()

last_update_id = None

print("Bot started")

while True:

    updates = get_updates(last_update_id)

    if "result" in updates:

        for update in updates["result"]:

            last_update_id = update["update_id"] + 1

            if "message" in update:

                text = update["message"]["text"].lower()

                if "top stocks" in text:

                    result = agent.analyze_top_stocks()

                    send_telegram(result)

                else:

                    send_telegram(
                        "Commands:\n"
                        "top stocks"
                    )

    time.sleep(30)