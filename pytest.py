import pytest
from datetime import datetime

def test_example():
    assert True  

if __name__ == "__main__":
   
    report_name = f"C:/Users/edwin/OneDrive/Escritorio/Nueva carpeta (4)/Reportes/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
  
    pytest.main([
        "--html=" + report_name,  
        "--maxfail=1",  
        "--disable-warnings"  
    ])

    print(f"Reporte generado en: {report_name}")
