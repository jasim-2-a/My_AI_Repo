import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)
datagen.fit(x_train)


model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1), padding='same'),
    BatchNormalization(),
    Conv2D(32, (3,3), activation='relu', padding='same'),
    MaxPooling2D((2,2)),
    Dropout(0.25),

    Conv2D(64, (3,3), activation='relu', padding='same'),
    BatchNormalization(),
    Conv2D(64, (3,3), activation='relu', padding='same'),
    MaxPooling2D((2,2)),
    Dropout(0.25),

    Flatten(),
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.5),
    Dense(10, activation='softmax')
])


model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ReduceLROnPlateau(factor=0.1, patience=3)
]


history = model.fit(datagen.flow(x_train, y_train_cat, batch_size=128),
                    epochs=30,
                    validation_data=(x_test, y_test_cat),
                    callbacks=callbacks)

loss, accuracy = model.evaluate(x_test, y_test_cat)
print(f"\n✅ Test Accuracy: {accuracy * 100:.2f}%")


y_pred = model.predict(x_test)
print("\n📊 Classification Report:")
print(classification_report(y_test, np.argmax(y_pred, axis=1)))


def plot_results():
    plt.figure(figsize=(12, 4))
    

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend()

    plt.subplot(1, 2, 2)
    cm = confusion_matrix(y_test, np.argmax(y_pred, axis=1))
    plt.imshow(cm, interpolation='nearest', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.show()

plot_results()


def predict_sample(index):
    image = x_test[index]
    prediction = model.predict(np.expand_dims(image, axis=0))[0]
    predicted_label = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    
    plt.figure(figsize=(6, 3))
    plt.imshow(image.squeeze(), cmap='gray')
    plt.title(f"Predicted: {predicted_label} ({confidence:.2f}%)\nActual: {y_test[index]}")
    plt.axis('off')
    plt.show()

print("\n🔍 Random Predictions:")
for i in np.random.choice(range(len(x_test)), 5, replace=False):
    predict_sample(i)