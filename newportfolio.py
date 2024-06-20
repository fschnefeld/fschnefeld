import streamlit as st

# Set the URLs for embedding
looker_url = "https://lookerstudio.google.com/embed/reporting/bf900ecb-3657-4901-b5bd-ab8899411118/page/p_e27a3gsx4c"
looker_html = f"""
<style>
    #looker-embed {{
        width: 100%;
        height: 100vh;
    }}
</style>
<iframe id="looker-embed" src="{looker_url}" frameborder="0" allowfullscreen></iframe>
"""

slides_url = "https://docs.google.com/presentation/d/1eUg7mOz2F3LxU7qaoh2DIn17yErVy3aFID6xYaGVV34/edit?usp=sharing"
slides_html = f"""
<style>
    #slides-embed {{
        width: 100%;
        height: 500px;
    }}
</style>
<iframe id="slides-embed" src="{slides_url}" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
"""

figma_url = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2Fj9vzQAVF8kRz8fNzRqhdOs%2FUntitled%3Fnode-id%3D1-1010%26t%3DdaH5wGTBiZgx0iwU-1"
figma_html = f"""
<style>
    #figma-embed {{
        width: 100%;
        height: 600px;
    }}
</style>
<iframe id="figma-embed" src="{figma_url}" frameborder="0"></iframe>
"""

tableau_html = """
<div class='tableauPlaceholder' id='viz1718877568872' style='position: relative'>
<noscript><a href='#'>
<img alt='Dashboard 5 ' src='https://public.tableau.com/static/images/Te/Template_17010282050560/Dashboard5/1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz' style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> 
<param name='site_root' value='' />
<param name='name' value='Template_17010282050560/Dashboard5' />
<param name='tabs' value='no' />
<param name='toolbar' value='yes' />
<param name='static_image' value='https://public.tableau.com/static/images/Te/Template_17010282050560/Dashboard5/1.png' />
<param name='animate_transition' value='yes' />
<param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' />
<param name='display_overlay' value='yes' />
<param name='display_count' value='yes' />
<param name='language' value='en-US' />
</object>
</div>                
<script type='text/javascript'>                    
var divElement = document.getElementById('viz1718877568872');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
if ( divElement.offsetWidth > 800 ) {{ 
    vizElement.style.width='1000px';vizElement.style.height='827px';
}} else if ( divElement.offsetWidth > 500 ) {{ 
    vizElement.style.width='1000px';vizElement.style.height='827px';
}} else {{ 
    vizElement.style.width='100%';vizElement.style.height='727px';
}}                     
var scriptElement = document.createElement('script');                    
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>
"""

# Set the page configuration
st.set_page_config(
    page_title="Data Journey Portfolio",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar buttons for navigation
st.sidebar.header("Navigation")
if st.sidebar.button("Home"):
    selected_page = "Home"
if st.sidebar.button("Dashboards"):
    selected_page = "Dashboards"
if st.sidebar.button("Code"):
    selected_page = "Code"
if st.sidebar.button("ML Models"):
    selected_page = "ML Models"
if st.sidebar.button("Data Pipelines"):
    selected_page = "Data Pipelines"
if st.sidebar.button("Articles"):
    selected_page = "Articles"

# Main content based on sidebar selection
if selected_page == "Home":
    st.title("Transforming Business Through Data: A Comprehensive Journey")
    st.header("Introduction")
    st.markdown("""
    Welcome to the journey of DataCorp, a retail company facing challenges in customer retention and sales growth. Our mission is to showcase how data-driven strategies can transform these challenges into opportunities for growth.
    """)
    st.header("Business Problem")
    st.markdown("""
    DataCorp has been experiencing a decline in customer retention and stagnant sales growth. To turn the tide, we embarked on a data-driven transformation journey.
    """)
    st.header("Data Collection and Storage")
    st.markdown("""
    ### Objective
    Explain the sources and methods of data collection.

    ### Content
    - **CRM data**: Customer demographics, purchase history, and interaction logs.
    - **Transactional data**: Sales records, product returns, and payment methods.
    - **Web data**: Website traffic, user behavior, and online engagement.
    - **Data storage solutions**: Databases, cloud storage.
    - **Data extraction tools and processes**: APIs, ETL pipelines.

    **Story**: "Our journey begins with the collection of diverse data sources. CRM data reveals customer preferences, transactional data highlights purchasing patterns, and web data uncovers online behavior. This data is securely stored and processed for further analysis."
    """)
    st.header("Data Analysis and Insights")
    st.markdown("""
    ### Objective
    Describe how data is processed and analyzed to generate insights.

    ### Content
    - **Data cleaning and preprocessing techniques**.
    - **Analytical tools and techniques**: Python, R, SQL.
    - **Key insights derived from the data**.

    **Story**: "Through rigorous data analysis, patterns emerged. We discovered that loyal customers were leaving due to unaddressed concerns, and marketing campaigns were not reaching the right audience. These insights were crucial for reshaping our strategy."
    """)

if selected_page == "Dashboards":
    st.header("Insights: Tableau Dashboard")
    st.markdown("""
    Here is an interactive Tableau dashboard that illustrates the insights derived from our data analysis.
    """)
    st.markdown(tableau_html, unsafe_allow_html=True)

if selected_page == "Code":
    st.header("Code")
    code_1 = '''import streamlit as st
from IPython.display import HTML
# define the URL of the Looker report
looker_url = "https://lookerstudio.google.com/embed/reporting/bf900ecb-3657-4901-b5bd-ab8899411118/page/p_e27a3gsx4c"
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

    st.code(code_1, language="python")
    code_2 = '''data = pd.read_csv("python_course/fb_data - dataset_Facebook.csv")
data.head()'''
    st.code(code_2, language="python")

if selected_page == "ML Models":
    st.header("ML Models")
    st.markdown("""
    ### Objective
    Describe machine learning models used in the project.

    ### Content
    - **Models used**: Classification, regression, clustering.
    - **Tools and libraries**: scikit-learn, TensorFlow, Keras.
    - **Model performance and evaluation**.

    **Story**: "By implementing machine learning models, we were able to predict customer churn and identify high-value customers. These models helped us tailor our marketing strategies and improve customer
""")