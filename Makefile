MANAGE = python manage.py
SOURCE = src

init-project:
	$(MANAGE) init_project

run:
	$(MANAGE) runserver

run-both:
	npm install --prefix ./frontend
	npm run watch --prefix ./frontend & $(MANAGE) runserver && fg

run-front:
	npm install --prefix ./frontend
	npm run watch --prefix ./frontend

fix:
	$(MANAGE) reset_db --noinput
	$(MANAGE) migrate  --noinput
	$(MANAGE) update_translation_fields
	$(MANAGE) sync_page_translation_fields
	rm -rf ./media/*
	$(MANAGE) init_project
	#npm install --prefix ./frontend
	$(MANAGE) runserver

fix-drooped-db:
	$(MANAGE) migrate  --noinput
	$(MANAGE) update_translation_fields
	$(MANAGE) sync_page_translation_fields
	rm -rf ./media/*
	$(MANAGE) init_project
	#npm install --prefix ./frontend
	$(MANAGE) runserver

mm:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

translation:
	$(MANAGE) update_translation_fields
	$(MANAGE) sync_page_translation_fields


docker-run:
	$(MANAGE) migrate --noinput
	#$(MANAGE) prod_init_project
	$(MANAGE) recovery_published_advertisements
	$(MANAGE) update_redis_om_filter_location_translations
	$(MANAGE) add_slug_to_all_advertisements
	$(MANAGE) compilemessages --ignore venv
	$(MANAGE) sync_page_translation_fields
	$(MANAGE) update_translation_fields
	$(MANAGE) collectstatic --noinput
	gunicorn config.wsgi:application --bind 0.0.0.0:8001 --workers 3 --access-logfile - --error-logfile - --log-level debug


run-vite:
	npm install --prefix ./frontend
	npm run build --prefix ./frontend

run-watch:
	npm run watch --prefix ./frontend

build:
	npm run build --prefix ./frontend

worker:
	celery -A config.celery_app worker -l INFO

beat:
	celery -A config.celery_app beat -l INFO

docker-run-local:
	$(MANAGE) migrate --no-input
	#rm -rf ./media/*
	$(MANAGE) init_project
	$(MANAGE) update_translation_fields
	$(MANAGE) runserver 0.0.0.0:8000

# messages command
messages:
	$(MANAGE) makemessages -l uk -i venv
	$(MANAGE) makemessages -d djangojs -l uk -i venv

	$(MANAGE) makemessages -l en -i venv
	$(MANAGE) makemessages -d djangojs -l en -i venv

	$(MANAGE) makemessages -l ru -i venv
	$(MANAGE) makemessages -d djangojs -l ru -i venv

	$(MANAGE) makemessages -l es -i venv -i src/home/models.py -i src/blog/models.py
	$(MANAGE) makemessages -d djangojs -l es -i venv -i src/home/models.py -i src/blog/models.py

	$(MANAGE) makemessages -l tr -i venv -i src/home/models.py -i src/blog/models.py
	$(MANAGE) makemessages -d djangojs -l tr -i venv -i src/home/models.py -i src/blog/models.py

compile:
	$(MANAGE) compilemessages -i .venv
