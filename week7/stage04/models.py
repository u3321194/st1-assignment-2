from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, time
from enum import Enum
from typing import ClassVar, Set, Tuple, Any


class Patient:
    def __init__(self, name: str, patient_id: str):
        if not name:
            raise ValueError("Patient name cannot be empty")
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        self.name = name
        self.patient_id = patient_id


class Practitioner:
    def __init__(self, name: str, practitioner_id: str, specialty: str):
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")
        self.name = name
        self.practitioner_id = practitioner_id
        self.specialty = specialty


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


@dataclass
class Appointment:
    patient: Any
    practitioner: Any
    date: date
    time: time
    status: AppointmentStatus = field(default=AppointmentStatus.SCHEDULED, init=False)

    _booked_slots: ClassVar[Set[Tuple[int, date, time]]] = set()

    def __post_init__(self) -> None:
        if self.patient is None:
            raise ValueError("An appointment requires a patient.")
        if self.practitioner is None:
            raise ValueError("An appointment requires a practitioner.")
        if self.date is None or self.time is None:
            raise ValueError("An appointment requires a date and time.")
        slot = self._slot_key()
        if slot in Appointment._booked_slots:
            raise ValueError("The practitioner already has an appointment at this date and time.")
        Appointment._booked_slots.add(slot)

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("A cancelled appointment cannot be cancelled again.")
        if self.status == AppointmentStatus.COMPLETED:
            raise ValueError("A completed appointment cannot be cancelled.")
        self.status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("A cancelled appointment cannot be changed to another status.")
        if self.status == AppointmentStatus.COMPLETED:
            raise ValueError("Appointment is already completed.")
        self.status = AppointmentStatus.COMPLETED

    def _slot_key(self) -> Tuple[int, date, time]:
        return (id(self.practitioner), self.date, self.time)