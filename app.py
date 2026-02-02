from fastapi import FastAPI
from sqlalchemy import create_engine, text
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

app = FastAPI()
fake = Faker('en_IN')

# ... (imports at the top)

# ... (after your imports)

# 1. Database Configuration Variables
DB_USER = "postgres"
DB_PASSWORD = "Poornimap24"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "hospital_analytics"

# 2. Define the Connection String
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Create the Engine (THIS LINE IS CRITICAL)
engine = create_engine(DATABASE_URL)

# 4. Your FastAPI endpoints follow below...
@app.post("/run-etl")
def run_hospital_etl():
    # Code can now find 'engine' globally
    # Now 'engine' will be recognized here
    """Generates 1,000+ records to meet project requirements."""
    try:
        # 1. Generate Doctors (Workload tracking)
        depts = ['Cardiology', 'Oncology', 'Orthopedics', 'Pediatrics', 'Emergency', 'General Medicine']
        branches = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']

        doctors = []
        for i in range(1, 21):
            doctors.append({
                'name': f"Dr. {fake.name()}",
                'department': random.choice(depts),
                'branch': random.choice(branches)
            })
        pd.DataFrame(doctors).to_sql('dim_doctors', engine, if_exists='append', index=False)

        # 2. Generate Patients (Demographics: Age, Gender, Insurance)
        patients = []
        for i in range(1, 501):
            patients.append({
                'name': fake.name(),
                'age': random.randint(1, 85),
                'gender': random.choice(['Male', 'Female', 'Other']),
                'insurance_type': random.choice(['Private', 'Government', 'None'])
            })
        pd.DataFrame(patients).to_sql('dim_patients', engine, if_exists='append', index=False)

        # 3. Generate Admissions (Fact Table for KPIs)
        admissions = []
        outcomes = ['Recovered', 'Improved', 'Transferred', 'Deceased']
        for i in range(1, 1001):
            adm_date = fake.date_time_between(start_date='-1y', end_date='now')
            stay_days = random.randint(1, 14)
            dis_date = adm_date + timedelta(days=stay_days)

            admissions.append ({
                'patient_id': random.randint(1, 500),
                'doctor_id': random.randint(1, 20),
                'admission_date': adm_date,
                'discharge_date': dis_date,
                'case_type': random.choice(['Emergency', 'Scheduled']),
                'outcome': random.choices(outcomes, weights=[70, 20, 5, 5])[0],
                'total_cost': round(random.uniform(15000, 250000), 2),
                'is_readmission': random.random() < 0.12  # 12% Readmission rate
        })
        pd.DataFrame(admissions).to_sql('fact_admissions', engine, if_exists='append', index=False)

        return {"status": "Data Loaded Successfully", "records": 1520}
    except Exception as e:
        return {"status": "Error", "detail": str(e)}