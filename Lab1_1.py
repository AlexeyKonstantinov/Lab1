class Element:
    def __init__(self, name="default", group=0, period=0, family = "default"):
        self.name = name
        self.group = group
        self.period = period
        self.family = family
        
def Answer(answer):
    if (answer == "Да"):
        return True
    else:
        return False


sMet = "Щелочные металлы"
szMet = "Щелочноземельные металлы"
ppMet = "Постпереходные металлы"
poluMet = "Полуметаллы"
Nemet = "Неметаллы"
Gal = "Галогены"
BlGaz = "Благородные газы"


elementArray = []
elementArray.append(Element("Li", 1, 2, sMet))
elementArray.append(Element("Be", 2, 2, szMet))
elementArray.append(Element("B", 13, 2, poluMet ))
elementArray.append(Element("C", 14, 2, Nemet))
elementArray.append(Element("N", 15, 2, Nemet))
elementArray.append(Element("O", 16, 2, Nemet))
elementArray.append(Element("F", 17, 2, Gal))
elementArray.append(Element("Ne", 18,2, BlGaz))
elementArray.append(Element("Na", 1, 3, sMet))
elementArray.append(Element("Mg", 2, 3, szMet))
elementArray.append(Element("Al", 13, 3, ppMet))
elementArray.append(Element("Si", 14, 3, poluMet))
elementArray.append(Element("P", 15, 3, Nemet))
elementArray.append(Element("S", 16, 3, Nemet))
elementArray.append(Element("Cl", 17, 3, Gal))
elementArray.append(Element("Ar", 18, 3, BlGaz))

if( Answer(input("Этот элемент входит во второй период? \n")) ):
    for element in elementArray[:]:
        if (element.period != 2):
            elementArray.remove(element)
else:
    for element in elementArray[:]:
        if (element.period != 3):
            elementArray.remove(element)

if( Answer(input("Этот элемент входит в cемейство щелочные металлы? \n")) ):
    for element in elementArray[:]:
        if (element.family != sMet):
            elementArray.remove(element)

elif ( Answer(input("Этот элемент входит в cемейство щелочноземельные металлы? \n")) ):
    for element in elementArray[:]:
        if (element.family != szMet):
            elementArray.remove(element)

elif ( Answer(input("Этот элемент входит в cемейство постпереходные металлы? \n")) ):
    for element in elementArray[:]:
        if (element.family != ppMet):
            elementArray.remove(element)

elif ( Answer(input("Этот элемент входит в cемейство полуметаллы? \n")) ):
    for element in elementArray[:]:
        if (element.family != poluMet):
            elementArray.remove(element)

elif ( Answer(input("Этот элемент входит в cемейство неметаллы? \n")) ):
    for element in elementArray[:]:
        if (element.family != Nemet):
            elementArray.remove(element)

elif ( Answer(input("Этот элемент входит в cемейство галогены? \n")) ):
    for element in elementArray[:]:
        if (element.family != Gal):
            elementArray.remove(element)

else:
    for element in elementArray[:]:
        if (element.family != BlGaz):
            elementArray.remove(element)

print("\n Вот что мы нашли по вашему запросу: \n")
for element in elementArray:
    print(element.name)


                            
    

