# Description: Dockerfile for the category_app
FROM python:3.11.3
ENV PYTHONUNBUFFERED True
# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application
ENV APP_HOME /root
WORKDIR $APP_HOME
COPY main.py $APP_HOME/category_app/

EXPOSE 8080
CMD ["uvicorn", "category_app.main:app", "--host", "0.0.0.0", "--port", "8080"]