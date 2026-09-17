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

Verification (Part F):
I ran smartcare_ai.py. It printed "Appointment added successfully!" for both appointments and displayed them correctly, so the AI code works.