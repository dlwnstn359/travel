import streamlit as st




pages = {
   "코스": [
        st.Page("dlwnstn.py", title="메인"),
        st.Page("z.py", title="1코스"),
        st.Page("x.py", title="2코스"),
        st.Page("c.py", title="3코스"),
        st.Page("v.py", title="4코스"),
        
    ]
    }



pg = st.navigation(pages)
pg.run()