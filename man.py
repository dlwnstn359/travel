import streamlit as st

# 학부모와 학생 비밀번호 설정
parent_password = "parent123"
student_password = "student123"

# 페이지 설정
pages = {
    "코스": [
        st.Page("dlwnstn.py", title="메인"),  # 메인 페이지
        st.Page("z.py", title="1코스"),  # 1코스 페이지
        st.Page("x.py", title="2코스"),  # 2코스 페이지
        st.Page("c.py", title="3코스"),  # 3코스 페이지
        st.Page("v.py", title="4코스"),  # 4코스 페이지 
    ]
}

# 4코스 페이지는 누구나 접근할 수 있게 설정
pg = st.navigation(pages)

# "4코스" 페이지는 비밀번호 없이 접근 가능하게 설정
if pg.current_page == "v.py":
    pg.run()  # 4코스 페이지는 누구나 볼 수 있음
else:
    # 다른 페이지는 비밀번호 인증 필요
    role = st.radio("회원 유형을 선택하세요", ("학부모", "학생"))
    
    if role == "학부모":
        password = st.text_input("학부모 비밀번호를 입력하세요", type="password")
        if password == parent_password:
            st.success("학부모 인증 완료")
            pg.run()  # 인증 후 페이지 실행
        else:
            st.warning("학부모 비밀번호가 틀렸습니다. 다시 입력해주세요.")
    elif role == "학생":
        password = st.text_input("학생 비밀번호를 입력하세요", type="password")
        if password == student_password:
            st.success("학생 인증 완료")
            pg.run()  # 인증 후 페이지 실행
        else:
            st.warning("학생 비밀번호가 틀렸습니다. 다시 입력해주세요.")
