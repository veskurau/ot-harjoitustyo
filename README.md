# Ohjelmistotekniikka, harjoitustyö

Tietovisasovellus, jossa pelaaja heittää noppaa ja saa silmäluvun perusteella jonkun aihealueen kysymyksen. Kaikkiin aihealueisiin oikein vastannut pelaaja voittaa pelin. 


## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Release: Viikon 5 deadline](https://github.com/veskurau/ot-harjoitustyo/releases/tag/viikko5)

## Komentorivitoiminnot

Riippuvuuksien asentaminen:

```bash
poetry install
```


Ohjelman suorittaminen:

```bash
poetry run invoke start
```


Testien ajo:

```bash
poetry run invoke test
```


Testikattavuusraportin luonti:

```bash
poetry run invoke coverage-report
```


Pylint:

```bash
poetry run invoke lint
```
