# Recommendation of the Best Location for Childrens Safety Place Using Machine Learning

아동폭력 문제 해결을 위한 교육기관 분포 공공데이터를 기반으로 최적의 아동안전지킴이집의 위치 추천 <br/>
Optimal Location Recommendation for Child Safety Place Based on Public Data on Educational Institution Distribution to Address Child Violence

### Table of contents 

1. [Overview](#1️⃣-overview)
2. [Role](#2️⃣-role)
3. [Skills](#3️⃣-skills)
4. [Process](#4️⃣-process)
5. [Structure](#5️⃣-structure)
6. [References](#6️⃣-references)


## 1️⃣ Overview

### 1-1. 대회 소개 및 수상 내역
* 대회 기간 : 2022.04.06 ~ 2022.07.06
* Machine Learning을 활용한 공공데이터 분석을 진행하였습니다.
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/ae4202cf-41e4-4a2b-8492-f8bc3d9397a9" alt="" width="45%" />
  <img src="https://github.com/user-attachments/assets/572df718-ebb2-4c41-90c3-4980cfcdab0d" alt="" width="45%" />
</p>


## 2️⃣ Role

|<img src="https://github.com/user-attachments/assets/bef1a11a-d69d-440a-9ed5-7c8f39548c5a" width="150" height="150"/>|<img src="https://github.com/user-attachments/assets/f9323ec6-0bfa-4dba-8589-4abb0948f2b7" width="150" height="150"/>|
|:-:|:-:|
|Jeong GangHyeon<br/>[@JUGAHY](https://github.com/JUGAHY)|Jang DaeHyeon<br/>[@JangDaeHyeon](https://github.com/JangDaeHyeon)|

### Jeong GangHyeon
* Machine Learning Development (K-Means, Elbow Method, Silhouette Method)
* Visualizing Maps with Folium
* Survey of child violence data and production of PPT

### Jang DaeHyeon
* Machine Learning Development (DBSCAN)
* Data Collection and Preprocessing
* Survey of child violence data and production of PPT


## 3️⃣ Skills

### Project skills 

__1. Language & Tool__ 

- Python 3.8 
- COLAB
  
__2. Machine Learning Model__

- K-Means, Elbow Method, Silhouette Method
- DBSCAN

__3. Visualization__

- Folium
- Mapboxgl

__4. Preprocessing__

- kakao geocode
- geopy


## 4️⃣ Process

![image](https://github.com/user-attachments/assets/ba3c7596-53dc-4aea-8110-d2a4e3a3594c)

### 4-1. Problem to be Solved
* 지역별 아동학대 피해 발견율이 높다는 건 그 만큼 많은 아동학대가 발생하고 있다는 것을 의미합니다.
* 많은 아이들이 적극적인 도움을 받지 못 하고 급한 상황에 도움을 청할 수 없어 큰 사고로 이어지고 있습니다.
  
![image](https://github.com/user-attachments/assets/d82d5421-628c-4fc4-8d49-b14cd91ed3cf)
![image](https://github.com/user-attachments/assets/634afea9-b954-4bb6-b25f-af9aee200f99)

### 4-2. Data Introduction
* [전라북도 시군구 위치 정보.json](https://muddy-sundial-48d.notion.site/Folium-30c9e3098756463e9edde541be1dc9fa)
    - Folium을 활용해 전라북도 시각화 하기 위한 방법 소개(전라북도의 각 시군구의 위도, 경도 테두리 데이터를 얻는 방법)
      ![image](https://github.com/user-attachments/assets/62328fef-35db-4724-a6a8-46a0c004c78d)

* [전북특별자치도교육청_학교현황](https://www.data.go.kr/data/3068876/fileData.do?recommendDataYn=Y)
    - 전라북도에 위치한 초등학교, 중학교, 고등학교의 위치를 얻을 수 있는 데이터입니다.
* [국토교통부_아동안전지킴이집](https://www.data.go.kr/data/15057866/openapi.do)
    - 아동안전지킴이집의 시설분류명, 시설 전화번호, 시설 새 도로명 주소를 얻을 수 있는 데이터입니다.
* [한국사회보장정보원_전라북도 어린이집 정보조회](https://www.data.go.kr/data/15101197/openapi.do)
    - 전라북도 내의 어린이집의 위치, 정원 수, 도로명 주소 등을 얻을 수 있는 데이터입니다.

### 4-3. Data Preprecessing
1. 수집한 공공데이터에서 전라북도 내의 어린이집, 초등학교, 중학교, 고등학교의 학교명과 주소를 뽑아 전라북도 전체 교육기관 데이터를 얻었습니다.
2. 오타, 띄어쓰기, 존재하지 않는 주소 등을 전처리해주었습니다.
3. kakao geocode, geopy를 활용하여 주소를 위도, 경도로 변환하였습니다.

![image](https://github.com/user-attachments/assets/39882d66-4ccf-4d04-98b9-07a744272c68)

### 4-4. K-means Algorithm
* K-means Algorithm은 여러 데이터의 K개의 중앙값을 찾고 그 중앙값으로 데이터의 군집을 분류하는 알고리즘입니다.
* 위의 K-means Algorithm 정의에서 여러 데이터(원)를 전라북도 교육기관으로 두고, 중앙값(별)을 아동안전지킴이집으로 두었습니다.
  
![image](https://github.com/user-attachments/assets/693cc9eb-d24b-4c5f-b25e-442b521b16e2)


**Process**

Ⅰ) 기존 아동안전지킴이집의 위치를 초기 평균값으로 지정해줍니다.<br/>
Ⅱ) 각 데이터와 각 평균값 사이의 거리를 계산합니다.<br/>
Ⅲ) 각 데이터를 가장 가까운 클러스터의 요소로 할당시킵니다.<br/>
Ⅳ) 클러스터의 평균을 다시 계산합니다.<br/>
Ⅴ) 군집화 결과에 변화가 없을 때까지 2-4 과정을 반복합니다.

![image](https://github.com/user-attachments/assets/1352f02e-5f94-4890-8e96-b2416842452b)

### 4-5. DBSCAN
* DBSCAN(Density-Based Spatial Clustering of Applications with Noise)은 머신 러닝에 주로 사용되는 클러스터링 알고리즘으로 Multi Dimension의 데이터를 밀도 기반으로 서로 가까운 데이터 포인트를 함께 그룹화하는 알고리즘입니다.
* DBSCAN은 밀도가 다양하거나 모양이 불규칙한 클러스터가 있는 데이터와 같이 모양이 잘 정의되지 않은 데이터를 처리할 때 유용하게 사용 가능합니다..

![image](https://github.com/user-attachments/assets/276cd4d6-4630-4fdf-858c-9f9ef56cbaff)

**Process**

* Hyperparameter
  * Epsilon : Cluster를 구성하는 최소의 거리
  * Min Points : Cluster를 구성 시, 필요한 최소 데이터 포인트 수
    
Ⅰ) 데이터 중, 임의의 포인트를 선택함.<br/>
Ⅱ) 선택한 데이터와 **Epsilon** 거리 내에 있는 모든 데이터 포인트를 찾음.<br/>
Ⅲ) 주변에 있는 데이터 포인트 갯수가 **Min Points** 이상이면, 해당 포인트를 중심으로 하는 Cluster를 생성한다.<br/>
Ⅳ) 어떠한 포인트가 생성한 Cluster 안에 존재하는 다른 점 중, 다른 Cluster의 중심이 되는 데이터 포인트가 존재한다면 두 Cluster는 하나의 Cluster로 간주한다.<br/>
Ⅴ) 1~4번을 모든 포인트에 대해서 반복한다.<br/>
Ⅵ) 어느 Cluster에도 포함되지 않는 데이터 포인트는 이상치로 처리한다. 


### 4-5. Conclusion Visualization

#### ① 임실군 (현재 아동안전지킴이집 위치 -> 교육시설 기반 아동안전지킴이집 위치) - K-means Algorithm

<p align="center">
  <img src="https://github.com/user-attachments/assets/f1d4aa1a-3f99-4640-bd72-216e15ef2189" alt="" width="45%" />
  <img src="https://github.com/user-attachments/assets/617646b3-75a6-4087-a22a-5058fd948282" alt="" width="45%" />
</p>


#### ② 전주시 덕진구 (현재 아동안전지킴이집 위치 -> 교육시설 기반 아동안전지킴이집 위치) - K-means Algorithm

<p align="center">
  <img src="https://github.com/user-attachments/assets/7560f4c6-02e6-4376-881d-45c334cee863" alt="" width="45%" />
  <img src="https://github.com/user-attachments/assets/fb652a02-26b4-4ec1-a9e1-e54438d33120" alt="" width="45%" />
</p>


#### ③ 임실군에서의 새로운 아동안전지킴이집을 만든다고 할때 추천 위치 - DBSCAN

![image](https://github.com/user-attachments/assets/a944f655-f41b-4269-8ae9-10c29d1b4af6)

#### ④ 전주시 덕진구에서의 새로운 아동안전지킴이집을 만든다고 할때 추천 위치 - DBSCAN

![image](https://github.com/user-attachments/assets/566eac05-fb5c-4a6e-bea1-5f19f9d00258)

## 5️⃣ Structure
```
Recommendation of the Best Location for Childrens Safety Place Using Machine Learning
├── README.md
├── data
│   ├── 각 지역 교육기관 위치
│   │   ├── 고창군_통합.csv
│   │   ├── 덕진구_통합.csv
│   │   └── ...
│   │
│   ├── 각 지역 지킴이집 위치
│   │   ├── 고창군_지킴이집.csv
│   │   ├── 덕진구_지킴이집.csv
│   │   └── ...
│   │
│   ├── 전라북도_시군구_위치_정보.json
│   └── 행정구역_시군구_별_주민등록세대수_20220629145146.csv
│
├── results
│   ├── KMeans
│   │   ├── Imsil_KMeans_Results       # 임실군 KMeans 최적화 결과
│   │   └── Deokjin_KMeans_Results     # 덕진구 KMeans 최적화 결과
│   │
│   └── DBSCAN
│       ├── Imsil_DBSCAN_Results       # 임실군 DBSCAN 최적화 결과
│       └── Deokjin_DBSCAN_Results     # 덕진구 DBSCAN 최적화 결과
│
└── notebooks
    ├── imsil_kmeans_clusters.ipynb
    ├── deokjin_kmeans_clusters.ipynb
    ├── imsil_dbscan_clusters.ipynb
    └── deokjin_dbscan_clusters.ipynb
```

## 6️⃣ References
