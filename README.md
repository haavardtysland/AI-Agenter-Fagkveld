# NK25 AI Agent Kurs

En enkel agent som foreslår aktiviteter basert på vær og lokasjon. Viser et typisk AI-agentmønster: systemprompt + funksjonsverktøy.

## 🚀 Kom i gang

### 1. Laste ned nødvendige pakker
```bash
pip install -r requirements.txt
```
eller
```bash
pip3 install -r requirements.txt
```
### 2. Sette opp miljøvariabler
1. Lag en fil som heter `.env` i roten av prosjektet
2. Sett opp følgende miljøvariabler
```
AZURE_OPENAI_API_KEY=denne får dere av meg på kurset
AZURE_OPENAI_ENDPOINT=https://nk-kurs-service.cognitiveservices.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4.1-mini
```

## 💬 Eksempel

```
📝 'Aktiviteter i Tromsø kl 17:00?'
📞 search_location → Tromsø
📞 get_weather(lat, lon, location_name="Tromsø", time_iso="2025-06-13T15:00:00Z")
📞 get_foursquare_categories()
📞 get_activities(lat, lon, categories="...")
💬 ...
```
