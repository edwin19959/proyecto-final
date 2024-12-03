import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

# Fixture para configurar el driver de Chrome
@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_comentarios(driver):
  
    driver.get("http://localhost:8081/Proyecto-Grupal")
    time.sleep(2)

 
    assert driver.title == "Sistema de Comentarios", f"Prueba fallida: Título incorrecto, esperado 'Sistema de Comentarios', pero se obtuvo {driver.title}"
    print("Prueba exitosa: Título de la página correcto.")


    nombre_input = driver.find_element(By.ID, "nombre")
    comentario_input = driver.find_element(By.ID, "comentario")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

 
    nombre_input.send_keys("Edwin Martínez")
    comentario_input.send_keys("Este es un comentario de prueba.")


    submit_button.click()
    time.sleep(2)

   
    try:
        comentarios = driver.find_element(By.ID, "comentarios")
        assert "Este es un comentario de prueba." in comentarios.text, "Prueba fallida: El comentario no se mostró correctamente."
        print("Prueba exitosa: Comentario enviado correctamente.")
    except NoSuchElementException:
        raise AssertionError("Prueba fallida: No se encontró la sección de comentarios.")


if __name__ == "__main__":
    report_name = f"C:/Users/edwin/OneDrive/Escritorio/Reportes/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
   
    pytest.main(["--html=" + report_name, 
                 "--maxfail=1", 
                 "--disable-warnings"])
