# Kitabu Stop

Kitabu Stop is a Django-based web application designed to provide users with access to free educational resources and a curated selection of books for purchase. The platform aims to make education accessible to everyone by offering a blend of free content and affordable books.

## Features

- **User Registration and Login**: Users can register and log in to access resources and purchase books.
- **Book Store**: Browse and purchase books with sale options.
- **Free Resources**: Access and download free educational resources.
- **Payment Integration**: Integrated with M-Pesa for seamless payments using `django_daraja`.
- **Responsive Design**: Mobile-friendly interface for all pages.
- **Contact Us**: Users can send messages or reach out via WhatsApp or phone.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

Ensure you have the following installed:

- Python (3.8 or higher)
- MySQL
- Virtualenv (optional but recommended)

### Steps

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd Kitabu-Stop
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   pip install django django_daraja pillow mysqlclient
   ```

4. **Configure Database**

   Create the database:

   ```sql
   CREATE DATABASE Kitabu_Stop;
   ```

   Update the `DATABASES` setting in your `settings.py` file:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'Kitabu_Stop',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
   }
   ```

5. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic
   ```

6. **Run the Server**

   ```bash
   python manage.py runserver
   ```

## Usage

- **Admin Panel**: Access the admin panel at `/admin` to manage users, products, and resources.
- **Book Store**: Browse and purchase books from the `/shop` page.
- **Free Resources**: Access free resources from the `/resources` page.
- **Payment**: Use the `/pay` page to make payments via M-Pesa.

## Dependencies

- **Django**: Web framework for building the application.
- **django_daraja**: Integration with M-Pesa for payment processing.
- **Pillow**: Image processing library for handling uploaded images.
- **mysqlclient**: MySQL database connector for Django.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [django_daraja](https://pypi.org/project/django-daraja/)
- [Pillow](https://pillow.readthedocs.io/)