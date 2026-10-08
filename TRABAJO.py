est=[]
mat=[]
notas=[]
while True:
    print("\n=== sistema académico ===")
    print("1. estudiantes")
    print("2. materias")
    print("3. notas")
    print("4. reporte")
    print("5. salir")
    try:
        op=int(input("opción: "))
        if op==1:
            print("\n=== estudiantes ===")
            print("1. registrar")
            print("2. ver")
            print("3. volver")
            x=int(input("opción: "))
            if x==1:
                id_est=int(input("id: "))
                existe=False
                for e in est:
                    if e["id"]==id_est:
                        existe=True
                if existe:
                    print("id ya registrado")
                else:
                    nom=input("nombre: ")
                    edad=int(input("edad: "))
                    gra=input("grado: ")
                    if nom!="" and gra!="" and edad>=5:
                        est.append({"id":id_est,"nombre":nom,"edad":edad,"grado":gra})
                        print("estudiante registrado")
                    else:
                        print("datos inválidos")
            elif x==2:
                if len(est)==0:
                    print("no hay estudiantes")
                else:
                    for e in est:
                        print(e["id"],"|",e["nombre"],"|",e["edad"],"|",e["grado"])
        elif op==2:
            print("\n=== materias ===")
            print("1. registrar")
            print("2. ver")
            print("3. volver")
            x=int(input("opción: "))
            if x==1:
                cod=input("código: ")
                existe=False
                for m in mat:
                    if m["codigo"]==cod:
                        existe=True
                if existe:
                    print("código ya registrado")
                else:
                    nom=input("materia: ")
                    pro=input("profesor: ")
                    cre=int(input("créditos: "))
                    if nom!="" and pro!="" and cre>0:
                        mat.append({"codigo":cod,"nombre":nom,"profesor":pro,"creditos":cre})
                        print("materia registrada")
                    else:
                        print("datos inválidos")
            elif x==2:
                if len(mat)==0:
                    print("no hay materias")
                else:
                    for m in mat:
                        print(m["codigo"],"|",m["nombre"],"|",m["profesor"],"|",m["creditos"],"créditos")
        elif op==3:
            print("\n=== notas ===")
            print("1. registrar nota")
            print("2. ver notas")
            print("3. volver")
            x=int(input("opción: "))
            if x==1:
                id_est=int(input("id estudiante: "))
                cod=input("código materia: ")
                estudiante=False
                materia=False
                for e in est:
                    if e["id"]==id_est:
                        estudiante=True
                for m in mat:
                    if m["codigo"]==cod:
                        materia=True
                if estudiante==False:
                    print("estudiante no encontrado")
                elif materia==False:
                    print("materia no encontrada")
                else:
                    eva=input("evaluación: ")
                    nota=float(input("nota: "))
                    porc=float(input("porcentaje: "))
                    acumulado=0
                    for n in notas:
                        if n["id"]==id_est and n["materia"]==cod:
                            acumulado+=n["porcentaje"]
                    if nota<0 or nota>5:
                        print("la nota debe estar entre 0 y 5")
                    elif porc<=0 or acumulado+porc>100:
                        print("porcentaje inválido")
                    else:
                        notas.append({"id":id_est,"materia":cod,"evaluacion":eva,"nota":nota,"porcentaje":porc})
                        print("nota registrada")
            elif x==2:
                id_est=int(input("id estudiante: "))
                encontrado=False
                for e in est:
                    if e["id"]==id_est:
                        print("\nestudiante:",e["nombre"])
                        encontrado=True
                if encontrado==False:
                    print("estudiante no encontrado")
                else:
                    for m in mat:
                        suma=0
                        porc=0
                        hay=False
                        for n in notas:
                            if n["id"]==id_est and n["materia"]==m["codigo"]:
                                hay=True
                                print(m["nombre"],"|",n["evaluacion"],"| nota:",n["nota"],"|",n["porcentaje"],"%")
                                suma+=n["nota"]*n["porcentaje"]
                                porc+=n["porcentaje"]
                        if hay:
                            promedio=suma/porc
                            print("promedio:",round(promedio,2),"| evaluado:",porc,"%")
        elif op==4:
            id_est=int(input("id estudiante: "))
            encontrado=False
            for e in est:
                if e["id"]==id_est:
                    print("\n=== reporte ===")
                    print("estudiante:",e["nombre"])
                    print("grado:",e["grado"])
                    encontrado=True
            if encontrado==False:
                print("estudiante no encontrado")
            else:
                promedios=[]
                for m in mat:
                    suma=0
                    porc=0
                    for n in notas:
                        if n["id"]==id_est and n["materia"]==m["codigo"]:
                            suma+=n["nota"]*n["porcentaje"]
                            porc+=n["porcentaje"]
                    if porc>0:
                        promedio=suma/porc
                        promedios.append(promedio)
                        if porc==100:
                            if promedio>=3:
                                estado="aprobada"
                            else:
                                estado="reprobada"
                        else:
                            estado="en curso"
                        print(m["nombre"],"| promedio:",round(promedio,2),"| estado:",estado)
                if len(promedios)>0:
                    general=sum(promedios)/len(promedios)
                    print("promedio general:",round(general,2))
                else:
                    print("no tiene notas registradas")
        elif op==5:
            print("saliendo...")
            break
        else:
            print("opción inválida")
    except ValueError:
        print("dato inválido")