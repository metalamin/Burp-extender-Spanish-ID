# Burp Extension for Spanish ID

## Spanish ID letter algorithm
The letter of the NIF is obtained from an algorithm known as module 23. The algorithm consists in applying the arithmetic operation of module 23 to the number of the DNI. Module 23 is the whole number obtained as a remainder of the integer division of the DNI number between 23. The result is a number between 0 and 22. Based on a known table, a letter is assigned. The combination of the DNI with that letter is the NIF.
[(Algoritmo para obtener la letra del NIF)][1]

[1]:https://es.wikibooks.org/wiki/Algoritmia/Algoritmo_para_obtener_la_letra_del_NIF

## Payload processor
The extension is a payload processor for the Burp intruder. It adds the check letter at the end of the numeric payload.

![Add payload processing](https://i.imgur.com/7I82lWk.png)
![Generated payloads](https://i.imgur.com/pzBuRfr.png)
