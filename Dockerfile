FROM python:3.11-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Install dos2unix and convert entrypoint.sh
RUN apt-get update && apt-get install -y dos2unix && dos2unix /app/entrypoint.sh

# Debug step to list files
RUN ls -la /app

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Run the web service on container startup
ENTRYPOINT ["/app/entrypoint.sh"]
