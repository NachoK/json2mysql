import pymysql, os, json

#Lee el archivo Json que esta en file
file = os.path.abspath('C:\laragon\www\django\scripts\json2mysql') + "\json_file.json"
json_data = open(file).read()
json_obj = json.loads(json_data)


#Validaciones y Verificaciones antes del insert
def validate_string(val):
    if val != None:
        if type(val) is int:
            #for x in val:
            #    print(x)
            return str(val).encode('utf-8')
        else: 
            return val


#Conectamos con la Base de Datos MySql
con = pymysql.connect(host = 'localhost',user = 'root',passwd = 'p4r4guaY',db = 'json2mysql')
cursor = con.cursor()


#Analizamos los datos json para insertar SQL
for i, item in enumerate(json_obj):
    id = validate_string(item.get("id", None))
    person = validate_string(item.get("person", None))
    year = validate_string(item.get("year", None))
    company = validate_string(item.get("company", None))
    cursor.execute("INSERT INTO json2mysql (id, person, year, company) VALUES (%s,	%s,	%s,	%s)", (id, person,	year,	company) )


con.commit()
con.close()

