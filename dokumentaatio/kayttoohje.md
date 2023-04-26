# Käyttöohje

Viimeisimmän version ohjelmasta löydät [täältä](https://github.com/veskurau/ot-harjoitustyo/releases)

## Konfiguraatiot

Pysyväistallennukseen liittyvien tiedostojen nimiä voidaan tarvittaessa muokata juuressa sijaitsevasta .env-tiedostossa. Jos tiedostoja ei löydy, ne luodaan alustuksen yhteydessä. 

## Ohjelman käynnistäminen

Ensimmäisellä käynnistyskerralla: 

1) Asenna ohjelman riippuvuudet:

```bash
poetry install
```

2) Pelaaja-tietokannan alustaminen (luo database.sqlite-tiedoston data-kansioon) 

Huom: Jos olet jo pelannut peliä ja tietoja on tallennettu database.sqlite-tiedostoon, niin tämä komento pyyhkii aiemmat tiedot

```bash
poetry run invoke build
```


Ohjelman suorittaminen kommennolla:

```bash
poetry run invoke start
```

## Pelin aloitus

Sinua pyydetään joko aloittamaan peli tai lisäämään kysymyksiä. Jos haluat pelaamaan, valitse aloita peli -vaihtoehto. Omia kysymyksiä voi lisätä toisesta vaihtoehdosta. 

## Pelaajien lisääminen

Valitse kuinka monta pelaajaa haluaa pelata (1-5). Anna tämän jälkeen pelaajille nimet. Ohjelma tulostaa myös aiemmin lisätyt pelaajat ja heidän voittojensa määrän. Jos haluat jatkaa samalla pelaajalla pelaamista, niin kirjoita vain kyseisen pelaajan nimi. Mikäli pelaajaa ei löydy tulostettavalta listalta, hänet lisätään sinne ja seuraavalla pelikerralla hänen nimensä löytyy listalta. 

## Pelin kulku

Ohjelma esittää pelaajalle kysymyksiä ja pelaajan pitää valita oikea vastaus numerona. 
Mikäli pelaaja vastaa kysymykseen oikein, niin hän saa jatkaa vuoroaan. Kun pelaaja vastaa uuteen aihealueeseen oikein, niin aihealue lisätään pelaajan tietoihin. Aihealueita on kahdeksan: maantiede, viihde, historia ja yhteiskunta, kirjallisuus ja taide, luonto ja tiede sekä urheilu ja vapaa-aika. 

Kun koko kierros on käyty läpi, niin ohjelma näyttää mihin aihealueisiin kukin pelaaja on vastannut oikein. Se pelaaja joka ensin vastaa kaikkiin kahdeksaan aihealueeseen oikein, hän voittaa pelin. Hänen tietoihinsa lisätään myös yksi voitto lisää, joka näkyy seuraavan kerran kun aloitetaan uusi peli. 

