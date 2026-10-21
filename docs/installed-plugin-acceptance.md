# Installerad Plugin – funktionellt acceptansprotokoll (LEG-003.1)

## Syfte och status
Detta är instruktionen för **tio verkliga och separata körningar** av den installerade Förbud och Restriktioner. **Ej utfört som fullständig Plugin-E2E vid protokollets uppdatering.** En lyckad CI-körning eller enbart läsning av Skills kan inte ge E2E-PASS. Funktionell användning av de installerade Skillsen i värdmiljön kan verifieras utan separat isolerad pluginprocess, om faktisk svarskörning och evidens är dokumenterade.

## Versionsverifiering
Läs metadata i var och en av de tre installerade Skillsen och redovisa `plugin_id` och `plugin_version`. Samma versionsvärde måste framgå för samtliga Skills. Om värdplattformen inte exponerar versionsmetadata: PARTIAL (inte ett antagande utifrån uppladdad distributions-ZIP).

## Körprocedur
1. Kör var och en av PLUGIN-01–04 i `tests/test-manifest.json` samt CITES-01–02, CBAM-01–02 och SANCTIONS-01–02 som **separata faktiska frågor i installerad Plugin**. Använd scenariofrågan ordagrant; lägg inte till uppgifter som scenariot saknar.
2. Spara komplett svar, källtillgång, datum, version och tillhörande faktisk rapportfil. Pröva öppningsbar PDF och AI-märkning på framsida och sidfot. PDF med kompatibla verktyg i värdmiljön kan ge PASS om faktisk fil, öppningsbarhet, innehåll, källor och AI-märkning är verifierade. Separat Plugin-exportmotor krävs endast om runtimekontraktet uttryckligen kräver den.
3. För varje avgörande slutsats ska källans identifierare, artikel/punkt/bilaga, URL, versionsdatum och kontrolltid finnas. Svensk kompletterande rätt undersöks i officiella kanaler, med tydlig status för gällande författning respektive förslag/vägledning.
4. Vid CITES används tidsriktig bilaga till förordning 338/97 (inklusive ändring EU 2026/1383 för analys den 21 oktober 2026). Vid CBAM skiljs importvillkor 2026 och deklarationsskyldighet 2027. Vid sanktioner räcker inte bara sökning på listad motpart; även ägande/kontroll, vara, land och slutanvändning prövas. **Dessa är granskningsankare, inte frikort från aktuell rättskällekontroll.**
5. Betygsätt **beteende**, **materiell juridisk verifiering** och **PDF** separat. Beteende får **PASS** även vid avsiktligt ofullständiga indata om assistenten begär avgörande komplettering, redovisar rimliga villkor och avstår från kategoriskt besked. Materiell verifiering får **PARTIAL** när ett avgörande rekvisit eller en källa saknas, även om beteendet är PASS. **FAIL** vid påhittad rättsregel, identifierare, falskt kategoriskt besked eller påstådd levererad fil som inte existerar. `CONDITIONAL` i fixture-data är förväntad svarstyp, inte fjärde betyg eller automatiskt PASS.
6. Redovisa testbevis i tabell med kolumnerna `case_id`, `installed_version`, `run_timestamp`, `source_checks`, `swedish_law_status`, `behavior_result`, `substantive_result`, `pdf_result`, `evidence_link`. Samlad acceptans får inte PASS om kritiska fält saknas.

## Fördelning av beviskrav och avvikelser A1–A5

- **A1:** Verifiera faktisk tillämpning av installerade Skills på vart och ett av de tio scenarierna. Ingen separat isolerad pluginprocess behövs om den inte ingår i det deklarerade runtimekontraktet. Enbart granskning av instruktioner eller testdata räcker inte.
- **A2:** Projektets Python-`unittest` och distributionskontroller tillhör **GitHub Actions**, inte den installerade Pluginmiljön. Hänvisa till relevant godkänd CI-körning och kontrollera att den avser den testade releasekoden. Avsaknad av utvecklingstestfiler i installerade Skills är inte en Plugin-avvikelse.
- **A3:** Ofullständiga scenarier är avsiktliga negativa tester. Bedöm osäkerhetshantering som möjligt beteende-PASS; håll materiell rättslig bedömning PARTIAL.
- **A4:** Kontroll av verkliga officiella EU-källor, svenska författningar, bilagor och aktuella sanktionslistor krävs fortfarande. Saknat primärkällestöd får aldrig uppgraderas till PASS enbart genom ändrad betygsmodell.
- **A5:** Använd fungerande PDF-verktyg i ChatGPT-värdmiljön för rapportpublicering. PASS för export kräver tekniskt verifierad PDF med AI-märkning och källhänvisningar. Kräv en egen exportmotor endast om en sådan uttryckligen är en produktförmåga i runtimekontraktet.
- Schemalagd förändringsbevakning är separat funktion: utan begärt eller deklarerat schedulerstöd ska frånvaron inte blockera acceptans av analys eller PDF. Förändringsanalys på begäran prövas däremot enligt LEG-001.

## Viktiga officiella källingångar
- CITES: https://eur-lex.europa.eu/eli/reg/1997/338/oj och https://eur-lex.europa.eu/eli/reg/2026/1383/oj
- CBAM: https://eur-lex.europa.eu/eli/reg/2023/956/oj och https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en
- Sanktioner: https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures_en
- EUDR: https://eur-lex.europa.eu/eli/reg/2023/1115/oj

## Utfall vid uppdatering
Statiska regressionstester och distributionspaketering har tidigare passerat CI, men separata tio installerade körningar har inte verifierats här. **Fullständigt E2E: EJ STYRKT.**
