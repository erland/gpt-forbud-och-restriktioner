# OpenAI Plugin Runtime Policy

OpenAI Plugin är en peer runtime som byggs från samma canonical projektkontrakt som övriga distributioner.

## Grundregler

1. Canonical instruktioner ska kompileras till en eller flera skills.
2. Plugin-specifik metadata ska genereras från canonical projektdata.
3. Knowledge och andra resurser ska klassificeras för plugin-runtime som instruktioner, references, assets eller runtime-relevanta scripts.
4. Runtime-specifika filer får inte bli nya canonical sanningskällor när motsvarande information redan finns i projektkontraktet.
5. Pluginpaketet ska vara deterministiskt byggbart.

## Paketgränser

Pluginpaketet får inte innehålla utvecklings- eller historikmaterial som inte behövs vid körning.

Följande ska exkluderas:

- tests/
- evals/
- research/
- .github/
- .git/
- build/
- dist/
- lokala cache- och temporärfiler

## Scripts

Scripts får endast inkluderas när de faktiskt behövs av plugin-runtime.

Att ett script finns i canonical projektet innebär inte automatiskt att det ska distribueras med pluginet.

När scripts distribueras ska plugin-adaptern deklarera sitt code-execution-behov explicit i
runtime-kontraktet och genererad `SKILL.md` ska instruera hosten att använda kompatibel
code execution när den finns. Obligatoriska script-tools ska göra code execution
`required`; blockerande canonical fallback ska bevaras som `block`.

En script-resurs och ett MCP-tool är olika integrationsformer. Avsaknad av MCP-wrapper får
inte ensam användas som skäl för att markera script-resursen som reducerad.

## Skills

Varje distribuerad skill ska ha ett giltigt `SKILL.md` med minst:

- name
- description

Skillstruktur ska härledas från canonical projektdata och inte dupliceras som separat handunderhållen runtimekonfiguration.

## Version 1-avgränsning

Plugin v1 är skills-first.

Följande ingår inte i v1:

- generering av MCP-serverkod
- avancerad MCP-konfiguration
- ChatGPT UI-komponenter
- lifecycle hooks
- plugin marketplace
- automatisk publicering till Plugin Directory

Dessa funktioner ska endast införas när ett konkret use case motiverar dem.

## State och workspace

Plugin ska inte vara beroende av tidigare chatthistorik när canonical workflow och workspace/state-kontraktet redan definierar en annan auktoritativ tillståndskälla.

## Kompatibilitet

Om plugin-runtime inte kan uppnå full funktionell parity med canonical projektkontraktet ska skillnaden dokumenteras i runtime parity och inte döljas genom runtime-specifika specialregler.

## ENG-001 – valfri körmotor

Plugin ska fungera för juridisk analys och PDF-publicering utan separat Engine-ZIP. Bara om ett deklarerat deterministiskt skript verkligen behövs och inte kan köras med redan tillgängliga resurser får assistenten erbjuda den separata Engine-distributionen. Läs alltid aktuell `plugin_version` från installerade Skills och verifiera att samtliga visar samma version. För en publicerad release med versionsnumret `X.Y.Z` ska Engine-artefakten heta `forbud-och-restriktioner-engine-X.Y.Z.zip` under GitHub Release `vX.Y.Z` i `https://github.com/erland/gpt-forbud-och-restriktioner/releases/tag/vX.Y.Z`. Ge en direktlänk till ZIP-filen endast när artefaktens existens har verifierats; annars hänvisa till releasens sida och redovisa att Engine-tillgänglighet inte har fastställts. Hämta aldrig `latest` eller fel version som substitut.

När användaren bifogat Engine-ZIP:en: kontrollera arkivsökvägar, manifest, SHA-256 för varje resurs, versionsidentitet och lämplig exekveringsmiljö innan skript körs. `scripts/selftest.py` kan kontrollera ett säkert extraherat arkiv. Skripten verifierar endast struktur/teknik; de fastställer inte juridisk korrekthet eller aktuell gällande rätt. PDF ska fortfarande kunna produceras via värdmiljöns kompatibla verktyg utan Engine. Misslyckad frivillig Engine-installation får inte blockera vanlig analys.
