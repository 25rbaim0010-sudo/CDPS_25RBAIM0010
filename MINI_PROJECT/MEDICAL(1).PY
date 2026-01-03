import random
import string

# -------------------- DATA MODELS --------------------

class Medicine:
    def __init__(self, name, dosage, frequency, duration, instructions):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.instructions = instructions


class Appointment:
    def __init__(self, department, doctor, date, time):
        self.id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        self.department = department
        self.doctor = doctor
        self.date = date
        self.time = time
        self.token = f"T{random.randint(100,999)}"
        self.medicines = self.sample_medicines()

    def sample_medicines(self):
        return [
            Medicine("Amoxicillin", "500mg", "3 times daily", "7 days", "After meals"),
            Medicine("Paracetamol", "650mg", "Every 6 hours", "5 days", "If fever"),
            Medicine("Vitamin D3", "60,000 IU", "Once weekly", "8 weeks", "With milk")
        ]


# -------------------- APPLICATION --------------------

class HospitalApp:
    def __init__(self):
        self.user = {}
        self.appointments = []
        self.departments = {
            "1": "Cardiology",
            "2": "Neurology",
            "3": "Orthopedics",
            "4": "General Medicine"
        }
        self.doctors = {
            "Cardiology": ["Dr. Rao", "Dr. Mehta"],
            "Neurology": ["Dr. Sharma", "Dr. Gupta"],
            "Orthopedics": ["Dr. Kumar", "Dr. Singh"],
            "General Medicine": ["Dr. Das", "Dr. Iyer"]
        }

    # ---------------- LOGIN ----------------
    def login(self):
        print("\n--- Login ---")
        self.user["name"] = input("Enter Name: ")
        self.user["phone"] = input("Enter Phone: ")
        print(f"\nWelcome {self.user['name']}!")

    # ---------------- DEPARTMENTS ----------------
    def select_department(self):
        print("\n--- Departments ---")
        for k, v in self.departments.items():
            print(f"{k}. {v}")
        choice = input("Select Department: ")
        return self.departments.get(choice)

    # ---------------- DOCTORS ----------------
    def select_doctor(self, department):
        print(f"\n--- Doctors in {department} ---")
        doctors = self.doctors[department]
        for i, d in enumerate(doctors, 1):
            print(f"{i}. {d}")
        return doctors[int(input("Select Doctor: ")) - 1]

    # ---------------- BOOK APPOINTMENT ----------------
    def book_appointment(self):
        dept = self.select_department()
        doctor = self.select_doctor(dept)
        date = input("Enter Date (DD-MM-YYYY): ")
        time = input("Enter Time (HH:MM): ")

        appointment = Appointment(dept, doctor, date, time)
        self.appointments.append(appointment)

        print("\n✅ Appointment Booked Successfully!")
        print(f"Token Number: {appointment.token}")

    # ---------------- HISTORY ----------------
    def view_history(self):
        print("\n--- Appointment History ---")
        if not self.appointments:
            print("No appointments found.")
            return

        for i, a in enumerate(self.appointments, 1):
            print(f"""
{i}. Token: {a.token}
   Department: {a.department}
   Doctor: {a.doctor}
   Date: {a.date}
   Time: {a.time}
""")

    # ---------------- MEDICINES ----------------
    def view_medicines(self):
        print("\n--- Prescribed Medicines ---")
        for a in self.appointments:
            print(f"\nToken: {a.token} | Doctor: {a.doctor}")
            for m in a.medicines:
                print(f"- {m.name} ({m.dosage}), {m.frequency}, {m.duration}")
                print(f"  Instructions: {m.instructions}")

    # ---------------- CANCEL ----------------
    def cancel_appointment(self):
        self.view_history()
        token = input("Enter Token Number to Cancel: ")
        self.appointments = [a for a in self.appointments if a.token != token]
        print("❌ Appointment Cancelled Successfully!")

    # ---------------- MENU ----------------
    def menu(self):
        while True:
            print("""
==============================
1. Book Appointment
2. View Appointment History
3. View Medicines
4. Cancel Appointment
5. Logout
==============================
""")
            choice = input("Select Option: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_history()
            elif choice == "3":
                self.view_medicines()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice!")


# -------------------- RUN APP --------------------

if __name__ == "__main__":
    app = HospitalApp()
    app.login()
    app.menu()
