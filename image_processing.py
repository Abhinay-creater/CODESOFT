import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path):
    # Load the image
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Scale pixel values to [0, 1]

    # Extract features
    features = model.predict(img)
    return features

# Load the trained captioning model (RNN or similar)
caption_model = load_model('your_caption_model.h5')

# Function to generate captions
def generate_caption(photo, max_length):
    # Placeholder for the start sequence
    start_sequence = ["<start>"]  # Use your actual start token
    in_text = ' '.join(start_sequence)
    
    for i in range(max_length):
        # Convert text to integer sequence, assuming you have a tokenizer
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length) 

        # Predict next word
        yhat = caption_model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)

        # Map integer back to word (assumes an inverse dictionary)
        out_word = word_map[yhat]

        # Stop if we reach the end token
        if out_word == "<end>":
            break

        # Append the word to input
        in_text += ' ' + out_word

    return in_text


# Example usage
img_path = 'path_to_image.jpg'  # Replace with your image path
features = extract_features(img_path)
caption = generate_caption(features, max_length=20)

print("Generated Caption: ", caption)

# Displaying the image
plt.imshow(load_img(img_path))
plt.title(caption)
plt.axis('off')
plt.show()
