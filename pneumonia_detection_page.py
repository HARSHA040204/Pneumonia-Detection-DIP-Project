import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize the image to match the model's expected input shape

    # If the image is grayscale, convert it to RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Use keras_image.img_to_array without changing the import statement
    img_array = keras_image.img_to_array(img)
    img_array = preprocess_input(img_array.reshape(1, 224, 224, 3))

    return img_array

def classify_prediction(prediction, threshold=0.5):
    # Assuming binary classification (Normal and Pneumonia)
    if prediction >= threshold:
        return "Pneumonia"
    else:
        return "Normal"

def pneumonia_detection_page():
    # st.title("Pneumonia Detection Based on Chest X-Ray")

    st.write("""
    Pneumonia typically presents as infiltrates or opacities on chest X-rays. 
    These areas represent regions of the lungs where air is replaced by fluid or inflammatory material.

    Common patterns include lobar pneumonia, affecting one lobe of the lung, 
    and bronchopneumonia, which involves smaller areas of the lungs.

    Early detection of pneumonia is crucial for prompt treatment and better outcomes. 
    Chest X-rays play a vital role in quickly identifying the infection and guiding healthcare providers in developing effective treatment plans.
    """)

    # Upload Image through Streamlit
    uploaded_file = st.file_uploader("Place your Chest X-Ray", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Preprocess the image
        img_array = preprocess_image(uploaded_file)

        # Load your Keras model
        # model = load_model('saved_modelcnn.h5')  # Update with your model's filename
        import gdown
        from tensorflow.keras.models import load_model

        # Replace 'YOUR_FILE_ID' with the actual file ID
        file_id = 'YOUR_FILE_ID'
        url = f'https://drive.google.com/uc?id={file_id}'

        # Specify the local file path to save the model
        output_path = 'saved_modelcnn.h5'

        # Download the file
        gdown.download(url, output_path, quiet=False)

        # Load the model
        model = load_model(output_path)


        # Make prediction using your model
        prediction = model.predict(img_array)[0]

        # Classify the prediction
        class_label = classify_prediction(prediction)

        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Display the prediction
        # Display the prediction with custom styling
        st.write(f"<p style='font-size: 24px; text-align: center;'>Prediction: {class_label}</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    pneumonia_detection_page()
