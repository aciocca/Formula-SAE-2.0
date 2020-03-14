GRIFFIN

1. Introduzione
GRIFFIN è un programma creato da un team di studenti di ingegneria informatica dell'Università di Perugia per rispondere alla necessità del team della Formula SAE di avere un software che si occupi della telemetria della macchina.
Il software si occupa sia del monitoraggio in tempo reale dei sensori presenti sulla macchina, sia del logging e analisi dei log a macchina ferma.

2. Set-Up
GRIFFIN necessita di Python 3.6 o superiore e della libreria pyserial, versione 3.4 o superiore, necessaria per comunicare con l'antenna usb.
Python può essere ottenuto all'indirizzo www.python.org/downloads/
pyserial può essere ottenuto all'indirizzo pypi.org/project/pyserial/ oppure tramite pip, con il comando pip install pyserial
Il programma può essere eseguito lanciando main.py

3. Issue Tracker
GRIFFIN è un progetto Open Source, ancora senza nessuna licenza, ma disponibile all'indirizzo github.com/aciocca/Formula-SAE-2.0

4. Features


Funzionalità:
- Acquisizione dei dati via antenna wireless [specifiche antenna]
	In un thread separato, abbiamo un modulo che polla constantemente il seriale per nuovi dati, se ne trova allora passa allo step successivo -) Possibile problema dove non legge dati perchè sta decodificando un pacchetto vecchio?
- Decodifica dei pacchetti in ricezione
	I pacchetti arrivono sottoforma di stringhe di byte, con un HEADER che ci dice a quale dizionario dobbiamo fare riferimento (4hz, 10hz, 100hz) e siccome ogni pacchetto ha una dimensione in byte fissa, dando così la possibilità di assegnare il dato alla key del dizionario corretta basandoci semplicemente sulla posizione all'interno della stringa e all'header
- Logging dei dati, con salvataggio su disco ogni X per resilenza ai crash
	Accedere al disco è un'operazione costosa, quindi abbiamo deciso un compromesso per  valido anche con il resto del team per ridurre al minimo il numero di accessi al disco senza però rischiare di perdere troppi dati in caso di crash
- Visualizzazione Real-Time dei dati della macchina
	Funzione principale del programma, il model avverte il controller che ci sono nuovi dati appena decodificati, il controller se non è già occupato prende i dati decodificati, aggiorna le variabili alle quali si appoggia il view e forza un refresh del view

POST GARA
- Lettura dei log salvati dal programma
STRETCH GOAL
- Comunicazione con la macchina 2 way (+ spie errore su macchina)
- Animazioni fluide
- Visualizzazione percorso GPS con possibilità di impostare punto di partenza
- Dati su giri percorsi e tempo sul giro
- Salvataggio dei log su server remoto
- Aggiornamento del view regolabile


5. Tecnologie usate
pyserial https://pythonhosted.org/pyserial/
Necessita di Python 2.7+
Multipiattaforma, può permettere il facile porting del codice anche su sistemi Linux e Mac OSX

asyncio

