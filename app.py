import os
from slack_bolt import App
from slack_sdk import WebClient
# from slack_bolt.adapter.socket_mode import SocketModeHandler


# Initializes your app with your bot token and socket mode handler
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
)

app.signing_secret=os.environ["SLACK_SIGNING_SECRET"],
app_token=os.environ["SLACK_APP_TOKEN"],
# app.port=int(os.environ.get("PORT", 3000))


web = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("message")
async def handle_message(event):
    message_text = event["message"]["text"].lower()
    contains_love = any(word in message_text for word in ["access"])

    trigger = None
    if "opstools" in message_text:
        trigger = "optstools"
    elif "appcenter" in message_text:
        trigger = "appcenter"
    elif "intercom" in message_text:
        trigger = "intercom"
    elif "confluence" in message_text:
        trigger = "confluence"

    IT_service = {"opstools": "47", "confluence": "94", "appcenter": "57", "intercom": "46"}
    if trigger is not None:
        try:
            await web.chat_postMessage(
                channel=event["message"]["channel"],
                thread_ts=event["message"].get("ts", event["message"].get("ts")),
                text=f"Please request the access via Freshservice \n https://google.com/items/{IT_service[trigger]}",
            )
            print("success")
        except Exception as e:
            print(str(e))



    
# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3001)))
    print("⚡️ app is running!")
     


#  socketmodeule hander in the libraly has the function to display a message on termina in the case print() isn't specified
