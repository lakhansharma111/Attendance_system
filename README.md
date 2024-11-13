# Attendance_system
Attendance Management System with Image Capture

# Objective
Develop a web application that allows a manager to create a roster for staff. Staff members should 
be able to mark their attendance by capturing their image using the webcam on a site-available 
laptop.

## Backend Requirements:
- Authentication & Authorization:
- Implement roles: Manager and Staff. Only authenticated managers can create/edit/view the roster. Only authenticated staff can mark their attendance.
- Roster Management:
- Managers should be able to Add new staff members to the roster. Set working days and shifts for each staff member, allowing different shifts for different days of the  week. Set 1-2 weekly offs per staff member. View the complete roster. Edit the details of any staff member in the roster.
- Staff members should be able to: Interchange their shifts among themselves.
### Attendance Management:
- Staff members should be able to: View their assigned shifts. Mark their attendance by capturing an image using the webcam, but only within 1 hour of their shift  timings. The system should store the attendance data, timestamp, and the captured image.








## Setup
 Clone the Repository:
 
git clone https://github.com/your-username/attendance-management-system.git
cd attendance-management-system
Create a Virtual Environment:

python3 -m venv env
source env/bin/activate
Install Dependencies:

pip install -r requirements.txt
Run Migrations:

python manage.py makemigrations
python manage.py migrate
Create a Superuser:

python manage.py createsuperuser
Run the Development Server:

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.
 
### API Endpoints
- 1. User Registration
Endpoint: POST /api/register/
RequestBody:
{
  "username": "saransh_vsi",
  "password": "Saransh@12",
"role": "Employee" or "Manager"
}
- 2. Login as a User
Endpoint: POST /api/token/
Request Body:
{
  "username": "saransh_vsi",
  "password": "Saransh@12"
}
Response:
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
Use the access token in further API requests for Authorization: Bearer <access_token>.
- 3. Add Employee (Manager Only)
Endpoint: POST /api/staff/
Request Body:
{
  "user": <user_id>,
  "weekly_off_days": "Saturday,Sunday"
}
- 4. Add Shift (Manager Only)
Endpoint: POST /api/shifts/
Request Body:
{
  "staff": <staff_id>,
  "day_of_week": "Monday",
  "shift_start": "00:00:00",
  "shift_end": "00:00:00"
}
- 5. Staff Attendance Register
Endpoint: POST /api/attendance/
Body Request (captured image in Base64):
{
  "staff": <staff_id>,
  "captured_image":  "image path"
} 
- 6. List of Attendees
Endpoint: GET /api/attendance/
Response:
[
  {
    "id": 1,
    "staff": 2,
    "timestamp": "",
    "captured_image": “image path"
  }
]
