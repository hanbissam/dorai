import streamlit as st

st.title("2회고사 대비 서·논술형 자동 채점 시스템")
st.caption("대상 파일: 2회고사 대비 모의 문항(260626).pdf")
st.write("---")

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
        score_1 = 1 if any(w in q1_1 for w in ["쉽", "친숙", "낮은", "노력", "취미"]) else 0
        score_2 = 0
        if any(w in q1_2 for w in ["혼자", "스스로", "독립", "자극 차단"]) and not any(w in q1_2 for w in ["함께", "모임", "같이"]):
            score_2 = 1
        score_3 = 1 if "사회적 억제" in q1_3.replace(" ", "") else 0
        
        total_q1 = score_1 + score_2 + score_3
        st.metric("획득 점수", f"{total_q1} / 3 점")

    st.write("---")
    
    # [서·논술형 2]
    st.subheader("[서·논술형 2] 설명문 작성 (각 2점, 총 4점)")
    st.info("주어진 첫 문장: 과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.")
    q2_1 = st.text_input("이어지는 문장 (1) 입력:")
    q2_2 = st.text_input("이어지는 문장 (2) 입력:")
    
    if st.button("서·논술형 2 채점하기"):
        score_2_1 = 0
        if "예시" in q2_1 or "예를 들어" in q2_1:
            if any(w in q2_1 for w in ["쉽", "친숙", "커피숍", "도서관", "모임"]):
                if any(w in q2_1 for w in ["효율", "높인다", "도움", "효과적", "잘된다"]):
                    score_2_1 = 2
        
        score_2_2 = 0
        if "대조" in q2_2 or any(w in q2_2 for w in ["반면", "반대로", "대조적으로"]):
            if any(w in q2_2 for w in ["어렵", "복잡", "도전"]):
                if any(w in q2_2 for w in ["혼자", "스스로", "집중", "독립"]):
                    score_2_2 = 2
        
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4 점")

    st.write("---")
    
    # [서·논술형 3] 연결성 및 필수 내용 정밀 검증
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        # (1) 시각 요소 채점
        score_3_1 = 0
        msg_3_1 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('혼자/스스로/독립/외부 차단'이 무조건 담겨야 함)
        has_required_content_v = any(w in q3_1_val for w in ["혼자", "스스로", "독립", "차단", "격리"])
        # [요소 B: 연출 효과] 검증
        has_effect_v = any(w in q3_1_val for w in ["환경", "집중", "전달", "이해", "시각화"])
        
        if not has_required_content_v:
            msg_3_1 = "오답 안내: [시각 연출 계획]에 어려운 과제 수행 시 필수적인 '혼자/독립된 환경'에 대한 내용이 누락되었습니다."
        elif has_required_content_v and not has_effect_v:
            msg_3_1 = "오답 안내: [시각 연출 계획]은 적절하나, 그것이 주는 [연출 효과]와 실질적으로 연결되지 않았거나 효과 서술이 미흡합니다."
        elif has_required_content_v and has_effect_v:
            score_3_1 = 3
            msg_3_1 = "정답: 시각 연출 계획과 효과의 논리적 연결성이 우수합니다."
            
        # (2) 청각 요소 채점
        score_3_2 = 0
        msg_3_2 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('고요/무음/잔잔/소음 제거'가 무조건 담겨야 함)
        has_required_content_a = any(w in q3_2_val for w in ["고요", "무음", "잔잔", "소음 없는", "적막"])
        # [요소 B: 연출 효과] 검증
        has_effect_a = any(w in q3_2_val for w in ["몰입", "대비", "강조", "분위기", "효과적"])
        
        if not has_required_content_a:
            msg_3_2 = "오답 안내: [청각 연출 계획]에 정적인 환경에 어울리는 필수 내용(고요함/무음 등)이 누락되었습니다."
        elif has_required_content_a and not has_effect_a:
            msg_3_2 = "오답 안내: [청각 연출 계획]은 적절하나, 그것이 주는 [연출 효과]와 실질적으로 연결되지 않았거나 효과 서술이 미흡합니다."
        elif has_required_content_a and has_effect_a:
            score_3_2 = 3
            msg_3_2 = "정답: 청각 연출 계획과 효과의 논리적 연결성이 우수합니다."
            
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")
        st.write(f"- 시각 요소 결과: {msg_3_1}")
        st.write(f"- 청각 요소 결과: {msg_3_2}")

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
            if any(w in q2_1 for w in ["전하가 정지", "머물러 있는 전기"]):
                if any(w in q2_1 for w in ["뜻한다", "의미한다", "말한다"]):
                    score_2_1 = 2
                
        score_2_2 = 0
        if any(w in q2_2 for w in ["비교", "대조"]):
            if any(w in q2_2 for w in ["흐르는 물", "고여 있는 물"]):
                if any(w in q2_2 for w in ["위험하지 않다", "피해가 없다", "안전하다"]):
                    score_2_2 = 2
                
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4 점")

    st.write("---")
    
    # [서·논술형 3] 연결성 및 필수 내용 정밀 검증
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        # (1) 시각 요소 채점
        score_3_1 = 0
        msg_3_1 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('높은 곳'과 '고여/정지된 물' 비유가 반드시 담겨야 함)
        has_required_content_v = any(w in q3_1_val for w in ["높은", "댐", "절벽"]) and any(w in q3_1_val for w in ["고여", "정지", "흐르지"])
        # [요소 B: 연출 효과] 검증
        has_effect_v = any(w in q3_1_val for w in ["시각화", "쉽게 이해", "상태를 전달", "특성"])
        
        if not has_required_content_v:
            msg_3_1 = "오답 안내: [시각 연출 계획]에 지문의 핵심 비유인 '높은 곳에 고여 있는 물'에 관한 필수 내용이 부재하거나 왜곡되었습니다."
        elif has_required_content_v and not has_effect_v:
            msg_3_1 = "오답 안내: [시각 연출 계획]은 적절하나, 지문의 특성을 설명하는 [연출 효과]와 실질적으로 연결되지 않았습니다."
        elif has_required_content_v and has_effect_v:
            score_3_1 = 3
            msg_3_1 = "정답: 비유적 연출 계획과 효과의 연결성이 적절합니다."
            
        # (2) 청각 요소 채점
        score_3_2 = 0
        msg_3_2 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('고요/적막/무음/소리 소거')
        has_required_content_a = any(w in q3_2_val for w in ["고요", "적막", "무음", "소리 소거", "조용한"])
        # [요소 B: 연출 효과] 검증 ('위험하지 않다/안전하다')
        has_effect_a = any(w in q3_2_val for w in ["위험하지", "안전", "피해가 없음", "특성 극대화"])
        
        if not has_required_content_a:
            msg_3_2 = "오답 안내: [청각 연출 계획]에 정전기의 정(靜)적인 특성을 나타낼 필수 소리 요소가 누락되었습니다."
        elif has_required_content_a and not has_effect_a:
            msg_3_2 = "오답 안내: [청각 연출 계획]은 적절하나, 안전성을 증명하는 최종 [연출 효과]와 실질적으로 연결되지 않았습니다."
        elif has_required_content_a and has_effect_a:
            score_3_2 = 3
            msg_3_2 = "정답: 청각 연출 계획과 안전성 결론 효과가 논리적으로 잘 연결되었습니다."
            
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")
        st.write(f"- 시각 요소 결과: {msg_3_1}")
        st.write(f"- 청각 요소 결과: {msg_3_2}")

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
        score_2 = 0
        if any(w in q1_2 for w in ["감정", "철학", "이야기"]) and any(w in q1_2 for w in ["아니다", "어렵다"]):
            score_2 = 1
        score_3 = 1 if any(w in q1_3 for w in ["미술계", "변화", "범주 확장", "상징"]) else 0
        
        total_q1 = score_1 + score_2 + score_3
        st.metric("획득 점수", f"{total_q1} / 3 점")

    st.write("---")
    
    # [서·논술형 2]
    st.subheader("[서·논술형 2] 설명문 작성 (각 2점, 총 4점)")
    q2_1 = st.text_input("이어지는 문장 (1) 입력:")
    q2_2 = st.text_input("이어지는 문장 (2) 입력:")
    
    if st.button("서·논술형 2 채점하기"):
        score_2_1 = 0
        if any(w in q2_1 for w in ["대조", "비교"]):
            if any(w in q2_1 for w in ["감정", "철학", "경험", "관점"]):
                if any(w in q2_1 for w in ["다르다", "없다", "종합적으로 담겨 있다"]):
                    score_2_1 = 2
                
        score_2_2 = 0
        if "예시" in q2_2:
            if any(w in q2_2 for w in ["에드몽", "벨라미", "초상화"]):
                if any(w in q2_2 for w in ["놀라움을 주었다", "판매되었다", "사례가 있다"]):
                    score_2_2 = 2
                
        st.metric("획득 점수", f"{score_2_1 + score_2_2} / 4 점")

    st.write("---")
    
    # [서·논술형 3] 연결성 및 필수 내용 정밀 검증
    st.subheader("[서·논술형 3] 영상 연출 계획 및 효과 (각 3점, 총 6점)")
    q3_1_val = st.text_area("시각 요소(Ⓐ) 및 효과 입력:")
    q3_2_val = st.text_area("청각 요소(Ⓑ) 및 효과 입력:")
    
    if st.button("서·논술형 3 채점하기"):
        # (1) 시각 요소 채점
        score_3_1 = 0
        msg_3_1 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('화가/인간/관객' 등 주체 등장 필수)
        has_required_content_v = any(w in q3_1_val for w in ["화가", "인간", "몰입", "고뇌", "관객", "눈물", "감동"])
        # [요소 B: 연출 효과] 검증 ('감정/철학/경험' 등의 내재적 가치와 울림 연결)
        has_text_evidence = sum(1 for w in ["감정", "철학", "경험", "관점", "배경"] if w in q3_1_val)
        has_conclusion_1 = any(w in q3_1_val for w in ["울림을 전달", "감동을 효과적으로", "가치를 생생하게 부각"])
        
        if not has_required_content_v:
            msg_3_1 = "오답 안내: [시각 연출 계획]에 인간의 예술적 행위나 주체(화가, 관객 등)에 대한 필수 내용이 빠져 있습니다."
        elif has_required_content_v and (has_text_evidence < 2 or not has_conclusion_1):
            msg_3_1 = "오답 안내: [시각 연출 계획]은 적절하나, 지문 속 인간 예술의 특성(감정, 철학 등) 및 정서적 울림 효과와 실질적으로 연결되지 않았습니다."
        elif has_required_content_v and has_text_evidence >= 2 and has_conclusion_1:
            score_3_1 = 3
            msg_3_1 = "정답: 인간 예술의 특성을 반영한 시각 연출 및 정서적 울림 효과가 잘 연결되었습니다."
            
        # (2) 청각 요소 채점
        score_3_2 = 0
        msg_3_2 = ""
        # [요소 A: 연출 계획] 필수 내용 검증 ('따뜻/선율/음악/숨소리/심장')
        has_required_content_a = any(w in q3_2_val for w in ["따뜻", "선율", "음악", "숨소리", "심장", "오케스트라"])
        # [요소 B: 연출 효과] 검증 ('대비'와 '남다른 감동 극대화')
        has_contrast = any(w in q3_2_val for w in ["대조", "대비", "메트로놈과 다른"])
        has_conclusion_2 = any(w in q3_2_val for w in ["감동을 청각적으로 극대화", "남다른 감동을 주는 이유를 부각"])
        
        if not has_required_content_a:
            msg_3_2 = "오답 안내: [청각 연출 계획]에 차가운 기계음과 대조되는 인간적 온기의 필수 청각 요소가 누락되었습니다."
        elif has_required_content_a and (not has_contrast or not has_conclusion_2):
            msg_3_2 = "오답 안내: [청각 연출 계획]은 적절하나, [장면 1]과의 유기적 대비 및 남다른 감동 유발 효과와 실질적으로 연결되지 않았습니다."
        elif has_required_content_a and has_contrast and has_conclusion_2:
            score_3_2 = 3
            msg_3_2 = "정답: 기계음과의 청각적 대비를 통해 남다른 감동을 이끌어내는 결론이 논리적으로 훌륭하게 연결되었습니다."
            
        st.metric("획득 점수", f"{score_3_1 + score_3_2} / 6 점")
        st.write(f"- (1) 시각 요소 결과: {msg_3_1}")
        st.write(f"- (2) 청각 요소 결과: {msg_3_2}")