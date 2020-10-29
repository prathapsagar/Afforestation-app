# Afforestation-app
Afforestation hotspot detector
Step 0 : Clone only the mysite folder. 

Note: In index.html, search for YOUR_API_KEY and replace it with your api key which is available on developers.google.com>get an api key (from the side bar)

Step 1: Download the ML model from https://drive.google.com/file/d/1SdLZmfR2wYVW_6TzSxHkBRcOj0R5uoHz/view?usp=sharing and put it into mapp/model folder along with the json file.

Step 2. Install Python3.6 by following step from https://towardsdatascience.com/building-python-from-source-on-ubuntu-20-04-2ed29eec152b

Note: This link is for Ubuntu users. Windows users please google it yourselves. Also, this project doesn't work for higher versions of Python such as 3.7+. So installing 3.6 is a must.

Step 3: Run the command: pip3.6 install -r requirements.txt

Step 4: Run the command:pip3.6 install imageai --upgrade

Step 5: Finally run the command python3.6 manage.py runserver from your mysite folder of you django app.

