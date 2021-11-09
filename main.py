import streamlit as st
from NER_visualizer import *
from coordinates_visualizer import *
from NN_regression import *
from streamlit_folium import folium_static
import os

def main():
    st.title('Study Group PayAI: RappiBank')
    st.markdown("<h1 style='text-align: center; color: black;'>2021-11-09</h1>", unsafe_allow_html=True)
    st.sidebar.image('images/Rappi.png')
    tabs = st.sidebar.multiselect("", ['NER spaCy', 'Orders Points Location', 'NN Regression'])
    if tabs:
        analyze = tabs[0]
        if analyze == "NER spaCy":
            st.title(analyze)
            dependency()
            st.markdown('#')
            st.markdown('* For more information, please read the [Documentation](https://spacy.io/usage/visualizers)')
            st.markdown('* [Github](https://github.com/explosion/spacy-streamlit) for the wrapper spaCy-streamlit')
            st.markdown('* You can fine-tune your very own NERs, [here](https://spacy.io/usage/training) you can find more information')
        elif analyze == 'Orders Points Location':
            st.title(analyze)
            try:
                st.header('Look at the spatial location of the orders for the specific selected hour...')
                folium_static(plot_map())
                st.header('Now, let us look at the traffic of orders based on an hourly basis...')
                st.write(orders_histogram())
                st.header('Finally, let us look at the relative number of orders per OS and Payment Method...')
                st.write(plot_treemap())
            except:
                pass

        elif analyze == 'NN Regression':
            st.title(analyze)
            st.write('Here we can train a NN to predict the squared of a given number. You can choose whether to (re)train your very own model or use the pre-trained one!!!')
            if st.button('Train'):
                train()
            else:
                pass

            if os.path.exists('model/model.h5'):
                sample = st.text_input('Please input a number: ')
                if st.button('Predict'):
                    st.write('Predicted output: ')
                    st.latex('\hat y = {:.2f}'.format(predict(float(sample))))
                    st.balloons()
                else:
                    pass
            else:
                pass

            
           
if __name__ == "__main__":
    main()