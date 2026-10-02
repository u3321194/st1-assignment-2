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

# --- Extra checks added after review ---

# 5. Status cannot be set directly
try:
    appt.status = AppointmentStatus.SCHEDULED
except AttributeError:
    print("Direct status change rejected: status is read-only")

# 6. Double-booking is prevented
bob = Patient("Bob Johnson", "P003")
appt2 = Appointment(bob, practitioner, date(2024, 7, 21), time(9, 0))
try:
    Appointment(patient, practitioner, date(2024, 7, 21), time(9, 0))
except ValueError as e:
    print("Double-booking rejected:", e)

# 7. A cancelled slot can be rebooked
rebooked = Appointment(bob, practitioner, date(2024, 7, 20), time(10, 0))
print("Cancelled slot rebooked with status:", rebooked.status)

# 8. A completed appointment cannot be cancelled
appt2.complete()
print("After complete, status:", appt2.status)
try:
    appt2.cancel()
except ValueError as e:
    print("Cancel after complete rejected:", e)