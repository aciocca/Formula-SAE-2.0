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
	Accedere al disco è un'operazione costosa, quindi abbiamo deciso un compromesso per  valido anche con il resto del team per ridurre al minimo il numero di accessi al disco senza però rischiare di perdere troppi dati in caso di crash,
	si usa pandas per gestire i .csv in modo ottimale
- Visualizzazione Real-Time dei dati della macchina
	Funzione principale del programma, il model avverte il controller che ci sono nuovi dati appena decodificati, il controller se non è già occupato prende i dati decodificati, aggiorna le variabili alle quali si appoggia il view e forza un refresh del view
- Dati su giri percorsi e tempo sul giro

POST GARA
- Lettura dei log salvati dal programma
	Caricati e gestiti tramite pandas
- Creazione di grafici con in input i dati salvati
	Si potrebbe usare plotly + una libreria per avere un minibrowser all'interno del nostro programma, oppure direttamente fare una gui in JS

	
STRETCH GOAL
- Comunicazione con la macchina 2 way (+ spie errore su macchina)
- Visualizzazione percorso GPS con possibilità di impostare punto di partenza
- Dati su giri percorsi e tempo sul giro
- Salvataggio dei log su server remoto
- Aggiornamento del view regolabile

5. Logica del programma 
Applicamo il design patter del Model View Controller
https://it.wikipedia.org/wiki/Model-view-controller

- MVC, perchè?
L'MVC garantisce un'ottimo grado di modularità al codice, permettendo il lavoro in parallelo senza interferenze di più sviluppatori e predispone anche ad un facile passaggio ad una web app in caso di necssità, richiedendo modifiche minime all'organizzazione del codice del programma.

	1) Boot
	L'entry point è il main.py, che si occupa di caricare il View
	2) Connessione al seriale
	Il view chiama il Controller, cha aprirà la comunicazione con il seriale e passerà l'oggetto creato al Model
	Il Model in un thread a parte avrà un loop dove chiederà dati in continuazione al seriale
	3)Il loop:
		3a) Decodifica
		Una volta letti dei dati dal seriale(N.B. CON IL PRIMO THREAD!), sottoforma di stringhe di byte, sempre il model si occuperà di decodificarli (IN UN ALTRO THREAD RISPETTO A QUELLO DI LETTURA) direttamente all'interno dello stesso loop
		3b) Aggiornamento
		Il Model aggiorna qui le variabili che poi successivamente verranno visualizzate dal View al prossimo loop di tkinter -D gestire lock delle variabili!! 
		-D Si potrebbe chiamare qui il controller (sul thread principale) una volta finito di aggiornare le variabili per avvertire il view dicendogli che ci sono dati nuovi da leggere, facendo qui il 
		check dell'accesso alle variabili
		3c) Salvataggio su file (NELLO STESSO THREAD DELLA LETTURA)
		Sempre nello stesso loop il model salva su dei file .csv, uno per ognuno dei tre blocchi di dati, chiudendo e salvando sul disco ogni {X} loop per evitare perdite di dati dovute ad eventuali crash del sistema
	4)L'aggiornamento del view
	Ad ogni tick di tkinter il view chiede al controller se ci sono nuovi dati, se si allora dice al controller di copiare tutte le variabili dal model al view (le variabili del view saranno di tipo tkString()) 

6. L'MVC nel dettaglio
	1) Il View
	Il view è composto dalle classi
	/
	/GRIFFIN/
	.........main.py				// Entry point
	.........__init__.py 			// Vuoto
	.........gui_griffin.py 		// Scheletro della gui, chiama lui tutti i moduli necessari per comporre la gui, le variabili dei dati della macchina fanno capo a lui, in quanto possono servire a più tab, ha lui il tk.root
	.........gui_connectiontab.py	// Tab dalla quale avviare la connessione al seriale o chiuderla
	.........gui_realtimetab.py		// Tab con i dati in tempo reale
	.........gui_****tab.py			// Tutte le altre tab avranno il loro rispettivo modulo
	.........gui_logic.py			// Gestisce la logica della gui e le sue variabili(greyare out alcune funzioni quando non disponibili o viceversa), contiene la classe GUI_LOGIC_HANDLER che deve essere passata ad ogni tab del programma
	........./interfaces/
	.....................serialinterface.py	// Chiamato da gui_logic.py, crea un oggetto serialhandler e lo passa a serialreader, si occupa anche di chiudere la connessione quando necessario
	.....................datainterface.py	// Chiamato sia da gui_griffin.py per controllare se ci sono dati nuovi, sia da serialreader.py per segnalare che ha finito di aggiornare i dati
	........./serialdata/
	.....................serialreader.py	// Gli viene passato l'oggetto connessione e in un thread a parte legge il seriale di continuo, è suo il loop 3) di cui sopra
	.....................dataframe.py
	.....................filehandler.py
	.....................formatdata.py
	.....................serialhandler.py
	........./res/			//Cartella con le immagini e le icone del programma

7. Tecnologie usate
tkinter
pyserial https://pythonhosted.org/pyserial/
Necessita di Python 2.7+
Multipiattaforma, può permettere il facile porting del codice anche su sistemi Linux e Mac OSX
