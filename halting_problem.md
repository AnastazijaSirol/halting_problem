# Halting problem
## Uvod
Svoj smo projekt izradili na temu Halting problema koju smo obradili tako što smo analizirali definiciju samog problema, objasnili kako funkcionira bazirajući se na Turingove strojeve, iznijeli dokaz pomoću programskog koda i moguće rješenje problema te opisali njegov utjecaj na razvoj softvera.
## Otkriće
Početkom 20. stoljeća matematičare je zanimalo povlače li određene premise za sobom određeni zaključak. Premise su pretpostavke koje si zadajemo, a zaključak želimo donijeti na temelju njih. Zanimalo ih je postoji li neki test ili automatiziran način koji bi dokazao ili demantirao donose li određene pretpostavke željeni zaključak. To je dovelo do problema odlučivanja i pitanja postoji li njegovo rješenje za logiku prvog reda i je li ona odlučujuća.
Alan Turing utvrdio je da logika prvog reda nije odlučujuća pomoću "black box problema" koji stvara kontradikciju i dovodi do halting problema. 
### Definiranje problema 
Halting problem ili problem zaustavljanja je poznati problem među programerima koji se ubraja u  probleme odlučivanja, odnosno probleme čiji ishodi mogu biti "da" ili "ne", a za određeni se program mogu definirati kao da/ne pitanja ulaznih vrijednosti.  
Halting problem podrazumijeva uočavanje hoće li se unosom određenog algoritma program zaustaviti ili izvoditi beskonačno. Pod zaustavljanjem se podrazumijeva prihvaćanje ili odbijanje određenog algoritma da bi se izbjeglo beskonačno izvođenje. Poznato je da se ne može napisati program koji bi mogao uvidjeti hoće li se neki drugi program zaustaviti u određenom trenutku ili ući u beskonačnu petlju kada se pokrene. 
Pretpostavimo li da postoji program A koji uvijek točno utvrđuje zaustavljanje nekog drugog programa, on bi funkcionirao tako da uzme neki drugi program kao ulaz i nakon njegove obrade utvrdi hoće li se taj program zaustaviti ili ne. Zatim se treba stvoriti stroj S koji bi obuhvaćao navedeni program, a radio bi tako da svaki program koji dobije kao ulaz proslijedi programu A i učini suprotno od onoga što A utvrdi. Dakle, ako program A utvrdi da se program zaustavlja, stroj S se nikada neće zaustaviti i suprotno. Problem nastaje kada stoj S, programu A, proslijedi vlastiti program. Nakon što program A utvrdi hoće li se program zaustaviti ili ne, stroj S učinit će suprotno od toga jer je tako dizajniran. To će dovesti do zaključka da je program A u krivu, što se ne poklapa s početnom pretpostavkom da je program A uvijek u pravu. Stoga, nije moguće stvoriti opći algoritam koji bi za svaki dani program znao hoće li se zaustaviti ili ne, zbog čega je ovaj problem nerješiv.
S obzirom na to da se smatra da je Alan Turing prvi dokazao problem zaustavljanja, on se najčešće povezuje s Turingovim strojevima, odnosno strojevima namijenjenim za manipulaciju simbolima.
## Teorija izračunljivosti
Teorija izračunljivosti ili rekurzije je grana teorijske informatike i matematičke logike koja sadrži i pojmove čiste matematike, a bavi se proučavanjem algoritama, njihovom složenošću i granicama samog računanja. Ona proučava probleme koji su računski rješivi tako što koristi različite modele računanja. Njezin razvoj započeo je početkom tridesetih godina dvadesetog stoljeća kada je predstavljena od strane Stephena Kleenea, Emila Posta, Kurta Godela, Alonza Churcha i Alana Turinga, a sve u svrhu shvaćanja koji su matematički problemi (rješivi i nerješivi) doveli do razvoja računala. Temelj teorije izračunljivosti postavio je Alan Turing pomoću svog modela računala, poznatog kao Turingov stroj.
### Računljivost i Turingov stroj
Računljivost podrazumijeva sposobnost računala da riješi neki problem pomoću algoritma u određenom vremenskom periodu. Jedan od osnovnih primjera za definiranje računljivosti i složenosti algoritama je Turingov stroj koji ima 3 glavna dijela, a to su traka, glava za čitanje i pisanje te jedinica za kontrolu stanja stroja.
Traka je beskonačni niz polja koja mogu biti označena jedinicom ili nulom (biti prazna). U jedno polje može biti upisan samo jedan znak. Traka može imati određen broj jedinica i beskonačan broj nula. Glava za čitanje i pisanje u svakom se trenutku nalazi iznad jednog polja u traci. Ona se kreće po traci korak po korak i skrenira ju tako što čita i ispisuje simbole. Ovakav se stroj uvijek nalazi u određenom stanju. Za svako polje i stanje u kojem se nalazi, pokreće se jedna od tri radnje. Prva radnja stroja je upisivanje ili brisanje jedinice iz polja. U slučaju da se polje već nalazi u traženom stanju, stroj ne izvodi radnju. Druga radnja stroja je pomicanje glave ulijevo ili udesno, odnosno ostajanje na istom mjestu. Posljednja faza je prijelaz u novo stanje ili ostajanje u istom. Sve su radnje određene posebnim pravilima, a svako pravilo govori o tome koje će se radnje izvesti, ovisno o trenutnom stanju i onime što je upisano u polju. Stroj ima i tablicu prijelaza u kojoj je definirano koju radnju stroj mora izvršiti u svakom stanju na temelju znaka u polju iznad kojeg se nalazi glava za čitanje i pisanje. 
![](https://study.com/cimages/multimages/16/turingmachineexample.png)
## Turingovi strojevi
Alan Turing stvorio je Turingov stroj kao matematičku apstrakciju ljudskog procesa računanja. Korištenjem Turingovog stroja, 1936. dokazao je da halting problem nad Turingovim strojevima nije odlučujuć, što znači da niti jedan Turingov stroj ne može prekinuti program i proizvesti točan odgovor za sve moguće kombinacije i ulazne vrijednosti nekog programa.
Turingovi strojevi mogu se definirati na više načina, no što se tiče rješivosti problemskih instanci sve su ekvivalentne. Razlika je u tome što su neki modeli Turingovih strojeva brži od drugih u rješavanju određenih klasa problema što je inspiriralo teoriju složenosti.
Tri modela Turingovog stroja bitna za halting problem su determanistički, nedetermanistički i univerzalni.
### Determanistički Turingov stroj
Premisa ovog stroja je da računanjem pomoću olovke i neograničenog papira na kvadratiće, gdje svaki kvadratić sadrži najviše jedan ili niti jedan znak konačnog alfabeta, uvijek je konačno mnogo kvadratića ispunjeno. 
Ukoliko neka osoba računa po unaprijed zadanim pravilima, imajući pregled nad konačno mnogo kvadratića ispred sebe, tijekom procesa računanja dolazi do promjene internog stanja i stanja svijesti koja odražavaju informacije o trenutačnom tijeku proračuna. Osoba koja računa, mijenja stanje svijesti i sadržaj tih kvadratića ovisno o internim stanjima, unaprijed određenim pravilima i znakovima zapisanim u njima.

**Komponente i konfiguracija determinističkog Turingovog stroja**
Deterministički Turingov stroj M je sedmorka (Q, Σ, Γ, _, s, F, δ), gdje je:

Q konačan skup čije elemente zovemo stanjima
Σ konačan ulazni alfabet
Γ konačan alfabet trake, takav da je Σ ⊂ Γ
_ ∈ Γ \ Σ posebno odabrani simbol blank koji predstavlja bjelinu
s ∈ Q istaknuto početno stanje
F ⊆ Q skup završnih stanja
δ funkcija prijelaza (parcijalna funkcija, što znači da nije nužno definirana na cijeloj domeni)
δ : (Q \ F) × Γ → Q × Γ × {☜, □, ☞}.

Deterministički Turingov stroj sastoji se od beskonačne trake i glave koja s nje čita i na nju ispisuje simbole konačnog alfabeta Γ. Stroj je na početku u istaknutom početnom stanju (s), a na, inače praznoj, beskonačnoj traci zapisani su simboli pomoću konačnog ulaznog alfabeta (Σ). Glava pročita simbol u svakom kvadratiću u traci i zapiše novi simbol iz nekog konačnog alfabeta ovisno o stanju u kojem se nalazi, t zatim promjeni stanje i pomiče s ulijevo (☜), ostaje na mjestu (□) ili se pomiče udesno (☞). Stroj prestaje s radom tek kada dođe u neko od završnih stanja (F), a traka tada sadrži zapisane izlazne podatke.
Traka je zapravo niz ćelija, od kojih sadrži najviše jedan ili niti jedan znak konačnog alfabeta. U taktu je popunjeno konačno mnogo ćelija koje sadrže neki simbol različit od bjeline. Stanje same trake formalno je opisano funkcijom "tape: N × N → Γ" koja za neki dati takt (t) i pripadajuću datu ćeliju (n) vraća rezultirajući simbol "tape(t, n)". To se odvija pod uvjetom da se konačno mnogo popunjenih ćelija može formulirati kao "(∀t ∈ N) (∃m ∈ N) |{ n ∈ N | tape(t, n) ≠ _ }| ≤ m".
Uz traku, Turingov stroj sadrži i glavu koja služi za čitanje i pisanje po traci. U jednom taktu, glava je točno nad jednom ćelijom u koju je zapisan trenutačni simbol. Simbol je trenutačni sve dok se glava nalazi točno iznad njega. Čim se pomakne na neku drugu ćeliju, simbol u toj ćeliji postaje trenutačni simbol. Formalna funkcija koja ukazuje nad kojom ćelijom se nalazi glava u nekom taktu glasi "head: N → N ", dok je funkciija koja daje trenutačni simbol "symb: N → Γ" definirana kao "symb(t) = tape(t, head(t))".
Što se tiče prethodno spomenutih stanja, u svakom se taktu, Turingov stroj nalazi u točno jednom, a njegova formalna funkcija je "N → Q.". Primarna svrha stanja Turingovih strojeva je imenovanje trenutačnih, pamćenje prethodnih ili zadavanje budućih akcija. Ta deskriptivna imena stanja pogodna su za praktičnu primjenu, no za teorijska razmatranja ih je bitno razlikovati. Stoga, skup stanja Turingovog stroja možemo identificirati s početnim segmentom duljine "|Q|" prirodnih brojeva. 
U praksi se koristi alfabet, što sličniji onom kojim je izrečen problem koji se rješava pomoću Turingovog stroja, no u teoriji je bolje koristiti fiksan alfabet. To se postiže tako da se zada jedan jedinstveni simbol bjeline za sve Turingove strojeve, a ostali simboli alfabeta su numerirani i predstavljeni prirodnim brojevima. Kao okosnicu svakog alfabeta Turingovog stroja uzima se baza 2, odnosno simboli 0 i 1.
Trenutačna konfiguracija Turingovog stroja opisuje sveukupno stanje stroja za neki dani takt. Ta konfiguracija pamti poziciju glave, trenutačno stanje i sadržaj same trake. Konfiguraciji je dovoljno pratiti samo sadržaj konačno mnogo ćelija u kojima je upisan neki simbol alfabeta, odnosno polja u kojima nisu bjeline. Konfiguracija ("cfg: N → N") formalno se zadaje kao funkcija takta "cfg(t) =〈 (state(t), head(t), { (n, tape(t, n)) | n ∈ N, tape(t, n) ≠ _ }) 〉".
Iz svega toga slijedi zaključak da je Turingove strojeve moguće kodirati kao sedmorke njihovih definicijskih komponenti (stanja (Q), konačnog ulaznog alfabeta (Σ), konačnog alfabeta trake (Γ), univerzalnog znaka za bjelinu (_), istaknutoog početnog stanja (s), skupa završnih stanja (F) i same funkcije prijelaza (δ to jest δ : (Q \ F) × Γ → Q × Γ × {☜, □, ☞})). Takvim se  kodovima može služiti kao cjelovitim opisom Turingovih strojeva, odnosno "desc(M) =〈M〉, gdje je M = (Q, Σ, Γ, _, s, F, δ)". Iz toga je vidljivo da postoji prebrojivo mnogo različitih Turingovih strojeva.

**Rad determinističkog Turingovog stroja**
Za rad determinističkog turingovog stoja potrebno je poznavati početne uvjete i pravila prijelaza.

POČETNI UVJETI
head(0) := 0
state(0) := s
PRAVILA PRIJELAZA
state(t + 1) := Δ(t)0
tape(t + 1, head(t)) := Δ(t)1

Pravila prijelaza za glavu
Ako je Δ(t)2 = ☜ i head(t) > 0, onda je head(t + 1) := head(t) − 1.
Ako je Δ(t)2 = □ ili ako je Δ(t)2 = ☜ i head(t) = 0, onda je head(t + 1) := head(t).
Ako je Δ(t)2 = ☞, onda je head(t + 1) := head(t) + 1

Za svaki "t ∈ N" vrijedi funkcija "n tape(t, n) niz u Γ." Za taj niz je važno to što "t = 0" zadaje korisnik (nije posljedica rada samog Turingovog stroja). Preciznije rečeno, korisnik, počevši od nulte ćelije trake, upisuje neku riječ ili prazninu nad samom ulaznom abecedom (Σ) dok je ostatak trake popunjen bjelinama. Ta riječ upisana u traku je ulaz i nakon što ga Turingov stroj primi započinje s radom u uvijek istim početnim uvjetima, od prvog takta nadalje. Ti početni uvjeti su: "state(t + 1) := Δ(t)0" i "tape(t + 1, head(t)) := Δ(t)1".
Stroj se zaustavlja ako je ispunjen uvjet "state(t) ∈ F" i na traci dobivamo izlaz. U suprotnom moramo uvesti funkciju "Δ(t) := δ(state(t), symb(t))." Ako pretpostavimo da je u funkciji "Δ" determinanta "t" onda komponente "Δ(t)" označavamo kao Δ(t)0, Δ(t)1 i Δ(t)2... s tim da se mora paziti da se poštuju pravila prijelaza: "state(t + 1) := Δ(t)0" i "tape(t + 1, head(t)) := Δ(t)1" i pravila prijelaza za glavu gdje imamo tri slučaja. Ako je Δ(t)2 = ☜ i head(t) > 0, onda je head(t + 1) := head(t) − 1; ako je Δ(t)2 = □ ili ako je Δ(t)2 = ☜ i head(t) = 0, onda je head(t + 1) := head(t); te ako je Δ(t)2 = ☞, onda je head(t + 1) := head(t) + 1.
Ukoliko funkcija prijelaza (δ) nije definirana za odgovarajući par stanja i simbola onda nije ni determinanta (Δ) definirana za "t". Zbog toga, Turingov stroj više nikada ne može stati jer njegovo ponašanje više nije specifično. U tom slučaju, Turingov stroj ulazi u beskonačnu petlju koju ne može prekinuti, a konfiguracija mu cijelo vrijeme ostaje nepromijenjena ("cfg(t) = cfg(t + 1)"). 
Turingov stroj konstantno očitava stanje i trenutačni simbol (onaj iznad kojeg se nalazi glava u tom trenutku) te ovisno o njima i funkciji prijelaza prelazi u novo stanje i piše novi simbol na mjesto starog te pomiče glavu (u lijevo, ostaje na mjestu ili u desno). Postoji i nekoliko specifičnih slučajeva kao na primjer kada se glava treba pomaknuti u lijevo, a već se nalazi u nultoj ćeliji. Tada se glava ne pomiče, a taj slučaj se smatra neizvršivim. To se može izbjeći korištenjem specijalnog ulaznog simbola, odnosno 'markera' početne trake i svih pravila zadavanja Turingovog stroja.

**Zadavanje determinističkog Turingovog stroja**
Zadavanje samog Turingovog stroja najjednostavnije je objasniti na primjeru. Ako kažemo da je funkcija prijelaza (δ) za Turingov stroj zapravo njegov program, možemo reći i da je onda svaki Turingov stroj zapravo evaluator svojeg programa/prijelazne funkcije. Ako kažemo da je programiranje djelatnost pisanja samog programa, možemo započeti s primjerom programiranja Turingovih strojeva. Kao primjer, uzet ćemo Turingov stroj koji ulazni broj u binarnom zapisu povećava za 1 tako što počne od najmanje značajnog bita. Svako od tih povećavanja se svodi na zadavanje svih komponenti (prije spomenute sedmorke) od kojih je najvažnija funkcija prijelaza (δ).

Turingov stroj za povećanje binarnog broja
Q = { sˇ0, sˇ1, sˇ2} δ(s0, _) = (s2, _, □)
Σ = { 0, 1 }        δ(s0, 0) = (s0, 1, ☞)
Γ = Σ ∪ { _ }       δ(s0, 1) = (s1, 0, ☞)
s = s0              δ(s1, _) = (s2, 1, □)
F = { sˇ2 }         δ(s1, 0) = (s0, 1, ☞)
                    δ(s1, 1) = (s1, 0, ☞)"
                   
Desni stupac sadrži tablično zadanu funkciju prijelaza prikazanu na slijedećoj slici:
![](data:image/png;base64,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)
Ova tablična funkcija na slici je prikazana pomoću usmjerenog označenog grafa. Čvorovi tog grafa (s0; s1; s2) predstavljaju stanja Turingovog stroja. Strelica lijevo na slici označava početno stanje bez izvora, a završno je zaokruženo dva puta. Bridovi (preostale strelice) prikazuju moguće tranzicije među stanjima (s0; s1; s2). Oni su označeni s tri vrijednosti koje se na njih odnose, a to su trenutačni simbol, novi simbol koji će biti zapisan na njegovom mjestu i pomak glave.
Ukoliko poznajemo opis nekog stroja i neku njegovu (bilo koju) konfiguraciju možemo uvijek nastaviti njegov rad, no samo ta dva podata nisu dovoljna za znanje o globalnom ponašanju bilo koje od njegovih funkcija (tape, head i cfg).

**Varijante**
1. Turingovi strojevi s neograničenom trakom s lijeva

Turingovi strojevi najčešće su 'prošireni' tako da je njihova traka neograničena s lijeva, što znači da je funkcija trake "tape' : N × Z → Γ" sve dok su vrijednosti head-a u obliku cijelih brojeva. To možemo postići tako da napravimo neki Turingov stroj M koji ima poluomeđenu traku, odnosno da ulazni alfabet proširimo s posebnim markerom koji se upisuje isključivo u nultu ćeliju. Zbog toga moramo definirati i novi skup stanja. Njega definiramo s "Q" = Q × { 1-, 0-, 0+, 1+ }".
Takav Turingov stroj M koristi parne ćelije za nenegaivne ćelije polazne trake, a neparne ćelije koristi za negativne. Glava se pomiče ili za dva mjesta lijevo ili desno ili ostaje na mjestu. Tako obilazi samo parne ili samo neparne ćelije. Ovakav Turingov stroj ima i dvije posebne oznake za svako stanje, a te oznake se sastoje od dva simbola. Svrha prvog simbola je pomicanje glave za dva mjesta i govori koliko se još mjesta mora pomaknuti. To može biti 1 ili 0 mjesta. Drugi simbol očitava nalazimo li se u pozitivnoj (+) ili negativnoj (-) ćeliji.
Do samog prijelaza s parnih (nenegativnih) na neparne (negativne) ćelije dolazi točno u onom trenutku kada se glava treba pomaknuti ulijevo s nulte ćelije. Pomaci polaznog stroja lijevo i desno (dok se nalazi na negativnom dijelu trake) mijenjaju smijer u novom Turingovom stroju M. Čak i uz ovakve modifikacije polazne relacije prijelaza lako se potvrdi da novi stroj M staje u isto vrijeme t daje isti rezultat kao i početni Turingov stroj.
2. Turingovi strojevi s više traka

Iako Turingovi strojevi mogu imati više traka to ne znači da su oni nužno i moćniji. Svaka od tih traka mora imati svoju pomičnu glavu koja je u potpunosti neovisna o drugim glavama. S obzirom na to da se smatra da jednom kada Turingov stroj počne raditi, nakon što se prva traka iskoristi za ulaz, ne smije se više mijenjati. Zbog toga se višetračni Turingovi strojevi mogu simulirati jednotračnim koji ima jednu neograničenu stranu (u pravilu desnu).

3. Turingovi strojevi s dvočlanim skupom završnih stanja

Postoji poseban i važan slučaj kada je skup završnih stanja Turingovih strojeva dvočlan (F = {A, R}). Kod tog skupa završnih stanja A je stanje prihvaćanja, a R je stanje odbacivanja. Sam korisnik ovisno o završnom stanju zaključuje prihvaća li takav Turingov stroj input (ulaznu riječ) ili ga ne prihvaća jer je stroj završio u stanju odbacivanja.
Ako pretpostavimo da postoji neki proizvoljni Turingov stroj M s takvim skupom završnih stanja i ako neki jezik "L(M)" definiramo kao skup svih riječi nad konačnim laznim alfabetom (Σ) koji taj stroj prihvaća dolazimo do sljedećih definicija jezika za Turingove strojeve.

"Za jezik L nad alfabetom Σ kažemo da je rekurzivan ili Turing-odlučiv, ako postoji
Turingov stroj M s ulaznim alfabetom Σ koji ulaznu riječ w nad Σ prihvaća točno kad je
w ∈ L, a u suprotnom je odbacuje. Kraće rečeno, M odlučuje jezik L, tj. L = L(M)."

"Za jezik L nad alfabetom Σ kažemo da je rekurzivno prebrojiv ili Turing-prepoznatljiv,
ako postoji Turingov stroj M' s ulaznim alfabetom Σ, koji ulaznu riječ w nad Σ prihvaća točno
kad je w ∈ L, a u suprotnom je ili odbacuje ili nikada ne staje. Kraće rečeno, M' prepoznaje
jezik L"

Dolazimo i do zaključka da je svaki rekurzivni jezik rekurzivno prebrojiv, no svaki rekurzivno prebrojiv jezik nije rekurzivan. Ako uzmemo da je L neki rezurzivno prebrojiv jezik nad ulaznim alfabetom "Σ" koji neki Turingov stroj M prepoznaje, možemo konstruirati Turingov stroj E (E = enumerator) koji ispisuje sve riječi iz jezika L. Turingov stroj E započinje rad s praznom trakom i generira sve riječi nad ulaznim alfabetom (Σ). Budući da je ulazni alfabet (Σ) konačan to je uvijek moguće i može se dobro urediti, zbog čega možemo na primjer generirati riječi u leksičkom poretku. To bi napravili tako da Turingov stroj E za i-tu riječ stavlja redom sve riječi do i uključujući i-tu na ulaz Turingovog stroja M tako da na svakom ulazu simulira najviše "i" koraka. Ukoliko Turingov stroj M prihvati riječ, Turingov stroj E ju zatim ispisuje. Na taj način Turingov stroj E testira sve riječi nad ulaznim alfabetom (Σ) za svako moguće konačno izvršavanje Turingovog stroja M. Na taj način enumerira sam jezik L.
S druge strane, ukoliko postoji enumerator za neki jezik, možemo napraviti neki Turingov stroj koji uspoređuje dani ulaz s enumeriranim riječima i traži poklapanje. Ako nađe poklapanje, prihvaća ga.
### Nedeterministički Turingov stroj
Za razliku od dererminističkih Turingovih strojeva koji funkcioniraju kao kombinirana akcija na više traka, nedeterministički Turingov stroj funkcionira kao masivno i paralelno računalo s kompleksnijim i moćnijim sustavom od sekvencijalnog koje predstavlja deterministički Turingov stroj.
Nedeterministički Turingov stroj se od determinističkog razlikuje po funkciji prijelaza i
završnim stanjima koja slijede princip podjele na prihvaćujuće (A) i odbacujuće (R). Neka je s
PS(X) označen partitivni skup skupa X, tada je nedeterministička funkcija prijelaza oblika:
δ : (Q \ {A,R}) × Γ → PS(Q × Γ × {☜, □, ☞})."
Nedeterministički Turingov stroj funkcionira tako da za svako stanje i simbol postoji skup akcija koje će uslijediti, a svaka od njih prevodi stroj u novo stanje, zapisuje novi simbol na traku i pomiče glavu. To se odvija potpuno neovisno, no i istodobno s drugim takvim akcijama. 
Njegov rad odgovara standardonj POSIX semantici fork(2) sistemskog poziva. Svako njegovo izračunavanje na danom ulazu je možda konačan niz konfiguracija indeksiranih taktom. To izračunavanje nedetermanističkkog Turingovog stroja je stablo koje je možda konačno, čiji su nivoi također indeksirani taktom. Na svakom od tih nivoa sadržan je skup trenutačnih konfiguracija, s time da svaka konfiguracija ne može imati više od "p := |Q × Γ × {☜, □, ☞}|" potomaka. Korijen tog stabla sačinjen je od početne konfiguracije. Maksimalni putovi u stablu predstavljaju jedno moguće determinističko izračunavanje na nekom danom ulazu. Oni koji započinju korijenom ne mogu se nastaviti ako i samo ako je dostiguto jedno od završnih stanja. Konačan maksimalni put terminira izvršavanje, što znači da nedetermanistički Turingov stroj prihvaća ulaz samo ako postoji barem jedno terminističko izvršavanje. Ukoliko su sva izračunavanja terminirajuća i ako je njihov rezultat stajanje, ulaz se odbacuje.
Svaki turingov stroj je nedeterministički, no svaki nedeterministički Turingov stroj ne može se simulirati determinističkim Turingovim strojem.
### Univerzalni Turingov stroj
Turing je na pitanje može li postojati neki stroj koji može simulirati svaki drugi Turingov stroj odgovorio:
"Postoji Turingov stroj U takav da za svaki Turingov stroj M i bilo koju riječ w nad njegovom
abecedom vrijedi: stroj U s ulazom〈(M, w)〉se zaustavlja ako i samo ako se zaustavlja stroj M s ulazom w i pritom oba stroja daju isti izlaz. Za U kažemo da je univerzalni Turingov stroj."
Univerzalni Turingov stroj smatra se izuzetno bitnim jer može izračunati svaku Turing-izračunljivu funkciju, odlučiti svaki rekurzivan jezik i prepoznati svaki rekurzivno prebrojiv jezik.
### Primjer Halting problema u Turingovom stroju
"Black box problem" funkcionira na principu Turingovog stroja koji u sebe prima neki ulaz i nakon toga određuje hoće li program, ovisno o danom ulazu, biti konačan ili će se izvoditi beskonačno. Ukoliko se utvrdi da će program završiti, Turingov stroj izbaci odgovor "da" i izvodi se beskonačno, a u suprotnom kada se utvrdi da će se program izvoditi beskonačno dobiva se odgovor "ne" i rad Turingovog stroja prestaje. To dovodi do paradoksa i samog "Halting problema".

**Ulaz** --> String po našem izboru
**Problem** --> Završava li se program u konačnom broju koraka?
**Rješenje**
Pretpostavimo da postoji Turingov stroj koji je namijenjen rješavanju problema koji smo zadali tako da vraća samo odgovor "da" ili "ne" ovisno o tome hoće li završiti u konačnom broju koraka. 

Ukoliko vrati "da" program se zaustavlja, a u suprotnom se izvodi beskonačno. To je prikazano na slici ispod.
![Slikovni prikaz](https://www.tutorialspoint.com/automata_theory/images/halting_machine.jpg)

Inverzni Turingov stroj postavlja se tako da ukoliko Turingov stroj ima konačan broj koraka za neki ulaz, stvara se beskonačna petlja, a ukoliko se program izvodi beskonačno Turingov stroj prestaje s radom. 
![Slikovni prikaz](https://www.tutorialspoint.com/automata_theory/images/inverted_halting_machine.jpg)
Zbog toga dolazi do kontradikcije i pitanja "Je li halting problem rješiv?". S obzirom na to da dolazi do paradoksa, zaključak je da je naša pretpostavka bila pogrešna. To nas dovodi do spoznaje da ne postoji stroj ili program koji može riješiti halting problem.
### Rješenje Halting problema 
Važno pitanje koje se postavlja u terminima Halting problema glasi može li se stvoriti algoritam koji će moći utvrditi hoće li se neki program zaustaviti ili ne. Halting problem u Turingovom stroju je pitanje može li se stvoriti algoritam koji će moći utvrditi hoće li zadani program uvijek završiti. Odgovor na oba pitanja je ne. Ne postoji opći algoritam koji može točno predvidjeti hoće li se neki program završiti ili će „zaglaviti“ u beskonačnoj petlji. 
Pretpostavimo da postoji stroj HM (P,I), gdje HM predstavlja stroj za zaustavljanje, P program, a I input, odnosno ulaz. Nakon što stroj primi oba ulaza, njegov će izlaz biti odgovor na pitanje hoće li se program P zaustaviti ili ne. Zatim zamislimo obrnuti stroj za zaustavljanje (IM) koji će uzeti program P kao ulaz i zauvijek se ponavljati ako HM vrati „da“, a zaustaviti ako HM vrati „ne“. Situacija u kojoj se IM prosljeđuje IM kao njezin ulaz, dovodi do kontradikcije. Nemoguće je da se vanjska funkcija zaustavi ako je njezina unutarnja funkcija u petlji, a isto tako je nemoguće da se vanjska funkcija zaustavi čak i ako se njezina unutarnja funkcija zaustavlja. U oba slučaja IM se ne zaustavlja, stoga možemo zaključiti da problem zaustavljanja nema rješenja.
![](https://files.codingninjas.in/article_images/halting-problem-in-the-theory-of-computation-1-1646145223.jpg)
![](https://files.codingninjas.in/article_images/halting-problem-in-the-theory-of-computation-2-1646145224.jpg)
![](https://files.codingninjas.in/article_images/halting-problem-in-the-theory-of-computation-3-1646145224.jpg)
## Dokaz Halting problema
``` py
def halting_oracle(f, input):
    # Pretpostavimo da ova funkcija može riješiti problem zaustavljanja.
    result = f(input)
    if result == "halt":
        return True
    else:
        return False

def paradoxical_program(halt_oracle):
    # Definira paradoks
    def g(input):
        if halt_oracle(g, input):
            #  Ako se g zaustavi na ulazu, ući će u beskonačnu petlju.
            while True:
                pass
        else:
            # Ako se g ne zaustavi na ulazu, zaustavit će se.
            return "halt"
    return g

def main():
    halt_oracle = halting_oracle
    paradox = paradoxical_program(halt_oracle)
    result = halt_oracle(paradox, paradox)
    # Ovo dovodi do kontradikcije jer rezultat mora biti ili True ili False.
    # Rezultat True dovodi do beskonačne petlje.
    # Rezultat false dovodi do zaustavljanja.
    # Pretpostavka da halting_oracle može riješiti problem zaustavljanja je netočna.

if __name__ == "__main__":
    main()
```
## Utjecaj na razvoj softvera
Definirali smo da je halting problem teorijski problem koji se odnosi na algoritamsko određivanje je li zadani program i ulaz izvršiv te došli do zaključka da ovaj problem nije rješiv u općenitim slučajevima. On je važan za razumijevanje algoritma i ograničenja samog računala, što dovodi do razvoja softvera u mnogim područjima informatike i računalstva.
### Sigurnost softvera
Zbog nemogućnosti određivanja hoće li se program zaustaviti, mogući su propusti i pogreške u kodu koje mogu dovesti do beskonačnog izvođenja programa. To je dovelo do razvoja raznih tehnika i alata za provjeru sigurnosti softvera kao što su formalna verifikacija, odnosno proces provjere ispravnosti softverskog sustava u odnosu na određenu specifikaciju te statička analiza koda koja podrazumijeva proces automatske analize koda bez pokretanja programa kako bi se otkrile potencijalne greške.
### Interakcija s UI
UI je korisničko sučelje, gdje dolazi do interakcije čovjeka i računala. Interakcija s UI posebno je važna za rad softvera i programa. Problem zaustavljanja utječe na komunikaciju s korisničkim sučeljem, zbog čega je važno da programi imaju opciju za prekid ili zaustavljanje. Ove opcije omogućuju kontrolu nad izvedbom i prekidom programa u slučaju grešaka, što se smatra iznimno bitnim za održavanje i stabilnost softvera.
### Automatizacija testiranja
Automatizacija testiranja je proces korištenja tehnika testiranja softvera ili programa bez interakcije s korisničkim sučeljem. Te tehnike stvorene su za testiranje funkcionalnosti i sigurnosti softvera. Njezin je cilj osiguravanje učinkovitog funkcioniranja programa te otkrivanje i uklanjanje pogrešaka prije pokretanja programa.
### Istraživanja
Halting problem mnogima je postao motivacija za razvijanje novih tehnika i alata za provjeravanje i analiziranje softvera. Takvi novi pristupi omogućavaju razvoj sigurnijeg i pouzdanijeg softvera. Jedan od njih je prethodno spomenuta automatizacija testiranja koja omogućava brže testiranje softvera te dovodi do softvera koji je bolji i sigurniji. Nove tehnike omogućavaju razvoj složenijih aplikacija što dovodi do općenitog razvoja računalne tehnologije.