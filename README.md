## Presentazione del Codice per la Simulazione della Propagazione dell'Onda

![Uploading wave_simulation.gif…]()


Il seguente codice Python è un'applicazione del metodo delle differenze finite per simulare la propagazione di un'onda in un dominio bidimensionale quadrato. Questo esempio pratico ha diverse finalità educative e dimostrative:

1. **Fondamenti Matematici**: Illustra l'implementazione numerica dell'equazione delle onde, una seconda equazione differenziale parziale (PDE) che descrive come un'onda si propaga nel tempo e nello spazio.
   
2. **Metodo delle Differenze Finite**: Utilizza un approccio numerico ben noto per risolvere equazioni differenziali parziali, rendendolo un ottimo punto di partenza per chi è nuovo ai metodi numerici applicati alle PDE.

3. **Condizioni al Contorno**: Introduce il concetto di condizioni al contorno e come possono essere implementate in una simulazione numerica. In questo caso, sono stati utilizzati sia bordi fissi che una "barriera" interna.

4. **Visualizzazione in Tempo Reale**: Il codice include un modo per visualizzare in tempo reale la propagazione dell'onda, rendendo immediatamente visibili gli effetti delle diverse condizioni al contorno.

5. **Salvataggio dei Risultati**: Oltre alla visualizzazione in tempo reale, il codice salva anche la simulazione come un'animazione GIF e come un'immagine PNG per l'analisi successiva.

Per utilizzare il codice, è necessario avere installate le librerie Python `NumPy`, `Matplotlib`, e `PIL` (Pillow).

Esegui il codice per osservare come un'onda si propaga attraverso un mezzo bidimensionale e come interagisce con gli ostacoli e i bordi.

![finitedifference](https://github.com/braucci/wave/assets/16705368/dd93d44e-692d-40ae-890d-ea780da16dbd)
