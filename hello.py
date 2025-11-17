import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.title("Hello Streamlit! 🚀")
st.write("이것은 Streamlit으로 만든 간단한 웹 애플리케이션입니다.")

# image = Image.open("example.jpg")
# st.image(image, caption="예제 이미지", use_column_width=True)


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)