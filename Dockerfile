# Stage 1: Build the FastAPI application
FROM python:3.8 AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY api.py .
COPY pokenum.py .
COPY logger.py .
COPY start_pokenum_web.py .
COPY libpoker-eval_139.0-1_amd64.deb /tmp/


# Stage 2: Build the Flask application
FROM python:3.14.0a3-slim AS final

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .
COPY templates/ ./templates
COPY logger.py .
COPY /.libs/ ./.libs
COPY /logs/ ./logs
COPY /gfx/ ./gfx
# Install the custom library from the .deb package
COPY --from=builder /tmp/libpoker-eval_139.0-1_amd64.deb /tmp/
RUN dpkg -i /tmp/libpoker-eval_139.0-1_amd64.deb
# Copy the FastAPI application built in Stage 1
COPY --from=builder /app /app

ENV LD_LIBRARY_PATH=/usr/local/lib


EXPOSE 8080
EXPOSE 8000

CMD ["python", "start_pokenum_web.py"]
