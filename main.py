from uniform_search import uniform_search  # Importa la funzione uniform_search dal modulo uniform_search

# Richiede all'utente di inserire la città di partenza e arrivo
start_point = input("Inserisci la città di partenza: ")
end_point = input("Inserisci la città di arrivo: ")

price_result, path_result = uniform_search(start_point, end_point) # Esegue l'algoritmo con le città inserite dall'utente

# Controlla se è il percorso è valido
if price_result is not None and path_result is not None:
    print(f"\nIl percorso più breve da {start_point} a {end_point} è:")
    print(chr(126) * 40) # formattazione

    for city, dist in path_result:     # Itera attraverso ogni città e distanza nel risultato del percorso
        print(f"Città {city.ljust(15)} | km: {dist}")     # Stampa il nome della città e la distanza accumulata
    print(chr(126) * 40)  # formattazione

    print(f"Distanza totale: {price_result} km\n")    # Stampa la distanza totale del percorso
else:
    # Se non è stato trovato alcun percorso, stampa un messaggio di errore
    print("Percorso non trovato, riprovare \n")
    