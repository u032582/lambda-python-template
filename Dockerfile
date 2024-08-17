# Use the official AWS Lambda Python 3.8 base image
FROM public.ecr.aws/lambda/python:3.8

# Copy the function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install any dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the CMD to your handler (app.lambda_handler)
CMD ["app.lambda_handler"]

####
