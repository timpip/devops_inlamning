
FROM ubuntu:latest


WORKDIR /usr/app/src


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        locales \
        python3 \
        python3-pip \
        python3-venv \
        python3-yaml \
        rsyslog \
        systemd \
        systemd-cron \
        sudo \
    && apt-get clean

RUN python3 -m venv /opt/venv


RUN /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install streamlit


COPY . .


EXPOSE 8501


ENV PATH="/opt/venv/bin:$PATH"


CMD ["streamlit", "run", "main.py"]

