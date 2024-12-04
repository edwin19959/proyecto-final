import os
import time
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys


report_dir = "C:/xampp/htdocs/Proyecto-Grupal/Proyecto-Grupal/resultados"
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

@pytest.fixture(scope="module")
def driver():
  
    service = Service(ChromeDriverManager().install())
    
  
    chrome_options = webdriver.ChromeOptions()
  
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
  
    driver.implicitly_wait(10)
    
    try:
        yield driver
    finally:
        driver.quit()

def test_form_submission(driver):

    driver.get("http://localhost:8081/Proyecto-Grupal")
    
   
    time.sleep(2)

    try:
       
        nombre_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "nombre"))
        )

      
        for char in "Edwin Martínez":
            nombre_input.send_keys(char)
            time.sleep(0.2) 

    
        comentario_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "comentario"))
        )

    
        comentario_text = "Este es un comentario de prueba."
        for char in comentario_text:
            comentario_input.send_keys(char)
            time.sleep(1)  

        time.sleep(1)

 
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        driver.save_screenshot(f"{report_dir}/antes_submit.png")

        submit_button.click()

        time.sleep(3)


        driver.save_screenshot(f"{report_dir}/despues_submit.png")

        try:
            alert_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "alert-container"))
            )
            print("Mensaje de alerta:", alert_container.text)
        except:
            print("No se encontró mensaje de alerta")

    except Exception as e:

        driver.save_screenshot(f"{report_dir}/error_submission.png")
        pytest.fail(f"Error durante el envío del formulario: {e}")


if __name__ == "__main__":
    
    report_name = f"{report_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    
    pytest.main([
        "-v",
        __file__,  
        "--html=" + report_name, 
        "--maxfail=1", 
        "--disable-warnings"
    ])