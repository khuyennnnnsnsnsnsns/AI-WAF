# AI-WAF

1 Install and move to AI-WAF directory
```bash
git clone https://github.com/PhongNoCode/AI-WAF.git

cd AI-WAF
```
2 Create a virtual environment and models folder
```bash
python3 -m venv venv

source venv/bin/activate

mkdir models
```
3 Install all libraries
```bash
pip install pandas scikit-learn joblib fastapi uvicorn flask requests scipy matplotlib seaborn
```
4 Filter the dataset
```bash
python3 filter_data.py
```
5 Add more malware payloads to the dataset
```bash
python3 add_payloads.py
```
6 Run AI_model
```bash
python3 train_model.py
```
7 Run file ai_service to activate AI WAF
```bash
uvicorn ai_service:app --port 8000
```
8 Open another terminal to run web

```bash
python3 web_app.py
```
9 Test these payloads and compare to modsecurity
```bash
11' or  WEIGHT_STRING(@@version)=WEIGHT_STRING(@@version) --

1+un/**/ion+se/**/lect+1,2,3--
```
