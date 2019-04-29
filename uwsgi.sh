pkill -f -9 uwsgi
nohup uwsgi --http 0.0.0.0:28021 --wsgi-file app.py --callable app --master --manage-script-name --processes 4 --threads 20 > logs/pyflask.out 2>&1 &
