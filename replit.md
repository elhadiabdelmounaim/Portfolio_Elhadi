# Running the imported portfolio

This project uses Python 3.12, Django 6.0.2, and the existing SQLite database
(`db.sqlite3`). Keep the current project structure and database.

## Run in Replit

Click **Run** to start the **Start application** workflow:

```sh
python manage.py runserver 0.0.0.0:5000
```

Dependencies are pinned in `requirements.txt` and installed in Replit's Python
package environment. Do not use the imported `venv` directory.

The required `SESSION_SECRET` is supplied through Replit Secrets. Never put its
value in source code.

## Pages

- `/`: public CV/portfolio
- `/contact`: contact form
- `/dashboard/login/`: CV Studio dashboard for editing the public profile, sections, and entries. Requires a project Superuser.
- `/admin/`: Django Admin for contact messages and lower-level CV records. It uses the same project accounts.

The two admin pages are separate interfaces, not separate accounts. Use the Django Superuser username and password on either sign-in page. The CV Studio dashboard only allows Superusers; Django Admin also checks Django's staff permissions.

Dashboard and admin access require an existing authorized account. To create a
new owner account if needed, run `python manage.py createsuperuser` interactively;
do not hardcode credentials.

## Checks and database updates

```sh
python manage.py check
python manage.py test
python manage.py showmigrations
```

The imported database already has all current migrations applied. After future
schema changes, back up the database before running `python manage.py migrate`.

## Publication

This run workflow is for development preview, not production. Before publishing,
configure production settings (`DEBUG=False`, explicit allowed hosts and trusted
origins), a production WSGI server, static-file serving, and durable database
storage. Do not replace SQLite without the user's approval.
