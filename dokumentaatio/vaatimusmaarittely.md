# Vaatimusmäärittely

## Sovelluksen tarkoitus

Trivial Pursuit tyyppinen tietovisasovellus. Pelaajat vuorotellen saavat tietyn aihealueen kysymyksen, johon yrittävät vastata oikein. Aihealueita on kuusi: maantiede, viihde, historia ja yhteiskunta, kirjallisuus ja taide, luonto ja tiede sekä urheilu ja vapaa-aika. 
Kaikkiin aihealueisiin oikein vastannut pelaaja voittaa pelin. 

## Käyttäjät

Sovelluksessa on vain yhdenlaisia normaaleja käyttäjiä. 
Voidaan kuitenkin harkita tarvitaanko jatkossa jonkinlainen ylläpitäjän rooli, joka esimerkiksi pystyy hallinnoimaan kysymyksiä tai pelaajia. 

## Perusversion tarjoama toiminnallisuus

- Luodaan selkeä rakenne ohjelmalle, kuten paketit, luokat ym.
- Tallennetaan ja säilytetään tiedot kysymyksistä tiedostoon
- Tallennetaan ja säilytetään tiedot pelaajista SQLite-tietokantaan
- Peliä voi pelata yksin tai yhdessä, kerralla maksimissaan 5 pelaajaa
- Pelaaja saa kysymyksen jostain aihealueesta sekä siihen liittyvät vastausvaihtoehdot
    - Pelaaja pyrkii valitsemaan oikean vaihtoehdon, jos vastaus on oikein, niin pelaajalle merkitään kyseisestä aihealueesta piste ja hän saa jatkaa 
    - Väärästä vastauksesta ei saa pistettä ja vuoro siirtyy seuraavalle pelaajalle 
    - Jos pelaaja vastaa samaan aihealueeseen oikein, niin hän ei saa enempää pisteitä, mutta saa jatkaa vuoroaan
- Kun pelaaja on vastannut kaikkiin aihealueisiin oikein, hän voittaa pelin
- Aloitetaan tekstikäyttöliittymästä, jonka jälkeen tehdään siitä graafinen versio

## Jatkokehitysideoita

- Kysymysten lisääminen tiedostoon pelin sisällä
- Tekstikäyttöliittymän päivittäminen graafiseksi
- Kirjautuminen joko normaalina käyttäjänä tai pääkäyttäjänä. Pääkäyttäjänä voi esimerkiksi luoda uusia kysymyksiä ja käyttäjiä tietokantaan
- Pelaajilla on yksilölliset tunnukset pelkän nimen sijasta, jonka avulla tallennetaan tiedot ja pelimenestys tietokantaan
- Parannetaan graafista käyttöliittymää esimerkiksi lisäämällä pelilauta ja sillä liikkuvat pelinappulat
- Lisätä jotain muita toiminnallisuuksia peliin, kuten oljenkorret, rosvosektorit yms. 
