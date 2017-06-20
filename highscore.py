import sqlite3

conn = sqlite3.connect('highscore.db')
cursor = conn.cursor()


# grava pontos
def grava_pontos(nome, pontos):
    cursor.execute("""
   INSERT INTO highscore (nome, score)
VALUES (?,?)
""", (nome, pontos))
    conn.commit()



# lendo os pontos
def ver_highscore():
    cursor.execute("""SELECT * FROM highscore""")
    scores = []
    for linha in cursor.fetchall():
        scores.append(linha)
    return scores

grava_pontos('Joesley', 50000)
print(ver_highscore())
