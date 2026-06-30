from flask import Flask, request, jsonify
import cv2
import numpy as np
import io
from PIL import Image
from processor import canny_edge_detection, sobel_operator, prewitt_operator, laplacian_edge_detection

app = Flask(__name__)

def pil_to_cv2(pil_image):
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def cv2_to_pil(cv2_image):
    return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    filter_type = request.form.get('filter', 'canny')
    
    try:
        img = Image.open(file.stream)
        img_cv = pil_to_cv2(img)
        
        if filter_type == 'canny':
            processed_img = canny_edge_detection(img_cv)
        elif filter_type == 'sobel':
            processed_img = sobel_operator(img_cv)
        elif filter_type == 'prewitt':
            processed_img = prewitt_operator(img_cv)
        elif filter_type == 'laplacian':
            processed_img = laplacian_edge_detection(img_cv)
        else:
            return jsonify({'error': 'Invalid filter type'}), 400
            
        # Convert grayscale result back to RGB for PIL
        if len(processed_img.shape) == 2:
            processed_img = cv2.cvtColor(processed_img.astype(np.uint8), cv2.COLOR_GRAY2RGB)
            
        result_pil = cv2_to_pil(processed_img)
        
        output = io.BytesIO()
        result_pil.save(output, format='PNG')
        output.seek(0)
        
        return output.getvalue(), 200, {'Content-Type': 'image/png'}
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)
