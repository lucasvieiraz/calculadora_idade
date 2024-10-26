from unittest.mock import patch
from datetime import datetime
import sys
import os

# Ajuste o caminho para encontrar o módulo `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import calcular_idade  # Importa apenas a função que queremos testar

def test_calcular_idade():
    # Define a data atual simulada
    with patch("app.datetime") as mock_datetime:
        mock_datetime.today.return_value = datetime(2024, 10, 26)
        mock_datetime.strptime = datetime.strptime  # Manter `strptime` original

        # Testa o cálculo da idade para uma data de nascimento fixa
        idade = calcular_idade("08/01/2006")
        assert idade == 18  # Ajuste o valor esperado de acordo com o cálculo
