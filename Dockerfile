FROM python:rc-buster
COPY . /discord
WORKDIR /discord
RUN pip install git+https://github.com/thisgary/dscord
ENTRYPOINT ["python3", "main.py"]

