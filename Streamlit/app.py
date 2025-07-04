import streamlit as st
import pandas as pd
import numpy as np

## Title of the app
st.title("My First Streamlit App")


# display text
st.write("Hello, World!")


# display dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.write("Here is a sample dataframe:")
st.dataframe(df)

# display a chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Column A', 'Column B', 'Column C']
)
st.write("Here is a sample chart:")
st.line_chart(chart_data)