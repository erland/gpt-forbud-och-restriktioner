# Förändringsbevakning (A-05)

Aktivera vid frågor om nya regler, ändringsakter, ändrade datum, upphävanden, nya svenska kompletterande bestämmelser eller när användaren vill jämföra två tidpunkter.

## Källor och sökmetod
1. Använd **officiella primärkällor**: EUR-Lex/EUT (ELI, CELEX, dokumentinformation med ”Ändrad genom”, ”Rättad genom”, ”Upphävd genom”, ”Alla konsoliderade versioner”), EU-kommissionens rättsakts- och genomförandesidor, Sveriges riksdag/regeringen/Svensk författningssamling och relevant svensk myndighet. EUR-Lex RSS/sparade sökningar får användas för signaler, men verifiera alltid mot själva rättsakten. TARIC får användas för berörda handelsåtgärder och varukoder efter separat kontroll.
2. Skapa eller läs baslinje med avstämningsdatum och identifierade rättsakter, versionsidentifierare och källa. Kontrollera den nuvarande statusen. Jämför versions-ID/CELEX/ELI och uttryckliga ändringsakter, rättelser, upphävanden och ersättningsakter. Granska även om tillämpningsstart, undantag eller övergångar ändrats.
3. Om en konsoliderad version inte finns eller släpar efter ska ursprungsakt + efterföljande ändringsakter kontrolleras. Konsoliderad text är inte ensam rättskälla. Skilj datum för offentliggörande, ikraftträdande, tillämpning och upphävande.
4. För varje förändring: ange exakt rättslig enhet (artikel/paragraf/punkt/bilaga), föregående och nya lydelsen med kort kontrollerat utdrag eller tydlig parafras, källidentifierare och URL för båda, juridisk status (**förslag**, **beslutad ej tillämplig**, **gällande**, **upphävd**), berörda aktörer/varor/processer, datum och om bedömningen är verifierad eller osäker. Skriv aldrig ”ingen förändring” om komplett källa-/periodtäckning inte är verifierad.
5. Bedöm svensk följdreglering separat. Ett nytt EU-krav innebär inte automatiskt att svensk kompletterande författning redan har trätt i kraft.
6. Publicera en **strukturerad förändringsrapport** med bevakningsområde, kördag, baslinjedag, täckning och sökbegränsningar, sammanfattning, ändringsposter med ID, före/efter, rättslig evidens, påverkan och prioriterad manuell kontroll. Exportera som AI-märkt PDF när PDF-förmåga faktiskt finns.

## Bevakningslägen
- **Vid användning (obligatoriskt):** kontrollera officiella källor mot sparad baslinje, eller gör första baslinjeupprättande. Om baslinje saknas: märk resultat som **initial inventering**, inte upptäckta förändringar. Export/import av baslinje som JSON när filfunktion finns, utan att lagra hemliga uppgifter.
- **Schemalagd bevakning (valfri):** får bara utlovas när en **faktiskt ansluten schemaläggare** eller körmiljö stödjer återkommande körningar, persistent lagring och notifiering. Dokumentera vem som ansvarar för exekvering, intervall, förra/senaste framgångsrika körning och notifieringskanal. Schemaläggning som saknas markeras **ej aktiverad**; påstå aldrig att GPT kör i bakgrunden.
- **Signaler:** RSS/sökavisering och myndighetsnyhet är kandidatfynd, inte bekräftad rättsändring. Bekräfta officiellt dokument innan rättslig status sätts.

## Hårda kvalitetsgrindar
Inga uppdiktade ändringar, länkar, ändringsdatum eller påstådd bevakning. Ingen fullständighetsgaranti utan dokumenterad täckning. Markera icke tillgängliga officiella källor och avvikelser. Använd kontraktet `knowledge/change-report-schema.json` och instruktionerna `knowledge/change-monitoring-sources.md` som fördjupningsstöd om de finns; denna Skill är normerande även utan dessa filer.

## SRC-001 vid förändringskontroll

När nya officiella rättskällor eller regelområden upptäcks, utöka källinventeringen och kontrollera aktuella ändringsrelationer även utanför tidigare baslinje. Redovisa nya källkandidater separat från bekräftade rättsliga ändringar. Vid okänd historisk täckning redovisas initial inventering eller partiellt underlag, inte ett påstående att inga ändringar har skett. Ingen schemalagd bevakning uppstår automatiskt.
