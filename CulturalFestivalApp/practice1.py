# streamlitの基本コンポーネント

import streamlit as st

input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)

st.title('Title')
st.header('Header')
st.subheader('SubHeader')
st.text('Text')
st.markdown('Markdown')

st.markdown("""
        <style>
        .fadein {
            opacity: 0;
            animation: fadeIn 2s ease-in-out forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)
st.markdown('<h1 class="fadein fadeout">🌟 ようこそ、武陽祭へ！</h1>', unsafe_allow_html=True)

st.write(['one', 'two', 'three'])

upload_file = st.file_uploader('Select a file')
# st.write(upload_file)
if upload_file is not None:
    st.write(upload_file)

# var = st.button('test')    
# st.write(var)
if st.button('click'):
    st.write('Hello, World')

if st.checkbox('hide and show'):
    st.write('show')

option = st.selectbox('Select a box', ['A', 'B', 'C'])
if option == 'A':
    st.write('A')

multi = st.multiselect('Select a multiselect', ['1-A', '1-B', '1-C'])
st.write(multi)
for mul in multi:
    if mul == '1-A':
        st.write('1-Aのマップを表示')
    if mul == '1-B':
        st.write('1-Bのマップを表示')

text_one = st.text_input('Input title', placeholder='write here.')
text_two = st.text_area('Input area title', placeholder='write here.')
st.write(text_one)
st.write(text_two)

password = st.text_input("パスワード", type="password")
if password == "pass1":
    st.write("ログインしました")



side_options = ['menu', 'map', 'event']
menu = st.sidebar.selectbox('メニュー', side_options)
if st.sidebar.button("classのボタン"):
     menu = 'class'

if menu == 'menu':
    st.write('メニュー画面を表示します')
elif menu == 'class':
    st.write('メッセージ画面を表示します')
else:
    st.write('エラー')


st.image("images/map.png", use_container_width=True)