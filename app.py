from flask import Flask, request, render_template, redirect, url_for
import os
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    image_data = request.form.get('imageData')
    if image_data:
        image_data = image_data.split(',')[1]  # Remove 'data:image/png;base64,' part
        image = Image.open(BytesIO(base64.b64decode(image_data)))

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'captured_image.png')
        image.save(filepath)

        return f'Image captured and saved as {filepath}', 200
    else:
        return 'No image data found', 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
