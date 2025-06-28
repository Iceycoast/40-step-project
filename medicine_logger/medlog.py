import json
from datetime import datetime

class Medicine:
    def __init__(self, name, dose, time_taken, date_taken):
        self.name = name
        self.dose = dose
        self.time_taken = time_taken
        self.date_taken = date_taken

    def to_dict(self):
        return {
            "name": self.name,
            "dose": self.dose,
            "time taken": self.time_taken.strftime("%H:%M"),
            "date taken": self.date_taken.strftime("%d-%m-%Y"),
        }

class MedicineLog:
    def __init__(self, filename="medicine_logger/data/medicines.json"):
        self.filename = filename

    def add_medicine(self, name, dose, time_taken, date_taken):
        new_medicine = Medicine(name, dose, time_taken, date_taken)
        med_dict = new_medicine.to_dict()

        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for entry in data:
            if (
                entry['name'] == med_dict['name'] and
                entry['time taken'] == med_dict['time taken'] and
                entry['date taken'] == med_dict['date taken']
            ):
                return "\n❗️This already exists in the data."

        data.append(med_dict)
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

        return (
            "\n✅ Log added successfully."
            f"\n💊 Medicine: {med_dict['name']}"
            f"\n💉 Dose: {med_dict['dose']}"
            f"\n⏰ Time: {med_dict['time taken']}"
            f"\n📅 Date: {med_dict['date taken']}"
        )

    def view_medicines(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                data.sort(
                    key=lambda item: datetime.strptime(
                        f"{item['date taken']} {item['time taken']}", "%d-%m-%Y %H:%M"
                    )
                )
                logs = ""
                for item in data:
                    logs += (
                        f"\n📅 [{item['date taken']} | {item['time taken']}] "
                        f"💊 {item['name']} - 💉 {item['dose']}\n"
                    )
                return logs if logs else "\nNo logs found."
        except (FileNotFoundError, json.JSONDecodeError):
            return "\nLogs not found."