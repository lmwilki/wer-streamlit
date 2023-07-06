FROM mcr.microsoft.com/devcontainers/python:1-3.10-bookworm
COPY . /app
WORKDIR /app

# pip install
RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "app.py" ]


