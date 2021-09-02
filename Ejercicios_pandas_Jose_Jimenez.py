#!/usr/bin/env python
# coding: utf-8

# # Ejercicios con `pandas`

# Importe las librerías necesarias:

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# Imprima las versiones de todas la librerías

# In[20]:


pip list


# Importe los datos desde [aqui](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). Asígnelos a una variable `chipo`.

# In[11]:


chipo=pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")


# Muestre las primeras 10 entradas del dataframe

# In[24]:


df=pd.DataFrame(chipo)
df.iloc[:10]


# Cual es el número total de observaciones en el dataset?

# In[27]:


# solucion 1
df.count()


# In[1]:


# solucion 2


# Cuantas columnas hay en el dataset? Copielas a una lista.

# In[45]:


encabezados=df.columns.values
len(encabezados)


# Imprima el nombre de las columnas

# In[43]:


print(encabezados)


# Como está indexado el dataset?

# In[ ]:





# Cual fue el objeto más pedido?

# In[57]:


mas_pedido=chipo.item_name.value_counts()
mas_pedido


# Para el objeto más pedido, cuantos fueron?

# In[58]:


#El objeto mas pedido fue Chicken Bowl, con un total de 726 unidades.
mas_pedido[:1]


# Cual fue el item más pedido en la columna `choice_description`?

# In[65]:


mas_pedido_choice_description=chipo.choice_description.value_counts()
mas_pedido_choice_description[:1]


# Cuantos items fueron pedidos en total?

# In[ ]:


mas_pedido_choice_description


# Convierte el precio en un `float`

# In[ ]:





# Cuanto fue la ganancia total en el periodo del dataset?

# In[ ]:





# Cúantos pedidos se hicieron?

# In[68]:


chipo.count()


# Cual fue el promedio de ganancia por orden?

# In[ ]:





# Cuántos items se vendieron en total?

# In[ ]:




