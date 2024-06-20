import streamlit as st
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
# Title of the application
st.title("Data Journey Portfolio")

# Introduction section
st.header("Introduction")
st.markdown("""
Welcome to our data journey, showcasing how strategic data consumption can transform business operations and drive success.
""")

# Data Collection and Storage section
st.header("Data Collection and Storage")
st.markdown("""
### Objective
Explain the sources and methods of data collection.

### Content
- **Data sources**: Sales data, customer feedback, web analytics.
- **Data storage solutions**: Databases, cloud storage.
- **Data extraction tools and processes**: APIs, ETL pipelines.

**Story**: "Our journey begins with the diverse data sources feeding into our data warehouse, ensuring all relevant information is captured accurately and stored securely."
""")

# Data Analysis and Insights section
st.header("Data Analysis and Insights")
st.markdown("""
### Objective
Describe how data is processed and analyzed to generate insights.

### Content
- **Data cleaning and preprocessing techniques**.
- **Analytical tools and techniques**: Python, R, SQL.
- **Key insights derived from the data**.

**Story**: "Through rigorous analysis, patterns emerged, revealing critical insights about customer behavior and operational efficiency."
""")

# Embed Tableau dashboard for insights
st.subheader("Insights: Tableau Dashboard")
st.markdown("""
Here is an interactive Tableau dashboard that illustrates the insights derived from our data analysis.
""")
# Replace with your Tableau dashboard URL
tableau_url = "https://public.tableau.com/views/BirdCase/Dashboard5?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link"
st.markdown(f'<iframe src="{tableau_url}" width="100%" height="900"></iframe>', unsafe_allow_html=True)

# Strategic Influence section
st.header("Strategic Influence")
st.markdown("""
### Objective
Show how data insights influence top-level strategy.

### Content
- **Case studies or examples of data-driven decisions**.
- **Impact on strategic planning**: Market expansion, product development.

**Story**: "Armed with data insights, the leadership team redefined their market strategy, focusing on high-potential regions and product lines."
""")

# Data Visualization and Reporting section
st.header("Data Visualization and Reporting")
st.markdown("""
### Objective
Demonstrate the creation and utility of dashboards/reports.

### Content
- **Tools used**: PowerBI, Tableau, Streamlit.
- **Key metrics and KPIs tracked**.
- **Examples of dashboards/reports**.

**Story**: "Interactive dashboards provided real-time visibility into performance metrics, empowering teams to make informed decisions swiftly."
""")

# Implementation and Impact section
st.header("Implementation and Impact")
st.markdown("""
### Objective
Highlight the tangible impact of data-driven strategies and visualizations.

### Content
- **Implementation of strategies based on data insights**.
- **Measurable outcomes**: Increased sales, improved efficiency.
- **Testimonials or feedback from stakeholders**.

**Story**: "The data-driven approach led to a significant increase in sales and operational efficiency, validated by enthusiastic feedback from key stakeholders."
""")

# Embed Google Slides presentation for business impact
st.subheader("Business Impact: Google Slides Presentation")
st.markdown("""
Here is a Google Slides presentation that demonstrates the business impact of our data-driven strategies.
""")
# Replace with your Google Slides presentation URL
slides_url = "https://docs.google.com/presentation/d/1eUg7mOz2F3LxU7qaoh2DIn17yErVy3aFID6xYaGVV34/edit?usp=sharing"
st.markdown(f'<iframe src="{slides_url}" width="100%" height="900" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>', unsafe_allow_html=True)

# Conclusion section
st.header("Conclusion")
st.markdown("""
### Objective
Summarize the journey and its overall impact.

### Content
- **Recap of the key points**.
- **Final thoughts on the importance of data in strategic decision-making**.

**Story**: "This journey underscores the transformative power of data, from strategic planning to operational execution, driving measurable success."
""")

# Embed Figma file for portfolio
st.subheader("Portfolio: Figma File")
st.markdown("""
Here is a Figma file that encapsulates the visual aspects of our data journey.
""")
# Replace with your Figma embed URL
figma_url = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2Fj9vzQAVF8kRz8fNzRqhdOs%2FUntitled%3Fnode-id%3D1-1010%26t%3DdaH5wGTBiZgx0iwU-1"
st.markdown(f'<iframe src="{figma_url}" width="100%" height="900" frameborder="0"></iframe>', unsafe_allow_html=True)
