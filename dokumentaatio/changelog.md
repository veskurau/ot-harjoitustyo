## Viikko 3

- Lisätty hakemistorakenne
- Lisätty Player-luokka, joka kuvaa pelin pelaajia
- Lisätty testejä Player-luokalle
- Lisätty PlayerRepository-luokka, joka aikanaan tulee vastaamaan käyttäjätietojen tallennuksesta tietokantaan
- Lisätty UI-luokka, joka vastaa käyttöliittymästä käyttäjälle

## Viikko 4
- Lisätty Question-luokka, joka kuvaa pelin kysymyksiä
- Lisätty QuestionRepository-luokka, joka tulee vastaamaan kysymysten tallennuksesta tietokantaan
- Lisätty GameService-luokka, joka vastaa sovelluslogiikasta
- Pylintin käyttöönotto projektissa ja koodin linttaus
- Autopep8 käyttöönotto projektissa ja koodin formatointi
- Paketti- ja luokkakaavion luominen
- Toiminnallisuuksien lisääminen GameService- ja UI-luokkiin
- Ohjelma kysyy kuinka monta pelaajaa pelaa ja luo tämän perusteella Player-oliot

## Viikko 5
- Lisätty ensimmäinen release GitHubiin
- Lisätty konfiguraatio tiedostoja ja otettu dotenv käyttöön
- Kysymykset tallennettu csv-tiedostoon, josta ne voidaan lukea
- Toiminnallisuuksien lisääminen, peli kysyy nyt kysymyksiä pelaajilta
- Ui, service ja entities -luokat päivitetty liittyen kysymyksiin
- Lisätty testejä kysymyksiin liittyvien toiminnallisuuksien osalta
- Koodin laadun tarkatus, formatointi ja linttaus
- Luotu sekvenssikaavio kysymysten hausta ja päivitetty arkkitehtuuri-kuvausta

## Viikko 6
- Lisätty docstring-kommentteja luokille, funktioille ja metodeille
- Kysymysten loppuessa ladataan kysymykset uudestaan tietokannasta
- Tekstikäyttöliittymän luettavuuden parantaminen
- Kysymysten lisääminen tietokantaan
- Lisätty SQLite-tietokantayhteys pelaajien tallentamista varten. Uudet pelaajat lisätään automaattisesti tietokantaan, pelaajan voittaessa tietokantaan päivitetään hänen voittojen määrä
- Uusien testien luominen ja vanhojen päivitys uusien toiminnallisuuksien osalta, kuten SQLite-tietokannan toiminta
- Dokumentaation päivitys, arkkitehtuurikuvauksen laajentaminen ja käyttöohjeiden lisäys
- Koodin laadun tarkastus
- Uusin release
