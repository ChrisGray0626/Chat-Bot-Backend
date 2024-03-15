FROM python:3.9-slim

EXPOSE 8000
# Set the working directory
WORKDIR /app
# Install the required denpendencies
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.zju.edu.cn/pypi/web/simple
# Copy the source code
COPY src ./src
# Set the environment variable PYTHONPATH
ENV PYTHONPATH /app
# Run the server
CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
