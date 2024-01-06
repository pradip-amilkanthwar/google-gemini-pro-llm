import streamlit as st

st.set_page_config(page_title="Sample streamlit website", use_column_width="wide")
st.header("This is a website title")
st.write(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque rutrum egestas ipsum. \nInteger eget eros quis ante ornare pharetra. \nNam eu mattis ligula. Vestibulum rutrum dolor eget purus maximus, id interdum sem tristique. Vivamus interdum sem eget malesuada interdum. \nSuspendisse eleifend fringilla urna vel gravida. In iaculis porta risus, ullamcorper bibendum magna euismod non. Proin dapibus suscipit ante eget sodales. \nNulla tempor, ex eget auctor varius, ex odio scelerisque tellus, et varius libero arcu vitae libero. Duis pretium, est id pretium posuere, libero lectus egestas dui, quis accumsan ante lorem at turpis. Integer eget feugiat sapien. \nUt scelerisque congue sapien, ac rutrum tellus bibendum in. Cras non pulvinar dui, ut molestie arcu. Pellentesque quis consequat tellus. Morbi placerat sagittis leo, ut fermentum eros. Suspendisse sodales elementum tortor sit amet feugiat."
)
st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("This is a column 1 header")
        st.write("##")
        st.write(
            "Nam sed egestas massa, ut tempor diam. Donec ac justo sit amet velit sodales dictum. Aliquam erat volutpat. Nunc non accumsan ligula. Phasellus sollicitudin, turpis nec finibus rutrum, metus augue elementum sem, facilisis sollicitudin velit dolor ut ante. Duis sagittis posuere feugiat. Suspendisse potenti. Integer egestas odio eget tempor euismod"
        )

    with col2:
        st.header("This is a right column header")
        st.write("##")
        st.write(
            "Donec et felis nisi. Ut viverra dignissim blandit. Fusce interdum augue molestie eros accumsan rhoncus. Aliquam ornare ante varius ligula vulputate, sed scelerisque enim hendrerit"
        )
