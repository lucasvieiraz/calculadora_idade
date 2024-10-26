from unittest.mock import patch
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import calcular_idade  

def test_calcular_idade():
    
    with patch("app.datetime") as mock_datetime:
        mock_datetime.today.return_value = datetime(2024, 10, 26)
        mock_datetime.strptime = datetime.strptime  

       
        idade = calcular_idade("08/01/2006")
        assert idade == 18 
