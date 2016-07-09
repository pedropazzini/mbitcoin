import psycopg2

class connector:
    """Classe que gera uma conexao com o banco para a execucao direta das QUERYS"""
    database_name="mercado_bitcoin_db"
    database_user="mercado_bitcoin_user"
    database_user_password="mercado_bitcoin_user_password"
    database_port="5423"
    database_host="localhost"
    
    conn = ""
    cursor = ""

    def __init__ (self):
        
        self.conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_user_password, port=self.database_port, host=self.database_host);
        self.cursor = self.conn.cursor();

    def execute (self, string):
        
        self.cursor.execute(string)
        return self.cursor.fetchall()

    def crud(self,string, commit = True):
        self.cursor.execute(string)
        if commit == True:
            self.conn.commit()

    def exit (self):
        self.cursos.close()
        self.conn.close()
