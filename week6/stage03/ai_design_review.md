# SmartCare AI Design Review (Stage 3)

## Part E – AI Design Review

**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt given:**
Act as a software design reviewer. Based only on the confirmed SmartCare requirements, suggest the classes and relationships for a domain model. Do NOT invent new requirements. For every class or relationship you suggest, state which requirement ID (FR-xx) supports it. If something is not supported by a requirement, do not include it.

**Summary of Copilot's review:**
- Agreed my three classes (Patient, Practitioner, Appointment) are sufficient and supported by the cited FRs.
- Suggested modelling patient, practitioner, appointments and appointmentHistory as relationships/associations rather than stored attributes.
- Confirmed the one-to-many relationships (Patient 1 — 0..* Appointment; Practitioner 1 — 0..* Appointment).
- Explicitly declined to add classes not supported by the requirements (e.g. MedicalRecord, Schedule, Notification, Reminder, Payment, Clinic), stating they were not justified by the FR references provided.

## Part F – Compare and Decide

| AI suggestion | Decision | Reason / evidence | Model change |
|---|---|---|---|
| Model patient and practitioner on Appointment as relationships instead of attributes. | Accepted | This makes more sense because an appointment connects a patient and a practitioner. FR-04 supports creating appointments for patients with practitioners. | Patient and Practitioner are shown as relationships with Appointment instead of attributes inside Appointment. |
| Remove appointmentHistory as a stored attribute and represent it through the Appointment relationship. | Modified | FR-08 requires the system to allow staff to view a patient's appointment history, but it does not say the history needs to be stored as a separate attribute. | Removed appointmentHistory as an attribute and used the Patient–Appointment relationship to represent the history. |
| Add extra classes such as MedicalRecord, Notification, Payment or Clinic. | Rejected | These classes are not supported by any of the confirmed functional requirements. Adding them would introduce features that the client did not ask for. | No extra classes were added to the domain model. |