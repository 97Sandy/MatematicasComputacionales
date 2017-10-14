

def main():
    sims=[] #Simbolos
    fin=[]  #Clausulas finales

    dummie=0  #para el dummie
    clausulas =0 #numero de clausulas originales
    clausulasN=0 #n. clausulas nuevas
    numl=0 #flag pal for
    k=0 #grado del ksat

    nombreArch=input("Introduce el nombre del archivo: ")

    entrada=open(nombreArch,"r") #recibimos el archivo de entrada
    salida=open("salida.txt","w")

    for linea in entrada:   #En este for obtenemos las variables y los simbolos los guardamos en un arraylist
        linea = linea.split()

        if numl == 1:
            dummie=int(linea[2])+1
            clausulas=int(linea[3])

        if numl >= 2:
            linea.remove('0')
            k = len(linea)
            for num in linea:
                sims.append(num)

        numl+=1

    entrada.close()


    if k == 1:
        fin.append(sims[0]+" "+sims[0]+" "+sims[0]+"0")
        clausulasN+=1
    if k == 2:
        fin.append(sims[0]+" "+sims[1]+" "+str(dummie)+" "+"0")
        fin.append(str(dummie*-1)+" "+sims[0]+" "+sims[1]+" "+"0")
        clausulasN+=2
    if k == 3:
        i=0
        while(i<len(sims)):
            fin.append(sims[i]+" "+sims[i+1]+" "+sims[i+2]+" 0")
            clausulasN+=1
            i+=3;
    if k>3:
        fin.append(sims[0] + " " + sims[1] + " " + str(dummie) + " 0")
        clausulasN += 1
        for i in range(2, len(sims)-2):
            fin.append(str(dummie*-1) + " " + sims[i] + " " + str(dummie+1) + " 0")
            dummie += 1
            clausulasN += 1

        fin.append(str(dummie* -1) + " " + sims[len(sims)-2] + " " + sims[len(sims)-1] + " 0")
        clausulasN += 1

    salida = open("salida.txt" , "w")

    salida.write("c A SAT instance generated from a 3-CNF formula that had "+str(clausulasN)+" clauses and "+str(dummie-1)+" variables\n")
    print("c A SAT instance generated from a 3-CNF formula that had "+str(clausulasN)+" clauses and "+str(dummie-1)+" variables\n")

    salida.write("p cnf "+str(dummie-1)+ " "+str(clausulasN)+"\n")
    print("p cnf "+str(dummie-1)+ " "+str(clausulasN)+"\n")
    for clausula in fin:
        salida.write(clausula+"\n")
        print(clausula+"\n")

    salida.close()

if __name__ == "__main__":
    main()

