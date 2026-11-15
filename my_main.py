# appointment_main.py
# Author: Sharath Srinivasan

from booking_queue import BookingQueue
from my_assistant import AppointmentHelper
from my_tool import AppointmentBook
from my_toolbox import AppointmentToolbox
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "9:00 am",
    "tuesday": "none",
    "wednesday": "11:00 am",
    "thursday": "11:00 am",
    "friday": "none",
}

INSTRUCTIONS = """You are Jaxon, a support assistant for Sharath's Shoe Shop.
Answer in one short sentence.
The office is at 122 Lumen Street, on the twelfth floor.
Bring any comfort soles or shoes to your appointment.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the client to the front desk."""

appointment_book = AppointmentBook(OPEN_TIMES)
booking_queue = BookingQueue(appointment_book)
tools = AppointmentToolbox(appointment_book, booking_queue)
model = OllamaModel("granite4.1:3b")
helper = AppointmentHelper("Jaxon", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")

print("Front desk review")
for request in booking_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['client']}, {request['day']} {request['time']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(booking_queue.approve(number))
    else:
        print(booking_queue.reject(number))

print(f"Bookings: {len(appointment_book.bookings)}")
