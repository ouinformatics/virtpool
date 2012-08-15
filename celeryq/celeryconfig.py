BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "floworks"
BROKER_PASSWORD = "floworksq"
BROKER_VHOST = "floworks"


CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "localhost",
    "database": "cybercom_queue",
    "taskmeta_collection": "cybercom_queue_meta"
}

