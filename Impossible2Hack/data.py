import sqlite3

conn = sqlite3.connect('data.db')

# conn.execute("INSERT INTO USERS('USERNAME','PASSWORD') VALUES(?,?)",('Beastboy','Person'))
# conn.commit()

input = input('Enter text: ')
query = f"SELECT * FROM USERS WHERE PASSWORD='{input}' and USERNAME='Nikola Tesla'"
print(query)
data = conn.execute(query)
i=0
for row in data:
    i+=1
print(i)