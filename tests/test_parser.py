from src.auth_parser import AuthParser

# 1. La línea de crimen
linea_test = "Dec 10 06:55:01 my-laptop sshd[12345]: Failed password for invalid user admin from 192.168.1.50 port 4040 ssh2"

# 2. Instanciamos
parser = AuthParser(linea_test)

# 3. ¿Funcionó? (Asumiendo que el Padre guarda la data en self.data o atributos)
print(f"IP Detectada: {parser.get_value("_Ip")}")
print(f"Usuario: {parser.get_value("_User")}")
