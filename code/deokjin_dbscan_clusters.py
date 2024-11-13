import folium
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN


# 데이터 로드 함수 정의
def load_data():
    geo_json_path = '/home/a202192025/전라북도 시군구 위치 정보.json'
    population_data_path = '/home/a202192025/행정구역_시군구_별_주민등록세대수_20220629145146.csv'
    safety_place_data_path = '/home/a202192025/덕진구_지킴이집.csv'
    city_data_path = '/home/a202192025/덕진구_통합.csv'

    geo_data = geo_json_path
    population_data = pd.read_csv(population_data_path, encoding='euc-kr')
    safety_place_data = pd.read_csv(safety_place_data_path, encoding='euc-kr').dropna(subset=['위도', '경도'])
    city_data = pd.read_csv(city_data_path, encoding='euc-kr').dropna(subset=['위도', '경도'])

    return geo_data, population_data, safety_place_data, city_data


# 위도와 경도 데이터를 결합하는 함수 정의
def combine_coordinates(safety_place_data, city_data):
    combined_latitudes = pd.concat([safety_place_data['위도'], city_data['위도']]).values
    combined_longitudes = pd.concat([safety_place_data['경도'], city_data['경도']]).values
    return combined_latitudes, combined_longitudes


# Folium 기본 지도 생성
def create_base_map():
    return folium.Map(location=[36, 127], tiles="cartodbpositron", zoom_start=7)


# 인구 밀도 Choropleth 레이어 추가 함수
def add_population_choropleth(map_obj, geo_data, population_data):
    folium.Choropleth(
        geo_data=geo_data,
        name='choropleth',
        data=population_data,
        columns=['Code', 'Population'],  # CSV 파일의 컬럼 이름에 맞게 조정 필요
        key_on='feature.properties.SIG_CD',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Population Rate (%)'
    ).add_to(map_obj)


# 위치 데이터에 대한 Circle Marker 추가 함수
def add_location_markers(map_obj, latitudes, longitudes):
    for i, (lat, lon) in enumerate(zip(latitudes, longitudes)):
        folium.CircleMarker(
            location=[lat, lon],
            radius=3,
            color='black',
            fill=True,
            fill_color='black',
            fill_opacity=0.7,
            popup=f"Location {i}",
            tooltip=f"Location {i}"
        ).add_to(map_obj)


# DBSCAN 클러스터링 및 클러스터 중심 좌표 추가 함수
def add_dbscan_clusters(map_obj, longitudes, latitudes):
    coords = np.array(list(zip(longitudes, latitudes)))
    dbscan = DBSCAN(eps=0.005, min_samples=5)
    labels = dbscan.fit_predict(coords)

    for label in set(labels):
        if label != -1:  # 노이즈 포인트는 제외
            cluster_points = coords[labels == label]
            center_lon, center_lat = cluster_points.mean(axis=0)
            folium.Marker(
                location=[center_lat, center_lon],
                popup=f"DBSCAN Cluster Center {label}",
                tooltip=f"DBSCAN Cluster Center {label}",
                icon=folium.Icon(color='blue', icon='star')
            ).add_to(map_obj)


# 사용자 정의 범례 추가 함수
def add_custom_legend(map_obj):
    legend_html = """
    <div style="position: fixed; bottom: 20px; left: 20px; width: 150px; height: 60px;
                border:2px solid grey; z-index:9999; font-size:10px; padding: 6px; background-color: white;">
        &nbsp; <i class="fa fa-circle fa-2x" style="color:black"></i>&nbsp; 데이터 위치 <br>
        &nbsp; <i class="fa fa-star fa-2x" style="color:blue"></i>&nbsp; DBSCAN 최적 위치
    </div>
    """
    map_obj.get_root().html.add_child(folium.Element(legend_html))


# 전체 지도를 생성하는 메인 함수
def create_map():
    geo_data, population_data, safety_place_data, city_data = load_data()
    latitudes, longitudes = combine_coordinates(safety_place_data, city_data)

    m = create_base_map()
    add_population_choropleth(m, geo_data, population_data)
    add_location_markers(m, latitudes, longitudes)
    add_dbscan_clusters(m, longitudes, latitudes)
    add_custom_legend(m)

    return m


# 지도 표시
map_display = create_map()
map_display