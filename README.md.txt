Project README: Hospital Performance Dashboard
Project Overview
This project provides a data-driven solution for hospital administrators to monitor clinical and operational efficiency. It tracks critical metrics such as Bed Occupancy Rate (180.00%), Average Length of Stay (7.48 days), and Doctor Utilization (45.00%).

Technical Architecture
Following the project's tooling restrictions, the solution consists of:

Database: A PostgreSQL/MySQL database structured with the provided schema.sql to manage patient demographics and admission facts.

Backend: A Flask/FastAPI application (app.py) that serves as the API layer for data extraction and transformation.

Frontend/BI: An interactive Power BI dashboard (Hospital performance dashboard.pbix) for real-time visualization and filtering.

Data Connectivity
The Power BI dashboard connects to the database via the backend API to ensure data integrity.

Users can interact with the dashboard using Department buttons (e.g., Cardiology, Emergency) and Slicers for Insurance and Case Type to filter the admission volume and outcomes.