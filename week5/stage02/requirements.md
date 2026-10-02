# SmartCare Requirements Specification v0.2

## Part A – Problem

SmartCare is a small community clinic that currently uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system to replace these manual processes.

## Part B – Stakeholders and Scope

### Stakeholders, Need and Evidence

| Stakeholder | Need | Evidence |
|---|---|---|
| Reception | To find patient information quickly and avoid duplicate bookings. | The brief says staff have difficulty finding patient information and report duplicate bookings. |
| Practitioners | To see appointments and patients' appointment history. | The brief mentions inconsistent appointment status and limited appointment history. |
| Patients | To have their information and appointments recorded correctly without double bookings. | The brief identifies problems with patient information, duplicate bookings and appointment records. |
| Management | A small and maintainable system to improve the current process. | The brief directly states that management wants a small, maintainable patient, practitioner and appointment system. |

### In Scope
- Managing patients and practitioners
- Creating and viewing appointments
- Keeping a record and updating the appointment status
- Viewing appointment history
- Searching for patient information
- Preventing any double bookings

### Out of Scope
- Processing online payments
- Patient mobile application
- Telehealth appointments
- Email reminders or sending an automatic SMS
- Integration with external medical systems

### Provisional / Open Features
- Patient login
- Patient online cancellation
- Reminders for their upcoming appointments
- Reporting and analytics


## Part C – Functional Requirements

FR-01: The system should enable staff members to create patient records which will contain the required patient information.

FR-02: The system should allow staff to find and view a patient's information.

FR-03: The system should only allow authorised staff members to create practitioner records.

FR-04: The system should enable staff to create appointments for patients with practitioners at a specified date and time.

FR-05: The system should prevent a practitioner from being booked for two appointments at the same date and time.

FR-06: The system should allow staff members to view scheduled appointments.

FR-07: The system should be able to record and update the status of an appointment.

FR-08: The system should allow staff to view a patient's appointment history.

FR-09: The system should allow staff members to update appointment information.

FR-10: The system should allow staff members to cancel an appointment for a patient and record that it was cancelled.


## Business Rules

- BR-01: A practitioner cannot have two appointments at the same date and time (FR-05, US-03).
- BR-02: An appointment cannot be created unless the patient, practitioner, date and time are provided (US-01 failure scenario).
- BR-03: Only authorised staff members can create practitioner records (FR-03).
- BR-04: A cancelled appointment must be recorded as cancelled rather than removed from the system (FR-10).


## Part D – Non-Functional Requirements

NFR-01 (Reliability): During normal operation, the system should be reliable for storing and retrieving both patient and practitioner appointment information.

NFR-02 (Usability): The system should allow reception staff to create, find and update appointment information by providing a simple interface.

NFR-03 (Data integrity): The system needs to maintain accurate information about patient and practitioner appointments so that it prevents conflicting practitioner bookings.

NFR-04 (Maintainability): The system needs to be set up in an organised manner which will prevent changes to one function from affecting other functions when updates are made in the future. For example, changing the appointment booking function should not affect the patient information or appointment history functions.

NFR-05 (Testability): The system should produce predictable results so that its main functions can be tested.


## Part E – User Stories and Acceptance Criteria

### US-01 – Creating an appointment
As a receptionist, I want to make an appointment for a patient with an available practitioner, so that the appointment is saved in the system.

- Given a valid patient, practitioner and available appointment time.
- When the receptionist creates the appointment.
- Then the appointment should be recorded and saved in the system with the correct patient, practitioner and time.

#### Failure Scenario
- Given the patient information is missing.
- When the receptionist attempts to create the appointment.
- Then the system should reject the appointment and indicate that the required information is missing.

### US-02 – Find patient information
As a receptionist, I want to be able to search for a patient, so that I can find their information easily.

- Given the patient has a record in the system.
- When the receptionist searches for the patient.
- Then the patient's information should appear.

#### Failure Scenario
- Given no matching patient record exists.
- When the receptionist searches for the patient.
- Then the system should indicate that there are no matching records.

### US-03 – Prevent double booking
As a receptionist, I want the system to prevent conflicting practitioner appointments, so that patients are not accidentally booked at the same time.

- Given a practitioner has no appointment at the selected time.
- When the receptionist books the appointment.
- Then the appointment should be created successfully.

#### Failure Scenario
- Given a practitioner already has an appointment at the same selected time.
- When the receptionist attempts to create another appointment at that time.
- Then the system should reject the booking.

### US-04 – Update appointment status
As a receptionist, I want to update an appointment's status, so that the system accurately reflects what happened to the appointment.

- Given an existing appointment.
- When the receptionist changes its status.
- Then the appointment should display the updated status.

#### Failure Scenario
- Given an appointment which does not exist.
- When the receptionist attempts to update its status.
- Then the system should indicate that the appointment cannot be found.

### US-05 – View appointment history
As a practitioner, I want to view a patient's appointment history, so that I can see their previous appointments.

- Given the patient has previous appointments.
- When the practitioner looks at the patient's history.
- Then the system should display the patient's previous appointments.

#### Failure Scenario
- Given the patient has no previous appointments.
- When the practitioner looks at the patient's history.
- Then the system should indicate that there are no previous appointments.


## Part H – Assumptions and Open Questions
1. What specific patient information needs to be stored?
2. What appointment statuses should the system provide?
3. Who should be authorised to create, edit or cancel appointments?
4. What exactly should count as a duplicate booking?
5. Should cancelled appointments remain in the patient's appointment history?