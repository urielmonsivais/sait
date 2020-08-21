set FLASK_APP=app/app
set FLASK_ENV=development

echo flask db init
echo flask db migrate -m "Added company table."
 flask run