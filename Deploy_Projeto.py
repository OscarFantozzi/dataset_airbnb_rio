#!/usr/bin/env python
# coding: utf-8

# In[14]:


# import pandas as pd

# df = pd.read_csv('bases_teste.csv')

# col = list(df.columns)[1:]

# print(len(col))


# In[3]:


import pandas as pd
import streamlit as st
import joblib


# 
# ## Importando o Modelo para Dentro do Python
# 
# 

# In[10]:



# modelo = joblib.load('modelo.joblib')
# modelo.feature_importances_


# In[4]:


# Trazendo as colunas que são as caracteristicas que o modelo precisa



#'host_is_superhost', 
# 'host_listings_count', 'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds'
# , 'amenities', 'extra_people', 'minimum_nights', 'instant_bookable', 'is_business_travel_ready', 
# 'ano', 'mes', 'property_type_Apartment', 'property_type_Bed and breakfast', 'property_type_Condominium', 
# 'property_type_Guest suite', 'property_type_Hostel', 'property_type_House', 'property_type_Loft', 'property_type_Others', 
# 'property_type_Serviced apartment', 'room_type_Entire home/apt', 'room_type_Hotel room', 'room_type_Private room', 
# 'room_type_Shared room', 'bed_type_Outros', 'bed_type_Real Bed', 'cancellation_policy_Outros', 'cancellation_policy_flexible', 
# 'cancellation_policy_moderate', 'cancellation_policy_strict', 'cancellation_policy_strict_14_with_grace_period']

 
   









x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable':0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period','Outros']
          }



dicionario = {}


for item in x_listas:
    
    for valor in x_listas[item]:
        
        dicionario[f'{item}_{valor}'] = 0
        





# Criar os campos de formulário no Streamlit


for item in x_numericos:
    
    if item == 'latitude' or item =='longitude':
        
        valor = st.number_input(f'{item}',step=0.00001,value=0.0,format='%.5f')
        
    elif item == 'extra_people' : 
        
        valor = st.number_input(f'{item}',step=0.01,value = 0.0)
    
    else:
        
        valor = st.number_input(f'{item}',step=1,value=0) # Cria os botões de acordo com a chave do dicionário
        x_numericos[item] = valor
    
    


    
for item in x_tf:
    valor = st.selectbox(f'{item}',('Sim','Não'))
    if valor == 'Sim':
        x_tf[item] = 1
        
    else:
        x_tf[item] = 0
    
    
for item in x_listas:
    
    valor = st.selectbox(f'{item}',x_listas[item])
    
    dicionario [f'{item}_{valor}'] = 1
    

# Criando o botão no streamlit

dicionario.update(x_numericos)
dicionario.update(x_tf)
botao = st.button('Prever Valor')

if botao:
    
    
    # Juntar um dicionário no outro

    
    dicionario.update(x_numericos)
    dicionario.update(x_tf)


# Criar um DataFrame

    valores_X = pd.DataFrame(dicionario,index=[0])


    df = pd.read_csv('bases_teste.csv')
    colunas = list(df.columns)[1:]

    valores_X = valores_X[colunas]

    modelo = joblib.load('modelo.joblib')

    preco = modelo.predict(valores_X)[0]

    st.write(preco)

    

    
 



# In[ ]:




