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
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA4MzBfNzgg%2FMDAxNjkzMzYzNDI4Mjkw.03czQzdbjkr-TEp65Ah0CMMNvgyCYKY2ZaO9K4No4Twg.KWbEfHJGunVSLS03Tni8_HkuusqWQPS_UK28DhSprJkg.JPEG.buddydoc%2F%25B9%25F6%25B5%25F0%25B4%25DA_%25B8%25BB%25C6%25BC%25C1%25EE_%25C6%25AF%25C2%25A1.jpg&type=a340"
    },
    {
        "name": "초코",
        "types": ["리트리버"],
        "year": "2016",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAyMTNfMTU4%2FMDAxNzA3ODA1ODYzNzkx.Z2ejeZfzxa_GzQsk4IYzkzFqvTF4Z3R3YVS8hoAwfG8g.9MGkcuR5GBYPNftrGcxM606xOcVPUNy51x-_ZLhhG1Ag.JPEG.savanna2020%2F%25BA%25BB%25B9%25AE%25C0%25CC%25B9%25CC%25C1%25F6_%25BB%25E7%25B9%25D9%25B3%25AA.jpg&type=a340",
    },
    {
        "name": "흰둥이",
        "types": ["시츄"],
        "year": "2017",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA4MTRfNzYg%2FMDAxNjkyMDA4MzI0MDk2.tw5GZe1qtxBL8EX48r9bgvTWfBnBhTnmBXCtnahShngg.rxoxWN0YMEjJFLSmFinLA6eABh84W2iDzQp13ky7dMwg.PNG.choi540%2Faf4f3a9d-eb5f-4510-addf-d11bac4fbaa9.png&type=a340",
    },
    {
        "name": "허세",
        "types": ["허스키"],
        "year": "2018",
        "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi3.ruliweb.com%2Fimg%2F22%2F12%2F12%2F18504190a1a56fde7.png&type=a340"
    },
    {
        "name": "성각",
        "types": ["진돗개"],
        "year": "2019",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA5MDhfNTgg%2FMDAxNjk0MTUxMTY1Mzcy.Jwm9xjCDxeoTp02rWWqcihCQgiXWknppLE09D2Ara6Ig.ik53pJwKcBfeSAYbeGsLmOnGiHRK9JgSsABeCEzD-A4g.PNG.merry_diary%2F%25C1%25F8%25B5%25BE%25B0%25B3_%25C1%25BE%25B7%25F9_%25BC%25F6%25B8%25ED_%25288%2529.PNG&type=a340"
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
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA5MDhfNTgg%2FMDAxNjk0MTUxMTY1Mzcy.Jwm9xjCDxeoTp02rWWqcihCQgiXWknppLE09D2Ara6Ig.ik53pJwKcBfeSAYbeGsLmOnGiHRK9JgSsABeCEzD-A4g.PNG.merry_diary%2F%25C1%25F8%25B5%25BE%25B0%25B3_%25C1%25BE%25B7%25F9_%25BC%25F6%25B8%25ED_%25288%2529.PNG&type=a340"
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
