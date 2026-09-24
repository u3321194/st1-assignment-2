from datetime import date, time
from models import Patient, Practitioner, Appointment, AppointmentStatus

# 1. Create valid objects
patient = Patient("Alice Smith", "P001")
practitioner = Practitioner("Dr. John Doe", "DR001", "General Practice")
appt = Appointment(patient, practitioner, date(2024, 7, 20), time(10, 0))
print("Created appointment with status:", appt.status)

# 2. Test invalid input (empty patient name should raise an error)
try:
    bad_patient = Patient("", "P002")
except ValueError as e:
    print("Invalid patient rejected:", e)

# 3. Cancel a scheduled appointment
appt.cancel()
print("After cancel, status:", appt.status)

# 4. Attempt an illegal repeated transition (cancel an already-cancelled appointment)
try:
    appt.cancel()
except ValueError as e:
    print("Illegal repeated cancel rejected:", e)