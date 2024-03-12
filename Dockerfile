FROM python:3.9-slim

EXPOSE 8000

WORKDIR /app

COPY . .
# Set the environment variable PYTHONPATH
ENV PYTHONPATH /app

RUN pip install -r requirements.txt -i https://mirrors.zju.edu.cn/pypi/web/simple

CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
