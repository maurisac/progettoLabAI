from queue import PriorityQueue
from map import map 


def check_cities(map, start_point, end_point):
    if start_point not in map:
        print(f"Città {start_point} non presente nel dataset")
        return False
    if end_point not in map:
        print(f"Città {end_point} non presente nel dataset")
        return False
    return True


def uniform_search(start_point, end_point):
    if not check_cities(map, start_point, end_point):  # Verifica dell'input
        return None, None 

    frontier_queue = PriorityQueue()  # Crea una coda di priorità per i nodi da espandere
    # Inizia con il nodo di partenza, costo 0, percorso con solo il nodo di partenza, e costo accumulato 0
    frontier_queue.put((0, [start_point], [0]))  
    
    fullfilled_nodes = set()  # Insieme per tenere traccia dei nodi già espansi

    while not frontier_queue.empty():  # Continua finché ci sono nodi da espandere
        price, path, medium_price = frontier_queue.get()  # Estrae il nodo con il costo più basso
        current_city = path[-1]  # Ottiene la città corrente dal percorso

        if current_city == end_point:  # Se la città corrente è la destinazione
            return price, list(zip(path, medium_price))  # Restituisce il costo totale e il percorso

        if current_city not in fullfilled_nodes:  # Se la città corrente non è già stata espansa
            fullfilled_nodes.add(current_city)  # Aggiunge la città corrente all'insieme dei nodi espansi

            for neigh, dist in map[current_city]:  # Per ogni vicino della città corrente
                if neigh not in fullfilled_nodes:  # Se il vicino non è già stato espanso
                    new_price = price + dist  # Calcola il nuovo costo accumulato
                    new_path = list(path)  # Crea una copia del percorso attuale
                    new_path.append(neigh)  # Aggiunge il vicino al nuovo percorso
                    new_medium_price = list(medium_price)  # Crea una copia dei costi accumulati
                    new_medium_price.append(new_price)  # Aggiunge il nuovo costo accumulato
                    # Inserisce il vicino nella coda di priorità con il nuovo costo e percorso
                    frontier_queue.put((new_price, new_path, new_medium_price))

    return None, None  # Se nessun percorso viene trovato, restituisce None, None
