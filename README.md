# 📲 Gerador Profissional de QR Code em Python

![Status do Projeto](https://img.shields.io/badge/status-em%20funcionamento-brightgreen?style=flat-square) ![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## 🚀 Sobre o Projeto

Este projeto consiste em um aplicativo desktop desenvolvido em **Python 3**, que gera QR Codes personalizados para URLs, com foco em perfis LinkedIn, sites pessoais, portfólios e outros links importantes.

Criado para profissionais e entusiastas que desejam uma solução local, rápida e visualmente elegante para gerar QR Codes sem depender de serviços online.

O aplicativo utiliza a biblioteca **Tkinter** para uma interface gráfica amigável e moderna, e as bibliotecas **qrcode** e **Pillow** para gerar imagens de alta qualidade.

---

## ✨ Funcionalidades Principais

- 🔗 **Entrada de URL customizada:** Insira qualquer link para gerar o QR Code correspondente.  
- 🎨 **Visualização em tempo real:** Veja o QR Code sendo gerado instantaneamente na tela.  
- 💾 **Salvar imagem automaticamente:** O QR Code gerado é salvo como arquivo PNG com nome padrão ou personalizado.  
- ✅ **Alta correção de erros:** Garantia de leitura confiável mesmo com QR Codes parcialmente danificados.  
- 🖥️ **Interface moderna:** Layout clean, cores sóbrias, botões estilizados e feedback visual.  
- 🌐 **Multiplataforma:** Funciona em Windows, Linux e macOS com Python instalado.  

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia          | Descrição                          | Ícone              |
|---------------------|----------------------------------|--------------------|
| Python 3.12         | Linguagem principal do projeto    | 🐍                 |
| Tkinter             | Framework GUI padrão do Python    | 🖥️                 |
| qrcode              | Biblioteca para gerar QR Codes    | 🔳                 |
| Pillow (PIL)        | Biblioteca para manipulação de imagens | 🖼️            |

---

## 📝 Requisitos

- Python 3.6 ou superior instalado (recomendado 3.12)  
- Instalar bibliotecas necessárias via pip:

## 🔸 Passo 1: Crie um ambiente virtual
Execute no terminal:
```bash 
python3 -m venv venv
```

## 🔸 Passo 2: Ative o ambiente virtual
```bash 
source venv/bin/activate
```
Você verá que aparece (venv) antes do seu nome no terminal.

## 🔸 Passo 3: Instale o pacote qrcode
```bash
pip install qrcode[pil]
```
## Se quiser também permitir que python funcione como python3:

bash
Copiar código
sudo apt install python-is-python3
🔸 Passo 4: Rode o seu script

## Digite ou cole a URL desejada e clique no botão Gerar QR Code.
 O QR Code aparecerá na tela e será salvo automaticamente na pasta do projeto como linkedin_qrcode.png.
 
## 📷 Captura de Tela

  <img src="https://github.com/user-attachments/assets/e39ccc23-132f-4eef-847f-4972be1874aa" alt="Imagem 2" />
    <img src="https://github.com/user-attachments/assets/9704d13a-c74c-4938-b4e9-7778d23d944a" alt="Imagem 3" />
    <img src="https://github.com/user-attachments/assets/0b8eba90-5509-4aa9-b6d1-144408099b14" alt="Imagem 4" />
        <img src="https://github.com/user-attachments/assets/46232a78-dc9a-4565-a1fe-f5de8e1b815c" alt="Imagem 5" />
    <img src="https://github.com/user-attachments/assets/79e3e6e6-b432-454a-8ea9-f19287b12f2f" alt="Imagem 6" />
    <img src="https://github.com/user-attachments/assets/4afa9d7b-768c-4f79-898e-152a513312ed" alt="Imagem 7" />
     <img src="https://github.com/user-attachments/assets/a21f0772-a455-4505-997c-00afe43796e1" alt="Imagem 1" />


## 🔧 Explicação Técnica
O projeto utiliza a biblioteca qrcode para gerar o código QR a partir do texto URL, aplicando parâmetros que definem o tamanho, margem e nível de correção de erro.

O resultado é convertido em imagem PNG com a biblioteca Pillow, que permite salvar o arquivo com alta resolução.

A interface gráfica é feita com Tkinter, permitindo criar janelas, botões e campos de entrada simples e funcionais, tornando a experiência do usuário agradável e intuitiva.

### 🚀 Possíveis Melhorias Futuras
📱 Adicionar opção para escolher o formato da imagem (SVG, JPG, PNG).

🎨 Permitir personalização de cores do QR Code (cores do fundo e do código).

📤 Integrar com APIs para envio automático do QR Code por email ou WhatsApp.

🗂️ Criar histórico de QR Codes gerados, com opção de visualização e reuso.

🌐 Transformar em aplicação web usando frameworks como Flask ou Django.
