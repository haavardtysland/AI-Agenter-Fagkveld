# 🇳🇴 Norsk Aktivitetsassistent - AI Agent

En enkel agent som foreslår aktiviteter basert på vær og lokasjon. Viser et typisk AI-agentmønster: systemprompt + funksjonsverktøy.

## 🚀 Kom i gang

```bash
pip install -r requirements.txt
export AZURE_OPENAI_API_KEY="din-azure-api-nøkkel"
export AZURE_OPENAI_ENDPOINT="https://din-ressurs.openai.azure.com/"
export AZURE_DEPLOYMENT_NAME="din-modell-deployment-navn"
python agent.py
```

Tillegg for verktøy:

- `FOURSQUARE_API_KEY` for aktivitetsøk.

## 📁 Filstruktur

- `agent.py` – Kjør agenten (Azure OpenAI via Agents SDK)
- `prompt.py` – Systemprompt og atferdsregler
- `config.py` – Konfig for Azure OpenAI
- `tools/` – Verktøy: `location_tool.py`, `weather_tool.py`, `activities_tool.py`, `__init__.py`
- `weather_category_tool.py` – Kategori-IDer for innendørs/utendørs/sport

## 🔧 Kontrakter (funksjonssignaturer)

- `search_location(city_name: str) -> str`
- `get_weather(lat: float, lon: float, location_name: str | None = None, time_iso: str | None = None) -> str`
- `get_foursquare_categories() -> str`
- `get_activities(lat: float, lon: float, query: str = "things to do", categories: str | None = None, limit: int = 5) -> str`

## 💬 Eksempel

```
📝 'Aktiviteter i Tromsø kl 17:00?'
📞 search_location → Tromsø
📞 get_weather(lat, lon, location_name="Tromsø", time_iso="2025-06-13T15:00:00Z")
📞 get_foursquare_categories()
📞 get_activities(lat, lon, categories="...")
💬 ...
```

_Kort, modulært, lett å forstå_ 🎯
