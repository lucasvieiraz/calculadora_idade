from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import enviar_email  # Ajuste o caminho conforme necessário


@patch('smtplib.SMTP')  # Mock do SMTP
def test_enviar_email(mock_smtp):
    usuario = "teste@exemplo.com"
    senha = "senha"
    destinatario = "destinatario@exemplo.com"
    assunto = "Assunto"
    texto = "Olá!\nEste e-mail foi enviado por um robô Python...\n"
    arquivo = None  # Defina como None para indicar a ausência de arquivo
    host = "smtp.exemplo.com"
    port = 587

    # Configuração do mock para SMTP
    mock_smtp_instance = MagicMock()
    mock_smtp.return_value = mock_smtp_instance

    # Chama a função `enviar_email`
    enviar_email(usuario, senha, destinatario, assunto, texto, arquivo)

    # Verifica se o SMTP foi configurado corretamente
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with(usuario, senha)
    mock_smtp_instance.sendmail.assert_called_once()  # Verifica se `sendmail` foi chamado
