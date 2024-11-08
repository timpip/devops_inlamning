# Use the latest version of Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /usr/app/src

# Update and install necessary packages
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

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv

# Make sure to use the virtual environment’s pip to upgrade it and install packages
RUN /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install streamlit

# Copy all files from the current directory into the container
COPY . .

# Expose the default Streamlit port
EXPOSE 8501

# Use the virtual environment’s Python and pip as default
ENV PATH="/opt/venv/bin:$PATH"

# Run the Streamlit application
CMD ["streamlit", "run", "main.py"]

