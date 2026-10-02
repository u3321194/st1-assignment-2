# Part A – Understand the Problem

## What data must be stored?
- **Patient name:** identifies the patient who has the appointment.
- **Practitioner name:** identifies which practitioner the patient is seeing.
- **Appointment time:** records when the appointment is scheduled.

These details are stored in a dictionary, with each appointment stored in the `appointments` list.

## What functions might be useful?
- `book_appointment()`: allows the receptionist to create a new appointment.
- `display_appointments()`: displays the appointments that have been booked.
- `edit_appointment()`: allows the receptionist to change an existing appointment.
- `cancel_appointment()`: allows the receptionist to cancel an appointment.
- `check_availability()`: checks whether a practitioner is already booked at a particular time.

## What could go wrong?
- **Data loss:** appointment data could be lost when the program is closed because it is not saved permanently.
- **Double booking:** a practitioner could be booked twice because the program does not check for existing appointments.
- **Invalid time:** an incorrect or invalid appointment time could be entered.
- **Blank inputs:** blank or `None` values could be entered for patient, practitioner or time.
- **Global list:** the `appointments` list could become difficult to manage as the program grows.
- **No editing or cancelling:** there is no way to edit or cancel an appointment.

## What requirements are unclear?
- **Time format:** what format should the appointment time use?
- **Duplicate booking:** what should count as a duplicate booking?
- **Patient details:** what patient information needs to be stored besides their name?
- **User permissions:** who is allowed to book, edit or cancel an appointment?
- **Data storage:** does appointment data need to be saved permanently after the program is closed?