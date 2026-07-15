### Reference Link
https://medium.com/@JavaFusion/build-your-first-fastapi-app-from-virtual-environment-to-uvicorn-server-342e1d069900

<hr>

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. To activate .venv
.venv\Scripts\Activate.ps1

# To deactivate .venv
deactivate

# 3. Install required packages
pip install fastapi uvicorn python-dotenv
pip install sqlalchemy psycopg2-binary 

# 4. To generate requirements.txt (like package.json)
pip freeze > requirements.txt

# If you want to install the packages mention in requirements.txt
pip install -r requirements.txt

# 5. To start the server
uvicorn main:app - reload
```


### For Swagger UI
http://127.0.0.1:8000/docs

### For ReDoc
http://127.0.0.1:8000/redoc