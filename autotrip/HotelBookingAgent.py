"""
This agent is responsible for getting Flight Ticket Booked

It will try to get the data every 10 seconds and log it to the console.
"""

from uagents import Agent, Context, Model
import json
import requests
import time
from typing import List

agent = Agent()

# In this example we will use:
# - 'agent': this is your instance of the 'Agent' class that we will give an 'on_interval' and an 'on_message' task
# - 'ctx': this is the agent's 'Context', which gives you access to all the agent's important functions
# - 'Model': this is the base class for messages that we will use to define a 'Request' message

MY_AGENTS_ADDRESS = {
    "CoordinatorAgent": "agent1q2ejux7u2y4s5w0yput8j5k2ty8sr3ayf7hk08hl2mnpgh4x5pktwf5m4es"
}

# MY_AGENTS_ADDRESS = {
#     "CoordinatorAgent": "agent1qdeux0h52xq6zxqyad84jdvl2xxt0amfrzyqw26yxxshttj5c73gjg2skpt"
# }


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
    ctx.logger.info(f"Received message from Sender : {sender}: Message : {msg}")

    # ctx.send is a function that sends a message to the specified agent address
    if sender == f"{MY_AGENTS_ADDRESS['CoordinatorAgent']}":
        request = Request(
            message="Hotel Booked!!!",
            time_sent=msg.time_sent,
            origin=msg.origin,
            destination=msg.destination,
            start_date=msg.start_date,
            end_date=msg.end_date,
            flight_number=msg.flight_number,
            price=msg.price,
            hotel_name="Mountainview",
        )
        ctx.logger.info(f"Replying message To Sender : {sender}: Message : {request} ")
        await ctx.send(sender, request)
    else:
        await ctx.send(sender, Request(message="Who are you?"))


if __name__ == "__main__":
    agent.run()
