# regelverksanalys

(för `canonical/skills/regelverksanalys/behavior.md`)

Aktiveras när användaren vill förstå ett område, rättsläget eller de praktiska skyldigheterna.

1. Definiera område, rättsområde, handelsriktning och relevant tidpunkt.
2. Sök officiella EU- och svenska källor, identifiera huvudsakliga rättsakter, kompletterande/ändrande/upphävande rättsakter, myndighetsvägledningar och officiella förarbeten.
3. Bygg en rättsaktskedja och separata datumfält för antagande, publicering, ikraftträdande, tillämpning och upphävande. Markera tidsmässigt partiell tillämpning.
4. Översätt krav till verksamhetsfrågor: vem, vad, vilka varor, vilken gränspassage, när, vilket dokument/tillstånd, vilken myndighet, undantag och källa.
5. Värdera varje påstående: belagt av primärrätt, myndighetsvägledning, officiellt förarbete, sekundärkälla eller osäker syntes.
6. Lämna strukturerat, källhänvisat analysunderlag till rapportpublicering.

### Artikelvis evidens och svensk rätt
Gör först en evidensrad för varje beslutsrelevant krav enligt kärnans fält. Klassificera rättskedjan som grundakt, ändringsakt, delegerad akt, genomförandeakt, ersatt/upphävd akt eller svensk kompletterande akt. Samla relevanta artiklar inklusive övergångsbestämmelser och bilagornas varuspecifikationer. Kontrollera konsoliderad lydelse mot senare ändringar och särskilt ikraftträdande kontra tillämpningsdatum.

Sök svenska komplement separat: riksdagen.se, svenskforfattningssamling.se, regeringen.se samt berörda myndigheter. Identifiera utfärdad rätt, förslag, ansvarig myndighet, sanktion och gränssnitt till Tullverket. Redovisa luckor öppet och skilj myndighetsvägledning från rättsligt bindande grund.

### Aktör-/varubaserad beslutsgång
1. Bestäm om varan/produkten faktiskt omfattas av tillämplig bilaga med KN-nummer och produktbeskrivning, inte endast nyckelord. 2. Bestäm import/marknadsintroduktion/vidareförsäljning/export och korrekt aktörsroll. 3. Bestäm datum och relevanta övergångsregler samt storlek/undantag. 4. Identifiera krav på DDS, förenklad deklaration, registrering, referensuppgift, riskbedömning och dokumentation endast om artikelstöd finns. 5. Visa myndighetsåtgärder och tullformaliteter separat. 6. Ge en villkorad slutsats med evidens-ID:n och kända osäkerheter.

Vid varukodsbedömning: kontrollera KN/TARIC mot officiell, tidsriktig bilaga och Tullverkets/EU:s TARIC-vägledning. Skillen får aldrig tilldela en sannolik kod som verifierad.

Ange alltid artikel eller paragraf, där det finns, och separat aktörsroll. Kontrollera aktuell TARIC-kod mot primärkälla.

### EUDR tre obligatoriska regressionsfall
Testa primär importör, nedströmsaktör och otillräcklig KN/TARIC-kod enligt `tests/eudr_cases.json` där tillgänglig. Artikel 5 enligt (EU) 2025/2650 innebär inte generell DDS för nedströmsaktörer. Om TARIC-kod inte verifierats: begär precisering, inte gissad klassificering. Även svenska SFS-nummer kräver primärverifiering.

### Kvalitetssäkring för EUDR

Pröva artikel 2, 3, 4, 4a, 5, 8–11 och 38 och bilaga I mot tillämplig lydelse. Gör en separat verifiering av svensk kompletterande rätt. Använd en daterad söklogg och redovisa ej verifierade uppgifter öppet. Ge inte PASS när avgörande källor eller rekvisit saknas.
