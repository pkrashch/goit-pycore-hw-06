# GoIT Python Core - Home Work 06: Object-Oriented Programming (OOP)

## Project Overview

This repository implements core **Object-Oriented Programming (OOP)** principles by building a fully functional, self-contained **Address Book** system.

---

## Repository Structure and Functionality (Solutions)

| Class | Purpose | Key Functionality |
| :--- | :--- | :--- |
| **`Field`** | Base class for all fields | Stores the field value (`self.value`). |
| **`Name`** | Name field | Inherits from `Field`. |
| **`Phone`** | Phone field | Implements **validation** (10 digits only) via `__init__`. |
| **`Record`** | Contact entry | Encapsulates `Name` and a list of `Phone` objects. Implements **add, remove, find, and edit** phone numbers. |
| **`AddressBook`** | Contact book | Inherits from **`collections.UserDict`**. Implements **`add_record`**, **`find`**, and **`delete`** methods. |

---

## Applied OOP Principles

* **Encapsulation:** Contact data (`self.phones`) is managed exclusively through the object's methods.
* **Inheritance:** `Name` and `Phone` inherit base functionality from the `Field` class.
* **Validation:** Custom exceptions (`raise ValueError` and implicit `KeyError`) are used to ensure data integrity.