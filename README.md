News Portal - জনপদ সংবাদ
Welcome to জনপদ সংবাদ, a Django-based news portal designed to manage and publish articles with user-friendly features like tagging, categorization, and commenting. This project is ideal for developing your skills in Django by working on an advanced, feature-rich application.

Table of Contents
Features
Technologies
Installation
Usage
Project Structure
License
Features
Article Management: CRUD operations for articles, including rich text editing, categorization, and tagging.
Categorization and Tagging: Articles can be assigned to categories and tagged for easy navigation and filtering.
Commenting System: Allows readers to leave comments with optional name and email input.
User Authentication: User registration, login, and profile management for authors.
Admin Dashboard: A dedicated dashboard for administrators to manage content and monitor site activity.
Technologies
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap (for styling)
Database: SQLite (or any other supported database of your choice)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Wahidu1/news-portal.git
cd news-portal
Create a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Go to http://127.0.0.1:8000/ to view the news portal.
For admin access, go to http://127.0.0.1:8000/admin/.
Usage
Admin Dashboard: Manage categories, articles, comments, and tags.
Author Management: Add and edit authors, view their profiles, and manage their articles.
Commenting: Allows readers to comment on articles, providing valuable feedback.
Project Structure
plaintext
Copy code
news-portal/
├── newsportal/             # Django app containing models, views, and templates
├── static/                 # Static files (CSS, JavaScript, images)
├── templates/              # HTML templates for rendering views
├── manage.py               # Django management script
├── requirements.txt        # Python package requirements
└── README.md               # Project README
License
This project is open source and available under the MIT License.
