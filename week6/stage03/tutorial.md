# Stage 3 Tutorial – From Requirements to Domain Models

## Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | It has its own data, behaviour, and is supported by FR-01, FR-02 and FR-08. |
| Practitioner | Yes | It has its own data, behaviour, and is supported by FR-03, FR-04 and FR-05. |
| Appointment | Yes | It has its own data, behaviour, and is supported by several functional requirements including FR-04, FR-05, FR-06, FR-07, FR-09 and FR-10. |
| Name | No | It is a piece of data belonging to Patient and Practitioner, not a class with its own behaviour. |
| Clinic | No | There is no functional requirement that requires a Clinic class. |
| Database | No | A database is a technical choice for storing data, not part of the clinic's problem domain. |
| Cancellation | No | Cancellation is an action performed on an Appointment through the `cancel()` method. |
| Status | No | Status is a value that an Appointment has, rather than a separate class. |

## CRC Cards

### Patient
- **Responsibilities:** Knows the patient's name, ID and appointment history; can store and provide patient information.
- **Collaborators:** Appointment

### Practitioner
- **Responsibilities:** Knows the practitioner's name, ID and scheduled appointments; can provide practitioner information.
- **Collaborators:** Appointment

### Appointment
- **Responsibilities:** Knows the patient, practitioner, date, time and status; can be created, updated and cancelled.
- **Collaborators:** Patient, Practitioner

## Relationship Reasoning

**Patient to Appointment: which relationship and why?**
This is an association with a one-to-many relationship. One patient can have zero or many appointments over time, while each appointment belongs to exactly one patient.

**Practitioner to Appointment: what multiplicity?**
The multiplicity is one-to-many. One practitioner can have zero or many appointments, while each appointment is booked with exactly one practitioner.

**Should Appointment inherit from Patient?**
No. An Appointment is not a type of Patient. It should have an association with Patient because an appointment has a patient.

**Does Clinic need to own every object?**
No. There is no requirement for one object to own all patients, practitioners and appointments. Adding a Clinic class would make the system larger and less maintainable without supporting a required feature.

## AI Model Critique

| AI proposal | Decision | Reason |
|---|---|---|
| PatientManager, PractitionerManager, AppointmentManager | Reject | No FR requires separate manager classes. They would add extra classes that duplicate the data and behaviour already handled by Patient, Practitioner and Appointment. |
| ClinicController | Reject | No requirement needs a controller for the whole clinic. Adding it would increase the system's size without supporting a required feature. |
| NotificationManager | Defer | Automatic notifications are not confirmed as in scope. Email reminders and SMS are out of scope, while reminders are only on the provisional list. |
| ScheduleEngine | Reject | FR-05 and FR-06 can be handled using the existing Practitioner and Appointment classes. A separate engine would add unnecessary complexity. |