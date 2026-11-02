# appointment_main.py
# Author: Sharath Srinivasan

from my_assistant import AppointmentHelper
from my_tool import AppointmentBook

OPEN_TIMES = {
    "monday": "9:00 am",
    "tuesday": "none",
    "wednesday": "11:00 am",
    "thursday": "11:00 am",
    "friday": "none",
}

appointment_book = AppointmentBook(OPEN_TIMES)
helper = AppointmentHelper(
    "Jaxon",
    "You help clients of Sharath's Shoe shop book an appointment time.",
    appointment_book,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
