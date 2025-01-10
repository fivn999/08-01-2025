import mysql.connector

def conecta_no_banco_de_dados():
    # Conectar ao servidor MySQL
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

    # Criar o cursor para interagir com o banco de dados
    cursor = cnx.cursor()

    # Verificar se o banco de dados 'aula06' existe
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "btCanes";')
    num_results = cursor.fetchone()[0]

    # Fechar a conexão inicial
    cnx.close()

    # Se o banco de dados não existe, criá-lo
    if num_results == 0:
        # Conectar-se novamente ao servidor MySQL para criar o banco de dados
        cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

        cursor = cnx.cursor()
        cursor.execute('CREATE DATABASE btCanes;')
        cnx.commit()

        # Conectar-se ao banco de dados recém-criado
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='btCanes'  # Especificar o banco de dados
        )

        cursor = cnx.cursor()

        # Criar a tabela de categoria de cursos
        cursor.execute('''
            CREATE TABLE categorias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                descricao TEXT
            );
        ''')

        # Criar a tabela de usuarios 
        cursor.execute('''
            CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                senha VARCHAR(255) NOT NULL
            );
        ''')

        # Criar a tabela de cursos
        cursor.execute('''
            CREATE TABLE cursos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                descricao TEXT,
                categoria_id INT,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE matriculas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_usuario INT,
                id_curso INT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY (id_curso) REFERENCES cursos(id)
            );
        ''')

        # Inserir dados iniciais na tabela 'usuarios'
        nome = "primeiro"
        email = "primeiro@gmail.com"
        senha = "123456"
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        cnx.commit()
     
        # Fechar a conexão
        cnx.close()
        
    try:
        # Conectar ao banco de dados 'aula06' existente
        bd = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='btCanes'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return bd