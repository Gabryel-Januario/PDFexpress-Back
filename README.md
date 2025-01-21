# Simple File Conversion API

Este projeto é uma API construída com Flask que permite o upload e conversão de arquivos em diferentes formatos, como:

- DOCX para PDF
- Imagens para PDF
- TXT para PDF
- XLSX para PDF

## Dependências

Este projeto depende das seguintes bibliotecas:

- Flask
- Pillow
- fpdf
- python-docx
- pywin32

## Como usar

### Instalar dependências

Para instalar as dependências do projeto, você pode usar o seguinte comando:


pip install -r requirements.txt

Executar o servidor
Para executar o servidor, basta rodar o arquivo principal da aplicação:

python app.py
O servidor será iniciado em http://127.0.0.1:5000.

Endpoints disponíveis
POST /upload: Faz o upload de um arquivo para o servidor.

Parâmetros:
file: O arquivo a ser enviado.
method: O método de conversão (docx_to_pdf, image_to_pdf, xlsx_to_pdf, txt_to_pdf).

POST /convert: Converte o arquivo enviado para o formato PDF.

Parâmetros:
filename: O nome do arquivo a ser convertido.
method: O método de conversão.
GET /download: Baixa o arquivo convertido em PDF.

Como funciona
O usuário envia um arquivo através do endpoint /upload.
O arquivo é salvo no servidor e, dependendo do método selecionado (docx_to_pdf, image_to_pdf, etc.), é convertido para um arquivo PDF.
O arquivo convertido pode ser baixado através do endpoint /download.
Contribuições


Sinta-se à vontade para contribuir para o projeto fazendo um fork e criando pull requests.
