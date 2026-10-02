# AI Usage - Stage 1 Lab

## Tool used
Microsoft Copilot (UC-approved GenAI tool)

## Part C - AI as tutor

Prompt I gave:
Act as a Python tutor. I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.
(followed by my book_appointment and display_appointments code)

Summary of Copilot's response:
- Explained what book_appointment() and display_appointments() do.
- Three limitations: global list, no validation, no duplicate handling.
- Improvements: use a class, add validation, check for booking conflicts.
- Asked two questions to test my understanding.

My answers to Copilot's two questions:
1. Why is using a global list for appointments potentially problematic as the program grows?
A global list can become difficult to manage because different parts of the program can access and change it. As the program gets bigger, this can make the code harder to organise and maintain.
2. What type of input validation would you add to make the booking function more reliable?
I would check that the patient name and practitioner name are not empty, and that the appointment time is in a valid date and time format. I would also check that the practitioner is not already booked at that time.


## Part D – AI-generated alternative

Prompt I gave:
Write a simple, beginner-friendly Python function that stores a patient name, practitioner name and appointment time. Do not use a database. Do not use a GUI.

What Copilot produced:
A version with add_appointment() and show_appointments(). It checks that all fields are filled before adding, stores each appointment in a dictionary inside a list, and prints a confirmation message. Saved as smartcare_ai.py.


## Part F – Verify Behaviour

I tested both versions with the same five inputs.

| Test case | Human version (smartcare_v01.py) | AI version (smartcare_ai.py) |
|---|---|---|
| Normal appointment (Carol Lee, Dr. John Doe, 2024-07-21 09:00 AM) | Accepted | "Appointment added successfully!" |
| Blank patient name | Rejected – ValueError: "Patient name, practitioner name and time cannot be empty" | Rejected – printed "All fields must be filled in." |
| Same practitioner and time (Dan Wu, Dr. John Doe, 2024-07-20 10:00 AM – same slot as Alice) | Accepted – double-booking was not prevented | Accepted – double-booking was not prevented |
| patient_name=None | Rejected – same ValueError | Rejected – printed "All fields must be filled in." |
| appointment_time=None | Rejected – same ValueError | Rejected – printed "All fields must be filled in." |

Finding: Both versions correctly reject blank and None inputs, but neither prevents double-booking. The human version raises a ValueError, which stops bad data in a way the calling code can detect, while the AI version only prints a message and returns.