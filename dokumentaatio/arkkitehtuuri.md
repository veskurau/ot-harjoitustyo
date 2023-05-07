# Arkkitehtuurikuvaus

## Rakenne ja sovelluslogiikka

Pakkausrakenteessa on seuraavat tasot:
- ui: vastaa käyttöliittymästä
- service: vastaa sovelluslogiikasta
- repositories: vastaa tietojen pysyväistallennuksesta
- entities: sisältää pelaajia ja kysymyksiä kuvaavat luokat

Käyttöliittymästä vastaa UI-luokka. Käyttöliittymä tarjoaa askelia käyttäjälle. Alussa kysytään haluaako pelaaja pelaaja aloittaa pelin, jonka jälkeen pyydetään pelaajien määrä ja nimet. Tämän jälkeen käyttöliittymä esittää pelaajille kysymyksiä ja ottaa vastaan heidän vastauksensa. 

Sovelluslogiikka on toteutettu pääosin GameService-luokassa. Käyttöliittymästä kutsutaan GameService-luokan metodeja. GameServicen kautta voidaan muun muassa: 
- lisätä pelaajia peliin ja tietokantaan
- pitää yllä pelissä olevia pelaajia, heidän oikeita vastauksia ja pistetilannetta
- antaa tieto pistetilanteesta
- pelin päättyessä tallentaa tieto voittajasta tietokantaan

![Pakkausrakenne ja luokat](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Tietojen pysyväistallennus

Pakkauksen repositories-luokat ovat vastuussa tietojen tallennuksesta. QuestionRepository vastaa pelin kysymyksien hallinnasta. Kysymyksiä säilytetään csv-tiedostossa. PlayerRepository vastaa pelin pelaajien hallinnasta. Pelaajien tietoja säilytetään SQLite-tietokannassa. 

### Tiedostot

Tieto kysymyksistä tallennetaan csv-tiedostoon, oletuksena data-kansiossa sijaitseva questions.csv -tiedosto. Juuressa sijaitsevaan .env-tiedostoon on merkitty tiedostojen nimet. 

Tiedot on tallennettu csv-tiedostoon seuraavassa muodossa:
Kategoria;Kysymys;Vastausvaihtoehto1;Vastausvaihtoehto2;Vastausvaihtoehto3;Vastausvaihtoehto4;Oikea vastaus numerona

Esimerkiksi: 
Maantiede;Mikä on Australian pääkaupunki?;Melbourne;Canberra;Sydney;Brisbane;2

Vastausvaihtoehtoja voi periaatteessa olla kuinka monta tahansa, mutta käytännössä niitä on 2-4.


Vastaavasti tieto pelaajista tallennetaan SQLite-tietokannan tauluun Players, josta löytyvät sarakkeet name ja wins. Juuressa sijaitsevasta .env-tiedostosta löytyy tiedoston nimi. Tietokannan alustus tehdään initialize_database.py -tiedoston kautta. Yhteyden muodostamiseen tarvittavat tiedot on tallennettu databa_connection.py -tiedostoon.

## Päätoiminnallisuudet

### Kysymysten haku

Ohjelman käynnistyessä GameService hakee kaikki kysymykset tietokannasta. Kysymykset tallennettaan Question-olioina listaan. Käyttöliittymästä kutsutaan sitten get_question-metodilla yksittäisiä kysymyksiä, jotka esitetään pelaajalle. 

![Sekvenssikaavio-kysymyksen-haku](./kuvat/arkkitehtuuri-sekvenssi-kysymyksen-haku.png)

### Pelaajien lisääminen

Pelin alussa käyttöliittymä pyytää pelaajien nimet. Käyttöliittymä kutsuu GameService-luokan metodia add_player. Pelaajan nimi lisätään mukaan nykyiseen peliin, josta GameService pitää kirjaa. Mikäli pelaajaa ei löydy tietokannasta, niin GameService lisää pelaajan kutsumalla PlayerRepository-luokan metodia create(name). Mikäli saman niminen pelaaja yritetään lisätä samaan peliin, niin toinen saman nimisistä jätetään huomioimatta. 

### Pelin päättyminen

Käyttöliittymä kutsuu jokaisella kierroksella GameServicen metodia someone_has_full_score. Mikäli metodi palauttaa arvon True, niin jollain pelaajalla on täydet 6/6 pistettä ja hän on voittanut pelin. Käyttöliittymä tulostaa käyttäjälle tiedon voitosta. Samalla GameService kutsuu PlayerRepository-luokan metodia add_win(name), joka lisää tietokantaan kyseiselle pelaajalle +1 wins sarakkeeseen. 

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Sovelluksen tekstikäyttöliittymä on melko karkea, graafinen käyttöliittymä toisi peliin lisämukavuutta. Käyttöliittymä on nyt toteutettu yhden tiedoston ja luokan sisään. Tässä olisi voinut olla mahdollista eriyttää koodia vielä erillisiin tiedostoihin/luokkiin. Koodi sisältää paikoittain myös melko paljon silmukoita ja ehtolauseita, näidenkin osalta koodia olisi voinut selkeyttää ja eriyttää toiminnallisuusksia vielä enemmän omien metodien alle. 