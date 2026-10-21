# Projektstatus 0.5.4

ZIP är fortsatt utvecklingsspår. GitHub Actions har lagts till som frivillig CI/release-distribution. Workflows anropar originalskripten från GPT Byggaren Engine 1.6.28, kör elva Python-tester, validering och release-readiness. Release-taggen bestämmer artefaktversion. GitHub-körning är ännu inte observerad. Installerat Plugin-E2E återstår; schemalagd bevakning är inte aktiverad.


## Runtimegranskning
OpenCode-mallen korrigerad och regressionskontroll av genererat ZIP-README tillagd. Chat ZIP:s ovillkorligt inkluderade `distribution-engine/` är en känd avvikelse i kanonisk Engine 1.6.26, dokumenterad i `docs/runtime-distribution-audit.md`; motorn är inte modifierad. GitHub Actions-körning av denna ändring ska verifieras på PR.


## Uppgradering till Engine 1.6.28

Uppdaterad kanonisk `scripts/build_distributions.py` och uttrycklig exkludering av `distribution-engine/` från Chat ZIP. GitHub Actions verifierar både distributionsbygge och att den genererade Chat ZIP-filen inte innehåller motorn. Installerat Plugin-E2E och schemalagd bevakning återstår.


## Engine 1.6.28

Plugin-Skills får versionsbunden `plugin_id`/`plugin_version` i SKILL.md. CI kontrollerar samtliga tre Skills i genererad Plugin-ZIP mot `plugin.json`. Versionsnummer härleds från GitHub Release-taggen i release-workflow; installerad miljö behöver ny Plugin-installation efter nästa release.
