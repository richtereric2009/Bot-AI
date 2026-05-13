from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r", encoding="utf-8").readlines()
    image = Image.open(image_path).convert("RGB")
    filter = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    array_image = np.asarray(image)
    normalized_image = (array_image.astype(np.float32) / 127.5 ) - 1
    filter[0] = normalized_image
    predictions = model.predict(filter)
    index = np.argmax(predictions)
    nome_classe = class_names[index]
    score = predictions[0] [index]
    return (nome_classe[2:], score)