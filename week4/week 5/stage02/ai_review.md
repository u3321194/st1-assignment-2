# SmartCare AI Requirements Review

## Part F – AI Requirements Review

Tool used: Microsoft Copilot (UC-approved GenAI tool)

Prompt given:
Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

Summary of Copilot's review:

- "Required patient information" (FR-01) is not defined — *evidence-based*.
- Appointment status types (FR-07) are not defined — *evidence-based*.
- Double-booking scope is inconsistent: the scope says "any double bookings" but FR-05 only covers practitioners — *evidence-based*.
- US-03 says patients are not booked at the same time, but FR-05 only prevents practitioner conflicts — *evidence-based*.
- "Authorised" staff (FR-03) is not defined — *needs validation*.
- "Managing" patients and practitioners is vague (create, edit or delete?) — *needs validation*.
- Whether appointment history includes cancelled appointments (US-05) — *needs validation*.
- Non-functional terms such as "reliable", "simple interface" and "predictable results" are not measurable — *evidence-based*.

Copilot did not invent new client requirements, it mainly raised clarification questions and flagged vague wording.

## Part G – Verify the AI Review

Define the required patient data — Accepted:
The brief states that the system will handle patient data, but it does not clarify exactly what type of data should be included. This needs to be clarified with the client.

Define the appointment statuses — Accepted:
The brief indicates that there is an issue with inconsistent appointment status, but it does not say what statuses should be included in the system.

Clarify the double booking issue (Scope vs FR-05) — Accepted:
The brief mentions duplicate bookings as a problem, while FR-05 specifically says that a practitioner cannot have two appointments at the same time. The exact definition of a duplicate booking should be clarified with the client.

Clarify authorised staff — Accepted:
FR-03 states that only authorised staff can create practitioner records. However, the brief does not say which staff members are authorised.

Clarify what managing includes — Accepted:
The scope says "managing patients and practitioners", but it does not explain what actions this includes, such as creating, viewing or updating records.

Clarify if history should include cancelled appointments — Unverified:
The brief requires an appointment history but does not specify whether cancelled appointments should remain in the history. This should be confirmed with the client rather than assumed.

Make non-functional requirements measurable — Modified:
Terms such as "reliable", "simple" and "predictable" are difficult to test exactly. Where possible, these should be made more specific, but no additional targets should be added without evidence from the client.

AI overreach — No major overreach identified:
The AI mainly identified areas that needed clarification rather than inventing new client requirements. Its suggestions were checked against the client brief before being accepted or modified.