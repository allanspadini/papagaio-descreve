import streamlit as st
from transformers import pipeline
from PIL import Image
from deep_translator import GoogleTranslator

def carrega_imagem(image_file):

    img = Image.open(image_file)
    return img


@st.cache_resource
def funcao():
    return pipeline('image-to-text',model='nlpconnect/vit-gpt2-image-captioning')
caption = funcao()


st.title('Papagaio descreve')
st.image('papagaio.jfif')




        
st.markdown('''O papagaio descreve gera legendas para imagens. 
Seu funcionamento é melhor em fotos e bem inferior em ilustrações.
''')
image_file = st.file_uploader('Suba uma imagem',type=['PNG','JPG','JPEG'])
        
if image_file is not None:
            
    st.image(image_file)
    dicionario = caption(carrega_imagem(image_file))
    st.markdown(' ## Descrição: \n')
    traducao = GoogleTranslator(source='auto', target='pt').translate(dicionario[0]['generated_text'])
    st.markdown('## '+ traducao)

