# Ohjelmistotekniikka, harjoitustyö

Tietovisasovellus, jossa pelaajat saa satunnaisesti tietyn aihealueen kysymyksiä. Kaikkiin aihealueisiin oikein vastannut pelaaja voittaa pelin. 


## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Release: Viikon 5 deadline](https://github.com/veskurau/ot-harjoitustyo/releases/tag/viikko5)
- [Release: Viikon 6 deadline](https://github.com/veskurau/ot-harjoitustyo/releases/tag/viikko6)

## Komentorivitoiminnot

### Asennus

Riippuvuuksien asentaminen:

```bash
poetry install
```

Pelaaja-tietokannan alustaminen:

```bash
poetry run invoke build
```

Ohjelman suorittaminen:

```bash
poetry run invoke start
```

### Muut komennot

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
