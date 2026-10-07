# Fælles aner

Et Python-program, der undersøger slægtskab og svarer på spørgsmålet: **Har to personer mindst én fælles ane?** Programmet tegner desuden et stamtræ med matplotlib.

Projektet er udviklet i programmering og følger MVC-arkitekturen.

## Funktioner

- Opretter personer med navn, mor og far (tre generationer)
- Udskriver oplysninger om en person
- Finder alle aner til en person rekursivt
- Finder fælles aner for to personer via `find_common_ancestor()`
- Afgør om to personer er i familie via `is_related()`
- Tegner et stamtræ

## Sådan kører du programmet

Kræver Python 3.10 eller nyere og matplotlib.

1. Klon repoet:
   ```bash
   git clone <link-til-dette-repo>
   cd Project-CommonAncestors
   ```
2. Installér matplotlib:
   ```bash
   pip install matplotlib
   ```
3. Kør programmet:
   ```bash
   python main.py
   ```
4. Kør testene:
   ```bash
   python test_model.py
   ```

## Eksempel på output

```text
Name: Nikolaj, Mother: Anne, Father: Peter
Name: Hans, Mother: Unknown, Father: Unknown
Nikolaj og Sofie: fælles aner = ['Hans', 'Ole', 'Anne', 'Grethe', 'Peter', 'Inge'], i familie = True
Nikolaj og Mads: fælles aner = ['Hans', 'Grethe'], i familie = True
Anne og Jens: fælles aner = [], i familie = False
```

## Filer og opbygning

| Fil | Lag | Ansvar |
|---|---|---|
| `model.py` | Model | Klassen `Person`, `FamilyModel` samt logik: `ancestors()`, `find_common_ancestor()` og `is_related()` |
| `view.py` | View | Klassen `FamilyView`: udskriver tekst og tegner stamtræ |
| `controller.py` | Controller | Klassen `FamilyController`: binder View og Model sammen |
| `main.py` | Start | Opretter familien og starter programmet |
| `test_model.py` | Test | Unittests til modellen |

## Klassediagram

`Person` har en association til sig selv: en person har en mor og en far af typen `Person`.

## Rekursion

`ancestors(person)` finder alle aner ved at tilføje personens forældre og derefter kalde sig selv på hver forælder.

- **Basistilfælde:** En person uden kendte forældre har ingen aner.
- **Rekursivt tilfælde:** Tilføj forælderen, og find forælderens aner.

De fælles aner for to personer findes via fællesmængden (`&`) af deres aner.

## Test

Testene dækker søskende, fætter/kusine, personer uden slægtskab og personer uden forældre (basistilfældet).

```bash
python test_model.py
```

## Arbejdsfordeling

| Navn | Bidrag |
|---|---|
| Atta-ur | Klassen `Person`, stamtræ-visualisering, MVC-struktur og rettelser |
| Tony Ibrahim | Tests, README, klassediagram og opsætning |

## Git-workflow

- `main` som hovedgren
- `refaktorisering-mvc`: omskrivning til MVC
- `feature-tests`: unittests
- Ændringer er merget via Pull Requests

## Forbedringsmuligheder

- Familien er nu hårdkodet i `main.py`, men kan indlæses fra en JSON-fil.
- Programmet finder kun slægtskab via fælles aner (ægtefæller regnes ikke med).
- Attributterne i `Person` kan gøres private med `@property`.
- Viewet kan laves som en grafisk brugerflade (fx Tkinter).

## Deltagere

- Atta-ur
- Tony Ibrahim
- Klasse: 3.O