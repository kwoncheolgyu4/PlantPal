from keras.applications import VGG16
from keras import Sequential
from keras.layers import Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator

# 데이터 로드 및 전처리
train_dir = './plant_image/train'   # 요부분 바꾸면 다른 것도 가능
test_dir = './plant_image/test'

train_dategen = ImageDataGenerator(
    rotation_range=180             # 회전
  , width_shift_range=0.2          # 좌우 이동
  , height_shift_range=0.2         # 상하 이동
  , horizontal_flip=True           # 좌우 반전
  , vertical_flip=True             # 상하 반전
  , brightness_range=[0.5, 1.5]    # 명암 증강
)
test_datagen = ImageDataGenerator()
train_generator = train_dategen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=32, class_mode='categorical', shuffle=True)
test_generator = test_datagen.flow_from_directory(test_dir, target_size=(224, 224), batch_size=32, class_mode='categorical', shuffle=True)
class_num = len(train_generator.class_indices)
labels = list(train_generator.class_indices.keys())
print(f'분류 수 : {class_num}, 라벨 : {labels}')


# tensorflow의 pre-trained model 가져오기
conv_layer = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3)) # 이전에 학습된 모델을 가져온 것
conv_layer.summary()
# VGG16 모델의 잘 학습 되어진 부분을 학습 되지 않도록 고정
for layer in conv_layer.layers:
    layer.trainable = False
    
model = Sequential() # 비어있는 모델을 만든 것
model.add(conv_layer) # 잘된 학습을 추가
model.add(Flatten()) # 식물 분류를 위한 fine tuning 부분
model.add(Dense(class_num, activation='softmax'))
model.summary()
# 위는 모델 구조 만든 것

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['acc'])
model.fit(train_generator
                    ,steps_per_epoch=train_generator.samples/train_generator.batch_size
                    ,epochs=1
                    ,validation_data=test_generator
                    ,validation_steps=test_generator.samples/test_generator.batch_size
                    ,verbose=1)
model.save('plant_model_1.h5')
