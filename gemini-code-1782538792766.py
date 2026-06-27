import streamlit as st

# 앱 제목 설정
st.title("2회고사 대비 서·논술형 자동 채점 시스템")
st.caption("대상 파일: 2회고사 대비 모의 문항(260626).pdf")
st.write("---")

# 세트 선택 라디오 버튼
set_choice = st.sidebar.radio(
    "채점할 문항 세트를 선택하세요:",
    ["[세트 1] 사회적 촉진과 억제", "[세트 2] 정전기의 특징", "[세트 3] AI와 인간의 예술"]
)

# -------------------------------------------------------------------------
# [세트 1] 사회적 촉진과 사회적 억제 로직
# -------------------------------------------------------------------------
if set_choice == "[세트 1] 사회적 촉진과 억제":
    st.header("실전 적용-1: 사회적 촉진과 사회적 억제")
    
    # [서·논술형 1]
    st.subheader("[서·논술형 1] 표 빈칸 채우기 (각 1점, 총 3점)")
    q1_1 = st.text_input("빈칸 (1) 입력:", placeholder="예: 쉽거나 친숙한 과제")
    q1_2 = st.text_input("빈칸 (2) 입력:", placeholder="예: 차분하게 혼자 집중하는 시간")
    q1_3 = st.text_input("빈칸 (3) 입력:", placeholder="예: 사회적 억제")
    
    if st.button("서·논술형 1 채점하기"):
        # (1)번 채점 및 동의어 인정
        score_1 = 0
        if any(w in q1_1 for w in ["쉽", "친숙", "낮은", "노력", "취미"]):
            score_1 = 1
        
        # (2)번 채점 및 오개념 필터링 ('함께', '모임' 들어가면 오답)
        score_2 = 0
        if any(w in q1_2 for w in ["혼자", "스스로", "독립", "자극 차단"]) and not any(w in q1_2 for w in ["함께", "모임", "같이"]):
            score_2 = 1
            
        # (3)번 채점 (고유 명사이므로 정확성 확인)
        score_3 = 1 if "사회적 억제" in q1_3.replace(" ", "") else 0
        
        total_q1 = score_1 + score_2 + score_3
        st.metric("획득 점수", f"{total_q1} / 3 점")
        st.write(f"- (1) 결과: {'정답' if score_1==1 else '오답 (키워드: 쉽거나 친숙한 과제)'}")
        st.write(f"- (2) 결과: {'정답' if score_2==1 else '오답 (키워드: 혼자 집중, 함께/모임 포함 시 오답)'}")
        st.write(f"- (3) 결과: {'정답' if score_3==1 else '오답 (고유명사: 사회적 억제)'}")

    st.write("---")
    
    # [서·논술형 2]
    st.subheader("[서·논술형 2] 설명문 작성 (각 2점, 총 4점)")
    st.info("주어진 첫 문장: 과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.")
    q2_1 = st.text_input("이어지는 문장 (1) 입력:")
    q2_2 = st.text_input("이어지는 문장 (2) 입력:")
    
    if st.button("서·논술형 2 채점하기"):
        # (1)번 문장 채점 (예시 방법 검증)
        score_2_1 = 0
        if "예시" in q2_1 or "예를 들어" in q2_1:
            if any(w in q2_1 for w in ["쉽", "친숙", "커피숍", "도서관", "모임"]):
                score_2_1 = 2
        
        # (2)번 문장 채점 (대조 방법 및 오개념 필터링)
        score_2_2 = 0
        if "대조" in q2_2 or any(w in q2_2 for w in ["반면", "반대로", "대조적으로"]):
            if any(w in q2_2 for w in ["어렵", "복잡", "도전", "혼자"]):
                score_2_2 = 2
        
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4 점")
        st.write(f"- 문장 (1) 결과: {'통과' if score_2_1==2 else '미흡 (설명방법 명칭 표기 및 쉽고 친숙한 과제 내용 확인)'}")
        st.write(f"- 문장 (2) 결과: {'통과' if score_2_2==2 else '미흡 (대조 표지 표현 및 어렵고 복잡한 과제 내용 확인)'}")

    st.write("---")
    
    # [서·논술형 3]
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        # 시각 요소 채점
        score_3_1 = 0
        if any(w in q3_1_val for w in ["혼자", "스스로", "독립", "차단"]):
            if any(w in q3_1_val for w in ["환경", "집중", "전달", "이해"]):
                score_3_1 = 3
            else:
                score_3_1 = 1  # 효과 기술 미흡
                
        # 청각 요소 채점
        score_3_2 = 0
        if any(w in q3_1_val for w in ["혼자", "스스로", "독립", "차단"]): # 어려운 과제 환경 검증
            if any(w in q3_2_val for w in ["고요", "무음", "잔잔", "소음 없는"]):
                if any(w in q3_2_val for w in ["몰입", "대비", "강조", "분위기"]):
                    score_3_2 = 3
                else:
                    score_3_2 = 1  # 효과 기술 미흡
        
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")
        st.write(f"- 시각 요소 채점 결과: {score_3_1}점")
        st.write(f"- 청각 요소 채점 결과: {score_3_2}점")

# -------------------------------------------------------------------------
# [세트 2] 정전기의 특징 로직
# -------------------------------------------------------------------------
elif set_choice == "[세트 2] 정전기의 특징":
    st.header("실전 적용-2: 겨울철 불청객 '정전기'")
    
    # [서·논술형 1]
    st.subheader("[서·논술형 1] 표 빈칸 채우기 (각 1점, 총 3점)")
    q1_1 = st.text_input("빈칸 (1) 입력:", placeholder="예: 높은 곳에 고여 있는 물")
    q1_2 = st.text_input("빈칸 (2) 입력:", placeholder="예: 이동하지 않고 머물러 있음")
    q1_3 = st.text_input("빈칸 (3) 입력:", placeholder="예: 위험하지 않음")
    
    if st.button("서·논술형 1 채점하기"):
        score_1 = 1 if any(w in q1_1 for w in ["높은 곳", "고여", "흐르지 않는 물"]) else 0
        
        # 오개념 필터링: 전하 상태에 '이동함', '흐름'이 들어가면 무조건 오답
        score_2 = 0
        if any(w in q1_2 for w in ["이동하지", "머물러", "정지"]) and not any(w in q1_2 for w in ["이동함", "흐름"]):
            score_2 = 1
            
        score_3 = 1 if any(w in q1_3 for w in ["위험하지", "피해가 없음", "안전"]) else 0
        
        total_q1 = score_1 + score_2 + score_3
        st.metric("획득 점수", f"{total_q1} / 3 점")

    st.write("---")
    
    # [서·논술형 2]
    st.subheader("[서·논술형 2] 설명문 작성 (각 2점, 총 4점)")
    st.info("주어진 첫 문장: 겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.")
    q2_1 = st.text_input("이어지는 문장 (1) 입력:")
    q2_2 = st.text_input("이어지는 문장 (2) 입력:")
    
    if st.button("서·논술형 2 채점하기"):
        score_2_1 = 0
        if "정의" in q2_1:
            if any(w in q2_1 for w in ["전하가 정지", "머물러 있는 전기", "뜻한다", "의미한다"]):
                score_2_1 = 2
                
        score_2_2 = 0
        if any(w in q2_2 for w in ["비교", "대조"]):
            if any(w in q2_2 for w in ["흐르는 물", "고여 있는 물"]) and any(w in q2_2 for w in ["위험하지"]):
                score_2_2 = 2
                
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4 점")

    st.write("---")
    
    # [서·논술형 3]
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        score_3_1 = 0
        if any(w in q3_1_val for w in ["높은 곳", "댐", "절벽"]) and any(w in q3_1_val for w in ["고여", "정지"]):
            if any(w in q3_1_val for w in ["비유", "이해", "상태"]):
                score_3_1 = 3
            else:
                score_3_1 = 1
                
        score_3_2 = 0
        if any(w in q3_2_val for w in ["고요", "적막", "무음", "소리 소거"]):
            # 결론 방향 검증: '위험하지 않음' 또는 '안전함' 결론이 도달해야 함
            if any(w in q3_2_val for w in ["위험하지", "안전", "전달", "특성 극대화"]):
                score_3_2 = 3
            else:
                score_3_2 = 1
                
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")

# -------------------------------------------------------------------------
# [세트 3] 인공지능 그림과 인간의 예술 로직
# -------------------------------------------------------------------------
elif set_choice == "[세트 3] AI와 인간의 예술":
    st.header("실전 적용-3: 생성형 인공 지능 그림과 인간의 예술")
    
    # [서·논술형 1]
    st.subheader("[서·논술형 1] 표 빈칸 채우기 (각 1점, 총 3점)")
    q1_1 = st.text_input("빈칸 (1) 입력:", placeholder="예: 로봇이 실수 없이 피겨 스케이팅을 해내는 경기")
    q1_2 = st.text_input("빈칸 (2) 입력:", placeholder="예: 감정이 없고 독자적인 철학이 없어 예술이 아니다")
    q1_3 = st.text_input("빈칸 (3) 입력:", placeholder="예: 예술의 범주를 확장하는 상징적 가치")
    
    if st.button("서·논술형 1 채점하기"):
        score_1 = 1 if any(w in q1_1 for w in ["로봇", "피겨", "스케이팅", "울리지 못함"]) else 0
        
        # 근거 2가지(감정, 철학/이야기) 중 최소 하나 이상과 결론(예술 아님)이 결합되어야 함
        score_2 = 0
        if any(w in q1_2 for w in ["감정", "철학", "이야기"]) and any(w in q1_2 for w in ["아니다", "어렵다"]):
            score_2 = 1
            
        score_3 = 1 if any(w in q1_3 for w in ["미술계", "변화", "범주 확장", "상징"]) else 0
        
        total_q1 = score_1 + score_2 + score_3
        st.metric("획득 점수", f"{total_q1} / 3 점")

    st.write("---")
    
    # [서·논술형 2]
    st.subheader("[서·논술형 2] 설명문 작성 (각 2점, 총 4점)")
    st.info("주어진 첫 문장: 인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.")
    q2_1 = st.text_input("이어지는 문장 (1) 입력:")
    q2_2 = st.text_input("이어지는 문장 (2) 입력:")
    
    if st.button("서·논술형 2 채점하기"):
        score_2_1 = 0
        if any(w in q2_1 for w in ["대조", "비교"]):
            if any(w in q2_1 for w in ["감정", "철학", "경험", "관점"]):
                score_2_1 = 2
                
        score_2_2 = 0
        if "예시" in q2_2:
            if any(w in q2_2 for w in ["에드몽", "벨라미", "초상화", "경매"]):
                score_2_2 = 2
                
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4_점")

    st.write("---")
    
    # [서·논술형 3] 세부 점수 분배 적용 [총 6점] 문항
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        # (1) 시각 요소 정밀 채점 (3점 만점 세부 로직)
        score_3_1 = 0
        has_visual_element = any(w in q3_1_val for w in ["화가", "인간", "몰입", "고뇌", "관객", "눈물", "감동"])
        has_text_evidence = sum(1 for w in ["감정", "철학", "경험", "관점", "배경"] if w in q3_1_val)
        
        if has_visual_element:
            if has_text_evidence >= 2 and any(w in q3_1_val for w in ["울림", "감동", "전달"]):
                score_3_1 = 3  # 만점
            elif has_text_evidence == 1:
                score_3_1 = 2  # 근거 부족 부분점수
            else:
                score_3_1 = 1  # 단순 서술
                
        # (2) 청각 요소 정밀 채점 (3점 만점 세부 로직)
        score_3_2 = 0
        has_audio_element = any(w in q3_2_val for w in ["따뜻", "선율", "음악", "숨소리", "심장", "오케스트라"])
        has_contrast = any(w in q3_2_val for w in ["대조", "대비", "메트로놈과 다른"])
        
        if has_audio_element:
            if has_contrast and any(w in q3_2_val for w in ["울림", "남다른 감동", "부각"]):
                score_3_2 = 3  # 만점
            elif any(w in q3_2_val for w in ["울림", "남다른 감동", "부각"]):
                score_3_2 = 2  # 대비 성격 누락 부분점수
            else:
                score_3_2 = 1  # 효과 미흡
                
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")
        st.write(f"- (1) 시각 요소 세부 점수: {score_3_1} / 3 점")
        st.write(f"- (2) 청각 요소 세부 점수: {score_3_2} / 3 점")