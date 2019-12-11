FROM heroku/miniconda

# Add our code
ADD ./ /opt/app
WORKDIR /. /opt/app

RUN conda config --add channels conda-forge 
RUN conda install portaudio

# Grab requirements.txt.
ADD ./requirements.txt /tmp/

# Install dependencies
RUN pip install -r /tmp/requirements.txt

# Hættir að virka hérna.
ENTRYPOINT ["python"]
CMD ["main.py"]