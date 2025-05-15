# Healthcare Backend System - Django REST Framework

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![DRF](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A backend system for a healthcare application built with Django REST Framework and PostgreSQL, featuring JWT authentication and management of patient-doctor relationships.

## Features

- **User Authentication**: Secure JWT-based registration and login system
- **Patient Management**: Create, read, update, and delete patient records
- **Doctor Management**: Create, read, update, and delete doctor records
- **Patient-Doctor Mapping**: Assign doctors to patients and manage relationships
- **RESTful API**: Clean, well-structured endpoints following REST conventions
- **PostgreSQL Database**: Relational database for secure data storage

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in and receive JWT tokens

### Patient Management
- `POST /api/patients/` - Add a new patient (Authenticated)
- `GET /api/patients/` - List all patients (Authenticated)
- `GET /api/patients/<id>/` - Get patient details
- `PUT /api/patients/<id>/` - Update patient details
- `DELETE /api/patients/<id>/` - Delete a patient

### Doctor Management
- `POST /api/doctors/` - Add a new doctor (Authenticated)
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/<id>/` - Get doctor details
- `PUT /api/doctors/<id>/` - Update doctor details
- `DELETE /api/doctors/<id>/` - Delete a doctor

### Patient-Doctor Mapping
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/` - List all mappings
- `GET /api/mappings/<patient_id>/` - Get doctors for a patient
- `DELETE /api/mappings/<id>/` - Remove doctor from patient

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/healthcare-backend.git
   cd healthcare-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your_django_secret_key
   DB_NAME=healthcare_db
   DB_USER=db_user
   DB_PASSWORD=db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing the API

You can test the API endpoints using Postman or any API client:

1. Register a new user at `POST /api/auth/register/`
2. Login to get JWT tokens at `POST /api/auth/login/`
3. Use the access token in the Authorization header for protected endpoints:
   ```
   Authorization: Bearer <your_access_token>
   ```
