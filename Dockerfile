FROM python:3.9

EXPOSE 8000

WORKDIR /app

COPY . .

ENV PYTHONPATH /app

RUN pip install -r requirements.txt -i https://mirrors.zju.edu.cn/pypi/web/simple
CMD ["python", "src/api/api.py"]
