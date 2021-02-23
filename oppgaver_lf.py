"""Oppgaver til kurs i NumPy holdt av NumFys ved Thorvald Ballestad, 2020
"""
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 0 -- Dersom du ønsker litt mer trening på det aller enkleste #######
# Du får her to lister: python_list, som er en vanlig liste, og numpy_array,
# som er en numpy array.
python_list = [1,2,3,10]
numpy_array = np.array(python_list)

# a)
# Skriv ut hvert element i lista multiplisert med to, først med python-lista og så med numpy array.
# Løsningen med numpy array skal ikke bruke for-løkke.
for i in python_list:
    print(i*2)

print(numpy_array*2)

# b)
# Bruk np.linspace til å lage en liste med 20 punkter mellom 0 og 1
linearly_spaced_points = np.linspace(0, 1, 20)

# c)
# Bruk np.arange til å lage en liste med punkter mellom 0 og 3.14, som har avstand 0.21
points_with_given_distance = np.arange(0, 3.14, 0.21)


# Oppgave 1 -- The basics ####################################################
# a) Lag en numpy array med 100 tall mellom -10 og 4
x1 = np.linspace(-10, 4, 100)

# b) Lag en numpy array med kvadratroten av alle tallene i lista fra oppgave a) (hint: np.sqrt)
x2 = np.sqrt(x1)

# c) Lag en numpy array med kvadratroten av alle tallen i lista fra oppgave a, men legg til 1.2 til hvert tall. F.eks., dersom tallet fra a) er 1, skal det korresponderende tallet i denne lista være (1+1.2)^0.5. (hint: np.sqrt)
x3 = np.sqrt(x1 + 1.2)



# Oppgave 2 -- Plotting ######################################################
# a) Plot f(x) = sqrt(x) for x mellom -10 og 4 (altså tallene fra oppgave 1)
plt.plot(x1, x2, label="$\sqrt{x}$")
##plt.legend()
##plt.show()

# b) I samme figur som i oppgave a), plot også g(x) = sqrt(x + 1.2). Husk å ha med legend.
plt.plot(x1, x3, label="$\sqrt{x+1.2}$")
plt.legend()
plt.show()

# Oppgave 3 -- Matriser ######################################################
data = np.arange(1,21).reshape(10,2)
# data har nå ti rader og to kolonner.
# Hent ut, ved å bruke slicing, andre kolonne
# av data (dette skal være en array som begynner med 2).
first_col = data[:, 1]  # "all rows, index 1 column"

# Oppgave 4 -- Stepping it up ################################################
# Vi skal nå gjøre det litt mer komplisert.
# La oss se på
# f(x,y) = 1/sqrt( (x^2 - 1)^2 + y^2).
# Vi ønsker å finne ut av hvordan denne funksjonen
# ser ut for ulike x og y.
# Vi kunne ha skrevet en dobbelt for-løkke, men det
# kan ta veldig lang tid å kjøre når x- og y-listene
# blir lange. Vi ønsker derfor å regne ut dette ved
# hjelp av NumPy og meshgrid.
# Lag en to-dimensjonal liste som er f(x,y) for
# x mellom 0 og 10, og y er mellom 20 og 100.

def f(x,y):
    return 1/np.sqrt((x**2-1)**2 + y**2)

x = np.linspace(0, 10, 100)
y = np.linspace(20, 100, 100)
xx,yy = np.meshgrid(x,y)
output = f(xx,yy)

# Oppgave 5 -- Plotting i 2D #################################################
# Plot f(x,y) fra forrige oppgave som et heatmap (pcolormesh).
# Husk å ha med en colorbar
plt.pcolormesh(xx,yy,output)
plt.colorbar()
plt.show()
