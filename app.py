#스트림릿 라이브러리 불러오기
import streamlit as st
st.set_page_config(
    page_title="나만의 사진첩",
    page_icon="C:\chat-gpt-prg\Streamlit-Album\images\카메라 아이콘.jpg"
)


st.title("강아지 모음집")

initial_pokemons = [
    {
        "name": "뽀미",
        "types": ["말티즈"],
        "year": "2015",
        "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMjc1/MDAxNzEwOTEzMzE3MTcw.zt7p-kJWEZw0pml0VW9h4_xpWZhtJA9SIAkTWuLywRgg.k5B3Fu2DqUhzIZ-OcWN1kvipeM4I7lC---0yu26ey-sg.JPEG/6ABBC9E6-9F9B-4A2D-8886-488D8AB47874.jpg?type=w800"
    },
    {
        "name": "초코",
        "types": ["리트리버"],
        "year": "2016",
        "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMTk4/MDAxNzEwOTEzMzE3MjI2.Ak4eBQjQMRrtpv1Qchb4BUz1t6dW5AN5mkj9iWaeMd0g.olYL9e2c8ccybgYn_oMYjY0PII6dmGiV0-MEsNsqqF8g.JPEG/A0DD673E-52B0-4704-8F32-EB87172D4713.jpg?type=w800",
    },
    {
        "name": "흰둥이",
        "types": ["시츄"],
        "year": "2017",
        "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMTk4/MDAxNzEwOTEzMzE3MjMw.7aT5ANu-UhipmJ1TOsKpZ4oNTHbGEhW9AlW9uUEBVpIg.Xo7S1aMCsis-g2PqkP5T4Dix2MtiudDn2hVZuci7vyAg.JPEG/AC30FD80-B6D7-48A7-B543-B87BA04E7828.jpg?type=w800",
    },
    {
        "name": "허세",
        "types": ["허스키"],
        "year": "2018",
        "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMjAw/MDAxNzEwOTEzMzE3MzQ0.R0vtHTl-pbs7qN6Y7EyVxIdGZkSzhgEhY0GISvhwCNgg.tUbRIKwyvmMfzf-vehgcX7ylOPI2nAuUlPFnXxTMM00g.JPEG/C35F151D-AD37-48B0-A55A-EF0EB3E4BF7F.jpg?type=w800"
    },
    {
        "name": "성각",
        "types": ["진돗개"],
        "year": "2019",
        "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMjc4/MDAxNzEwOTEzMzE3MDAw.OYbdWCyJYWNrjSuB0W1I0wXbBg5HRsz2vTj6xnQqHqgg.fX1gIXV3dpxWPiKYJvjItxCdvSPBuqdNBlBo38Xq90kg.JPEG/9EC29AE3-0AA0-45A7-B36A-40C633EE4D8D.jpg?type=w800"
    }  
]

type_emoji_dict = {
    "말티즈": "",
    "리트리버": "",
    "시츄":"",
    "허스키":"",
    "진돗개":""    
}
#예시 데이터
example_pokemon = {
    "name": "성각",
    "types": ["진돗개"],
    "year": "2019",
    "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyNDAzMjBfMjc4/MDAxNzEwOTEzMzE3MDAw.OYbdWCyJYWNrjSuB0W1I0wXbBg5HRsz2vTj6xnQqHqgg.fX1gIXV3dpxWPiKYJvjItxCdvSPBuqdNBlBo38Xq90kg.JPEG/9EC29AE3-0AA0-45A7-B36A-40C633EE4D8D.jpg?type=w800"
}

#하나만 추가되는 현상을 수정하기 위함
if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload,auto_complete",auto_complete)
#데이터 받는 폼 형성
with st.form(key="form"):
    col1,col2,col3 = st.columns(3)
    with col1:
        name = st.text_input(label="사진 이름",
                             value = example_pokemon["name"] if auto_complete else "")
    with col2:
        types = st.multiselect(label="강아지 종류",
                            options=list(type_emoji_dict.keys()),
                            max_selections=2,
                            default=example_pokemon["types"] if auto_complete else[]) 
    with col3:
        year = st.text_input(label="사진 연도",
                             value = example_pokemon["year"] if auto_complete else "")        
    image_url = st.text_input(label="사진 url",
                              value=example_pokemon["image_url"] if auto_complete else "")
    submit = st.form_submit_button(label="Submit")
    if submit :
        if not name:
            st.error("강아지의 이름을 입력해주세요.")
        elif not (year.isdigit() and len(year)==4):
            st.error("숫자로 연도를 입력해주세요")
        elif len(types) == 0:
            st.error("강아지의 종류를 적어도 한개 선택해주세요")
        else:
            st.success("강아지를 추가할 수 있습니다")
            st.session_state.pokemons.append({
                "name":name,
                "types":types,
                "year":year,
                "image_url":image_url if image_url else "./images/없음.jpg"
            })
   
        

#창의 간격을 줄이면 화면이 부자연스러워지는걸 방지하고자 간격을 3만큼 지정
for i in range(0,len(st.session_state.pokemons),4):
    row_pokemons = st.session_state.pokemons[i:i+4]
    cols = st.columns(4)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}.{pokemon['name']}**",expanded=True):
                #이름 불러오기
                st.subheader(pokemon["name"])
                #연도 불러오기
                st.subheader(pokemon['year'])
                #이미지 불러오기
                st.image(pokemon["image_url"])
                #이모티콘 추가
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                #타입은 배열이기 때문에 구분자를 적용
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label='삭제',key =i+j,use_container_width=True)
                if delete_button :
                    print("delete button clicked")
                    del st.session_state.pokemons[i+j]
                    #곧바로 반영??
                    st.rerun()
