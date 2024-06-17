from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sel_close = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3///97e3uVBMaVAAAAHklEQVQI12MIDQ0NARFBDAEMDFzkEl6rVq1i0AISAIlSC03msuDYAAAAAElFTkSuQmCC"
sel_empty = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEW9vb17e3tXxGy+AAAAEElEQVQI12P4/5+hgYF4BAAJYgl/JfpRmAAAAABJRU5ErkJggg=="
sel_1 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AAP97e3u7pKrVAAAAJUlEQVQI12NYBQQMDQxAACUCgAQjiGAFEaIQLiYhGgojEHqBGAB4Gw2cMF3q+AAAAABJRU5ErkJggg=="
sel_2 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AewB7e3vro336AAAANUlEQVQI12NYBQQMDQxAACFCQxkYGkNDHRgaA1gdgGJgIhQowRoCknUAygIZYCVgAqwNQQAA1rsQB7h1rwIAAAAASUVORK5CYII="
sel_3 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3/AAB7e3uBZQfoAAAAKUlEQVQI12NYBQQMDQxAACYaQ0PBhAOQywojWIFiIAIhBlICJiDaEAQAtlYPHU2zahQAAAAASUVORK5CYII="
sel_4 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AAHt7e3vZn4u5AAAAJklEQVQI12NYBQQMDQxAACFERWFECIxoDA11ABNAJUAuBsGARAAAgHoNeXfAhZYAAAAASUVORK5CYII="
sel_5 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb17AAB7e3sERFEmAAAAKUlEQVQI12NYBQQMDQxAACYaQ0MdoEQAiBsAEYNIAJWwQgi4Oog2BAEA7gEQV+EiCoQAAAAASUVORK5CYII="
sel_6 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0Ae3t7e3tXnVpnAAAAKklEQVQI12NYBQQMDQxAACFCQxkYGsFEAAOMgIo5ALmsEALMBSmGaEMQAOO9EHd34ZsRAAAAAElFTkSuQmCC"

minen = {}
for i in range(480): minen[i] = 'x'

exception_up = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,	28]
exception_down = [451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478]
exception_l = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420]
exception_r = [59, 89, 119, 149, 179, 209, 239, 269, 299, 329, 359, 389, 419, 449]
exception_up_l = 0
exception_up_r = 29
exception_down_l = 450
exception_down_r = 479
list = ['1','2','3','4','5','6','0']

# ожидание кликабельности элемента по селектору
def el_to_be_clickable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
        )

# ожидание НЕ кликабельности элемента по селектору
def el_not_to_be_clickable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 10).until_not(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
        )
    
# цикл чтения. Нужно потом сделать, чтобы сохранялся последний клик
def read():
    el_not_to_be_clickable('#tile0[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3///97e3uVBMaVAAAAHklEQVQI12MIDQ0NARFBDAEMDFzkEl6rVq1i0AISAIlSC03msuDYAAAAAElFTkSuQmCC"]')
    for i in range(480):
        el_to_be_clickable('#tile{}'.format(i))
        el = browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(i))
        attrValue = el.get_attribute('src')
        if minen[i] == 'm':
            continue
        if attrValue == sel_close:
            minen[i] = 'x'
        elif attrValue == sel_empty:
            minen[i] = '0'
        elif attrValue == sel_1:
            minen[i] = '1'
        elif attrValue == sel_2:
            minen[i] = '2'
        elif attrValue == sel_3:
            minen[i] = '3'
        elif attrValue == sel_4:
            minen[i] = '4'
        elif attrValue == sel_5:
            minen[i] = '5'
        elif attrValue == sel_6:
            minen[i] = '6'

'''Ставим мины'''
def min_flag():
    for i in range(480):
        if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,	28,
                    451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478,
                    30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420,
                    59, 89, 119, 149, 179, 209, 239, 269, 299, 329, 359, 389, 419, 449,
                    0, 29, 450, 479]:
            continue
        # присвоение значений для соседних от i клеток
        obj_around = {
            'LU': minen[i - 31],
            'MU': minen[i - 30],
            'RU': minen[i - 29],
            'LM': minen[i - 1],
            'RM': minen[i + 1],
            'LD': minen[i + 29],
            'MD': minen[i + 30],
            'RD': minen[i + 31]
            }
        purpose_around = {
            'LU': i - 31,
            'MU': i - 30,
            'RU': i - 29,
            'LM': i - 1,
            'RM': i + 1,
            'LD': i + 29,
            'MD': i + 30,
            'RD': i + 31
            }
        pos_x = [x for x in obj_around if obj_around[x] not in list] # список позиций со значением 'x' или 'm'

        if minen[i] == '1' and len(pos_x) == 1:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'
        if minen[i] == '2' and len(pos_x) == 2:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'
        if minen[i] == '3' and len(pos_x) == 3:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'
        if minen[i] == '4' and len(pos_x) == 4:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'
        if minen[i] == '5' and len(pos_x) == 5:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'
        if minen[i] == '6' and len(pos_x) == 6:
            for j in pos_x:
                minen[purpose_around[j]] = 'm'

'''Тыкаем поля'''
def opening():
    for i in range(480):
        list = ['1','2','3','4','5','6','0']
        if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,	28,
                    451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478,
                    30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420,
                    59, 89, 119, 149, 179, 209, 239, 269, 299, 329, 359, 389, 419, 449,
                    0, 29, 450, 479]:
            continue
        obj_around = {
            'LU': minen[i - 31],
            'MU': minen[i - 30],
            'RU': minen[i - 29],
            'LM': minen[i - 1],
            'RM': minen[i + 1],
            'LD': minen[i + 29],
            'MD': minen[i + 30],
            'RD': minen[i + 31]
            }
        purpose_around = {
            'LU': i - 31,
            'MU': i - 30,
            'RU': i - 29,
            'LM': i - 1,
            'RM': i + 1,
            'LD': i + 29,
            'MD': i + 30,
            'RD': i + 31
            }
        pos_x = [x for x in obj_around if obj_around[x] == 'x'] # список позиций со значением 'x'
        pos_m = [m for m in obj_around if obj_around[m] == 'm'] # список позиций со значением 'm'

        if minen[i] == '1' and len(pos_m) == 1 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()
        if minen[i] == '2' and len(pos_m) == 2 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()
        if minen[i] == '3' and len(pos_m) == 3 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()
        if minen[i] == '4' and len(pos_m) == 4 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()
        if minen[i] == '5' and len(pos_m) == 5 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()
        if minen[i] == '6' and len(pos_m) == 6 and len(pos_x) > 0:
            for j in pos_x:
                browser.find_element(By.CSS_SELECTOR, '#tile{}'.format(purpose_around[j])).click()


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=chrome_options)

try:
    link = 'https://xn--80a4adb6f.com/'
    browser.get(link)

    el_to_be_clickable('#toolbar>img:nth-child(10)')
    browser.find_element(By.CSS_SELECTOR, '#toolbar>img:nth-child(10)').click()

    el_to_be_clickable('#toolbar>img:nth-child(10)')
    browser.find_element(By.CSS_SELECTOR, '#toolbar>img:nth-child(10)').click()

    lost_el = browser.find_element(By.CSS_SELECTOR, '#tile269')
    browser.execute_script("window. scrollBy(0, 100)")

    el_to_be_clickable('#tile0')
    browser.find_element(By.CSS_SELECTOR, '#tile0').click()

    read()

    min_flag()

    opening()


finally:
    print(minen)
    time.sleep(5)
    browser.quit()