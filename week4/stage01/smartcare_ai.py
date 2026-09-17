appointments = []

def add_appointment(patient, practitioner, time):
    # Basic validation
    if not patient or not practitioner or not time:
        print("All fields must be filled in.")
        return

    # Create a simple appointment record
    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }

    # Store it in the list
    appointments.append(appointment)
    print("Appointment added successfully!")

def show_appointments():
    if not appointments:
        print("No appointments yet.")
        return

    for appt in appointments:
        print(f"{appt['patient']} → {appt['practitioner']} at {appt['time']}")


# --- Test the AI version ---
add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")
show_appointments()