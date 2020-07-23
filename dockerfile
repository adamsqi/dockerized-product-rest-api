FROM python

ENV PYTHONUNBUFFERED=0

RUN pip install --upgrade pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
COPY ./app /app
WORKDIR /app

RUN pip install -r /app/requirements.txt --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
CMD pytest tests/ && python -u /app/main.py