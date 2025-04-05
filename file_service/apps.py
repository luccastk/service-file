from django.apps import AppConfig
from dotenv import load_dotenv
import threading
import py_eureka_client.eureka_client as eureka_client
import atexit 
import os

dotenv_path = f".env.prod"

load_dotenv(dotenv_path)

server = os.environ.get("EUREKA_SERVER")
name = os.environ.get("EUREKA_APP_NAME")
port = int(os.environ["EUREKA_APP_PORT"])
host = os.environ.get("EUREKA_APP_INSTANCE")
class FileServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file_service'

    def ready(self):
        def register_with_eureka():
            try:
                eureka_client.init(
                    eureka_server=server,
                    app_name=name,
                    instance_port=port,
                    instance_host=host
                )
            except Exception as e:
                print("Register failed: ", e)

        threading.Thread(target=register_with_eureka, daemon=True).start()

        def unregister_eureka():
            try:
                eureka_client.stop()
            except Exception as e:
                print("Failed to unregister: ", e)

        atexit.register(unregister_eureka)