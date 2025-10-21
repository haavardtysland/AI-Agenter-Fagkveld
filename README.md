# AI Agenter Fagkveld

En enkel agent ved bruk av function tools. Viser et typisk AI-agentmønster: systemprompt + funksjonsverktøy.

## 🚀 Kom i gang

#### (Valgfri: lag et python environment)

For å unngå å clustere den globale konfigurasjonen kan man lage et environment ved å gjøre følgende:
Lag ved å skrive:
`python -m venv ai_agent_env`, og aktiver med: `source ai_agent_env/bin/activate`

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

### Bli kjent med oppsettet

1.  Lag en ny branch ved å skrive `git checkout -b oppgave-1`
2.  Gjør det slik at agenten kun svarer på spørsmål om favorittpersonen sin. Hint: Gjør endringer i system promptet.
3.  Lag et nytt function tool som sier hva favoritthobbyen til personen er (husk å endre på `__init__.py` i `tools`-mappen for å kunne importere funksjonen). Til videre kan det være lurt å printe noe i starten av hver function tool, så man kan se om agenten faktisk bruker funksjonen.
4.  Lag et function tool som gir deg en tilfeldig vits. Bruk dette gratis API-et `https://official-joke-api.appspot.com/random_joke`. Tips: bruk requests-pakken. Tips 2: Lim inn url'en i en nettleser for å se hvilket format endepunktet returnerer.
5.  Hmm.. disse vitsene funket ikke like bra på norsk. Få agenten til å gi de på originalspråket.
6.  Commit endringene dine i branchen ved å skrive `git add .` og `git commit -m "oppgave 1 var veldig gøy"`.

### Cocktailplanlegger

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

### Planleggeragenten

Denne oppgaven går ut på å få en agent til å planlegge hva den skal gjøre før den starter å gjøre det. Til å løse oppgaven trenger du en agent med noen tools tilgjengelig. Har kan du bruke agenten fra en av de andre oppgavene, eller en annen agent du har laget.

1. Endre systempromptet slik at agenten alltid skal:

   - Først skrive en plan (kort, nummerert).
   - Deretter utføre planen og svare.

2. Test med spørsmål som krever flere steg, for eksempel: “Finn en cocktail med gin, sjekk om jeg har ingrediensene, og si hva jeg må handle.”

Agenten skal da først skrive noe som:

```md
Plan:

1. Finne cocktail med gin.
2. Sammenligne ingredienser.
3. Liste opp manglende.
```

og deretter utføre stegene.

3. Utfordring: Lag et lite verktøy som printer ressoneringen i terminalen før agenten svarer, så man ser hvordan agenten tenker.

### Agent med personlighet

Denne oppgaven går ut på å gi agenten forskjellige personligheter, og få agenten til å kunne endre personlighet dynamisk

1. Legg til en variabel mode i koden med verdier som "formell", "sarkastisk", "entusiastisk".
2. I systempromptet, gi beskjed om å svare med den tonen som mode beskriver.
3. La brukeren endre modus midt i samtalen ved å skrive for eksempel modus: sarkastisk.

### Filagenten

I denne oppgaven skal vi simulere en databasetilkobling ved å bruke lokale filer på PC'en.
Oppgaven krever også at man lager noen enkle .txt-filer i prosjektmappen.

1. Lag et tool read_file(path) som åpner en tekstfil og returnerer innholdet.
2. Lag et tool list_files() som viser alle filer i prosjektmappen.
3. Få agenten til å svare på spørsmål som:

```md
“Hva står det i oppgaver.txt?”
“Finn en fil som inneholder ordet ‘cocktail’.”
```

4. Få agenten til å oppsummere innholdet i filer, i stedet for å skrive alt

### MCP

I denne oppgaven skal vi utvide agentens verktøykasse ved å koble til en MCP-server. Dermed kan agenten bruke tools utenfor vår egen kode.

1. Vi bruker github sin MCP-server. Lag en token i github ved å gå til https://github.com/settings/personal-access-tokens
2. Fyll inn følgende i koden for å aktivere agentens MCP-egenskaper:

```py
  github_mcp = MCPServerStreamableHttp({
            "url": "https://api.githubcopilot.com/mcp/",
            "headers": {"Authorization": f"Bearer {DIN_GITHUB_TOKEN}"}
            })

        await github_mcp.connect()

        agent = Agent(
            name="NK25_AI_Agent_Kurs",
            instructions=get_system_prompt(),
            mcp_servers=[github_mcp],
            tools=[get_favorite_person],
            model=OpenAIChatCompletionsModel(
                model=Config.AZURE_DEPLOYMENT_NAME,
                openai_client=client,
            )
        )
```

3. Få agenten til å liste opp tilgjengelige verktøy
4. Bruk verktøyene. Du kan for eksempel spørre hvilke repoer som inneholder Java-kode.

### Lag en agent fra scratch

I denne oppgaven lager du en minimal agent uten rammeverk – kun med et par kjernefunksjoner og et bittelite “minne”. Målet er å forstå agent-sløyfen: tenk → sjekk tool → utfør → vurder → evt. fortsett.

1. Lag et minimalt “minne” Bruk en liste context = [] for samtaleloggen (prompt + svar). Legg inn max-lengde (f.eks. siste 6 meldinger) for å unngå at den blir for stor.
2. Implementer call_llm(prompt: str) -> str
3. Implementer noen grunn-komponenter som, som think(), check_for_tool(), og evaluate() og execute(), trenger ikke alle med en gang.
4. Få agenten til å kalle på en funksjon via naturlig språk fra en bruker.
5. Prøv å få agenten til å få tilgang til svaret på funksjonskallet, prøv å få den til å tenke videre, osv.

### Kreativ frihet

Velg et API og lag en kul agent utifra det 😎 Her kan du også finne en MCP-server for å gi agenten ekstra funksjonalitet!
