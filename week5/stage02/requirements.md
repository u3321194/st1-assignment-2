# SmartCare Requirements Specification v0.2

## Part B – Stakeholders and Scope

### Stakeholders
1. Reception 
2. Partitioners 
3. Patients 
4. SmartCare Management 

### In Scope
- Managing patients and practitioners 
- Creating and viewing the appoinments 
- Keeping a record and updating the appointment status 
- Viewing apppointment history
- Searching for the patients information 
- Preventing any double bookings 

### Out of Scope
- Processing the online payments 
- Patient moblie application 
- Telehealth appointments 
- Email reminders or sending an automatic SMS 
- Integration with the external medical systems 

### Provisional / Open Features
- Patient login 
- Patient online cancelation 
- Reminders for thier upcoming appointments 
- Reporting and analytics


## Part C – Functional Requirements

FR-01: The system should enable the staff memebers to create patients records which will contain the required patient's information. 

FR-02: The system should allow the staff to find and view the patient's information. 

FR-03: The system should only allow authorised staff members to create the practitoners records.

FR-04: The system should enable the staff to create appointments for patients with practitioners at a specified date and time. 

FR-05: The system should be able to prevent practitioner from being booked for two appointments at the same date and time. 

FR-06: The system should allow the staff members to view the scheduled appointments 

FR-07: The system should be able to record and update the status of an appointment 

FR-08: The system should allow to view the patients appointment history

FR-09: The system should also allow the staff members to update appointment information

FR-10: The system also be able to help the staff members to cancel an appointment for patients and record that it was cancelled as well. 




## Part D – Non-Functional Requirements

NFR-01 (Reliability): During normal operation, the system should be reliable for storing and retrieving both patients and practitoners appointment information.

NFR-02 (Usability): The system should be able to allow the recepetion to staff to create, find and update appointment informtation or data by providing a simple interface. 

NFR-03 (Data integrity): The system needs to maintain accurate information regarding the patients and practioners appointments so that it prevents  conflicting practioner bookings. 

NFR-04 (Maintainability): The system needs to be set up in an organised manner which will prevent changes to one function from affecting other functions when updates are made in the future. For example, changing the appointment booking function should not affect the patient information or appointment history functions.

NFR-(05) (Testability): The system should be able to produce predicatble results so that it can test the main functions. 



## Part E – User Stories and Acceptance Criteria

### US-01 – Creating an appointment
As a receptionist, I will make an appointment for the patient with a practitioner who is avaliable so that the appointmnet is saved in the system. 

- Given a valid patient, practioner and avaliable appointment time.
- When the receptioist creates the appointment.
- Then the appoinment should be recorded and saved in the system with the correct patient, practioner and time.

# Failure Scenario
- Given the patient information is missing 
- When the receptionist attempts to create the appointment 
- Then the system should reject the appointment and indicate that the required information is currently missing 

### US-02 - Find patient informtation
As a receptionist, I want to be able to search for a patient so that i can find thier information easily.  

- Given the patient has a record in the system.  
- When the receptionist searches for the patient.
- Then the patient's information should appear.

# Failure Scenario 
- Given no matching patient record exists.
- When the receptionist searches for the patient. 
- Then the system should be able to indicate that there are no matching records. 

### US-03 - Prevent Double Booking 
As a receptionist, I want to prvenet the system from conflicting practioner appointments so that the patients are not accidently booked at the same. 

- Given a practitioner has no appointment at the selected time. 
- When the receptionist books the appointment. 
- Then the appointment should be created sucessfully. 

## Failure Scenario 
- Given a practitioner already has an appointment at the same selected time. 
- When the receptionist attempts to create another appointment at that time.
- Then the system should reject the booking. 

### US-04 - Update Appointment Status 
As a receptionist, I want to update an appointment's status so that the system accurately reflects what happened to the appointment.

- Given an existing appointment. 
- When thbe receptionist chnages its status. 
- Then the appointment should display the updated status. 

# Failure Scenario
- Given an appointment which does not exist. 
- When the receptionst attempts to update its status. 
- Then the system should indicate that the appointment cannot be found. 

### US-05 - View appointment history
As a practitioner, I want to view a patient's appointment history so I can see their previous appointments.

- Given the patient has previous appointments.
- When the practitioner looks at the patient's history.
- Then the system should display the patient's previous appointments.

# Failure Scenario
Given the patient has no previous appointments.
When the practitioner looks at the patient's history.
Then the system should indicate that there are no previous appointments.



## Part H – Assumptions and Open Questions
1. What specific patient information needs to be stored?
2. What appointment statuses should the system provide?
3. Who should be authorised to create, edit or cancel appointments?
4. What exactly should count as a duplicate booking?
5. Should cancelled appointments remain in the patient's appointment history?
