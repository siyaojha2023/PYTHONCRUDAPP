FROM python:3.9-alpine
WORKDIR /usr/src/app
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py makemigrations api && \
    python manage.py migrate


EXPOSE 3000
CMD ["python", "manage.py", "runserver"]