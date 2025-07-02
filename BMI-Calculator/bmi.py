from datetime import datetime
from health_advice import get_health_advice

class BMI:
    def __init__(self,name,age,gender,height_cm,weight_kg):
        self.name = name
        self.age = age
        self.gender = gender 
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.date = datetime.now()

    def calculate_bmi(self) -> float :
        height = self.height_cm/100
        return round(self.weight_kg/(height**2),1)
    
    def get_bmi_category(self,bmi:float) -> str:
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25:
            return "normal"
        elif 25 <= bmi < 30:
            return "overweight"
        else:
            return "obsese"

    def raw_dict(self) -> dict:
        return {
            "date": self.date.strftime("%d-%m-%Y"),
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height_cm,
            "weight": self.weight_kg
        }
    def add_derived_dict(self,data_dict:dict) -> dict:
        bmi = self.calculate_bmi()
        category = self.get_bmi_category(bmi)
        advice = get_health_advice(self.age, self.gender, bmi, category)

        data_dict.update({
            "bmi": bmi,
            "category": category,
            "advice": advice
        })
        return data_dict
    
    def to_dict(self) -> dict:
        return self.add_derived_dict(self.raw_dict())