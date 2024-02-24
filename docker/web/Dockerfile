FROM python:3.12

ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
ADD ./docker/web/requirements.txt /workspace/
RUN apt -y update && apt install -y ffmpeg
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
ADD ./workspace/ /workspace/

ARG UID
ARG GID
ARG UNAME

ENV UID ${UID}
ENV GID ${GID}
ENV UNAME ${UNAME}

RUN groupadd -g ${GID} ${UNAME}
RUN useradd -u ${UID} -g ${UNAME} -m ${UNAME}
