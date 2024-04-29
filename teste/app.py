from flask import Flask, request, render_template
from PIL import Image
import io
import base64
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    img_bytes = uploaded_file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Salvando a imagem no diretório de uploads com um nome único
    filename = str(uuid.uuid4()) + '.jpg'
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    img.save(filepath)

    # Convertendo a imagem em base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    img_str = 'data:image/jpeg;base64,' + img_base64

    return render_template('upload.html', img_data=img_str)

if __name__ == '__main__':
    app.run(debug=True)
