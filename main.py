import random

# Datele problemei
capacitate_maxima = 40
valori = [100, 120, 5, 7, 60, 15, 92, 77, 40, 35]
greutati = [2, 5, 7, 12, 3, 2, 9, 4, 12, 11]
populatie_dim = 20  # Dimensiunea populației
nr_generatii = 100  # Numărul de generații
probabilitate_mutatie = 0.1
probabilitate_incrucisare = 0.8

# Funcția de fitness
def calculeaza_fitness(individ):
    valoare_totala = sum(val for i, val in enumerate(valori) if individ[i] == 1)
    greutate_totala = sum(gre for i, gre in enumerate(greutati) if individ[i] == 1)
    if greutate_totala > capacitate_maxima:
        return 0  # Penalizare dacă depășim capacitatea
    return valoare_totala

def genereaza_populatie(dimensiune):
    return [[random.randint(0, 1) for _ in range(len(valori))] for _ in range(dimensiune)]

def selectie_ruleta(populatie, fitness):
    total_fitness = sum(fitness)
    if total_fitness == 0:
        return random.choice(populatie)
    selectia = random.uniform(0, total_fitness)
    partial_sum = 0
    for individ, fit in zip(populatie, fitness):
        partial_sum += fit
        if partial_sum >= selectia:
            return individ

# Încrucișare între doi părinți
def incrucisare(parinte1, parinte2):
    punct_taiere = random.randint(1, len(parinte1) - 1)
    copil1 = parinte1[:punct_taiere] + parinte2[punct_taiere:]
    copil2 = parinte2[:punct_taiere] + parinte1[punct_taiere:]
    return copil1, copil2

def mutatie(individ):
    for i in range(len(individ)):
        if random.random() < probabilitate_mutatie:
            individ[i] = 1 - individ[i]

def algoritm_genetic():
    populatie = genereaza_populatie(populatie_dim)
    for generatie in range(nr_generatii):
        fitness = [calculeaza_fitness(individ) for individ in populatie]
        populatie_noua = []

        while len(populatie_noua) < populatie_dim:
            parinte1 = selectie_ruleta(populatie, fitness)
            parinte2 = selectie_ruleta(populatie, fitness)

            if random.random() < probabilitate_incrucisare:
                copil1, copil2 = incrucisare(parinte1, parinte2)
            else:
                copil1, copil2 = parinte1, parinte2

            mutatie(copil1)
            mutatie(copil2)

            populatie_noua.append(copil1)
            populatie_noua.append(copil2)

        populatie = populatie_noua[:populatie_dim]

    # Determinarea celui mai bun fitness
    fitness_final = [calculeaza_fitness(individ) for individ in populatie]
    index_max = fitness_final.index(max(fitness_final))
    return populatie[index_max], max(fitness_final)

solutie, valoare_maxima = algoritm_genetic()
print("Soluție optimă:", solutie)
print("Valoare maximă:", valoare_maxima)