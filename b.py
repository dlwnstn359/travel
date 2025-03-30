import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd


# 학부모와 학생 비밀번호 설정
parent_password = "parent123"
student_password = "student123"

# 페이지 설정
pages = ["메인", "1코스", "2코스", "3코스", "4코스"]

# 페이지 선택
page = st.selectbox("페이지를 선택하세요", pages)

# "4코스" 페이지는 비밀번호 없이 접근 가능하게 설정
if page == "4코스":
    st.title("4코스 페이지")
    st.write("이곳은 누구나 접근할 수 있는 페이지입니다.")
    # 4코스 페이지 관련 내용 추가
    # 예시: st.image("4course_image.jpg")
    
else:
    # 나머지 페이지들은 비밀번호 입력 필요
    role = st.radio("회원 유형을 선택하세요", ("학부모", "학생"))

    if role == "학부모":
        password = st.text_input("학부모 비밀번호를 입력하세요", type="password")
        if password == parent_password:
            st.success("학부모 인증 완료")
            # 인증 후 선택된 페이지 내용 표시
            if page == "메인":
                st.title("메인 페이지")
                st.write("메인 페이지 내용입니다.")
                # 예시: st.image("main_image.jpg")
            elif page == "1코스":
                st.title("1코스 페이지")
                st.write("1코스 페이지 내용입니다.")
                # 예시: st.image("1course_image.jpg")
            elif page == "2코스":
                st.title("2코스 페이지")
                st.write("2코스 페이지 내용입니다.")
                # 예시: st.image("2course_image.jpg")
            elif page == "3코스":
                st.title("3코스 페이지")
                st.write("3코스 페이지 내용입니다.")
                # 예시: st.image("3course_image.jpg")
                
        else:
            st.warning("학부모 비밀번호가 틀렸습니다. 다시 입력해주세요.")
    
    elif role == "학생":
        password = st.text_input("학생 비밀번호를 입력하세요", type="password")
        if password == student_password:
            st.success("학생 인증 완료")
            # 인증 후 선택된 페이지 내용 표시
            if page == "메인":
                st.title("메인 페이지")
                st.write("메인 페이지 내용입니다.")
                # 예시: st.image("main_image.jpg")
            elif page == "1코스":
                st.title("1코스 페이지")
                st.write("1코스 페이지 내용입니다.")
                # 예시: st.image("1course_image.jpg")
            elif page == "2코스":
                st.title("2코스 페이지")
                st.write("2코스 페이지 내용입니다.")
                # 예시: st.image("2course_image.jpg")
            elif page == "3코스":
                st.title("3코스 페이지")
                st.write("3코스 페이지 내용입니다.")
                # 예시: st.image("3course_image.jpg")
        else:
            st.warning("학생 비밀번호가 틀렸습니다. 다시 입력해주세요.")
