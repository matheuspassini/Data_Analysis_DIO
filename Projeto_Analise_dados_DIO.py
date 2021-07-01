#!/usr/bin/env python
# coding: utf-8

# # Trabalhando com a análise de dados mundiais

# In[2]:


import pandas as pd


# In[17]:


data = pd.read_csv('./datasets/Gapminder.csv', delimiter=';')


# In[18]:


data


# In[19]:


data.columns = ['pais', 'continente', 'ano', 'expec_vida', 'populacao', 'pib']


# In[20]:


data.head(3)


# In[21]:


data.shape


# In[22]:


data.dtypes


# In[23]:


data.continente.unique()


# In[24]:


data.isnull().sum()


# In[25]:


df = data.dropna(subset=['continente'])


# In[27]:


df.isnull().sum()


# In[63]:


df.describe()


# In[28]:


import plotly.express as px


# In[46]:


fig = px.bar(df, x=df.continente.unique(), y=
df.pais.groupby(df.continente).nunique(), title = 'Quantidade de países por continente na pesquisa')
fig.show()


# In[62]:


mean_expec = df.expec_vida.groupby(df.ano).mean()
fig = px.line(df, x=df.ano.sort_values().unique(), y=mean_expec, title='Expectativa de vida no mundo por ano')
fig.show()


# In[66]:


mean_expec_pais = df.expec_vida.groupby(df.continente).mean()
fig = px.bar(df, x=df.continente.unique(), y=mean_expec_pais, title='Expectativa de vida média no mundo')
fig.show()


# In[88]:


soma = df.populacao.groupby(df.ano).sum()
fig = px.line(df, x=df.ano.sort_values().unique(), y=soma, title='População mundial')
fig.show()


# In[232]:


fig = px.bar(df, x=df.ano.sort_values().unique(), 
             y=df.populacao.groupby(df.ano).sum(), 
            color=df.expec_vida.groupby(df.ano).mean(), 
             height=400)
fig.show()


# # Trabalhando com análise de planilhas do Excel

# In[94]:


df1 = pd.read_excel('./datasets/Aracaju.xlsx')
df2 = pd.read_excel('./datasets/Fortaleza.xlsx')
df3 = pd.read_excel('./datasets/Natal.xlsx')
df4 = pd.read_excel('./datasets/Recife.xlsx')
df5 = pd.read_excel('./datasets/Salvador.xlsx')


# In[95]:


dataset = pd.concat([df1,df2,df3,df4,df5])


# In[97]:


dataset


# In[99]:


dataset.dtypes


# In[100]:


dataset['LojaID'] = dataset['LojaID'].astype('object')


# In[101]:


dataset.isnull().sum()


# In[102]:


dataset.mean()


# In[105]:


dataset['receita'] = dataset['Vendas'].mul(dataset['Qtde'])


# In[106]:


dataset.head()


# In[107]:


dataset['Receita/Vendas'] = dataset['receita'] / dataset['Vendas']


# In[108]:


dataset.head()


# In[109]:


dataset.receita.max()


# In[110]:


dataset.receita.min()


# In[111]:


dataset.nlargest(3,'receita')


# In[113]:


dataset.nsmallest(3,'receita')


# In[121]:


ci = dataset.Cidade.unique()
receita_ci = dataset.receita.groupby(dataset.Cidade).sum()
fig = px.bar(dataset, x=ci, y=
receita_ci, title = 'Receita por cidade brasileira',
            labels={'x':'Cidade', 'y':'Receita'}
            )
fig.show()


# In[123]:


dataset.sort_values('receita', ascending = False).head(5)


# In[124]:


dataset['Data'] = dataset['Data'].astype('int64')


# In[125]:


dataset.dtypes


# In[127]:


dataset['Data'] = pd.to_datetime(dataset['Data'])


# In[128]:


dataset.receita.groupby(dataset.Data.dt.year).sum()


# In[129]:


dataset['Ano_Venda'] = dataset['Data'].dt.year


# In[130]:


dataset.head(7)


# In[133]:


dataset['mes'], dataset['dia'] = (dataset['Data'].dt.month, dataset['Data'].dt.day)


# In[134]:


dataset.sample(5)


# In[135]:


dataset.Data.min()


# In[136]:


dataset.Data.max()


# In[137]:


dataset['diferenca_dias'] = dataset['Data'] - dataset['Data'].min()


# In[138]:


dataset.sample(3)


# In[139]:


dataset['trimestre'] = dataset['Data'].dt.quarter


# In[140]:


dataset.sample(2)


# In[144]:


#Filtrando as vendas de 2019 do mês de março
vendas_mar_2019 = dataset.loc[(dataset['Data'].dt.year == 2019)&(dataset['Data'].dt.month == 3)]
vendas_mar_2019


# In[148]:


dataset['LojaID'].value_counts(ascending=True).plot(kind='barh');


# In[149]:


dataset.receita.groupby(dataset['Data'].dt.year).sum().plot(kind='pie')


# In[151]:


dataset.Cidade.value_counts()


# In[152]:


import matplotlib.pyplot as plt


# In[156]:


dataset['Cidade'].value_counts().plot.bar(title = 'Total de vendas por Cidade', color = 'green')
plt.xlabel('Cidade')
plt.ylabel('Total Vendas');


# In[157]:


plt.style.use('ggplot')


# In[158]:


dataset.Qtde.groupby(dataset.mes).sum().plot()
plt.xlabel('Mês')
plt.ylabel('Total de Produtos vendidos por mês')
plt.legend();


# In[159]:


dataset.Qtde.groupby(dataset.mes).sum()


# In[160]:


df_2019 = dataset[dataset.Ano_Venda == 2019]


# In[167]:


df_2019.Qtde.groupby(df_2019.mes).sum().plot(marker = 'o')
plt.xlabel('Mês')
plt.ylabel('Total produtos vendidos em 2019')
plt.legend();


# In[169]:


plt.hist(dataset.Qtde, color='purple');


# In[171]:


plt.scatter(x=df_2019['dia'], y = df_2019.receita);


# # Análise exploratória de vendas

# In[172]:


plt.style.use('seaborn')


# In[174]:


d = pd.read_excel('./datasets/AdventureWorks.xlsx')


# In[175]:


d.head()


# In[177]:


d.dtypes


# In[178]:


d.isnull().sum()


# In[179]:


#Receita total
d['Valor Venda'].sum()


# In[180]:


#Custo total
d['custo'] = d['Custo Unitário'].mul(d['Quantidade'])


# In[182]:


d.head(1)


# In[183]:


d['custo'].sum()


# In[185]:


d['lucro'] = d['Valor Venda'] - d['custo']


# In[186]:


d.head(1)


# In[188]:


round(d['lucro'].sum(),2)


# In[189]:


d['entrega'] = d['Data Envio'] - d['Data Venda']


# In[191]:


d.head(1)


# In[192]:


d['entrega'] = (d['Data Envio'] - d['Data Venda']).dt.days


# In[193]:


d.entrega.dtype


# In[195]:


d.entrega.groupby(d.Marca).mean()


# In[200]:


#lucro por ano e marca
pd.options.display.float_format = '{:20,.2f}'.format
d.lucro.groupby([d['Data Venda'].dt.year, d.Marca]).sum()


# In[205]:


#Total de produtos vendidos
d.Quantidade.groupby(d.Produto).sum().sort_values().plot(kind='barh');


# In[208]:


d.lucro.groupby(d['Data Venda'].dt.year).sum().plot(kind='bar', title = 'Lucro por Ano')
plt.xlabel('Ano')
plt.ylabel('Receita');


# In[209]:


d_2009 = d[d['Data Venda'].dt.year == 2009]


# In[210]:


d_2009.head(1)


# In[213]:


d_2009.lucro.groupby(d_2009['Data Venda'].dt.month).sum().plot();


# In[220]:


d_2009.lucro.groupby(d_2009.Marca).sum().plot(kind='bar')
plt.ylabel('Lucro')
plt.xlabel('Marca')
plt.xticks(rotation='horizontal');


# In[218]:


d_2009.lucro.groupby(d_2009.Classe).sum().plot(kind='bar', title='Lucro por Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');


# In[222]:


d.entrega.describe()


# In[223]:


plt.boxplot(d['entrega']);


# In[224]:


plt.hist(d.entrega);


# In[229]:


print(d.entrega.min())
print(d.entrega.max())


# In[230]:


d[d.entrega == 20]

