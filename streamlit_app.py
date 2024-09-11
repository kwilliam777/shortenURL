import streamlit as st
import pyshorteners

# Streamlit 앱 설정
st.title("URL 단축기")
st.write("긴 URL을 입력하고 '단축하기' 버튼을 눌러 URL을 단축하세요.")

# 사용자로부터 URL 입력 받기
long_url = st.text_input("긴 URL을 입력하세요:")

# URL 단축 기능
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

# '단축하기' 버튼을 클릭했을 때 실행되는 부분
if st.button("단축하기"):
    if long_url:
        try:
            short_url = shorten_url(long_url)
            st.success(f"단축된 URL: {short_url}")
            st.write(f"[단축된 URL 열기]({short_url})")
        except Exception as e:
            st.error(f"URL 단축 중 오류가 발생했습니다: {e}")
    else:
        st.warning("단축할 URL을 입력하세요.")
