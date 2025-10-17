# AI Agenter Fagkveld

En enkel agent ved bruk av function tools. Viser et typisk AI-agentmønster: systemprompt + funksjonsverktøy.

## 🚀 Kom i gang

#### 1. Klon ned prosjektet

`git clone https://github.com/haavardtysland/NK25-AI-Agent-Kurs.git`

#### 2. Laste ned nødvendige pakker

Skriv `pip install -r requirements.txt` i terminalen

#### 3. Sette opp miljøvariabler

1. Lag en fil som heter `.env` i roten av prosjektet
2. Sett opp følgende miljøvariabler

```
AZURE_OPENAI_API_KEY={Deles på fagkveld}
AZURE_OPENAI_ENDPOINT=https://fagkveld-foundry.cognitiveservices.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4o
```

#### 4. Kjøre agenten

1. Skriv `python agent.py` i terminalen
2. Spør "Hvem er favorittpersonen din?"
3. Du kan alltid skrive `'q'`,`'exit'`, `'quit'`, `'bye'` eller `'ha det'` for å avslutte samtalen.

## Oppgaver

### 1. Bli kjent med oppsettet

1.  Lag en ny branch ved å skrive `git checkout -b oppgave-1`
2.  Gjør det slik at agenten kun svarer på spørsmål om favorittpersonen sin. Hint: Gjør endringer i system promptet.
3.  Lag et nytt function tool som sier hva favoritthobbyen til personen er (husk å endre på `__init__.py` i `tools`-mappen for å kunne importere funksjonen). Til videre kan det være lurt å printe noe i starten av hver function tool, så man kan se om agenten faktisk bruker funksjonen.
4.  Lag et function tool som gir deg en tilfeldig vits. Bruk dette gratis API-et `https://official-joke-api.appspot.com/random_joke`. Tips: bruk requests-pakken. Tips 2: Lim inn url'en i en nettleser for å se hvilket format endepunktet returnerer.
5.  Hmm.. disse vitsene funket ikke like bra på norsk. Få agenten til å gi de på originalspråket.
6.  Commit endringene dine i branchen ved å skrive `git add .` og `git commit -m "oppgave 1 var veldig gøy"`.

### 2. Cocktailplanlegger

I denne oppgaven skal vi lage en agent som kan hjelpe deg med å finne oppskrift på en cocktail basert på ingredienser du har i kjøleskapet.

Vi skal bruke dette gratis API-et for hele oppgaven: `https://www.thecocktaildb.com/api.php?ref=public_apis&utm_medium=website`.

1. Gå tilbake til master branchen ved å skrive `git checkout master`.
2. Lag en ny branch for oppgave 2.
3. Lag et nytt function tool som gir agenten tilgang til alle ingredienser på API-et. Bruk dette endepunktet: `https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list`.
4. Få agenten til å gjøre alle ingredienser om til `snake_case`. Det vil da for eksempel si at `Light Rum` blir til `light_rum`. Hint: Gjør endringer i system promptet.
5. Lag et nytt function tool agenten kan bruke til å hente mulige cocktails du kan lage, ut ifra en ingrediens du selv har. Bruk dette endepunktet: `https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}`.
6. Få agenten til å foreslå de mulige cocktailsene du kan lage, og spørre deg om hvilken av dem du vil lage.
7. Lag et nytt function tool slik at agenten kan hente detaljer om cocktailen du har valgt. Bruk dette endepunktet `https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}`. Hint: `Ha cocktail_id` som argument i funksjonen.
8. Få agenten til å gi handleliste på ingredienser som mangler, i tillegg til fremgangsmåte på hvordan man lager cocktailen.
9. Commit endringene dine i branchen.

### 3. Kreativ frihet

Velg et gratis API og lag en kul agent utifra det 😎
