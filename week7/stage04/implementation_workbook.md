# SmartCare v0.4 – Domain Implementation Workbook

## Part A – Approved UML (confirmed before coding)
The implementation follows the approved Stage 3 UML: Patient (name, ID), Practitioner (name, ID, specialty), and Appointment (patient, practitioner, date, time, status), with one-to-many relationships between Patient/Practitioner and Appointment.

## 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
|---|---|---|---|
| Patient (name, ID) | Patient class | Yes | Type hints + validation for empty name/ID |
| Practitioner (name, ID, specialty) | Practitioner class | Yes | Adds specialty; no database logic |
| Appointment (patient, practitioner, date, time, status) | Appointment dataclass | Yes | Uses AppointmentStatus enum |
| Status attribute | AppointmentStatus enum | Yes | SCHEDULED, COMPLETED, CANCELLED |
| One-to-many relationships | patient/practitioner passed into Appointment | Yes | Appointment links a Patient and Practitioner |

## 2. Domain Invariants

| Class | Invariant / rule | How protected |
|---|---|---|
| Patient | Name and ID cannot be empty | ValueError raised in __init__ |
| Practitioner | Name and ID cannot be empty | ValueError raised in __init__ |
| Appointment | Must have patient, practitioner, date and time | ValueError raised in __post_init__ |
| Appointment | A practitioner cannot be double-booked | Class-level _booked_slots registry checks the slot |
| Appointment | Status changes only via methods, not direct assignment | cancel() and complete() control transitions |
| Appointment | A cancelled appointment cannot be cancelled again or reactivated | cancel()/complete() raise ValueError on illegal transitions |

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
|---|---|---|
| Appointment – Patient | Composition / association | An appointment *has* a patient; it is not a type of patient |
| Appointment – Practitioner | Composition / association | An appointment *has* a practitioner; not inheritance |
| Appointment – PatientRecord | No inheritance | Appointment is not a kind of patient record; inheritance would be wrong |

## Part E – Review of AI-Generated Code (Appointment)

| Check | Finding | Action |
|---|---|---|
| Model consistency | Appointment matches the UML (patient, practitioner, date, time, status) | Accepted |
| Bug: `from future import annotations` | Should be `from __future__ import annotations` — would crash | Fixed |
| Bug: `def post_init` | Should be `__post_init__`, or validation never runs | Fixed |
| Public state mutation | Status cannot be set directly; only via cancel()/complete() | Good, kept |
| Unnecessary inheritance | None added | Good |
| Invented dependencies | No database/UI/notification/service classes added | Good |
| Error handling | Raises ValueError for invalid input and illegal transitions | Good, kept |
| Extra `complete()` method | Added beyond the UML; AI justified it as making COMPLETED terminal | Accepted with note |

## Part G – Refactor
After reviewing the AI-generated Appointment class, I fixed two bugs (`__future__` import and `__post_init__` method name) so validation and conflict-checking actually run. No unnecessary classes or dependencies were added by the AI, so no further removal was needed. The final implementation stays consistent with the approved UML: three focused classes, type hints, validation, and protected status transitions.