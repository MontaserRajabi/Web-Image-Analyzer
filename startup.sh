#!/bin/sh
apt-get update && apt-get install -y libtiff-dev libgl1
streamlit run app.py --server.port=8000 --server.address=0.0.0.0