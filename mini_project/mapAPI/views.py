from django.shortcuts import render, redirect, get_object_or_404


def main_test(request):

    return render(request, 'mapAPI/main_v2.5.html')


# def path_search(request):
# # <<셀레늄 구조 네이버>>
# from selenium import webdriver as wd
# driver = wd.Chrome(executable_path='chromedriver.exe')

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# # -------------------------------------------------------------------------------
# # //네이버맵 홈페이지 접속
# driver.get('https://map.naver.com/v5/directions/-/-/-/mode?c=14107103.1786139,4494701.9630842,15,0,0,0,dh')
# driver.implicitly_wait(5)
# # -------------------------------------------------------------------------------
# # //자동차 이용
# driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a').click()
# # //도보 이용
# # driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[3]/a').click()
# # -------------------------------------------------------------------------------
# # //출발지(start) 검색
# driver.find_element_by_id('directionStart0').send_keys('인천공항')
# driver.find_element_by_id('directionStart0').send_keys(Keys.RETURN)
# time.sleep(2)
# # -------------------------------------------------------------------------------
# # //도착지 검색
# driver.find_element_by_id('directionGoal1').send_keys('천안시청')
# driver.find_element_by_id('directionGoal1').send_keys(Keys.RETURN)
# time.sleep(2)
# # --------------------------------------------------------------------------------
# # //길찾기 버튼
# driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div/directions-search/div[2]/button[3]').click()
