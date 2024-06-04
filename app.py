from os import name
from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
import pymysql
app=Flask(__name__)
## Nos permite acceder desde una api externa
CORS(app)
## Funcion para conectarnos a la base de datos de mysql
def conectar(vhost,vuser,vpass,vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn
##registrar especies 
@app.route("/registrar/",methods=['POST'])
def reptiles():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into registro (nombre,nombre_cientifico,tipo_de_especie,veneno,habitos,habitat,fecha_avistamiento,escamas) values \
            ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(request.json['nombre'],\
            request.json['nombre_cientifico'],request.json['tipo_de_especie'],request.json['veneno'],request.json['habitos'],request.json['habitat'],request.json['fecha_avistamiento'],request.json['escamas']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)

##consulta especifica
@app.route("/consultar/<nombre>",methods=['GET'])
def consulta_reptiles(nombre):
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM registro where nombre='{0}' """.format(nombre))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'nombre':datos[0],'nombre_cientifico':datos[1],'tipo_de_especie':datos[2],'veneno':datos[3],'habitos':datos[4],'habitat':datos[5],'fecha_avistamiento':datos[6],'escamas':datos[7]}
            return jsonify({'registro':dato,'mensaje':'Registro  encontrado'})
        else:
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

##actualizar especies
##@app.route("/actualizar_reptiles/<cod_reptiles>",methods=['PUT'])
##def actualizar_reptiles(cod_reptiles):
    ##try:
        ##conn=conectar('localhost','root','','ras')
        ##cur = conn.cursor()
        ##x=cur.execute(""" update reptiles set nombre='{0}',nombre_cientifico='{1}',veneno='{2}',habitos='{3}',habitad='{4}',cola_terminal='{5}',escamas='{6}'where \
            ##cod_reptiles={7}""".format(request.json['nombre'],request.json['nombre_cientifico'],request.json['veneno'],request.json['habitos'],request.json['habitad'],request.json['cola_terminal'],request.json['escamas'],cod_reptiles))
        ##conn.commit()
        ##cur.close()
        ##conn.close()
        ##return jsonify({'mensaje':'Registro Actualizado'})
    ##except Exception as ex:
        ##print(ex)
        ## return jsonify({'mensaje':'Error'})

    
##registrar avistador
@app.route("/registrar_avistador/",methods=['POST'])
def avistador():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into avistador (ficha,clave,nombre_usuario) values \
            ('{0}','{1}','{2}'""".format(request.json['ficha'],\
                request.json['clave'],request.json['nombre_usuario']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)

## registar p_siga
@app.route("/registrar_p_siga/",methods=['POST'])
def p_siga():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into p_siga (nombre_usuario,clave,ocupacio) values \
            ('{0}','{1}','{2}'""".format(request.json['nombre_usuario'],\
                request.json['clave'],request.json['ocupacion']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)

## reporte especies
@app.route("/avistamiento/",methods=['POST'])
def avistar():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into avistamiento (ubicacion,hora,aspecto,ataco,imagen) values \
            ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['ubicacion'],\
                request.json['hora'],request.json['aspecto'],request.json['ataco'],request.json['imagen']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Reporte agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)





















#@app.route("/")
#def tipo_de_especie():
   # try:
     #conn=conectar('localhost','root','','ras')
        #cur = conn.cursor()
        #cur.execute(""" select reptiles.cod_reptiles,reptiles.nombre as nom_reptil,reptiles.nombre_cientifico,anfibios.cod_anfibios,anfibios.nombre as nom_anfibio,anfibios.nombre_cientifico
                        #from tipo_de_especie 
                        #inner join reptiles on tipo_de_especie.cod_especie=reptiles.cod_reptiles
                        #inner join anfibios on tipo_de_especie.cod_especie=anfibios.cod_anfibios""")
        #datos=cur.fetchall()
        #data=[]
        #for row in datos:
            #dato={'codigo_especie,':row[0],'nombre':row[1],'nombre_cientifico,':row[2],}
            #data.append(dato)
       # cur.close()
        #conn.close()
        #return jsonify({'especies':data,'mensaje':'Baul de especies'})
    #except Exception as ex:
        #print(ex)
        #return jsonify({'mensaje':'Error'})
if name=='main_':
    app.run(debug=True)