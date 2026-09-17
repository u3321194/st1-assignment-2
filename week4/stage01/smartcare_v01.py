print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


# --- Enhanced version: lists, dictionaries and functions ---

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name or not practitioner_name or not appointment_time:
        raise ValueError("Patient name, practitioner name and time cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()


# --- Limitations ---
# 1. Appointments are not saved permanently — all data is lost when the program is closed.
# 2. The receptionist cannot enter information — patient, practitioner and appointment details are hard-coded.
# 3. The program allows double-booking — it does not check if a practitioner is already booked at that time.
# 4. There is no date/time validation — the appointment time is accepted as text without checking it is valid.
# 5. There is no option to edit or cancel appointments — once added, an appointment can only be displayed.


# --- Part G improvement ---
# I improved the validation so the function now checks that the patient name,
# practitioner name AND appointment time are all provided, not just the patient name.
