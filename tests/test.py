from unittest.mock import patch
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_data_hoje():
    data_mock = datetime(2024, 10, 26).date()  # 
    
    with patch("builtins.input", return_value="08/01/2006"):  
        with patch("app.datetime") as mock_datetime:
            mock_datetime.today.return_value = datetime(2024, 10, 26)  

            import app 
            assert app.hoje.date() == data_mock 

def teste_nascimento():
     with patch("builtins.input", return_value="08/01/2006"):
        import app
        assert app.nascimento == "08/01/2006"

