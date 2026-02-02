-- Create Schema for Hospital Performance Dashboard
-- Compatible with PostgreSQL and MySQL

-- 1. Patient Dimension Table
CREATE TABLE public.dim_patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20), -- Supports Male, Female, Other
    insurance_type VARCHAR(50) -- Supports Government, None, Private
);

-- 2. Doctor Dimension Table
CREATE TABLE public.dim_doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

-- 3. Admissions Fact Table
CREATE TABLE public.fact_admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    department VARCHAR(50), -- Cardiology, Emergency, Oncology, etc.
    admission_date DATE,
    discharge_date DATE,
    case_type VARCHAR(50), -- Emergency, Scheduled
    outcome VARCHAR(50), -- Deceased, Improved, Recovered, Transferred
    is_readmission BOOLEAN, -- Used for Readmission Rate (11.67%)
    total_cost DECIMAL(10, 2),
    FOREIGN KEY (patient_id) REFERENCES public.dim_patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES public.dim_doctors(doctor_id)
);