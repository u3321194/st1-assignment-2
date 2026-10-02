# Stage 2 Tutorial – From Problems to Requirements

## Activity 1 – Stakeholder Map

| Stakeholder | Need | Potential conflict |
|---|---|---|
| Reception | To find patient information quickly and avoid duplicate bookings. | The no double-booking rule could slow down or block a booking if the practitioner is already booked. |
| Practitioners | To see appointments and patients' appointment history. | Patients' need for privacy could clash with practitioners wanting full patient history. |
| Patients | To have their information and appointments recorded correctly without double bookings. | Receptionists and practitioners need to access or change patient data, which could conflict with patients' need for privacy and accuracy. |
| Management | A small and maintainable system to improve the current process. | Practitioners and receptionists may want more features, which could make the system larger and more complex. |

## Activity 2 – Functional or Non-Functional?

| Requirement | Classification | Reason |
|---|---|---|
| The system shall allow staff to cancel an appointment. | Functional | It is an action the system performs. |
| The system should remain responsive for the course-scale dataset. | Non-functional | It describes the system's speed and performance. |
| The system shall retain cancelled appointments. | Functional | It describes something the system must do with the data. |
| Core business logic should be independently testable. | Non-functional | It describes a quality of the system's design. |
| The system shall search for a patient by ID. | Functional | Searching is an action the system performs. |

## Activity 3 – Repair Ambiguous Requirements

| Requirement | Problem | Clarification question |
|---|---|---|
| The system should be easy to use. | "Easy" is subjective and does not specify how many steps, how much time, or how much training is acceptable. | What steps should a user need to complete a task, and how much training should be required? |
| Patient search should be fast. | "Fast" is unclear because it does not specify a maximum search time in seconds. | How many seconds should a patient search take at most? |
| The system should securely manage data. | "Securely" is unclear because it does not specify what security measures are required or who can access the data. | Who should be allowed to view or change patient data, and what security measures are required? |
| Appointments should normally be easy to cancel. | "Normally" does not define the exceptions, and "easy" does not specify the steps or time required to cancel. | Are there any situations where an appointment cannot be cancelled, such as late cancellations? |

## Activity 4 – AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Out of scope | SMS/email reminders are on the out-of-scope list. |
| Facial recognition login. | Unsupported | It is not mentioned in the brief or requirements. |
| Receptionists create appointments. | Confirmed | FR-04 covers staff creating appointments. |
| Online payment. | Out of scope | Online payments are on the out-of-scope list. |
| Practitioners view schedules. | Confirmed | FR-06 covers viewing scheduled appointments, and practitioners need to see appointments in the stakeholder table. |
| AI recommends treatments. | Unsupported | It is not mentioned and is outside the appointment-booking purpose of the system. |
| Cancelled appointments remain in history. | Assumption requiring validation | Open question 5 asks whether cancelled appointments should remain in history, so it has not been confirmed. |

## Exit Question

Why is "AI suggested it" not sufficient evidence for a requirement?

A real requirement has to come from what the client or stakeholders actually need. If you add something just because AI suggested it, you could include unnecessary features or requirements that the client did not ask for.