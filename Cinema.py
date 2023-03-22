class Cinema:
        def __init__(self, host, user, password, database):
            self.conn = mysql.connector.connect(
                host=host, user=user, password=password, database=database
            )
            self.cursor = self.conn.cursor()

        def cadastrar_filme(self, titulo, genero, duracao):
            sql = "INSERT INTO filmes (titulo, genero, duracao) VALUES (%s, %s, %s)"
            values = (titulo, genero, duracao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"Filme '{titulo}' cadastrado com sucesso.")

        def cadastrar_cliente(self, nome, idade, email):
            sql = "INSERT INTO clientes (nome, idade, email) VALUES (%s, %s, %s)"
            values = (nome, idade, email)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"Cliente '{nome}' cadastrado com sucesso.")

        def comprar_ingresso(self, id_cliente, id_filme, quantidade):
            sql = "INSERT INTO vendas (id_cliente, id_filme, quantidade) VALUES (%s, %s, %s)"
            values = (id_cliente, id_filme, quantidade)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"{quantidade} ingressos para o filme {id_filme} vendidos para o cliente {id_cliente}.")

        def gerar_relatorio(self):
            sql = """
                SELECT f.titulo, SUM(v.quantidade)
                FROM filmes f
                INNER JOIN vendas v ON f.id = v.id_filme
                GROUP BY f.titulo
                ORDER BY SUM(v.quantidade) DESC
            """
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            print("Relatório de vendas:")
            for row in results:
                print(f"{row[0]} - {row[1]} ingressos vendidos.")

        def fechar_conexao(self):
            self.cursor.close()
            self.conn.close()