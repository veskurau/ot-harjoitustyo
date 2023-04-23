# Vaatimusmäärittely

## Sovelluksen tarkoitus

Trivial Pursuit tyyppinen tietovisasovellus. Pelaajat vuorotellen saavat tietyn aihealueen kysymyksen, johon yrittävät vastata oikein. Aihealueita on kahdeksan: maantiede, viihde, historia ja yhteiskunta, kirjallisuus ja taide, luonto ja tiede sekä urheilu ja vapaa-aika. 
Kaikkiin aihealueisiin oikein vastannut pelaaja voittaa pelin. 

## Käyttäjät

Lähtökohtaisesti sovelluksella tulee olemaan vain yhdenlaisia normaaleja käyttäjiä. 
Voidaan kuitenkin harkita tarvitaanko jonkinlainen ylläpitäjän rooli, joka esimerkiksi pystyy lisäämään kysymyksiä.

## Perusversion tarjoama toiminnallisuus

- Luodaan tarvittava rakenne, kuten luokat ym. (tehty)
- Aluksi vain yksi pelaaja pelaa peliä, mutta tavoitteena lisätä myös moninpeli (tehty)
- Tallennetaan tiedot kysymyksistä tiedostoon (tehty)
- Pelaaja saa kysymyksen jostain aihealueesta sekä siihen liittyvät vastausvaihtoehdot (tehty)
- Pelaaja pyrkii valitsemaan oikean vaihtoehdon, jos vastaus on oikein, niin pelaajalle merkitään kyseisestä aihealueesta piste ja hän saa jatkaa. Väärästä vastauksesta ei saa pistettä ja vuoro siirtyy seuraavalle pelaajalle. Jos pelaaja vastaa samaan aihealueeseen oikein, niin hän ei saa enempää pisteitä, mutta saa jatkaa vuoroaan (tehty)
- Kun pelaaja on vastannut kaikkiin aihealueisiin oikein, hän voittaa pelin 
- Tallennetaan tiedot pelaajista SQLite-tietokantaan
- Kysymyksiä voidaan lisätä tietokantaan
- Aloitetaan tekstikäyttöliittymästä, jonka jälkeen tehdään siitä graafinen versio

## Jatkokehitysideoita

- Kirjautuminen joko normaalina käyttäjänä tai pääkäyttäjänä. Pääkäyttäjänä voi esimerkiksi luoda uusia kysymyksiä ja käyttäjiä tietokantaan
- Pelaajilla on yksilölliset tunnukset, joista tallennetaan tiedot ja pelimenestys tietokantaan
- Parannetaan graafista käyttöliittymää esimerkiksi lisäämällä pelilauta ja sillä liikkuvat pelinappulat
- Lisätä jotain muita toiminnallisuuksia peliin, kuten oljenkorret, rosvosektorit yms. 
