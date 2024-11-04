import pandas as pd

# 데이터 파일 경로
data_file_path = "C:\\Users\\82103\\Documents\\백석대\\3학년 2학기 (2023)\\빅데이터 사회현상분석\\경기도 동물등록현황.csv"  # 데이터 파일 경로를 적절히 지정해야 합니다.

# 데이터 파일 읽기
df = pd.read_csv(data_file_path, encoding='EUC-KR')

# 조건 1: 생년 범위 필터링
df = df[(df['생년'] >= 2019) & (df['생년'] <= 2023)]

# 조건 2: RFID 구분 필터링
rfid_categories = ['내장형', '외장형', '인식형']
df = df[df['RFID구분'].isin(rfid_categories)]

# 조건 3: 축종 필터링
animal_types = ['개', '고양이']
df = df[df['축종'].isin(animal_types)]

# 조건 4: 시군구명 필터링
cities = ['성남시', '수원시', '용인시', '평택시', '화성시']
df = df[df['시군구명'].isin(cities)]

# 결과를 새로운 파일에 저장
output_file_path = "C:\\Users\\82103\\Documents\\백석대\\3학년 2학기 (2023)\\빅데이터 사회현상분석\\filtered_data.csv" # 새로운 파일 경로를 지정합니다.
df.to_csv(output_file_path, index=False)  # 데이터프레임을 CSV 파일로 저장합니다.

print(f"전처리된 데이터를 {output_file_path}에 저장했습니다.")
