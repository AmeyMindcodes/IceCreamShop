# Ice Cream Wonderland

A delightful Django-based website for an ice cream shop, featuring a responsive design, online ordering system, and admin dashboard.

## Features

- Responsive design using Bootstrap 5
- Product catalog with different ice cream flavors
- Online ordering system
- Contact form for customer inquiries
- Admin dashboard for managing products, orders, and customer messages
- Image gallery
- Mobile-friendly interface

## Tech Stack

- Python 3.x
- Django 5.x
- Bootstrap 5
- SQLite (development) / PostgreSQL (production)
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/IceCreamShop.git
cd IceCreamShop
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser to see the website.

## Deployment

### Preparing for Production

1. Update settings for production:
   - Set `DEBUG = False` in settings.py
   - Update `ALLOWED_HOSTS` with your domain
   - Configure a production database (PostgreSQL recommended)
   - Set up proper email settings

2. Collect static files:
```bash
python manage.py collectstatic
```

### Deploying to PythonAnywhere

1. Sign up for a PythonAnywhere account at https://www.pythonanywhere.com/

2. Upload your code:
```bash
git clone https://github.com/yourusername/IceCreamShop.git
```

3. Set up a virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.9 icecreamshop-env
pip install -r requirements.txt
```

4. Configure the web app:
   - Go to the Web tab and create a new web app
   - Choose "Manual configuration" and select Python 3.9
   - Set the virtual environment path
   - Configure WSGI file to point to your Django project
   - Set up static files mapping

5. Configure environment variables:
   - Add environment variables for sensitive information
   - Set `DJANGO_SETTINGS_MODULE` to `IceCreamShop.settings`

6. Reload the web app and visit your site!

### Deploying to Heroku

1. Install the Heroku CLI and log in:
```bash
heroku login
```

2. Create a Procfile in your project root:
```
web: gunicorn IceCreamShop.wsgi --log-file -
```

3. Create a runtime.txt file:
```
python-3.9.7
```

4. Add the following to requirements.txt:
```
gunicorn
django-heroku
whitenoise
```

5. Update settings.py for Heroku:
```python
import django_heroku
# At the bottom of settings.py
django_heroku.settings(locals())
```

6. Create a new Heroku app:
```bash
heroku create icecream-wonderland
```

7. Add a PostgreSQL database:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

8. Push to Heroku:
```bash
git push heroku main
```

9. Run migrations:
```bash
heroku run python manage.py migrate
```

10. Create a superuser:
```bash
heroku run python manage.py createsuperuser
```

## Admin Dashboard

Access the admin dashboard at `/admin` to:
- Manage ice cream flavors
- View and process customer orders
- Read and respond to contact messages
- Update website content

## Customization

- Edit templates in the `templates` directory
- Modify styles in the CSS files
- Add new views in `core/views.py`
- Create new URL patterns in `core/urls.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or support, please contact:
- Email: info@icecreamwonderland.com
- Website: https://www.icecreamwonderland.com