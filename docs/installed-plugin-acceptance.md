# Installerad Plugin – funktionellt acceptansprotokoll (LEG-003)

## Syfte och status
Detta är instruktionen för **tio verkliga och separata körningar** av den installerade Förbud och Restriktioner. **Ej utfört som fullständig Plugin-E2E vid protokollets uppdatering.** En lyckad CI-körning, läsning av installerade Skills eller separat PDF-produktion kan inte ge E2E-PASS.

## Versionsverifiering
Läs metadata i var och en av de tre installerade Skillsen och redovisa `plugin_id` och `plugin_version`. Samma versionsvärde måste framgå för samtliga Skills. Om värdplattformen inte exponerar versionsmetadata: PARTIAL (inte ett antagande utifrån uppladdad distributions-ZIP).

## Körprocedur
1. Kör var och en av PLUGIN-01–04 i `tests/test-manifest.json` samt CITES-01–02, CBAM-01–02 och SANCTIONS-01–02 som **separata faktiska frågor i installerad Plugin**. Använd scenariofrågan ordagrant; lägg inte till uppgifter som scenariot saknar.
2. Spara komplett svar, källtillgång, datum, version och tillhörande faktisk rapportfil. Pröva öppningsbar PDF och AI-märkning på framsida och sidfot. Skilj hostens PDF-verktyg från eventuell installerad specifik exportmotor; en egen motor krävs endast om runtimekontraktet uttryckligen kräver den.
3. För varje avgörande slutsats ska källans identifierare, artikel/punkt/bilaga, URL, versionsdatum och kontrolltid finnas. Svensk kompletterande rätt undersöks i officiella kanaler, med tydlig status för gällande författning respektive förslag/vägledning.
4. Vid CITES används tidsriktig bilaga till förordning 338/97 (inklusive ändring EU 2026/1383 för analys den 21 oktober 2026). Vid CBAM skiljs importvillkor 2026 och deklarationsskyldighet 2027. Vid sanktioner räcker inte bara sökning på listad motpart; även ägande/kontroll, vara, land och slutanvändning prövas. **Dessa är granskningsankare, inte frikort från aktuell rättskällekontroll.**
5. Betygsätt **PASS** när samtliga avgörande rekvisit, villkor, källor och utdata är kontrollerade; **PARTIAL** vid tillgänglighetsbrist eller väsentligt osäkert rekvisit korrekt markerat; **FAIL** vid påhittad rättsregel, kod, källa, falskt kategoriskt besked eller utlovad fil som inte finns. För ofullständiga fall kan korrekt villkorad slutsats vara ett godkänt **beteende** även om juridisk omfattningsbedömning förblir PARTIAL.
6. Redovisa testbevis i tabell med kolumnerna `case_id`, `installed_version`, `run_timestamp`, `source_checks`, `swedish_law_status`, `behavior_result`, `substantive_result`, `pdf_result`, `evidence_link`. Samlad acceptans får inte PASS om kritiska fält saknas.

## Viktiga officiella källingångar
- CITES: https://eur-lex.europa.eu/eli/reg/1997/338/oj och https://eur-lex.europa.eu/eli/reg/2026/1383/oj
- CBAM: https://eur-lex.europa.eu/eli/reg/2023/956/oj och https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en
- Sanktioner: https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures_en
- EUDR: https://eur-lex.europa.eu/eli/reg/2023/1115/oj

## Utfall vid uppdatering
Statiska regressionstester och distributionspaketering har tidigare passerat CI, men separata tio installerade körningar har inte verifierats här. **Fullständigt E2E: EJ STYRKT.**
