FROM python:alpine
WORKDIR /app
COPY app .
RUN pip install pyramid
EXPOSE 80
CMD [ "python", "test.py" ]