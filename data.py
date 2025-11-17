# Python3 샘플 코드 #
import requests
import streamlit as st

url = 'http://apis.data.go.kr/B553662/trnspPoiInfoService/getTrnspPoiInfoList'
params ={'serviceKey' : st.secrets["API"]["SERVICE_KEY"], 'pageNo' : '1', 'numOfRows' : '1', 'type' : 'json', 'srchFrtrlNm' : '가지산', 'srchPlaceTpeCd' : 'TRANS' }

response = requests.get(url, params=params)
print(response.content)