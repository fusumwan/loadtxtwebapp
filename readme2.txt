python -m venv .venv
.venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt


======================================

pip freeze > requirements.txt
pip freeze > requirements2.txt

=============run project===============

uvicorn main:app --reload
uvicorn main:app --host 127.0.0.1 --port 8080 --reload
uvicorn main:app --host 127.0.0.1 --port 8080 --reload --ssl-keyfile=key.pem --ssl-certfile=cert.pem

uvicorn accountslogin.main:app --host 127.0.0.1 --port 8080 --reload --ssl-keyfile=key.pem --ssl-certfile=cert.pem

uvicorn accountslogin.main:app --host 127.0.0.1 --port 8080 --reload --ssl-keyfile ./accountslogin/loadtxtwebapp_ssl_key.pem --ssl-certfile ./accountslogin/loadtxtwebapp_ssl_cert.pem

python accountslogin.main:app --host 127.0.0.1 --port 8080 --reload 

Stop the server
ctrl + c 

====================

pip list
==============================
…or create a new repository on the command line
echo "# fastapibacked" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:fusumwan/fastapibacked.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin git@github.com:fusumwan/fastapibacked.git
git branch -M main
git push -u origin main
===================
git pull
git add .
git commit -m "Updating"
git branch -M main
git push -u origin main


=========================================
below is container image url
docker.io/timothyfudocker/loadtxtwebapp:v1.3

docker.io/timothyfudocker/loadtxtwebapp:latest
============== create your google cloud run service===========
Go to google cloud 
https://console.cloud.google.com/

then go to Artifact Registry
Enable Artifact Registry API




Go to google cloud the go to google cloud run


select Deploy container


Deploy one revision from an existing container image

below is container image url
docker.io/timothyfudocker/learnwiseaiwebapp:latest

Authentication *

Allow unauthenticated invocations
Check this if you are creating a public API or website.

CPU allocation and pricing

CPU is only allocated during request processing
You are charged per request and only when the container instance processes a request.

Minimum number of instances
1

===============================================================================================
.\bats\keytool_installation.bat
$env:Path += ";C:\Program Files\Java\jdk-25\bin"
keytool -help


===============================================================================================
First, you need to have an SSL certificate and a private key. You can generate a self-signed certificate for testing using keytool / OpenSSL:


keytool -genkeypair -alias loadtxtwebapp_ssl -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore loadtxtwebapp_ssl.p12 -validity 3650 -ext "san=dns:localhost,ip:127.0.0.1"
$env:Path += ";C:\Program Files\Java\jdk-25\bin"
keytool -genkeypair -alias loadtxtwebapp_ssl -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore loadtxtwebapp_ssl.p12 -validity 3650 -ext "san=dns:localhost,dns:loadtxtwebapp-82082989871.europe-west1.run.app,ip:127.0.0.1"

password:
1234qwer

First and last name:
loadtxtwebapp

Organizational unit:
Individual

Organization:
Individual

City:
Melbourne

State:
Melbourne

two-letter City code:
AU

correct?
yes

keytool -export -keystore loadtxtwebapp_ssl.p12 -alias loadtxtwebapp_ssl -file loadtxtwebapp_ssl.crt

right click the certificate
install the certificate
choose current user
choose place all certification
choose Trusted Root Certification Authorities


openssl pkcs12 -in loadtxtwebapp_ssl.p12 -out loadtxtwebapp_ssl_cert.pem -nokeys
openssl pkcs12 -in loadtxtwebapp_ssl.p12 -out loadtxtwebapp_ssl_key.pem -nocerts -nodes

copy loadtxtwebapp_ssl_cert.pem accountslogin/loadtxtwebapp_ssl_cert.pem
copy loadtxtwebapp_ssl_key.pem accountslogin/loadtxtwebapp_ssl_key.pem

uvicorn accountslogin.main:app --host 127.0.0.1 --port 8000 --reload --ssl-keyfile=loadtxtwebapp_ssl_key.pem --ssl-certfile=loadtxtwebapp_ssl_cert.pem

update the main.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")


====================================================================================================

Import-Certificate -FilePath "C:\WebDevelopment\WorkspaceFastAPI\loadtxtWebapp\loadtxtWebapp\loadtxtwebapp_ssl_cert.pem" -CertStoreLocation Cert:\CurrentUser\Root

=====================================================================================
you can use Microsoft Edge to browse your FastAPI web application. If you have set up HTTPS correctly, Edge will be able to access your FastAPI application over HTTPS without any issues.

### To ensure smooth browsing in Edge:
1. **Correct SSL Setup**: Make sure your SSL certificate is properly configured in your FastAPI app. If you're using a self-signed certificate for local development, you might need to manually add it to Edge's trusted certificates to prevent security warnings.

2. **Accessing the Application**:
   - Simply open Edge and navigate to `https://localhost` or `https://<your-ip-address>`.
   - If the certificate is trusted or from a recognized Certificate Authority (CA), Edge should display the site without security alerts.

3. **Handling Self-Signed Certificates** (if used):
   - When using a self-signed certificate, Edge might show a security warning. To avoid this, import the self-signed certificate into Edge's trusted certificate store.
   - **Steps to Trust the Certificate**:
     - Open **Edge > Settings**.
     - Go to **Privacy, search, and services > Security**.
     - Click on **Manage certificates** under **Certificates and security**.
     - Import the self-signed certificate (`cert.pem`) into the **Trusted Root Certification Authorities**.

4. **Private IP/Domain Access**: If you access the FastAPI application via a private IP address or domain, ensure that the SSL certificate's `Common Name (CN)` or `Subject Alternative Name (SAN)` matches the domain/IP used to access the site.

By setting up these configurations, Edge will be able to browse your FastAPI HTTPS web application without any issues or security warnings.


=================================================



========================
git checkout main




============================

# 0) (Optional) back up any local work
git stash push -m "backup before reset" --include-untracked

# 1) Get the latest objects from origin
git fetch origin --prune

# 2) Ensure you’re on main
git switch main  # or: git checkout main

# 3) Hard‑reset main to the target commit
git reset --hard f1e6c4f

# 4) (Optional) remove untracked files/dirs to fully mirror that commit
git clean -fd

# 5) Verify
git show --oneline -s


===============================
git stash push -m "backup before reset" --include-untracked
git fetch origin --prune
git switch main
git reset --hard f1e6c4f
git clean -fd
git show --oneline -s


======================

# 1) Make sure you're on main
git switch main

# 2) Fetch the latest from origin
git fetch origin

# 3) Rebase your local commits onto origin/main
git pull --rebase origin main
# If conflicts appear: fix files, then
#   git add <fixed files>
#   git rebase --continue
# Repeat until rebase finishes.

# 4) Push
git push origin main


============================
git switch main
git fetch origin
git pull --rebase origin main
git push origin main



==========================

git pull
git add .
git commit -m "Updating"
git branch -M main
git push -u origin main




============================
To force push your local version to replace the remote repository, you can use:


git push --force-with-lease origin main

==========================================Windows installation guide==========================================

winget install Microsoft.VisualStudio.2022.BuildTools
python -m venv .venv

#Change execution policy permanently (requires admin rights):

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.venv\Scripts\activate

# 升級打包工具到最新（對取得 wheels 好重要）
python -m pip install --upgrade pip setuptools wheel

# 極重要：先安裝幾個最易出事的底層依賴，並強制用二進制 wheel
pip install --only-binary=:all: "cffi>=2.0.0,<2.1" "cryptography<46" "asyncpg==0.30.0"

# （可選）如果曾經試裝失敗，先清一清快取
pip cache purge

pip install fastapi uvicorn starlette pydantic
pip install sqlalchemy alembic databases aiomysql PyMySQL
pip install passlib bcrypt PyJWT
pip install email-validator
pip install flask
pip install bs4
pip install gtts
pip install pydub
pip install audioop-lts
pip install sentence_transformers
pip install python-multipart
pip install -r requirements.txt

==========================================Windows installation guide==========================================


# Export requirements.txt
pip freeze > requirements.txt



=========================================
below is container image url

docker.io/timothyfudocker/learnwiseaiwebapp:v1.3


======================
.venv/Scripts/activate
=================================

python -m uvicorn accountslogin.main:app --port 8080 --reload --ssl-keyfile=accountslogin/loadtxtwebapp_ssl_key.pem --ssl-certfile=accountslogin/loadtxtwebapp_ssl_cert.pem
==========================
https://127.0.0.1:8080/

https://127.0.0.1:8080/wikivoiceverseai



==========================

git pull
git add .
git commit -m "Updating"
git branch -M main
git push -u origin main


