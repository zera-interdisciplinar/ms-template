# ms-template

Template base para novos microsserviços do Zera. É o ponto de partida ao criar um serviço novo:
clone/copie a estrutura daqui em vez de montar tudo do zero.

## O que já vem pronto

- API mínima em **FastAPI** (`main.py`), com um endpoint `/health` para checagem de liveness/readiness
  e um `/` só para confirmar que o serviço está de pé.
- `Dockerfile` baseado em `python:3.12-slim`, pronto para build e deploy em produção.
- Manifests de **Kubernetes** (`k8s/`) para os ambientes de QA e produção (deployment + service).
- Workflows de **CI/CD** (`.github/workflows/`) para rodar testes e publicar em QA e produção.
- Testes de exemplo (`test_main.py`) usando `pytest` + `TestClient` do FastAPI.

## Como usar

1. Crie o novo repositório a partir deste template.
2. Troque o nome do serviço em `main.py`, `Dockerfile`, `k8s/*.yaml` e nos workflows.
3. Substitua os endpoints de exemplo pela API real do serviço, mantendo o `/health`.
4. Ajuste `requirements.txt` conforme as dependências do serviço.

## Rodando localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

## Testes

```bash
pytest
```
