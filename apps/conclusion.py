import streamlit as st


def app():
    st.title('Conclusion')

    st.markdown("""

        - As the population and the number of suicides have a positive correlation, using
        the number of suicides per 100k population would be better and effective metric

        - The number of males that have commited suicides have exceeded that of the
        females by a very large margin. Difference in the male and female population might
        have a slight contribution to this. But still, the difference in number of suicides
        between both the classes is huge

        - The Boomer Generation has suffered the most from this problem, followed by the Silent
        Generation.

        - Even thought we can't see a perfect negative correlation between gdp and the rate
        of suicides, it can be seen that as the gdp increases, the suicide rate gradually
        decreases.
    
        - The number of suicides per 100k population 
        for most of the contries in the plot is controlled to a certain extent and
        does not increase after a certain point in time. this is due to the increase in population in 
        the recent decades and the correlation between the population and the number of suicides
    
    """)