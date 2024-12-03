import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path="RUTA_DEL_WEBDRIVER")  
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get("http://localhost:8081/Proyecto-Grupal/")  

 
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "comentarioForm"))
    )


    nombre = driver.find_element(By.ID, "nombre")
    comentario = driver.find_element(By.ID, "comentario")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    nombre.send_keys("Usuario de Prueba")
    comentario.send_keys("Este es un comentario de prueba generado por Selenium.")
    submit_button.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    mensaje = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Comentario guardado correctamente" in mensaje