FROM centos:latest

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING UTF-8
ENV CONDA_DIR /opt/conda
ENV NB_USER=nbuser
ENV NB_UID=1011
ENV NB_PYTHON_VER=2.7

# Python binary and source dependencies
RUN yum install -y curl wget java-headless bzip2 gnupg2 sqlite3 \
    && yum clean all -y \
    && cd /tmp \
    && wget -q https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh \
    && echo d0c7c71cc5659e54ab51f2005a8d96f3 Miniconda3-4.2.12-Linux-x86_64.sh | md5sum -c - \
    && bash Miniconda3-4.2.12-Linux-x86_64.sh -b -p $CONDA_DIR \
    && rm Miniconda3-4.2.12-Linux-x86_64.sh \
    && export PATH=/opt/conda/bin:$PATH \
    && yum install -y gcc gcc-c++ glibc-devel \
    && /opt/conda/bin/conda install --quiet --yes python=$NB_PYTHON_VER 'nomkl' \
			    'ipywidgets=5.2*' \
			    'matplotlib=1.5*' \
			    'scipy=0.17*' \
			    'seaborn=0.7*' \
			    'cloudpickle=0.1*' \
			    statsmodels \
			    pandas \
			    'dill=0.2*' \
			    notebook \
			    jupyter \
    && pip install widgetsnbextension \
    && yum erase -y gcc gcc-c++ glibc-devel \
    && yum clean all -y \
    && rm -rf /root/.npm \
    && rm -rf /root/.cache \
    && rm -rf /root/.config \
    && rm -rf /root/.local \
    && rm -rf /root/tmp \
    && useradd -m -s /bin/bash -N -u $NB_UID $NB_USER \
    && usermod -g root $NB_USER \
    && chown -R $NB_USER $CONDA_DIR \
    && conda remove --quiet --yes --force qt pyqt \
    && conda remove --quiet --yes --force --feature mkl ; conda clean -tipsy


ENV PATH /opt/conda/bin:$PATH

ADD loader.py /app/loader.py

CMD["python"]