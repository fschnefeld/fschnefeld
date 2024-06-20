import streamlit as st
#from IPython.display import HTML
        # define the URL of the Looker report
looker_url = "https://lookerstudio.google.com/embed/reporting/bf900ecb-3657-4901-b5bd-ab8899411118/page/p_e27a3gsx4c"
code = '''import streamlit as st
from IPython.display import HTML
        # define the URL of the Looker report
looker_url = ""

# define the HTML code to embed the report with full-width styling
looker_html = f"""
<style>
    #looker-embed {{
        width: 100vh;
        height: 100vh;
    }}
</style>
<iframe id="looker-embed" src="{looker_url}" frameborder="0" allowfullscreen></iframe>
"""

# display the report in Streamlit using the HTML code
st.set_page_config(
                page_title="Frederik's Portfolio",
                page_icon=":man_technologist:",
                layout="wide",
                initial_sidebar_state="expanded")

with st.container():
    st.subheader("My portfolio page")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do I do?")

# Define the sidebar menu items
menu_items = ["Home", "Socials", "Code", "Projects", "Dashboard"]

# Create the sidebar with the menu items
st.sidebar.header("Some sort of menu")
selected_item = st.sidebar.selectbox("", menu_items)

    # Define the URL for the LinkedIn profile
linkedin_url = "https://www.linkedin.com/in/your-linkedin-profile/"
# Show the selected page content
if selected_item == "Home":
    st.write("Welcome to the home page!")
if selected_item == "Projects":
    wtih st.container():
        st.write("These are some of my projects")
        st.code("")
if selected_item == "Dashboard":
    with st.container():
        st.markdown(looker_html, unsafe_allow_html=True)


else:
# Add a button that links to the LinkedIn profile
    st.button("To my LinkedIn")

#To run, remember to type "streamlit run Portfolio.py" in the terminal'''

code_2 = '''data = pd.read_csv("python_course/fb_data - dataset_Facebook.csv")
data.head()'''

# define the HTML code to embed the report with full-width styling
looker_html = f"""
<style>
    #looker-embed {{
        width: 100vh;
        height: 100vh;
    }}
</style>
<iframe id="looker-embed" src="{looker_url}" frameborder="0" allowfullscreen></iframe>
"""

# display the report in Streamlit using the HTML code
st.set_page_config(
                page_title="Frederik's Portfolio",
                page_icon=":man_technologist:",
                layout="wide",
                initial_sidebar_state="expanded")

with st.container():
    st.subheader("My portfolio page")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do I do?")

# Define the sidebar menu items
menu_items = ["Home", "Socials", "Code", "Projects", "Dashboard"]

# Create the sidebar with the menu items
st.sidebar.header("Some sort of menu")
selected_item = st.sidebar.selectbox("", menu_items)
container = st.container()
    # Define the URL for the LinkedIn profile
linkedin_url = "https://www.linkedin.com/in/your-linkedin-profile/"
# Show the selected page content
if selected_item == "Home":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write("Welcome to the home page!")
    with col2:
        st.title("Left-Bottom Quadrant")
        st.write("Content for left-bottom quadrant goes here.")
if selected_item == "Projects":
    with container:
        with container:
            st.write("These are some of my projects")
            st.code(code, language="python")
    with container:
        st.markdown(looker_html, unsafe_allow_html=True)
if selected_item == "Code":
    with container:
        st.code(code_2, language="python")
else:
# Add a button that links to the LinkedIn profile
    st.button("To my LinkedIn")

#To run, remember to type "streamlit run Portfolio.py" in the terminal
