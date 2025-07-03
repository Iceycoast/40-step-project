from pathlib import Path
import json
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent

MEAL_LOG = BASE_DIR / "MealLogger" / "meal_logs.json"
WATER_LOG = BASE_DIR / "Water-Intake-tracker" / "water_intake.json"
BMI_LOG = BASE_DIR / "BMI-Calculator" / "bmi_log.json"

def load_json(path: Path):
    if not path.exists():
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Could not parse JSON from {path.name}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error reading {path.name}: {e}")
        return []

def list_to_dict_by_date(entries):
    result = defaultdict(list)
    for entry in entries:
        date = entry.get('date')
        if date:
            result[date].append(entry)
    return dict(result)

def extract_water_summary(water_data: dict) -> dict:
    summary = defaultdict(dict)
    for date, entries in water_data.items():
        total_ml = sum(entry.get('quantity', 0) for entry in entries)
        summary[date]['water_ml'] = total_ml
    return summary

def extract_meal_summary(meal_data: dict) -> dict:
    summary = defaultdict(dict)
    for date, entries in meal_data.items():
        total_calories = sum(entry.get('calories', 0) for entry in entries)
        summary[date]['calories'] = total_calories
    return summary

def extract_bmi_summary(bmi_data: list) -> dict:
    summary = defaultdict(dict)
    for entry in bmi_data:
        date = entry.get('date')
        if not date:
            continue
        summary[date]['bmi'] = entry.get('bmi')
    return summary

def get_aggregated_data():
    meal_data_raw = load_json(MEAL_LOG)
    water_data_raw = load_json(WATER_LOG)
    bmi_data = load_json(BMI_LOG)

    meal_data = meal_data_raw if isinstance(meal_data_raw, dict) else list_to_dict_by_date(meal_data_raw)
    water_data = water_data_raw if isinstance(water_data_raw, dict) else list_to_dict_by_date(water_data_raw)

    summary = defaultdict(dict)

    water_summary = extract_water_summary(water_data)
    meal_summary = extract_meal_summary(meal_data)
    bmi_summary = extract_bmi_summary(bmi_data)

    for date in water_summary:
        summary[date].update(water_summary[date])
    for date in meal_summary:
        summary[date].update(meal_summary[date])
    for date in bmi_summary:
        summary[date].update(bmi_summary[date])

    return dict(summary)
