# SmartCare Domain Model - Class Skeletons (Stage 3)
# Structure only - full behaviour is not implemented yet.


class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id

    def view_details(self):
        pass


class Practitioner:
    def __init__(self, name, practitioner_id):
        self.name = name
        self.practitioner_id = practitioner_id

    def view_schedule(self):
        pass


class Appointment:
    def __init__(self, patient, practitioner, date, time, status):
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = status

    def create(self):
        pass

    def update_status(self):
        pass

    def cancel(self):
        pass


# --- Part H: Consistency Check ---
# The class skeletons match the UML model in domain_model.md:
# - Patient and Practitioner each hold a name and ID (matching the diagram attributes).
# - Appointment holds patient, practitioner, date, time and status, and links a Patient
#   and a Practitioner (matching the one-to-many relationships).
# - The methods (view_details, view_schedule, create, update_status, cancel) match the
#   behaviours listed in Part B and the UML diagram.
# - Full behaviour has not been implemented yet; the methods are placeholders (pass),
#   as required for this stage.