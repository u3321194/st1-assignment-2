# AI Engineering Log – Stage 4

**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt given:**
Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.
(Plus the Appointment attributes, business rules and status list.)

**AI-generated contribution:**
Copilot produced the Appointment class as a dataclass with an AppointmentStatus enum, protected status transitions via cancel() and complete(), a class-level registry to prevent practitioner double-booking, and validation in __post_init__. It also explained its design decisions.

**My decisions and changes:**
- Fixed two bugs before use: `from future import annotations` → `from __future__ import annotations`, and `def post_init` → `def __post_init__` (without this, no validation would run).
- Found that `status` was still a public field, so any code could set it directly and bypass cancel()/complete(). Changed it to a private `_status` with a read-only `status` property.
- Found that cancel() did not free the booked slot, so a cancelled time could never be rebooked. cancel() now removes the slot from the registry.
- Replaced the `Any` type hints for patient and practitioner with `Patient` and `Practitioner`.
- Accepted the enum and protected transitions (matched the UML and business rules).
- Accepted the added complete() method, noting it makes COMPLETED a terminal state.
- Kept the class focused: no database, UI, notification or service classes were added.

**Verification evidence:**
I tested the classes in test_checks.py. The output confirmed: a valid appointment is created as SCHEDULED, an empty patient name is rejected, a scheduled appointment can be cancelled, and cancelling an already-cancelled appointment is blocked. After the further fixes, I added four more checks: setting status directly is rejected, double-booking is rejected, a cancelled slot can be rebooked, and a completed appointment cannot be cancelled. All eight checks passed (full output in implementation_workbook.md).