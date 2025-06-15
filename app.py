import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Function to preprocess image
def preprocess_image(image):
    try:
        # Convert to RGB to ensure 3 channels
        img = image.convert('RGB')
        # Resize to 224x224
        img = img.resize((224, 224))
        # Convert to numpy array and normalize
        img_array = np.array(img) / 255.0
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        # Verify shape
        if img_array.shape != (1, 224, 224, 3):
            raise ValueError(f"Unexpected image shape: {img_array.shape}")
        return img_array
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

# Tumor descriptions
tumor_info = {
    'Glioma': 'Glioma adalah tumor yang berasal dari sel glial di otak atau sumsum tulang belakang. Biasanya ditemukan di otak besar dan dapat bervariasi dari jinak hingga ganas.',
    'Meningioma': 'Meningioma adalah tumor yang tumbuh dari meninges, lapisan pelindung otak dan sumsum tulang belakang. Sebagian besar bersifat jinak, tetapi bisa menyebabkan gejala jika menekan otak.',
    'Pituitary Tumor': 'Tumor hipofisis adalah pertumbuhan abnormal pada kelenjar hipofisis, yang mengatur hormon. Biasanya jinak, tetapi dapat memengaruhi fungsi hormonal.',
    'No Tumor': 'Tidak ada tumor yang terdeteksi pada citra MRI. Namun, konsultasikan dengan dokter untuk pemeriksaan lebih lanjut.'
}

# Page configuration
st.set_page_config(page_title="Klasifikasi Tumor Otak", layout="wide", icon="🧠")
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
        padding: 20px;
        font-family: 'Roboto', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg, #28a745, #34c759);
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        border-radius: 8px;
        transition: background 0.3s, transform 0.2s;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #218838, #2db54d);
        transform: scale(1.02);
    }
    .title {
        font-size: 36px;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    .result {
        font-size: 28px;
        font-weight: bold;
        color: #fff;
        margin-bottom: 10px;
    }
    .confidence {
        font-size: 20px;
        color: #fff;
        margin-bottom: 15px;
    }
    .info-text {
        font-size: 16px;
        color: #7f8c8d;
        line-height: 1.6;
    }
    .disclaimer {
        font-size: 14px;
        color: #7f8c8d;
        margin-top: 20px;
    }
    .progress-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        overflow: hidden;
        margin-bottom: 20px;
    }
    .progress-fill {
        background: linear-gradient(90deg, #28a745, #34c759);
        height: 100%;
        transition: width 0.5s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='title'>Klasifikasi Tumor Otak Berbasis AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Unggah Citra MRI untuk Mendeteksi Jenis Tumor Otak Secara Cepat dan Akurat</p>", unsafe_allow_html=True)

# Load model with error handling
try:
    model_path = 'brain_tumor_model.keras'
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Please ensure the model is in the correct directory.")
        st.stop()
    model = tf.keras.models.load_model(model_path)
    class_names = ['Glioma', 'Meningioma', 'Pituitary Tumor', 'No Tumor']
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Create two columns
col1, col2 = st.columns([1, 1])

# Left column: Image upload and processing
with col1:
    st.markdown("<div style='padding: 10px;'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Pilih Citra MRI (JPEG/PNG)", type=["jpg", "png"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Citra MRI Anda", use_container_width=True)
            
            if st.button("Proses Citra"):
                with st.spinner("Memproses citra..."):
                    # Preprocess and predict
                    img_array = preprocess_image(image)
                    if img_array is None:
                        st.stop()
                    prediction = model.predict(img_array)
                    predicted_class = class_names[np.argmax(prediction)]
                    confidence = np.max(prediction) * 100
                    
                    # Store results in session state for right column
                    st.session_state['predicted_class'] = predicted_class
                    st.session_state['confidence'] = confidence
                    st.session_state['processed'] = True
        except Exception as e:
            st.error(f"Error processing image: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

# Right column: Results and additional info
with col2:
    st.markdown("<div style='padding: 10px;'>", unsafe_allow_html=True)
    if 'processed' in st.session_state and st.session_state['processed']:
        # Result card
        st.markdown(f"<p class='result'>Hasil Klasifikasi: {st.session_state['predicted_class']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='confidence'>Tingkat Kepercayaan: {st.session_state['confidence']:.2f}%</p>", unsafe_allow_html=True)
        
        # Progress bar
        st.markdown(f"""
            <div class='progress-bar'>
                <div class='progress-fill' style='width: {st.session_state['confidence']}%;'></div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<p class='info-text'>{tumor_info[st.session_state['predicted_class']]}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("<p class='disclaimer'>Disclaimer: Ini adalah alat bantu diagnosis dan tidak menggantikan penilaian medis profesional.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)