import streamlit as st
import pandas as pd
import plotly.graph_objects as go



file, uploaded_files = None, None
filename = None

# Display a title
st.title('3D Scatter Plot')

# upload a dataset as CSV
st.sidebar.subheader("Upload your dataset as CSV format.")
st.sidebar.write('Note: The first row MUST be header for column names.')
uploaded_files = st.sidebar.file_uploader("", type='csv', accept_multiple_files=True)


if uploaded_files != None:
    files = {}
    for uploaded_file in uploaded_files:
        files[uploaded_file.name] = uploaded_file

    filename = st.sidebar.selectbox('Choose the filename for ploting.', files.keys())
    if filename != None:
        file = files[filename]


if file != None:

    # Store as pandas DataFrame
    df = pd.read_csv(file)

    # Show the table data when checkbox is ON.
    if st.checkbox('Show the dataset as table data'):
        st.dataframe(df)


    # Select the column names to plot.
    st.sidebar.header('Select the column names to plot.')

    x_lbl = st.sidebar.selectbox('x axis: ', df.columns)
    y_lbl = st.sidebar.selectbox('y axis: ', df.drop(columns=[x_lbl]).columns)
    z_lbl = st.sidebar.selectbox('z axis: ', df.drop(columns=[x_lbl, y_lbl]).columns)


    # Create an object for 3d scatter
    trace1 = go.Scatter3d(
        x = df[x_lbl], y = df[y_lbl], z = df[z_lbl],
        mode = 'markers',
        marker = dict(size=5, color='red'),
    )

    # Create an object for graph layout
    fig = go.Figure(data=[trace1])
    fig.update_layout(
        scene = dict(
        xaxis_title = x_lbl,
        yaxis_title = y_lbl,
        zaxis_title = z_lbl),
        margin=dict(r=20, b=10, l=10, t=10),
    )

    st.plotly_chart(fig, use_container_width=True)


