# 📁 service-file

Microserviço responsável pelo **upload, armazenamento e parsing de arquivos**, com foco em arquivos CSV. Desenvolvido com Django REST Framework.

---

## 📌 Objetivo

Receber arquivos enviados por outros microsserviços ou interfaces, realizar validação/parsing e armazenar de forma organizada, permitindo **download via ID de requisição**.

---

## ⚙️ Stack Tecnológica

- **Linguagem:** Python
- **Framework:** Django REST Framework (DRF)
- **Service Discovery:** Eureka (via `py-eureka-client`)

---

## 📁 Endpoints Principais

### 📤 Upload

- `POST /v1/upload/`  
  Envia um arquivo CSV para ser armazenado e processado.  
  Campos esperados: `file`, `storeId`

### 📥 Download

- `GET /v1/download/<request_id>/`  
  Realiza o download do arquivo correspondente ao ID da requisição.

### 💓 Health

- `GET /health/`  
  Verifica se o serviço está online.

---

## 🧩 Integração com Eureka

O serviço registra-se automaticamente no Eureka ao iniciar:

```python
from py_eureka_client import eureka_client

eureka_client.init_registry_client(
    eureka_server="http://eureka:8761/eureka",
    app_name="service-file",
    instance_port=8000,
    instance_host="service-file"
)
