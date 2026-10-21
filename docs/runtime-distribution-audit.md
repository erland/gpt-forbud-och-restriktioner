# Runtimegranskning efter v0.5.3

## OpenCode – åtgärdat i projektet

`templates/README.opencode.md.tpl` var ärvd från GPT Byggaren och beskrev felaktigt verktyg för GPT-projekt, `projectRoot` och en `.opencode/tools/`-katalog som inte levererades. Ersatt med projektspecifik dokumentation för Förbud och Restriktioner. `tests/test_runtime_docs.py` granskar såväl mallen som den byggda OpenCode-distributionens README. CI kör testet också efter bygget.

## Chat ZIP – identifierad brist i Engine 1.6.26

I `scripts/build_distributions.py` anropar `build_chat()` alltid `bundle_distribution_engine(root, out)`. Den funktionen kopierar byggskript, mallar och `gpt-project.yaml` till `distribution-engine/`, oberoende av:

- `runtime.chat_zip.include` / `exclude`
- att projektet inte deklarerar några körbara runtime-tools (`tools.tools: []`)
- att ingen Skill kräver dessa byggresurser

Därför kan **inte** Chat ZIP göras minimal enbart med en ändring i projektprofilen. Det är en paketeringsfråga i den kanoniska GPT Byggaren-motorn, inte en anledning att redigera dess incheckade originalskript separat i detta projekt.

### Föreslagen motorändring (separat PR i GPT Byggaren)

1. Gör offline-generatorns inclusion villkorad av ett explicit runtimebehov/kontraktsfält och behåll ett särskilt opt-in för GPT:er som faktiskt bygger andra GPT:er.
2. Kopiera endast deklarerade Skill-resurser och runtime-tools (byggskript är inte per automatik runtime-tools).
3. Lägg till två regressionstester: enkel analys-GPT ska sakna `distribution-engine/`; GPT Byggaren ska fortfarande kunna paketera sin byggmotor när behovet är explicit.
4. Uppdatera byggmallar, validator och kompatibilitetsdokumentation samtidigt. Utvärdera förändringen mot alla fem distributioner för att undvika regressioner.

**Nuvarande status:** Chat-paketet innehåller fortsatt `distribution-engine/`. Detta är dokumenterat men **inte korrigerat** i denna projekt-PR. Integritet, funktion och kanonisk byggprocess prioriteras framför en lokal bypass.

## Verifiering och begränsningar

CI kör byggmotorns ordinarie test-, bygg- och distributionsvalidering samt en extra kontroll av OpenCode-README inuti ZIP-filen. Ett lyckat CI-resultat verifierar paketering, inte live-webbsökning, myndighetsjuridik eller PDF-generering i den installerade Plugin-assistenten.
