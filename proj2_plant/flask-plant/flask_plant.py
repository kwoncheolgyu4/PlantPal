from flask import Flask, render_template, request, jsonify, url_for
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
from keras.applications import VGG16
from keras import Sequential
from keras.layers import Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.src.utils import load_img, img_to_array
from keras.models import load_model
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "*"}})

# 파일 크기 제한 설정 (16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB로 파일 크기 제한 설정

# 업로드 폴더 설정
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 업로드 폴더가 없다면 생성
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 미리 모델을 로드하고 클래스 라벨을 설정합니다.
model = load_model('./plant_model_30.h5')
train_dir = './plant_image/train'
train_datagen = ImageDataGenerator()
train_generator = train_datagen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=32, class_mode='categorical')
labels = list(train_generator.class_indices.keys())

@app.route('/python-view')
def python_view():
    return render_template('python_view.html')

@app.route("/upload", methods=['POST'])
def upload():
    if 'file' not in request.files:
        print("Error: 'file' not in request.files")
        return jsonify({'error': 'no file'})

    file = request.files['file']
    print(file)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # 클라이언트에 반환할 경로를 URL 형식으로 변환
        file_url = url_for('static', filename=f'uploads/{filename}', _external=True)
        print(f"File saved to: {filepath}")

        # 업로드된 파일을 사용하여 분석 실행
        prediction_label, confidence = fn_predict(model, filepath)

        return jsonify({
            'message': 'File uploaded and analyzed successfully',
            'file_path': file_url,
            'prediction': prediction_label,
            'confidence': confidence
        })

    return jsonify({'error': 'File upload failed'})

# 영어 라벨과 한글 라벨의 매핑
label_mapping = {
    "aug": "아욱",
    "bongseonhwa": "봉선화",
    "chamchwi": "참취",
    "dambaepul": "담배풀",
    "dwaejigamja": "돼지감자",
    "gaji": "가지",
    "gasiogalpi": "가시오갈피",
    "gomchwi": "곰취",
    "jebissug": "제비쑥",
    "kkulpul": "꿀풀",
    "memil": "메밀",
    "minari": "미나리",
    "neogjulgosali": "넉줄고사리",
    "oi": "오이",
    "susemioi": "수세미오이",
    "yeoju": "여주",
}


# 파일 경로를 받아 예측을 수행하는 함수
def fn_predict(p_model, p_file):
    image = load_img(p_file, target_size=(224, 224))
    image_array = img_to_array(image).reshape((1, 224, 224, 3))

    # 예측 수행
    pred = p_model.predict(image_array)
    idx = np.argmax(pred)
    label = labels[idx]
    confidence = pred[0][idx] * 100

    # 한글로 변환된 라벨
    korean_label = label_mapping.get(label, label)  # 매핑이 없으면 영어 라벨 그대로

    print(f"Prediction: {korean_label}, Confidence: {confidence}%")
    return korean_label, confidence

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')