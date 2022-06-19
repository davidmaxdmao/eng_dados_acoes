import paramiko
from paramiko.ssh_exception import AuthenticationException


class OperacoesSftp:

    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

    def cliente_sftp(self):

        try:
            transporte = paramiko.Transport((self._host, self._port))
            transporte.connect(username=self._username, password=self._password)
            cliente = paramiko.SFTPClient.from_transport(transporte)

        except AuthenticationException as e:
            # TODO logar a mensagem de erro
            # f'Falha na conecexão com o SFTP. {e}'

            return False

        return cliente

    def get_arquivo(self, remote_path, localpath):
        
        try:
            cliente = self.cliente_sftp()
            cliente.get(remote_path, localpath)
        
        except FileNotFoundError as e:
            # TODO logar a mensagem de erro
            # f'Erro inesperado ao tetnar recuperar arquivo do servidor. f{e}'

            return False
        
        except Exception as e:
            # TODO logar a mensagem de erro
            # f'Erro inesperado ao tetnar recuperar arquivo do servidor. f{e}'

            return False

        cliente.close()

        return True

    def enviar_arquivo(self, remote_path, localpath):

        cliente = self.cliente_sftp()

        try:
            cliente.put(localpath, remote_path)
            cliente.close()
        
        except FileNotFoundError as e:
            # TODO logar a mensagem de erro
            # f'Erro inesperado ao enviar arquivo para o servidor. {e}'

            return False

        except Exception as e:
            # TODO logar a mensagem de erro
            # f'Erro inesperado ao enviar arquivo para o servidor. {e}'

            return False
        
        return True
