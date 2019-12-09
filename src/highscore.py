import sqlite3

conn = sqlite3.connect("highscore.db")
cursor = conn.cursor()


# criando a tabela (schema)
def cria_tabela():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS highscore("
        "   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
        "   nome TEXT NOT NULL,"
        "   score INTEGER"
        ");"
    )
    conn.commit()


# grava pontos
def grava_pontos(nome, pontos):
    cursor.execute("INSERT INTO highscore (nome, score) VALUES (?,?)", (nome, pontos))
    conn.commit()


# lendo os pontos
def ver_highscore():
    cursor.execute("SELECT * FROM highscore ORDER BY score DESC")
    scores = []
    for linha in cursor.fetchall():
        scores.append(linha)
    return scores


# lendo os pontos
def limpar_scores():
    cursor.execute("DELETE FROM highscore")
    conn.commit()
