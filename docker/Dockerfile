# Start from debian linux image (DockerHub)
FROM debian:oldstable

# Add custom label
LABEL maintainer="René Crans renecrans@gmail.com" \
      version="1.0" \
      description="This docker image runs the fixed seqClass.py in python "

# Install python (after apt-get update)
RUN apt-get update && apt-get install -y python3 && apt-get install -y python-is-python3

# Copy 'seqClass.py' to the container
ADD seqClass.py /

# Give execution permissions to seqClass.py
RUN chmod +x /seqClass.py 

# Add /scripts folder to the PATH environment variable
ENV PATH="$PATH:/" 
