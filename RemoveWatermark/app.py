from flask import Flask, request, send_file, render_template
import cv2
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    analysis = analyze_image(file_path)
    return render_template('analysis.html', analysis=analysis, filename=file.filename)


def analyze_image(file_path):
    img = Image.open(file_path)
    return {
        "format": img.format,
        "size": img.size,  # (width, height)
        "mode": img.mode  # e.g., RGB
    }


@app.route('/remove_watermark/<filename>', methods=['POST'])
def remove_watermark(filename):
    # 获取输入和输出路径
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(PROCESSED_FOLDER, filename)

    # 获取水印区域坐标
    coordinates = request.json
    if not coordinates:
        return "未选择水印区域", 400

    try:
        # 读取图片
        image = cv2.imread(input_path)
        if image is None:
            return "无法读取图片", 400

        # 创建掩码
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        
        # 获取图片尺寸
        height, width = image.shape[:2]
        
        # 计算实际像素坐标
        x = int(coordinates['x'] * width)
        y = int(coordinates['y'] * height)
        w = int(coordinates['width'] * width)
        h = int(coordinates['height'] * height)
        
        # 在掩码上标记水印区域
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
        
        # 使用修复算法去除水印
        result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
        
        # 保存结果
        cv2.imwrite(output_path, result)
        
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return str(e), 500


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))


if __name__ == '__main__':
    app.run(debug=True)