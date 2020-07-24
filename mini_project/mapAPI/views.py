from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, HttpResponse

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json


def main_test(request):

    return render(request, 'mapAPI/main_v2.0.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def path_search(request):
    # <<셀레늄 구조 네이버>>
    # //연결
    data = request.body.decode('utf-8')
    if data:
        data = json.loads(data)

        
    driver = wd.Chrome(executable_path='chromedriver.exe')

    #-------------------------------------------------------------------------------
    # //네이버맵 연결
    driver.get(
        'https://map.naver.com/v5/directions/-/-/-/mode?c=14107103.1786139,4494701.9630842,15,0,0,0,dh')
    driver.implicitly_wait(5)
    #-------------------------------------------------------------------------------
    # //자동차 버튼
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/l0.5]/a').click()
    #-------------------------------------------------------------------------------
    # //경유지 추가 버튼
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/di0.5]/butto0.5]').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/di0.5]/butto0.5]').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/di0.5]/butto0.5]').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/di0.5]/butto0.5]').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/di0.5]/butto0.5]').click()
    #-------------------------------------------------------------------------------
    #//리스트값 입력
    click_list = data
    a = len(click_list)
    #------------------------------------------------------------------------------
    # //출발지 입력
    driver.find_element_by_id('directionStart0').send_keys(data[0]['road_address_name'])
    time.sleep(0.5)
    driver.find_element_by_id('directionStart0').send_keys(Keys.RETURN)
    time.sleep(0.5)
    #-------------------------------------------------------------------------------
    # //경유지 입력
    for i in range(1, a-1):
        keys_val = click_list[i]['address_name'] + \
            " "+click_list[i]['place_name']
        print(keys_val)
        driver.find_element_by_id('directionVia%s' % (i+1)).send_keys(keys_val)
        time.sleep(0.5)
        driver.find_element_by_id('directionVia%s' %
                                  (i+1)).send_keys(Keys.RETURN)
        time.sleep(0.5)
    #-------------------------------------------------------------------------------
    # //도착지 입력
    keys_last_val = click_list[a-1]['address_name'] + \
        " "+click_list[a-1]['place_name']
    driver.find_element_by_id('directionGoal6').send_keys(keys_last_val)
    time.sleep(0.5)
    driver.find_element_by_id('directionGoal6').send_keys(Keys.RETURN)
    time.sleep(0.5)
    #--------------------------------------------------------------------------------
    # //길찾기 버튼
    driver.find_element_by_xpath(
        '//*[@id="container"]/div[1]/shrinkable-layout/directions-layout/directions-result/div/directions-search/di0.5]/butto0.5]').click()

    return HttpResponse(driver.current_url)