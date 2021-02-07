import sqlite3
import json

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
data = json.load(open('data.json'))

with conn:
    cursor.execute("""CREATE TABLE IF NOT EXISTS definitions (
                    word TEXT,
                    definition TEXT
                    );""")


for i, word in enumerate(data.keys(), start=1):
    if isinstance(data[word], list):
        for def_idx in data[word]:
            with conn:
                cursor.execute("INSERT INTO definitions VALUES (:word, :definition)",
                               {'word': word, 'definition': def_idx})
        print(f'Finished uploading {word} ({i}/{len(data)})')

    else:
        with conn:
            cursor.execute("INSERT INTO definitions VALUES (:word, :definition)",
                           {'word': word, 'definition': data[word]})
        print(f'Finished uploading {word} ({i}/{len(data)})')
