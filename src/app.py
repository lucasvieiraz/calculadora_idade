import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(usuario, senha, destinatario, assunto, texto, arquivo=None):
    servidor = smtplib.SMTP(host="smtp.exemplo.com", port=587)
    servidor.starttls()
    servidor.login(usuario, senha)

    msg = MIMEMultipart()
    msg["From"] = usuario
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(texto, "plain"))

    # Verifique se o arquivo foi fornecido antes de tentar anexá-lo
    if arquivo:
        with open(arquivo, "rb") as file:
            msg.attach(MIMEText(file.read(), "base64"))

    servidor.sendmail(usuario, destinatario, msg.as_string())
    servidor.quit()
