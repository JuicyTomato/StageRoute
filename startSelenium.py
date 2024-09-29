#TESTING SELENIUM

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By #per cercare id html
# from selenium.webdriver.common.keys import Keys #per usare tastiera
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC    #aspettare la presenza di un elemento prima di procedere

# import time

# service = Service(executable_path="/home/pepe/visualStudioCodeProjects/tirocinio/selenium129/chromedriver")
# driver = webdriver.Chrome(service=service)

# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# driver.get("https://wikipedia.org/")

# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.ID, "searchInput"))
# ) #aspetta 5 secondi prima di cercare searchInput

# inputElement = driver.find_element(By.ID, "searchInput")
# inputElement.clear()
# #send keys to it (class)
# inputElement.send_keys("Napoleone Bonaparte" + Keys.ENTER)

# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "regnal name"))
# ) #aspetta 5 secondi prima di cercare searchInput

# #Per andare sul link by the text
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "regnal name")
# link.click()

# time.sleep(5)

# driver.close()

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #per cercare id html
from selenium.webdriver.common.keys import Keys #per usare tastiera
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#service = Service(executable_path="/home/pepe/visualStudioCodeProjects/tirocinio/selenium129/chromedriver")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver.get("https://orteil.dashnet.org/cookieclicker/")


try:
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label"))
    ) #aspetta 5 secondi prima di cercare searchInput
    button = driver.find_element(By.CLASS_NAME, "fc-button-label")
    button.click()
    
except TimeoutException:
    print("Continuing...")



try:
    button = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))    #Puoi farlo come by.ID,"langSelect-EN" -> ma provare XPATH
    ) #aspetta 5 secondi prima di cercare searchInput
    button.click()
except TimeoutException:
    print("Continuando...")


cookieId = "bigCookie"

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, cookieId))
) #aspetta 5 secondi prima di cercare searchInput
button = driver.find_element(By.ID, cookieId)
    

#quanti biscuits abbiamo
howManyCookies = "cookies"
productPriceP = "productPrice"
productP = "product"

while True:
    button.click()
    cookiesCount = driver.find_element(By.ID, howManyCookies).text.split(" ")[0]
    cookiesCount = int(cookiesCount.replace(",",""))
    
    for i in range(4):
        productPrice = driver.find_element(By.ID, productPriceP + str(i)).text.replace(",","")

        if not productPrice.isdigit():
            continue

        productPrice = int(productPrice)

        if cookiesCount >= productPrice:
            product = driver.find_element(By.ID, productP + str(i))
            product.click()
            break



time.sleep(115)

driver.close()