import pymysql, os, json, requests

# Se descarga archivo JSON
file = requests.get(url='https://raw.githubusercontent.com/NachoK/json_file/main/json_file.json')
print('EL ARCHIVO JSON SE DESCARGO CORRECTAMENTE')

# Se guardar el archivo JSON en el disco
data = file.json()
with open('YourData.json', 'w') as f:
    json.dump(data, f)


print('ARCHIVO GUARDADO CORRECTAMENTE')

# Se Lee el archivo JSON
file = "YourData.json"
json_data=open(file).read()
json_obj = json.loads(json_data)


# Se hace la validación del JSON
def validate_string(val):
   if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


print('JSON VALIDADO CORECTAMENTE')
# Se conecta a la base de datos mysql
con = pymysql.connect(host = 'localhost', port = 3306,user = 'root',passwd = 'p4r4guaY',db = 'json2mysql')
cursor = con.cursor()


print('SE CONECTO CORRECTAMENTE A LA BASE DE DATOS')

# Se limpia primero la tabla para evitar Claves primarias duplicadas
cursor.execute("TRUNCATE TABLE json2mysql")

# Se analiza los datos json en inserción SQL
for i, item in enumerate(json_obj):
    id = validate_string(item.get("id", None))
    person = validate_string(item.get("person", None))
    year = validate_string(item.get("year", None))
    company = validate_string(item.get("company", None))
# Insert SQL
    cursor.execute("INSERT INTO json2mysql (id, person, year, company) VALUES (%s,	%s,	%s,	%s)", (id, person,	year,	company) )


print("LOS DATOS SE GUARDARON CORRECTAMENTE")
print("PROGRAMA FINALIZADO CON EXITO")
con.commit()
con.close()