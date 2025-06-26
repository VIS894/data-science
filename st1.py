## streamlist app 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import altair as alt

#st.title("Vishal Dadwani")
st.set_page_config(
    page_title="vishal",
    page_icon="rain" ,
     layout="centered" 

)
st.title("Vishal Dadwani")
st.title("VISHAL")
st.header("1.text element")
st.subheader("markdown,code,latex")
st.markdown("**bold text,*italic text*,code text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()
st.metric(label="revenue", value="1000+", delta="+10%",delta_color="inverse")
st.error("this is ab error message")
st.warning("this is a warning message")
st.info ("this is an info message")
st.success("this is a success message")
st.exception("this is an exception message")

st.header("3.data display")
df = pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

st.divider()

st.header("4.charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.chart(df.reset_index()).mark_line().encode(x='index', y='a')
st.altair_chart(chart, use_container_width=True)
fig, ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.pyplot(fig)


st.divider()