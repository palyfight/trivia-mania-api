FROM python:3

# Update to latest PIP
RUN pip install --upgrade pip

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

COPY . /app
#COPY main.py /app
#COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT python app/main.py