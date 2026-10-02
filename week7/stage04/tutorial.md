# Stage 4 Tutorial – Object-Oriented Design Decisions

## Activity 1 – Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | Refuses an empty name or patient ID. | Other code can create a Patient and access its stored name and patient ID. |
| Practitioner | Refuses an empty name or practitioner ID. | Other code can create a Practitioner and access its name, practitioner ID and specialty. |
| Appointment | Requires a patient, practitioner, date and time, and prevents double-booking. Its status can only change through `cancel()` or `complete()`. | Other code can create it, read its status, or call `cancel()` and `complete()`. |

## Activity 2 – Composition or Inheritance?

| Relationship | Decision | Reason |
|---|---|---|
| Appointment and Patient | Composition/association | An Appointment has a Patient; it is not a type of Patient. |
| Appointment and Practitioner | Composition/association | An Appointment has a Practitioner; it is not a type of Practitioner. |
| Doctor and Practitioner (hypothetical) | Inheritance | A Doctor is a type of Practitioner and can share its common attributes. |
| Clinic and Appointment | Composition/association | A Clinic would have many Appointments; an Appointment is not a type of Clinic. |

## Activity 3 – Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**
Appointment – It should make the decision because the status is Appointment's own data and the transition rules belong to the Appointment.

**Who validates a patient name?**
Patient – It should validate the name because the name is the Patient's own data and Patient is responsible for its validity.

**Should Appointment execute SQL? Why?**
No – Appointment should not run SQL because database logic is separate from the domain model. If the database changes, Appointment could also need to change, creating unnecessary dependencies.

**Should the UI decide whether a status transition is legal?**
No – The rule should live in Appointment so every part of the program, including the UI and tests, must follow the same status-transition rules.

## Activity 4 – AI Code Critique

| Problem | What goes wrong | Correction |
|---|---|---|
| 1. Public status mutation | Any code can directly change `status` and bypass the rules in `cancel()` and `complete()`. | Make `_status` private and expose `status` as a read-only property so changes only happen through `cancel()` or `complete()`. |
| 2. SQL inside `cancel()` | Appointment becomes dependent on the database, making the class harder to maintain and test. | Move database operations into a separate data-access or persistence layer. |
| 3. NotificationManager dependency | Appointment depends on notifications even though automatic email/SMS notifications are out of scope. | Remove the NotificationManager dependency and keep notifications outside the Appointment class unless the requirement is confirmed. |
| 4. Inheritance from PatientRecord | Appointment is incorrectly treated as a type of PatientRecord, which does not match the domain model. | Use an association where Appointment has a Patient instead of inheriting from