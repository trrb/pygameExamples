import sqlite3

quest = int(input())
lis = []
with sqlite3.connect('caravans.db') as db:
    cur = db.cursor()
    result = cur.execute(
        f"""SELECT name FROM Distances
        WHERE (distance + length) * 1.0 / {quest} <= rate""").fetchall()
    for i in range(len(result)):
        result[i] = result[i][0]
        rate = cur.execute(
            f"""SELECT (distance + length) * 1.0 / rate FROM Distances
            WHERE name == '{result[i]}'""").fetchone()
        lis.append((result[i], rate[0]))
lis_sorted = sorted(lis, key=lambda x: x[1], reverse=True)
for el in lis_sorted:
    print(el[0])
