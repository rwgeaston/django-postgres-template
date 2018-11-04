---
Quick local setup
---

Django project for storing entities! with names!

    docker-compose up

First time you run it you need to also do

    docker-compose exec web python app/manage.py migrate
    docker-compose exec web python app/manage.py createsuperuser

You need a local_settings.py file in main folder with settings like

    SECRET_KEY = 'testing'
    DEBUG = True
    ALLOWED_HOSTS = ['0.0.0.0']

But these are not appropriate for production. You can also make the google login button work somehow, idk.

API with GET/POST/PUT/DELETE is here

    http://0.0.0.0:8000/api/v1/things/

Django admin is, as usual, found at

    http://0.0.0.0:8000/admin/

For local development you should make a 3.6+ virtualenv and

    pip install -r local_requirements.txt
    ./test.sh

You will have a git precommit hook which runs pylint, unit tests and python black format enforcer.

---
AWS setup
---

Make an AWS account. Make an EC2 amazon linux instance. Save the .pem keyfile; follow instructions on AWS to ssh to it

yum install git, nginx

Install docker as https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#install_docker

and docker compose as https://docs.docker.com/compose/install/#install-compose

Make an ssh key as here https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/

and add the key to your github here https://github.com/settings/keys

Setup EC2 security group which allows inbound 80 and 443 and all outbound. Add your instance to this group.

    git clone https://github.com/rwgeaston/django-postgres-template django

If you want to clone it to a different folder, you'll have to change some stuff in nginx config.

    cp deployment_config/nginx.conf /etc/nginx/conf.d/default.conf

You might need to change some things in default.conf such as ip address, and maybe folder names depending on your
username and other setup.

    sudo chkconfig nginx on
    sudo service nginx start

You might need to chmod +x all the folders down to /files/ and then you should find http://0.0.0.0 and
http://0.0.0.0/great_document.txt work remotely with the appropriate ip address.

Since nginx is already looking for /admin/ and /api/ from port 8000, you should be able to follow instructions
 as in local setup and django will be live as well.
