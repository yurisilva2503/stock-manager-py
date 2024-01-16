import sqlite3
from datetime import datetime


class DataBase():
    def __init__(self, name='system.db'):
        self.name = name
        self.connection = None

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except sqlite3.Error as e:
                print('Erro ao fechar a conexão:', e)

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL,
                    UNIQUE(user)
                );
            """)
        except sqlite3.Error as e:
            print('Erro ao criar a tabela:', e)

    def insert_user(self, name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users (name, user, password, access) VALUES (?,?,?,?)
            """, (name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print('Erro')

    def check_user(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password:
                    if linha[4] == "Administrador":
                        return "Administrador"
                    elif linha[4] == "Usuário":
                        return "Usuário"

            return "sem acesso"
        except Exception as e:
            print("Erro durante a verificação do usuário:", str(e))

    def check_user_exists(self, username):
        query = "SELECT COUNT(*) FROM users WHERE user = ?"
        params = (username,)
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()[0]
        cursor.close()

        if result > 0:
            return True
        else:
            return False

    def create_table_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    Codigo_Produto TEXT,
                    Nf_e TEXT,
                    Serie TEXT,
                    Data_Emissao TEXT,
                    Chave_de_Acesso TEXT,
                    Cnpj_Emitente TEXT,
                    Emitente TEXT,
                    Descricao TEXT,
                    Unidade TEXT,
                    Preco TEXT,
                    Quantidade TEXT,
                    Total TEXT,
                    Data_Entrada TEXT,
                    Avaria TEXT,


                );
            """)
        except sqlite3.Error as e:
            print('Erro ao criar a tabela:', e)

    def register_products(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                          descricao, unidade, preco, quantidade, total, data_entrada, avaria):
        try:
            cursor = self.connection.cursor()

            # Verificando se o produto já existe na tabela
            cursor.execute("SELECT Quantidade FROM products WHERE Codigo_Produto = ?", (codigoproduto,))
            existing_quantity = cursor.fetchone()

            if existing_quantity:
                # Atualizando a quantidade do produto existente
                new_quantity = int(existing_quantity[0]) + int(quantidade)
                cursor.execute("UPDATE products SET Quantidade = ? WHERE Codigo_Produto = ?",
                               (new_quantity, codigoproduto))
            else:
                # Inserindo um novo registro na tabela
                cursor.execute("""
                    INSERT INTO products (Codigo_Produto, Nf_e, Serie, Data_Emissao, Chave_de_Acesso, Cnpj_Emitente, 
                    Emitente, Descricao, Unidade, Preco, Quantidade, Total, Data_Entrada, Avaria)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente, descricao,
                      unidade, preco, quantidade, total, data_entrada, avaria))

            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao cadastrar produto:', str(e))
            return 'Erro'

    def select_all_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM products ORDER BY Quantidade")
            products = cursor.fetchall()
            return products
        except:
            pass

    def delete_products(self, codprod):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM products WHERE Codigo_Produto = '{codprod}'")

            self.connection.commit()

            return 'Produto excluído com sucesso!'
        except:
            return 'Erro ao excluir produto!'

    def update_products(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                        descricao, unidade, preco, quantidade, total, data_entrada, avaria):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE products SET
            Codigo_Produto = ?,
            Nf_e = ?,
            Serie = ?,
            Data_Emissao = ?,
            Chave_de_Acesso = ?,
            Cnpj_Emitente = ?,
            Emitente = ?,
            Descricao = ?,
            Unidade = ?,
            Preco = ?,
            Quantidade = ?,
            Total = ?,
            Data_Entrada = ?,
            Avaria = ?

            WHERE Codigo_Produto = ?
        """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente, descricao, unidade,
              preco, quantidade, total, data_entrada, avaria, codigoproduto))
        self.connection.commit()

    def create_table_saida_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS saida_produtos (
                    Codigo_Produto TEXT,
                    Nf_e TEXT,
                    Serie TEXT,
                    Data_Emissao TEXT,
                    Chave_de_Acesso TEXT,
                    Cnpj_Emitente TEXT,
                    Emitente TEXT,
                    Descricao TEXT,
                    Unidade TEXT,
                    Preco TEXT,
                    Quantidade TEXT,
                    Total TEXT,
                    Data_Entrada TEXT,
                    Avaria TEXT,
                    Data_Saida TEXT,


                );
            """)
        except sqlite3.Error as e:
            print('Erro ao criar a tabela:', e)

    def register_saida(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                       descricao, unidade, preco, quantidade, total, data_entrada, avaria, data_saida):
        try:
            cursor = self.connection.cursor()

            # Convertendo as datas para objetos datetime
            data_entrada = datetime.strptime(data_entrada, '%d/%m/%Y').date()
            data_saida = datetime.strptime(data_saida, '%d/%m/%Y').date()

            # Formatndo as datas para o formato "DD/MM/AAAA"
            data_entrada_str = data_entrada.strftime('%d/%m/%Y')
            data_saida_str = data_saida.strftime('%d/%m/%Y')

            # Verificando se o produto já existe na tabela com a mesma data de saída
            cursor.execute("SELECT Quantidade FROM saida_produtos WHERE Codigo_Produto = ? AND Data_Saida = ?",
                           (codigoproduto, data_saida_str))
            result = cursor.fetchone()

            if result:
                existing_quantity = result[0]

                # Atualizando a quantidade do produto existente
                new_quantity = int(existing_quantity) + int(quantidade)
                cursor.execute(
                    "UPDATE saida_produtos SET Quantidade = ? WHERE Codigo_Produto = ? AND Data_Saida = ?",
                    (new_quantity, codigoproduto, data_saida_str))
            else:
                # Inserindo um novo registro na tabela
                cursor.execute("""
                    INSERT INTO saida_produtos (Codigo_Produto, Nf_e, Serie, Data_Emissao, Chave_de_Acesso, 
                    Cnpj_Emitente, Emitente, Descricao, Unidade, Preco, Quantidade, Total, Data_Entrada, Avaria, Data_Saida)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                      descricao, unidade, preco, quantidade, total, data_entrada_str, avaria, data_saida_str))

            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao cadastrar saída de produto:', str(e))
            return 'Erro'

    def update_saida(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                     descricao, unidade, preco, quantidade, total, data_entrada, avaria, data_saida):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE saida_produtos SET
            Codigo_Produto = ?,
            Nf_e = ?,
            Serie = ?,
            Data_Emissao = ?,
            Chave_de_Acesso = ?,
            Cnpj_Emitente = ?,
            Emitente = ?,
            Descricao = ?,
            Unidade = ?,
            Preco = ?,
            Quantidade = ?,
            Total = ?,
            Data_Entrada = ?,
            Avaria = ?,
            Data_Saida = ?

            WHERE Codigo_Produto = ?
        """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente, descricao, unidade,
              preco, quantidade, total, data_entrada, avaria, data_saida, codigoproduto))
        self.connection.commit()

    def select_all_saida(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM saida_produtos")
            produtos_saida = cursor.fetchall()
            return produtos_saida
        except Exception as e:
            print('Erro ao recuperar saída de produtos:', str(e))
            return []

    def remove_produto(self, codigoproduto):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM products WHERE Codigo_Produto = ?", (codigoproduto,))
            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao remover produto:', str(e))
            return 'Erro'

    def remove_saida(self, codigoproduto, data_saida):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM saida_produtos WHERE Codigo_Produto = ? AND Data_Saida = ?",(codigoproduto, data_saida,))
            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao remover produto da tabela de saída:', str(e))
            return 'Erro'

    def create_table_geral(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS geral (
                    Codigo_Produto TEXT,
                    Nf_e TEXT,
                    Serie TEXT,
                    Data_Emissao TEXT,
                    Chave_de_Acesso TEXT,
                    Cnpj_Emitente TEXT,
                    Emitente TEXT,
                    Descricao TEXT,
                    Unidade TEXT,
                    Preco TEXT,
                    Quantidade TEXT,
                    Total TEXT,
                    Data_Entrada TEXT,
                    Avaria TEXT,
                    Data_Saida TEXT,


                );
            """)
        except sqlite3.Error as e:
            print('Erro ao criar a tabela:', e)

    def register_geral(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                       descricao, unidade, preco, quantidade, total, data_entrada, avaria, data_saida):
        try:
            cursor = self.connection.cursor()

            # Convertendo as datas para objetos datetime
            data_entrada = datetime.strptime(data_entrada, '%d/%m/%Y').date()
            data_saida = datetime.strptime(data_saida, '%d/%m/%Y').date()

            # Formatando as datas para o formato "DD/MM/AAAA"
            data_entrada_str = data_entrada.strftime('%d/%m/%Y')
            data_saida_str = data_saida.strftime('%d/%m/%Y')

            # Verificando se o produto já existe na tabela com a mesma data de saída
            cursor.execute("SELECT Quantidade FROM geral WHERE Codigo_Produto = ? AND Data_Saida = ?",
                           (codigoproduto, data_saida_str))
            result = cursor.fetchone()

            if result:
                existing_quantity = result[0]

                # Atualizando a quantidade do produto existente
                new_quantity = int(existing_quantity) + int(quantidade)
                cursor.execute(
                    "UPDATE geral SET Quantidade = ? WHERE Codigo_Produto = ? AND Data_Saida = ?",
                    (new_quantity, codigoproduto, data_saida_str))
            else:
                # Inserindo um novo registro na tabela
                cursor.execute("""
                    INSERT INTO geral (Codigo_Produto, Nf_e, Serie, Data_Emissao, Chave_de_Acesso, 
                    Cnpj_Emitente, Emitente, Descricao, Unidade, Preco, Quantidade, Total, Data_Entrada, Avaria, Data_Saida)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                      descricao, unidade, preco, quantidade, total, data_entrada_str, avaria, data_saida_str))

            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao cadastrar saída de produto:', str(e))
            return 'Erro'

    def update_geral(self, codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                     descricao, unidade, preco, quantidade, total, data_entrada, avaria, data_saida):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE geral SET
            Codigo_Produto = ?,
            Nf_e = ?,
            Serie = ?,
            Data_Emissao = ?,
            Chave_de_Acesso = ?,
            Cnpj_Emitente = ?,
            Emitente = ?,
            Descricao = ?,
            Unidade = ?,
            Preco = ?,
            Quantidade = ?,
            Total = ?,
            Data_Entrada = ?,
            Avaria = ?,
            Data_Saida = ?

            WHERE Codigo_Produto = ?
        """, (codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente, descricao, unidade,
              preco, quantidade, total, data_entrada, avaria, codigoproduto, data_saida))
        self.connection.commit()

    def select_all_geral(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM geral ORDER BY Preco")
            products = cursor.fetchall()
            return products
        except:
            pass

    def remove_geral(self, codigoproduto, data_saida):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM geral WHERE Codigo_Produto = ? AND Data_Saida = ?",
                           (codigoproduto, data_saida))
            self.connection.commit()
            return 'Ok'
        except Exception as e:
            print('Erro ao remover produto da tabela geral:', str(e))
            return 'Erro'

    def reduce_quantidade_saida(self, codigoproduto, quantidade_retorno, data_saida):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE saida_produtos SET quantidade = quantidade - ? WHERE Codigo_Produto = ? AND Data_Saida = ?",
            (quantidade_retorno, codigoproduto, data_saida))
        self.connection.commit()

    def reduce_quantidade_geral(self, codigoproduto, quantidade_retorno, data_saida):
        cursor = self.connection.cursor()
        if data_saida:
            cursor.execute("UPDATE geral SET quantidade = quantidade - ? WHERE Codigo_Produto = ? AND Data_Saida = ?",
                           (quantidade_retorno, codigoproduto, data_saida))
        else:
            cursor.execute("UPDATE geral SET quantidade = quantidade - ? WHERE Codigo_Produto = ?",
                           (quantidade_retorno, codigoproduto))
        self.connection.commit()

    def remove_all_saida(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM saida_produtos')
        self.connection.commit()

    def remove_all_geral(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM geral')
        self.connection.commit()


if __name__ == '__main__':
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_products()
    db.create_table_saida_produtos()
    db.create_table_geral()
    db.close_connection()
