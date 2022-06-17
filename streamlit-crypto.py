import streamlit as st

st.set_page_config(layout="wide") 

#-------------------
# Streamlit Sidebar
#-------------------
fiat = ['USD','EUR','GBP']
tokens = df_scrape.Symbol.values 

# filters selectbox
st.sidebar.title("Filters")
select_token = st.sidebar.selectbox('Tokens', tokens)
select_fiat = st.sidebar.selectbox('Fiat', fiat)

# special expander objects
st.sidebar.markdown('***')
with st.sidebar.expander('Help'):
    st.markdown('''
                    - Select token and fiat of your choice.
                    - Interactive plots can be zoomed or hovered to retrieve more info.
                    - Plots can be downloaded using Plotly tools.''')

#-------------------
# Title Image
#-------------------
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.image('title.png',width=600)
with col3:
    st.write("")
    
st.markdown('***')

#-------------------
# Add crypto logo and name
#-------------------
col1, col2 = st.columns([1,10])
with col1:
    try:
        st.image(f'logos/{select_token}.png',width=70)
    except:
        pass
with col2:
    st.markdown(f'''## {dic1[select_token]}''')
    
#-------------------
# Candlestick chart with moving averages
#-------------------  
st.plotly_chart(fig, use_container_width=True)

#-------------------
# Line Chart with daily trends
#-------------------
st.plotly_chart(fig, use_container_width=True)

#-------------------
# Table showing top 25 cryptos
#-------------------
st.plotly_chart(fig, use_container_width=True)
