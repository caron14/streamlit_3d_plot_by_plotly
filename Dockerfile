FROM python:3.9

WORKDIR /opt
RUN pip install --upgrade pip
RUN pip install numpy \
				pandas \
				scikit-learn \
				matplotlib \
				seaborn \
				plotly \
				streamlit

WORKDIR /work

