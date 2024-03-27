# Run Celery worker
run-celery:
	@celery -A tasks worker --loglevel=info -P solo