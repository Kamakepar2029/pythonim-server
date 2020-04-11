# pythonim-server
## Pythonim Server
### Copy the folowing code:
```
sudo -s
apt install python-pip
pip install flask
mkdir pythonim-server
cd pythonim-server
virtualenv env
source env/bin/activate
echo 'Execute command "deactivate" to stop the pythonim-server'
cat ../server.py > ./server.py
Your server will be availible at 127.0.0.1:5000
python server.py
```
