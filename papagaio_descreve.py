import streamlit as st
from transformers import pipeline
from PIL import Image
from deep_translator import GoogleTranslator

def carrega_imagem(image_file):

    img = Image.open(image_file)
    return img


@st.cache_resource
def funcao():
    return pipeline('image-to-text',model='Salesforce/blip-image-captioning-large')
caption = funcao()


st.title('Papagaio descreve')
st.image('papagaio.jfif')
menu = ['Home','Sobre']
escolha = st.sidebar.selectbox('Menu',menu)

if escolha == 'Home':
        

    image_file = st.file_uploader('Suba uma imagem',type=['PNG','JPG','JPEG'])
        
    if image_file is not None:
            
        st.image(image_file)
        dicionario = caption(carrega_imagem(image_file))
        st.markdown(' ## Descrição: \n')
        traducao = GoogleTranslator(source='auto', target='pt').translate(dicionario[0]['generated_text'])
        st.markdown('## '+ traducao)

else:
    st.markdown('''
    Esta aplicação gera a descrição de uma imagem. Este é um exemplo de um recurso que utiliza tecnologias avançadas de inteligência artificial para interpretar e descrever imagens, melhorando a acessibilidade e a experiência do usuário. Uma característica fundamental dessa acessibilidade é o uso de "alt-text" (texto alternativo).

O alt-text é uma breve descrição que pode ser atribuída a uma imagem em uma página da web. Este texto é lido pelos leitores de tela, softwares que são comumente utilizados por pessoas com deficiência visual para navegar na Internet. Quando esses leitores encontram uma imagem, eles leem o alt-text para fornecer uma descrição do conteúdo visual.

A importância do alt-text vai além de sua função essencial para a acessibilidade. Ele também tem um papel significativo na otimização para mecanismos de busca (SEO). Os algoritmos de busca usam o alt-text para entender o conteúdo de uma imagem e indexá-la corretamente, o que pode ajudar a melhorar a classificação de uma página nos resultados de busca.

Além disso, o alt-text pode ser útil em situações em que a imagem não pode ser carregada por algum motivo, como uma conexão de Internet lenta ou um link quebrado. Nesses casos, o alt-text pode fornecer algum contexto sobre o que a imagem deveria ser, melhorando a experiência geral do usuário.

Portanto, seja para melhorar a acessibilidade, otimizar a SEO ou aprimorar a experiência do usuário, o uso de alt-text em imagens é uma prática recomendada na criação de conteúdo para a web. A aplicação que gera descrições de imagens pode ser uma ferramenta valiosa para ajudar a criar alt-texts eficazes e precisos.''')


