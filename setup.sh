apt install python python-pip python-dev
pip install tornado
pip install mapproxy
wget http://miniupnp.free.fr/files/download.php?file=miniupnpc-2.0.tar.gz -O miniupnpc-2.0.tar.gz
tar -zxvf miniupnpc-2.0.tar.gz
rm miniupnpc-2.0.tar.gz
cd miniupnpc-2.0
make
make install
make pythonmodule

