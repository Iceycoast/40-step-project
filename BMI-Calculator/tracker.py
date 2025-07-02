import json
from typing import List, Dict
from pathlib import Path
from bmi import BMI

class BMITracker:
    def  __init__(self,filename:str = "bmi_log.json"):
        self.filename = Path(filename)
        self.data = self.load_data()


    def load_data(self) -> list[dict]:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def save_data(self):
        with open(self.filename, 'w', encoding= 'utf-8') as f:
            json.dump(self.data, f, indent=4)


    def add_data(self,bmi_entry:BMI) -> str:
        entry = bmi_entry.to_dict()
        self.data.append(entry)
        self.save_data()
        return "your entry has been added succesfully"
    

    def get_entries_for(self, name: str) -> list[dict]:
        return [entry for entry in self.data if entry['name'].lower() == name.lower()]
    

    def view_logs_by_name(self, name: str) -> str:
        entries = self.get_entries_for(name)

        if not entries:
            return f"No entries found for {name}."

        return "".join([self.format_entry(entry, idx) for idx, entry in enumerate(entries, 1)])


    def get_user_log_count(self, name:str) -> int:
        return len(self.get_entries_for(name))


    def delete_all_by_name(self, name: str) -> str:
        matches = self.get_entries_for(name)
        if not matches:
            return f"No entries found for {name}."

        self.data = [entry for entry in self.data if entry['name'].lower() != name.lower()]
        self.save_data()
        return f"Deleted {len(matches)} entries for {name}."


    def delete_entry_by_index(self, name:str, index:int) -> str:
        matches = self.get_entries_for(name)
        if not matches:
            return f"No logs found for {name}"
        
        for idx, entry, in enumerate(matches,1):
            print(f"{idx}. {entry['date']} - BMI: {entry['bmi']} - {entry['category']}")

        if index<1 or index > len(matches):
            return f"Invalid index. {name} only has {len(matches)} entries."

        count = 0 
        for i, entry in enumerate(self.data,):
            if entry['name'].lower() == name.lower():
                count += 1 
                if count == index:
                    del self.data[i]
                    self.save_data()
                    return f"Entry {index} for {name} has been deleted."
                
        return f"❌ Failed to delete entry {index} for {name}."
    

    def format_entry(self, entry:dict, idx:int) -> str:
        return(
            f"\n\n🔹 ENTRY {idx}"
            f"\nDate:      {entry['date']}"
            f"\nName:      {entry['name']}"
            f"\nAge:       {entry['age']}"
            f"\nGender:    {entry['gender']}"
            f"\nHeight:    {entry['height']} cm"
            f"\nWeight:    {entry['weight']} kg"
            f"\nBMI:       {entry['bmi']}"
            f"\nCategory:  {entry['category']}"
            f"\nAI Advice: {entry['advice']}"
            f"\n" + "-" * 30
        )
    

    def view_data(self) -> str:
        if not self.data:
            return "No entries found"
        return "".join([self.format_entry(entry,idx) for idx, entry in enumerate(self.data,1)]) 