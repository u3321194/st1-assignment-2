# Stage 1 Tutorial – Why Software Engineering Still Matters

## Activity 1 – Think-Pair-Share

**If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?**

1. An engineer needs to understand the client's needs, ask the right questions, and turn them into clear requirements before writing any code.
2. An engineer needs to test the code against the requirements and verify that it works correctly, including checking for cases where it may produce incorrect results.
3. An engineer needs to understand software design and programming well enough to identify problems in AI-generated code and decide which suggestions should be accepted, changed or rejected.

## Activity 2 – Is This Software Engineering?

| Scenario | Programming? | Software engineering? | Why? |
|---|---|---|---|
| A – A student writes a 50-line Python calculator | Yes | No | Code is being written, but there are no stakeholders, formal requirements, or ongoing testing and maintenance. |
| B – A team develops a payroll system used by 5,000 employees | Yes | Yes | It involves programming as well as stakeholders, requirements, testing, security, reliability, teamwork and long-term maintenance. |
| C – An AI assistant generates a simple appointment application from one prompt | Yes | No | Code is produced, but the clinic's requirements were not gathered or checked, and the software was not properly tested. |

## Activity 3 – SmartCare Problem Analysis

### Task 1 – Identify stakeholders

| Stakeholder | What do they need? |
|---|---|
| Reception | Fast booking and searching of patient and appointment information. |
| Practitioners | Access to patient history and their appointment schedules. |
| Patients | Accurate and private patient records and appointment information. |
| Management | A small, simple and maintainable system. |

### Task 2 – Identify current problems

1. **Duplicate bookings:** The current system can result in appointments being double-booked.
2. **Difficulty locating patient records:** Patient information can be difficult to find in paper records and spreadsheets.
3. **Inconsistent appointment status:** Appointment statuses are not consistently recorded or updated.
4. **Limited practitioner availability:** It is difficult to see when practitioners are available.

### Task 3 – Ask client questions

1. What patient information needs to be stored besides the patient's name and ID?
2. What should count as a duplicate booking?
3. Who should be allowed to create, edit and cancel appointments?
4. What appointment statuses should the system support?
5. Should cancelled appointments remain in the appointment history, and does the data need to be saved permanently?

## Activity 4 – Critique an AI Response

| Suggestion | Client evidence? | In scope? | Decision | Reason |
|---|---|---|---|---|
| Appointment management | Yes | Yes | Accept | It directly matches the client's need to manage appointments. |
| Facial recognition login | No | No | Reject | The client did not request facial recognition, and it adds unnecessary security complexity. |
| AI diagnosis recommendations | No | No | Reject | The client wants appointment management, not medical diagnosis features. |
| Patient search | Yes | Yes | Accept | It addresses the problem of patient records being difficult to find. |
| Online payment | No | No | Reject | Payments were not requested and would add financial functionality outside the stated need. |
| Practitioner schedule view | Yes | Yes | Accept | It addresses the limited visibility of practitioner availability. |
| Insurance processing | No | No | Reject | Insurance processing was not requested and would add unnecessary complexity. |
| Treatment-plan generation | No | No | Reject | Treatment planning is not part of managing patients, practitioners or appointments. |

## Exit Question

**Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.**

Testing and verifying the software is the activity that matters most because AI-generated code can run without errors while still being logically incorrect, so an engineer must check that it actually meets the client's requirements.