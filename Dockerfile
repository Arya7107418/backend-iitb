# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim



# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 5: Install any necessary dependencies
RUN pip install -r requirements.txt

# Step 6: Copy the current directory contents into the container at /app
COPY . /app/.

# Step 8: Run the application (start the Django server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
