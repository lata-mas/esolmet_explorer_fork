# %% 
import duckdb
import pandas as pd
# %%
con = duckdb.connect('esolmet.db')

# %%
df = con.execute("SELECT * FROM lecturas").fetchdf()
df
# %%

df_wide = df.pivot(index='fecha', columns='variable', values='valor')


# Opcional: ordenar por fecha
df_wide = df_wide.sort_index()
df_wide
# %%
