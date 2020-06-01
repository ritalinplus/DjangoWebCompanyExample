# DjangoWebCompanyExample
Example of Company webpage made with Django, we find a couple of apps described below:

* core:  Manage statics and generic views like about, store and home.
* blog: Used for create and manage the categories and post for the blog section (through django customized admin).
* contact: Used for send emails using django forms.
* pages: Used for manage generic pages like legal notice and privacy policy (through django admin and ckeditor).
* services: Used for manage company services (through django admin)
* social: Used for manage social media (through django admin)

---------------------------------------------------

The users and groups created in the inital data are:

**Users:**

* root:toor
* test:098f6bcd4621d373cade4e832627b4f6

**Group**:

* Personal

In the initial data also appear a generic pages like privacy policy and couple of services and blogs entries.

---------------------------------------------------

To deploy:

* clone project
* `docker-compose up` in the docker-compose.yml path.
* Load initial_data fixture if you want `docker-compose run web python manage.py loaddata core/fixtures/initial_data.json`

