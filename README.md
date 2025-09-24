# Bulk Email Automation System using Django

## Project Overview
A web-based system to send personalized bulk emails using reusable templates and recipient lists. Allows admins to create email templates, upload CSV/Excel files with recipient data, and automatically send customized emails via Gmail SMTP.

## Features
- Upload CSV/Excel files with email addresses.
- Create dynamic email templates with placeholders (e.g., `{{username}}`).
- Send personalized HTML emails automatically.
- Secure email sending with CSRF protection.
- Gmail SMTP integration for reliable email delivery.

## Technologies Used
- **Backend:** Django, Python, Pandas
- **Frontend:** HTML, Bootstrap, Django Templates
- **Email Integration:** Gmail SMTP

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bulk-email-django.git
   
2. Navigate to the project directory:
   ```bash
   cd bulk-email-django
   
3. Install dependencies:
  ```bash
  pip install -r requirements.txt


4. Apply migrations:
  ```bash
  python manage.py migrate

5. Run the development server:
  ```bash
  python manage.py runserver
