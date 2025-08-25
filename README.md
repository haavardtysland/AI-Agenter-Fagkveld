# NK25 AI Agent Kurs

En enkel agent som foreslår aktiviteter basert på vær og lokasjon. Viser et typisk AI-agentmønster: systemprompt + funksjonsverktøy.

## 🚀 Kom i gang

#### 1. Klon ned prosjektet

`git clone https://github.com/haavardtysland/NK25-AI-Agent-Kurs.git`

#### 2. Laste ned nødvendige pakker

Skriv `pip install -r requirements.txt` i terminalen

#### 3. Sette opp miljøvariabler

1. Lag en fil som heter `.env` i roten av prosjektet
2. Sett opp følgende miljøvariabler

```
AZURE_OPENAI_API_KEY=denne får dere av meg på kurset
AZURE_OPENAI_ENDPOINT=https://nk-kurs-service.cognitiveservices.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4.1-mini
```

#### 4. Kjøre agenten

1. Skriv `python agent.py` i terminalen
2. Spør "Hvem er favorittpersonen din?"

## Oppgaver

### 1. Bli kjent med oppsettet

 1. Lag en ny branch ved å skrive `git checkout -b oppgave-1` 
 2. Gjør det slik at agenten kun svarer på spørsmål om favorittpersonen sin
 3. Lag et nytt function tool som sier hva favoritthobbyen til personen er
 4. Lag et function tool som gir deg en tilfeldig vits. Bruk dette gratis API-et `https://official-joke-api.appspot.com/random_joke`. Tips: bruk requests pakken
 5. Hmm.. disse vitsene funket ikke like bra på norsk. Få agenten til å gi de på originalspråket.
 6. Commit endringene dine i branchen ved å skrive `git add .` og `git commit -m "oppgave 1 var veldig gøy"`
 
### 2. Cocktailplanlegger

I denne oppgaven skal vi lage en agent som kan hjelpe deg med å finne oppskrift på en cocktail basert på ingredienser du har i kjøleskapet.

Vi skal bruke dette gratis API-et for hele oppgaven: `https://www.thecocktaildb.com/api.php?ref=public_apis&utm_medium=website`.

1. Gå tilbake til master branch ved å skrive `git checkout master`.
2. Lag en ny branch for oppgave 2.
3. Lag et nytt function tool som lister alle tilgjengelige ingredienser på API-et. Bruk dette endepunktet: `www.thecocktaildb.com/api/json/v1/1/list.php?i=list`
4. Få agenten til å gjøre alle ingredienser om til snake_case. Det vil da for eksempel si at `Light Rum` blir til `light_rum`. Hint: Gjør endringer i system promptet.
5. Lag et nytt function tool agenten kan bruke til å hente oppskrifter på hver cocktail. Bruk dette endepunktet: `https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}`
6. Få agenten til å foreslå de ulike oppskriftene slik at du kan svare hvilken du vil ha.
7. Lag et nytt function tool slik at agenten kan hente detaljer om cocktailen du har valgt. Bruk dette endepunktet `https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}"`
8. Få agenten til å gi handleliste på ingredienser som mangler, i tillegg til fremgangsmåte på hvordan man lager cocktailen.

### 3. Kreativ frihet 

Velg et gratis API og lag en kul agent utifra det 😎
