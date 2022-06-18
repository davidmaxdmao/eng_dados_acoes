import paramiko


class OperacoesSftp:

    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

    def cliente_sftp(self):
        transporte = paramiko.Transport((self._host, self._port))
        transporte.connect(username=self._username, password=self._password)
        cliente = paramiko.SFTPClient.from_transport(transporte)

        return cliente

    def get_planilha_ftp(self, remote_path, localpath):
        
        try:
            cliente = self.cliente_sftp()
            cliente.get(remote_path, localpath)
        
        except Exception as e:
            return False

        cliente.close()

        return True

    def backup_planilha(self, remote_path, localpath):

        cliente = self.cliente_sftp()

        try:
            cliente.put(localpath, remote_path)
            cliente.close()

        except Exception as e:
            return False
        
        return True
