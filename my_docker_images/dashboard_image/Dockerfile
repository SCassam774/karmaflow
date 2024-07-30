FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    && apt-get clean
RUN pip3 install --upgrade pip
RUN pip3 install pandas plotly dash matplotlib
ADD dashboard_container.py /my_dashboard/dashboard_container.py
WORKDIR /my_dashboard/
CMD python3 dashboard_container.py
