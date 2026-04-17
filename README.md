# Guia de uso do ngrok no Linux

Este guia mostra como:

1. Instalar o ngrok no Linux (Debian/Ubuntu).
2. Autenticar o ngrok com seu authtoken.
3. Expor a porta TCP usada pelo servidor.
4. Conectar com o cliente Python.

## 1) Instalar o ngrok

Execute no terminal:

```bash
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com bookworm main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok
```

## 2) Autenticar o ngrok

Depois da instalação, rode:

```bash
ngrok config add-authtoken 32Cmf52eF7yyHPn9iuOlSlRB3j9_7W4EA2AULaJN4bmg5LhYV
```

## 3) Expor a porta TCP do servidor

Com seu servidor escutando na porta 18861, execute:

```bash
ngrok tcp 18861
```

O ngrok vai mostrar um endpoint parecido com este:

- Host: 0.tcp.sa.ngrok.io
- Porta: 14243

## 4) Conectar com o cliente Python

Em outro terminal, rode:

```bash
python client.py 0.tcp.sa.ngrok.io 14243 (mude o número da porta se necessário)
```

Se estiver tudo correto, o cliente deve receber a resposta do servidor remoto.
