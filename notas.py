
def verificarnota(p_nota):
  if type(p_nota) not in [int, float]:
    raise TypeError("La nota debe ser un número decimal o entero")
    #return ("La nota debe ser un número decimal o entero")
  if p_nota>75 and p_nota<=100:
   return("O")
  elif p_nota>=60 and p_nota<=75:
    return("A")
  elif p_nota>=50 and p_nota<=59:
    return("B")
  elif p_nota>=40 and p_nota<=49:
    return("C")
  elif p_nota>0 and p_nota<40:
    return("D")
  else:
    return("Inválida")



