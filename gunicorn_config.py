import os

porta = os.getenv('APP_PORTA', default=8081)
workers = os.getenv('APP_WORKERS', default=2)

bind = f"0.0.0.0:{porta}"
workers = int(workers)