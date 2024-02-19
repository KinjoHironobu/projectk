FROM python:3.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
ADD requirements.txt /workspace/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
ADD . /workspace/