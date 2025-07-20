# Stage 1: Build dependencies
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -t ./package

# Copy all .py files into package
COPY *.py ./package/

# Stage 2: Build final Lambda image
FROM public.ecr.aws/lambda/python:3.11

# Copy only the necessary app code and dependencies
COPY --from=builder /app/package ${LAMBDA_TASK_ROOT}

# Set Lambda handler (main.lambda_handler assumes main.py defines this function)
CMD ["main.lambda_handler"]
