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

6. Load static images
```bash
python manage.py collectstatic --noinput
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ in your browser to see the website.

## Deployment

Website is running on this site https://amee.pythonanywhere.com you can check.

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
- Email: ameygolait123@gmail.com
- Website: https://www.icecreamwonderland.com
