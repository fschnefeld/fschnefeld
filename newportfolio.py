import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import nbformat
from nbconvert import HTMLExporter
from IPython.display import HTML
#from streamlit_embedcode import github_gist
import base64

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
ml_model = "https://app.hex.tech/9b615ac9-56f9-406c-a30e-28703fdc2191/app/594909d0-f6f8-4efb-9698-dfaa4fd8fd05/latest?embedded=true"
ml_model_html = f"""
<link rel="stylesheet" href="https://static.hex.site/embed/embedStyles.css">
<div class="hex-embed">
<iframe width="1000" height="1400" frameborder="0" src="{ml_model}" ></iframe>
<a href="https://hex.tech/?embed" target="_blank">
  <img src="https://static.hex.site/embed/hex-logo-embed.png" alt="Hex - a modern data workspace for collaborative notebooks, data apps, dashboards, and reports." />
</a>
<div>
"""
sheets_url = "https://docs.google.com/spreadsheets/d/1IIiPYvZpyd1Zup6F2BR_IsT19gSDP_MtfO_Th_GSgKE/edit?gid=0#gid=0"
sheets_html = f"""
<style> 
    #sheets-embed {{
        width: 100%;
        height: 750px;
    }}
</style>
<iframe id="sheets-embed" src="{sheets_url}" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
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
        height: 1200px;
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
selected_page = st.sidebar.radio("Go to", ["Home", "Dashboards", "Code", "ML Models", "Data Pipelines", "Articles", "API"], index=0)

# Main content based on sidebar selection
if selected_page == "Home":
    st.title("Welcome to my Portfolio!")

    # Insert the button linking to GitHub page here
    if st.button('My Github page'):
        st.write('[Click here to visit my Github page](https://github.com/fschnefeld)')
    st.header("Introduction")
    st.markdown("""
    In my portfolio I've tried to exhibit some of the stuff that I've worked on and to give you an insight into what I do. The idea is to showcase how data-driven strategies can transform these challenges into opportunities for growth.
    """)
    st.header("Business Problem")
    st.markdown("""
    DataCorp has been experiencing a decline in customer retention and stagnant sales growth. To turn the tide, we embarked on a data-driven transformation journey.
    """)
    
    st.markdown(slides_html, unsafe_allow_html=True)
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
    st.markdown(sheets_html, unsafe_allow_html=True)
    st.header("Data Warehouse migration")
    st.markdown(
        """
        ## Tools used: Y42, dbt

        ### Project description: 
        **The project involved migrating a data warehouse from Y42 v1 to v3.**

        ### Scope
        **The scope of the project included converting existing UI data models into SQL models compatible with Y42 v3**

        **Total amount of models rebuilt: 80**

        **Amount of SQL: 4-5,000 lines**

        ### Key takeaways: 

        - **Creating and querying from staging models instead of directly from BigQuery sources**
        - **Adapting UI models to performant SQL logic, using best practices such as CTEs and Intermediary CTEs**
        - **Implementing Incremental Logic to reduce query load**
        - **Ongoing data validation against v1 tables**
        - **Running refactor of BQ SQL** 
        """
    )

    dbt_project_image = 'https://files.oaiusercontent.com/file-nHBmtCSnS4hijP4U68WC6Xgy?se=2024-06-27T13%3A27%3A31Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D299%2C%20immutable&rscd=attachment%3B%20filename%3Dimage.png&sig=mJHQdQMHJTBCjCmbo/lieyIbc7VRo1bDDzbY6tPlTSg%3D'
    st.header("The below image gives a idea of the project. Taken from my own dbt")
    st.markdown(
        """
        
        """
    )
    st.image(image=dbt_project_image, use_column_width="auto")

if selected_page == "Dashboards":
    st.header("Insights: Tableau Dashboard")
    st.markdown("""
    Here is an interactive Tableau dashboard that illustrates the insights derived from our data analysis.
    """)
    st.markdown(figma_html, unsafe_allow_html=True)

if selected_page == "Code":
    st.header("Code")
    st.markdown("This is the code section where you can find various code snippets and examples.")
    
    code_1 = '''import streamlit as st
from IPython.display import HTML
# define the URL of the Google Slides presentation
slides_url = "https://docs.google.com/presentation/d/1eUg7mOz2F3LxU7qaoh2DIn17yErVy3aFID6xYaGVV34/edit?usp=sharing"
# create the HTML code to embed the Google Slides presentation
slides_html = f"""
<style>
    #slides-embed {{
        width: 100%;
        height: 500px;
    }}
</style>
<iframe id="slides-embed" src="{slides_url}" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
"""
st.markdown(slides_html, unsafe_allow_html=True)
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data from a local CSV file
data = pd.read_csv('/content/drive/MyDrive/Colab_Notebooks/trainingdata.csv')

# Assuming the target column is named 'conversion' and has values 0 or 1
# 0: Convert in next session, 1: Convert in this session
X = data.drop(["conversion"], axis=1)
y = data['conversion']

# Define categorical and numerical columns
categorical_cols = ['event', 'region', 'channel', 'device', 'source']
numerical_cols = [col for col in data.columns if data[col].dtype in ['int64', 'float64']]

# Create a preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and evaluate the pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', LogisticRegression(multi_class='ovr', random_state=42))])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

next_session_conversions = (y_pred == 2)

# Indices of users predicted to convert in the next session
indices_next_session = [index for index, value in enumerate(next_session_conversions) if value]

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))'''

    st.code(code_1, language='python')

if selected_page == "ML Models":
    st.header("Machine Learning Models")
    st.markdown(ml_model_html, unsafe_allow_html=True)
    
if selected_page == "Data Pipelines":
    st.header("Data Pipelines")
    st.markdown("""
    ### Overview
    Our data pipelines are designed to efficiently collect, process, and transform data into valuable insights.
    """)
    st.markdown("""
    ![Data Pipeline Flowchart](https://example.com/data-pipeline-flowchart.png)
    """)
    
    st.markdown("""
    ### Key Components
    - **Data Ingestion**: Extracting data from various sources.
    - **Data Processing**: Cleaning and transforming data.
    - **Data Storage**: Storing processed data in databases.
    - **Data Analysis**: Analyzing data to derive insights.
    """)
    st.markdown(sheets_html, unsafe_allow_html=True)

    st.title("DBT Cloud Project View")
    
    code_2 = '''-- models/pnl_analysis.sql
with sales_orders_table as {{ ref('core_orders')}}
,    opex as {{ ref('core_opex')}} 

, revenue AS (
    SELECT
        order_date,
        SUM(order_amount) AS total_revenue
    FROM
        sales_orders_table
    WHERE
        status = 'completed'
    GROUP BY
        order_date
),

cogs AS (
    SELECT
        order_date,
        SUM(cost_of_goods_sold) AS total_cogs
    FROM
        raw.sales_orders
    WHERE
        status = 'completed'
    GROUP BY
        order_date
),

gross_profit AS (
    SELECT
        r.order_date,
        r.total_revenue,
        c.total_cogs,
        (r.total_revenue - c.total_cogs) AS gross_profit
    FROM
        revenue AS r
    LEFT JOIN
        cogs AS c
    ON
        r.order_date = c.order_date
),

operating_expenses AS (
    SELECT
        expense_date,
        SUM(expense_amount) AS total_operating_expenses
    FROM
        opex
    GROUP BY
        expense_date
),

net_profit AS (
    SELECT
        gp.order_date,
        gp.total_revenue,
        gp.total_cogs,
        gp.gross_profit,
        oe.total_operating_expenses,
        (gp.gross_profit - oe.total_operating_expenses) AS net_profit
    FROM
        gross_profit AS gp
    LEFT JOIN
        opex AS oe
    ON
        gp.order_date = oe.expense_date
)

SELECT
    order_date AS date,
    total_revenue,
    total_cogs,
    gross_profit,
    total_operating_expenses,
    net_profit
FROM
    net_profit
ORDER BY
    date;'''

    st.code(code_2, language='sql')

if selected_page == "Articles":
    st.header("Articles")
    st.markdown("Explore various articles and blogs related to our data journey.")
    
    articles = [
        {
            "title": "Why everyone should care about query performance",
            "url": "https://snowfield.substack.com/p/why-everyone-should-care-about-query"
        },
        {
            "title": "Building Effective Data Pipelines",
            "author": "John Smith",
            "url": "https://example.com/data-pipelines"
        }
    ]
    
    for article in articles:
        st.markdown(f"### {article['title']}")
        st.markdown(f"**Author:** {article['author']}")
        st.markdown(f"[Read more]({article['url']})")
    
    st.markdown("""
    ### Latest Blog Post
    Our latest blog post discusses the impact of machine learning on customer retention strategies.
    """)
    
    st.markdown("""
    ![ML Blog Post](https://example.com/ml-blog-post.png)
    """)
    
    st.markdown("""
    ### Key Takeaways
    - Machine learning models can predict customer churn.
    - Personalized marketing campaigns increase customer retention.
    """)
    st.markdown(sheets_html, unsafe_allow_html=True)

if selected_page == "API":
    st.header("API")
    st.markdown("""
    ## Welcome to the API Page
    This page allows you to search for player valuations using the API.
    """)
    
    player_name = st.text_input("Enter player name:")
    
    if st.button("Search"):
        if player_name:
            player_data = search_player_valuation(player_name)
            if player_data is not None and not player_data.empty:
                st.dataframe(player_data)
            else:
                st.warning("No data found for the specified player.")
        else:
            st.warning("Please enter a player name.")
