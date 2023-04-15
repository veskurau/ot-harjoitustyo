# Vaatimusmäärittely

## Sovelluksen tarkoitus

Trivial Pursuit tyyppinen tietovisasovellus. Pelaajat vuorotellen heittävät noppaa ja saavat tämän perusteella tietyn aihealueen kysymyksen, johon yrittävät vastata oikein. 
Kaikkiin aihealueisiin oikein vastannut pelaaja voittaa pelin. 

## Käyttäjät

Lähtökohtaisesti sovelluksella tulee olemaan vain yhdenlaisia normaaleja käyttäjiä. 
Voidaan kuitenkin harkita tarvitaanko jonkinlainen ylläpitäjän rooli, joka esimerkiksi pystyy lisäämään kysymyksiä.

## Perusversion tarjoama toiminnallisuus

- Luodaan tarvittava rakenne, kuten luokat ym. (tehty)
- Aluksi vain yksi pelaaja pelaa peliä, mutta tavoitteena lisätä myös moninpeli (tehty)
- Tallennetaan tiedot kysymyksistä ja muista tarvittavista tiedoista SQLite tietokantaan
- Aloitetaan tekstikäyttöliittymästä, jonka jälkeen tehdään siitä graafinen versio
- Pelaaja heittää noppaa, jonka perusteella saadaan kysymys jostain aihealueesta sekä siihen liittyvät vastausvaihtoehdot
- Pelaaja pyrkii valitsemaan oikean vaihtoehdon, jos vastaus on oikein, niin pelaajalle merkitään kyseisestä aihealueesta piste ja hän saa heittää noppaa uudestaan, väärästä vastauksesta ei saa pistettä ja vuoro siirtyy seuraavalle pelaajalle (jos sellainen on)
- Kun pelaaja on vastannut kaikkiin aihealueisiin oikein, hän voittaa pelin 
- Kysymyksiä voidaan lisätä tietokantaan

## Jatkokehitysideoita

- Kirjautuminen joko normaalina käyttäjänä tai pääkäyttäjänä. Pääkäyttäjänä voi esimerkiksi luoda uusia kysymyksiä ja käyttäjiä tietokantaan
- Pelaajilla on yksilölliset tunnukset, joista tallennetaan tiedot ja pelimenestys tietokantaan
- Parannetaan graafista käyttöliittymää esimerkiksi lisäämällä pelilauta ja sillä liikkuvat pelinappulat
- Lisätä jotain muita toiminnallisuuksia peliin, kuten oljenkorret, rosvosektorit yms. 
