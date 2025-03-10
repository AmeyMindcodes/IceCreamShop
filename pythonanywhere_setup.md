# Deploying Ice Cream Shop to PythonAnywhere (Free Tier)

PythonAnywhere offers a free tier that includes:
- 1 web app
- 512MB storage
- Shared CPU
- HTTPS support
- Custom domain support

## Step 1: Sign Up for PythonAnywhere

1. Go to [PythonAnywhere](https://www.pythonanywhere.com/) and sign up for a free account.

## Step 2: Set Up a Web App

1. After logging in, go to the Dashboard.
2. Click on the "Web" tab.
3. Click on "Add a new web app".
4. Choose "Manual configuration".
5. Select Python 3.11.
6. Click "Next" and your web app will be created.

## Step 3: Clone Your Repository

1. Go to the "Consoles" tab.
2. Start a new Bash console.
3. Clone your repository:
   ```bash
   git clone https://github.com/AmeyMindcodes/IceCreamShop.git
   ```

## Step 4: Set Up a Virtual Environment

1. In the Bash console, create and activate a virtual environment:
   ```bash
   cd IceCreamShop
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Step 5: Configure Your Web App

1. Go back to the "Web" tab.
2. In the "Code" section, set:
   - Source code: `/home/YOUR_USERNAME/IceCreamShop`
   - Working directory: `/home/YOUR_USERNAME/IceCreamShop`
   - WSGI configuration file: Click on the link to edit it

3. Replace the contents of the WSGI file with:
   ```python
   import os
   import sys

   # Add your project directory to the sys.path
   path = '/home/YOUR_USERNAME/IceCreamShop'
   if path not in sys.path:
       sys.path.insert(0, path)

   # Set environment variables
   os.environ['DJANGO_SETTINGS_MODULE'] = 'IceCreamShop.settings'
   os.environ['SECRET_KEY'] = 'your-secret-key-here'
   os.environ['DEBUG'] = 'False'
   os.environ['ALLOWED_HOSTS'] = 'YOUR_USERNAME.pythonanywhere.com'

   # Activate your virtual environment
   activate_this = '/home/YOUR_USERNAME/IceCreamShop/venv/bin/activate_this.py'
   with open(activate_this) as file_:
       exec(file_.read(), dict(__file__=activate_this))

   # Import Django
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

   Replace `YOUR_USERNAME` with your PythonAnywhere username.

4. In the "Virtualenv" section, set the path to your virtual environment:
   ```
   /home/YOUR_USERNAME/IceCreamShop/venv
   ```

## Step 6: Set Up Static Files

1. In the "Static files" section, add:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/IceCreamShop/staticfiles`
   
   And another entry:
   - URL: `/media/`
   - Directory: `/home/YOUR_USERNAME/IceCreamShop/media`

## Step 7: Collect Static Files and Migrate Database

1. Go back to your Bash console.
2. Make sure you're in the project directory and the virtual environment is activated.
3. Run:
   ```bash
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

## Step 8: Reload Your Web App

1. Go back to the "Web" tab.
2. Click the "Reload" button for your web app.

## Step 9: Access Your Website

Your website should now be accessible at:
```
https://YOUR_USERNAME.pythonanywhere.com
```

## Troubleshooting

If you encounter any issues:
1. Check the error logs in the "Web" tab.
2. Make sure all paths are correct and match your PythonAnywhere username.
3. Ensure your virtual environment is properly set up and all dependencies are installed.
4. Check that your ALLOWED_HOSTS setting includes your PythonAnywhere domain. 