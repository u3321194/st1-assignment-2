# SmartCare v0.1 – Initial Engineering Brief and AI Activity Card

## 1. Problem Summary

SmartCare currently uses spreadsheets and paper records to manage patients, practitioners and appointments. This can lead to duplicate bookings, difficulty finding patient records, inconsistent appointment statuses and limited visibility of practitioner availability. The clinic wants a small and simple system to manage this information without becoming a complex hospital information system. However, the current request is not detailed enough to start coding because important requirements are still unclear. For example, the clinic has not confirmed the appointment time format, who can make changes, what counts as a duplicate booking, or how appointment data should be stored.

## 2. Initial Stakeholders

| Stakeholder | Possible need |
|---|---|
| Reception | Fast booking and searching of patient and appointment information. |
| Practitioners | Access to patient history and their appointment schedules. |
| Patients | Accurate and private patient records and appointment information. |
| Management | A small, simple and maintainable system. |

## 3. Initial Features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Appointment management | Confirmed | The client directly said they need software to manage appointments. |
| Patient search | Confirmed | The brief identifies difficulty finding patient records as a current problem. |
| Practitioner schedule view | Confirmed | The brief identifies limited visibility of practitioner availability as a current problem. |
| Cancel appointments | Provisional | Cancellation is identified as a current problem, but the exact cancellation requirements and permissions have not been fully confirmed. |

## 4. Questions for the Client

1. What patient information needs to be stored besides the patient's name and ID?
2. What should count as a duplicate booking?
3. Who should be allowed to create, edit and cancel appointments?
4. What appointment statuses should the system support?
5. Should cancelled appointments remain in the appointment history, and does the data need to be saved permanently?

## 5. What We Do Not Yet Know

1. **Appointment time format:** We do not yet know what format the clinic wants for appointment dates and times.
2. **Permanent data storage:** We do not know whether appointment and patient data must be saved permanently after the program is closed.
3. **Appointment statuses:** We do not yet know which appointment statuses the clinic wants the system to support.

---

# AI Activity Card – Ask, Check, Explain

## Before AI

Before using AI, I understood that the code stored appointments as dictionaries in a list and allowed users to book and display appointments. I could already see problems such as data not being saved, hard-coded input, double-booking, no time validation, and no way to edit or cancel appointments.

## AI Request

Tool: Microsoft Copilot (UC-approved GenAI tool). Prompt used (full details in `ai_usage.md`):

> Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function. 1. Explain what the code does. 2. Identify three limitations. 3. Suggest improvements. 4. Do not rewrite the whole application. 5. Ask me two questions to test my understanding.

## Evaluate

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Global list is a limitation | ✔ | | | |
| No validation | ✔ | | | |
| No duplicate handling | ✔ | | | |
| Use a class | ✔ | | | |
| Check for booking conflicts | ✔ | | | |

## Decide

| Suggestion | Decision | Reason |
|---|---|---|
| Global list is a limitation | Accept | A global list becomes harder to manage as the program grows. |
| No validation | Accept | Acted on in Part G – validation added for patient, practitioner and time. |
| No duplicate handling | Accept | Confirmed in Part F – a second appointment for the same practitioner and time was accepted. |
| Use a class | Keep unverified | Not needed for the Stage 1 prototype; to be considered in later stages. |
| Check for booking conflicts | Keep unverified | Not implemented or tested in Stage 1; requires clarifying what counts as a duplicate booking. |

## Verify

- [x] Run the code
- [x] Test normal input
- [x] Test unusual input (blank names and `None`)
- [x] Compare with requirements
- [ ] Ask tutor/peer
- [ ] Check documentation

I ran the code, tested normal input, tested unusual input including blank names and `None`, and tested double-booking. I also compared the results with the requirements. Results are recorded in Part F of `ai_usage.md`.

## Explain

**Can I explain the final code without reading the AI response?**
Yes. I can explain that it stores appointments in a list of dictionaries and uses functions to book and display appointments, with validation added for the required fields.

**What do I still need to understand?**
I still need to understand how to properly prevent double-booking and how to save appointment data permanently.