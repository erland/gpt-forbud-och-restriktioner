# {{GPT_NAME}} – OpenCode

Detta paket innehåller **Förbud och Restriktioner**, en AI-assistent för källspårbar analys av EU:s och Sveriges regler om införsel och utförsel.

## Kom igång

1. Packa upp ZIP-filen i en egen katalog.
2. Öppna katalogen som workspace i OpenCode.
3. OpenCode läser `AGENTS.md` som huvudinstruktion och använder de tre Skills som följer med under `.opencode/skills/`.
4. Be assistenten analysera ett område, exempelvis EUDR/DDS, ELAN-1L eller CITES. Precisera handelsriktning, aktör, varuslag och tidpunkt när det har betydelse.
5. Granska källor, rättslig status, osäkerheter och eventuell AI-märkt PDF före användning som beslutsunderlag.

## Innehåll

- `AGENTS.md`: gemensamma beteenderegler och källkrav.
- `.opencode/skills/`: regelverksanalys, rapportpublicering och förändringsbevakning.
- `.opencode/runtime-contract.json`: deklarerade funktioner och begränsningar.
- `knowledge/`: referensmaterial för analyserna.
- `opencode.json`: runtimekonfiguration.

## Begränsningar

Körmiljön måste erbjuda webbtillgång för aktuell källkontroll och filgenerering för PDF-export. Om någon förmåga saknas ska assistenten redovisa det och inte påstå att den har utfört kontrollen eller skapat en fil. Schemalagd bevakning ingår inte automatiskt.

Paketet innehåller **inte** GPT Byggarens projektverktyg eller `.opencode/tools/` om inga körbara verktyg uttryckligen deklarerats. Förbud och Restriktioner är en regelverksassistent, inte ett verktyg för att bygga andra GPT:er.

## Version

{{VERSION}}
