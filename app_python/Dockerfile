FROM python:3.9.6-alpine
LABEL maintainer="r.talalaeva@innopolis.university"

ENV VENV_PATH=/opt/venv \
    PYTHONDONTWRITEBYTECODE=1
ENV PATH="$VENV_PATH/bin:$PATH"
RUN apk add --no-cache gcc musl-dev && \
    python -m venv $VENV_PATH && \
    adduser --disabled-password app -s /bin/sh -h /home/app

WORKDIR /home/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

USER app

EXPOSE 8000

COPY --chown=app:app moscow_time/ ./moscow_time/

CMD ["uvicorn", "moscow_time.main:app", "--host", "0.0.0.0", "--port", "8000"]
