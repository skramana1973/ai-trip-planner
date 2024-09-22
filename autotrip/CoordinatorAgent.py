from uagents import Agent, Context, Model
import time
from datetime import datetime, timedelta
from typing import List


agent = Agent()

MY_AGENTS_ADDRESS = {
    "CoordinatorAgent": "agent1q2ejux7u2y4s5w0yput8j5k2ty8sr3ayf7hk08hl2mnpgh4x5pktwf5m4es",
    "WeatherAgent": "agent1qwzhmzhrj6nx3yt3uuemp4q94fl2xuldzjpft03jjxzaewryt2k9kmga4fh",
    "FlightBookingAgent": "agent1qf3cdt7zcvqwsehd3h9eccs7tlt4v4t3yrcfs2v8x3jtzvqm8v36yeylmt6",
    "HotelBookingAgent": "agent1qw556xyn7x70krn8a2wejlu7003m8r3l2jq0a0mhs0c3tvlkvakxzjnnpaq",
    "CalendarAccessAgent": "agent1qtw6sxh7s5dag75c7uyrg9asyduevkvqs8cc9enzm6e9jgyjlf8k6qk897v",
    "EmailAgent": "agent1q2e6c3zf6t6qw5a2tw7ntwz5cmn20nuuppwteaypeddnmp7xns3l7gzagzk",
}

# MY_AGENTS_ADDRESS = {
#     "CoordinatorAgent": "agent1qdeux0h52xq6zxqyad84jdvl2xxt0amfrzyqw26yxxshttj5c73gjg2skpt",
#     "WeatherAgent": "agent1qwzhmzhrj6nx3yt3uuemp4q94fl2xuldzjpft03jjxzaewryt2k9kmga4fh",
#     "FlightBookingAgent": "agent1qfp79k3ngnz6g8mad2rez9t5ulg9a54tax0j4z9c9uye0q2469zrgl8fhws",
#     "HotelBookingAgent": "agent1qf98ytrngrcetvdkau7cp8ctcq4m4ql72f02d59zcsundjwgvf6dgcgnduq",
#     "CalendarAccessAgent": "agent1qtw6sxh7s5dag75c7uyrg9asyduevkvqs8cc9enzm6e9jgyjlf8k6qk897v",
#     "EmailAgent": "agent1qf7ssrlrct2rf8jkkthnqlzfv2x3pltrpyt2lta67wkqq540jrlazl96kng",
# }


# In this example we will use:
# - 'agent': this is your instance of the 'Agent' class that we will give an 'on_interval' and an 'on_message' task
# - 'ctx': this is the agent's 'Context', which gives you access to all the agent's important functions
# - 'Model': this is the base class for messages that we will use to define a 'Request' message
# We define a message type called Request that consists of the single string field 'message'.
class Request(Model):
    time_sent: str
    message: str
    origin: str
    destination: str
    start_date: str
    end_date: str
    flight_number: str
    price: List[float]
    hotel_name: str


# This decorator tells the agent how to handle messages that match the 'Request' type. It will execute everytime a message is received.
@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):

    # ctx.logger.info(f"Received message from {sender}: {msg}")

    # Write all the logic here to Coordinate with several Agents

    if sender == f"{MY_AGENTS_ADDRESS['FlightBookingAgent']}":
        ctx.logger.debug(f"Received message from {sender}: Message : {msg}")
        ctx.storage.set(f"FlightBookingAgent_{msg.time_sent}", f"{msg.message}")
        # current_msg = ctx.storage.get(f"FlightBookingAgent_{msg.time_sent}" ) or ''
        # ctx.logger.info("FINAL FlightBookingAgent : " + current_msg)

    if sender == f"{MY_AGENTS_ADDRESS['HotelBookingAgent']}":
        ctx.logger.debug(f"Received message from {sender}: Message : {msg}")
        ctx.storage.set(f"HotelBookingAgent_{msg.time_sent}", f"{msg.message}")
        # current_msg = ctx.storage.get(f"HotelBookingAgent_{msg.time_sent}" ) or ''
        # ctx.logger.info("FINAL HotelBookingAgent : " + current_msg)

    if sender == f"{MY_AGENTS_ADDRESS['EmailAgent']}":
        ctx.logger.debug(f"Received message from {sender}: Message : {msg}")
        ctx.storage.set(f"EmailAgent_CONFIRM_{msg.time_sent}", f"{msg.message}")
        # current_msg = ctx.storage.get(f"EmailAgent_{msg.time_sent}" ) or ''
        # ctx.logger.info("FINAL EmailAgent : " + current_msg)

    flight_confirmation_message = (
        ctx.storage.get(f"FlightBookingAgent_{msg.time_sent}") or ""
    )
    ctx.logger.debug("FINAL FlightBookingAgent : " + flight_confirmation_message)
    hotel_confirmation_message = (
        ctx.storage.get(f"HotelBookingAgent_{msg.time_sent}") or ""
    )
    ctx.logger.debug("FINAL HotelBookingAgent : " + hotel_confirmation_message)
    email_confirmation_message = (
        ctx.storage.get(f"EmailAgent_CONFIRM_{msg.time_sent}") or ""
    )

    email_sent_message = ctx.storage.get(f"EmailAgent_SENT_{msg.time_sent}") or ""
    ctx.logger.debug("FINAL Sent EmailAgent : " + email_sent_message)

    if (
        (flight_confirmation_message != "")
        and (hotel_confirmation_message != "")
        and (email_confirmation_message != "")
    ):

        ctx.logger.info(f"ALL TASKS COMPLETED EMAIL ALSO SENT !!! EmailAgent : {msg}")

        # Save somewhere

        # Access this from UI

        # Whatsapp the confirmations details - Optional

    elif (flight_confirmation_message != "") and (
        hotel_confirmation_message != "" and (email_sent_message == "")
    ):
        ctx.logger.debug(
            "Both conditions are true and email havnt sent so proceeding to send email..."
        )

        # ctx.send is a function that sends a message to the specified agent address
        ctx.logger.debug("Sending email content to EmailAgent")

        email_request = Request(
            message="Send Email to ?",
            time_sent=msg.time_sent,
            origin=msg.origin,
            destination=msg.destination,
            start_date=msg.start_date,
            end_date=msg.end_date,
            flight_number=msg.flight_number,
            price=msg.price,
            hotel_name=msg.hotel_name,
        )
        await ctx.send(f"{MY_AGENTS_ADDRESS['EmailAgent']}", email_request)

        ctx.storage.set(f"EmailAgent_SENT_{msg.time_sent}", f"{msg.message}")
        ctx.logger.debug(f"Message sent to EmailAgent message : {email_request} ")
    else:
        ctx.logger.debug("One or both conditions are false. Cannot proceed.")


# This decorator tells your agent to run the function below it on a time interval with the specified 'period' in seconds.
# @agent.on_interval(period=10.0)
@agent.on_event("startup")
async def send_message(ctx: Context):

    # Get the current time in milliseconds
    current_time_milliseconds = int(time.time() * 1000)
    ctx.logger.info(f"Current Time in MilliSeconds : {current_time_milliseconds}")

    # ctx.logger.info("Sending message to WeatherAgent")
    # weather_request = Request(message="Send me weather report", time_sent=str(current_time_milliseconds))
    # await ctx.send(f"{MY_AGENTS_ADDRESS['WeatherAgent']}", weather_request)
    # ctx.logger.info(f"Message sent to WeatherAgent message : {weather_request} ")
    dummy_start_date = (datetime.now() + timedelta(days=5)).strftime(
        "%Y-%m-%d"
    )  # 30 days from now
    dummy_end_date = (datetime.now() + timedelta(days=10)).strftime(
        "%Y-%m-%d"
    )  # 60 days from now

    flight_request = Request(
        time_sent=str(current_time_milliseconds),
        message="Can you book my flight ?",
        origin="SFO",
        destination="BOS",
        start_date=dummy_start_date,
        end_date=dummy_end_date,
        flight_number="",
        price=[],
        hotel_name="",
    )

    ctx.logger.debug("Sending flight booking info to FlightBookingAgent")

    await ctx.send(f"{MY_AGENTS_ADDRESS['FlightBookingAgent']}", flight_request)
    ctx.logger.info(f"Message sent to FlightBookingAgent message : {flight_request} ")

    ctx.logger.debug("Sending hotel booking info to HotelBookingAgent")

    hotel_request = flight_request
    hotel_request.message = "Can you book my Hotel ?"
    await ctx.send(f"{MY_AGENTS_ADDRESS['HotelBookingAgent']}", hotel_request)
    ctx.logger.info(f"Message sent to HotelBookingAgent message : {hotel_request} ")


if __name__ == "__main__":
    agent.run()
