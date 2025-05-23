# BlogStory
# Intuitive Blog Post Website

This repository contains a Django-based blog website project. It provides a basic blog platform with features like user authentication, blog post creation, category filtering, and a like system.

## Features

* User registration and login
* Creating and publishing blog posts
* Categorizing blog posts
* Filtering blogs by category and date
* Liking blog posts
* Responsive design

## Technologies Used

* Django
* Python
* HTML
* CSS
* JavaScript
* Bootstrap

## Project Structure

* **intuitive_blog_post_website/**: The main project directory.
    * `settings.py`: Project settings and configurations.
    * `urls.py`: URL routing for the project.
* **blogs/**: The blog application directory.
    * `models.py`: Database models for blog posts, categories, and likes.
    * `views.py`: View functions handling blog logic.
    * `templates/blogs/**`: HTML templates for blog pages.
    * `static/`: Static files (CSS, JavaScript).

## Installation

1. Clone the repository: `git clone https://github.com/your-username/intuitive-blog-post-website.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    * On Windows: `myenv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Apply database migrations: `python manage.py migrate`
6. Create a superuser account: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`
8. Start Command : `gunicorn intuitive_blog_post_website.wsgi`

## Config envs on render 
ALLOWED_HOSTS=**************
DATABASE_URL=**************
DB_HOST=**************
DB_NAME=**************
DB_PASSWORD=**************
DB_PORT=**************
DB_USER=**************
DJANGO_DEBUG=**************
DJANGO_SECRET_KEY=**************

## Usage

* Access the website in your browser at `http://127.0.0.1:8000/`.
* Register a new user or log in with an existing account.
* Create, edit, and publish blog posts.
* Filter blog posts by category and date.
* Like blog posts.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.