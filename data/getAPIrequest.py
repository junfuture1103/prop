import requests
import xml.etree.ElementTree as ET

url = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayStatsNew/1/5/20220301'

response = requests.get(url)
xml_data = response.content

# XML 데이터 파싱
root = ET.fromstring(xml_data)

# 'CardSubwayStatsNew' 요소에서 모든 'row' 요소를 찾아서 각각의 정보 출력
print("서울시 지하철 승하차 인원 데이터:")
for row in root.findall('.//row'):
    use_date = row.find('USE_DT').text
    line_num = row.find('LINE_NUM').text
    station_name = row.find('SUB_STA_NM').text
    ride_num = row.find('RIDE_PASGR_NUM').text
    alight_num = row.find('ALIGHT_PASGR_NUM').text
    work_date = row.find('WORK_DT').text

    print(f"날짜: {use_date}, 라인: {line_num}, 역: {station_name}")
    print(f"승차 인원: {ride_num}, 하차 인원: {alight_num}")
    print(f"데이터 기록일: {work_date}\n")
