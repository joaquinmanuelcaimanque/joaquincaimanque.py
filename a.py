#definir 2 candidatos

Cand1=(input("ingrese nombre del candidato 1"))
Cand2=(input("ingrese nombre del candidato 2"))

#preguntar la cantidad d votantes

Cant=(int(input("ingrese la cantidad de votantes")))

v_Cand1=0
v_Cand2=0

voto=int(input(F"ingrese por quien votara {Cand1} o el {Cand2}"))

if voto==1:
    v_Cand1=v_Cand1+1
elif voto==2:
    v_Cand2+v_Cand2+1
else:
    print("error en el voto")      

if v_Cand1>v_Cand2:
        print("el ganador es {cand1} con votos {v_cand1}")

elif v_Cand2>v_Cand1:
     print("el ganador es {cand1} con votos {v_cand2}")