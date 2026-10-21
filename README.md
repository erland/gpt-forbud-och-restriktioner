# Förbud och Restriktioner

GPT för rättslig analys av import och export inom EU med officiella källor, versionskedja och AI-märkt PDF.

Utvecklingsspår: **ZIP**. GitHub är inte ett krav.

Distributionerna byggs från den versionerade GPT Byggaren Engine 1.6.27.

## Förändringsbevakning (v0.4.0)
Vid användning jämförs officiella källor med importerad eller tidigare sparad baslinje; utan baslinje görs initial inventering. Schemalagd bevakning kräver extern faktiskt ansluten schemaläggare och ingår inte som aktiv tjänst.

## GitHub Actions (frivilligt i ZIP-spåret)

`.github/workflows/ci.yml` kör tester, kanonisk distributionsbyggare, validering och release-readiness vid PR/push mot `main` eller manuellt. `.github/workflows/release.yml` bygger alla fem runtimepaket och projekt-ZIP när en GitHub Release publiceras, använder versionsnumret från `vX.Y.Z` och laddar upp ZIP, SHA256SUMS och leveransmanifest till releasen. Det kräver att GitHub Actions har skrivbehörighet för release-uppladdning (`contents: write`).

Workflows använder de incheckade, oförändrade byggskripten från GPT Byggaren Engine 1.6.27; de hämtar inte en rörlig `latest`-motor. Om motorn ska uppgraderas bör originalskripten uppdateras tillsammans med projektet och kontrolleras i PR. Lokal ZIP-byggning kräver inte GitHub.

## Runtimekorrigering efter v0.5.3
OpenCode-paketets README är projektspecifik och kontrolleras även i genererat ZIP-arkiv i CI. Chat ZIP innehåller fortfarande kanonisk offline-byggmotor på grund av ett ovillkorligt anrop i GPT Byggaren Engine 1.6.26; detta kan inte styras bort enbart i projektprofilen. Se [runtimegranskningen](docs/runtime-distribution-audit.md). Ingen lokal ersättningsbyggare har införts.

## GPT Byggaren Engine 1.6.27

Projektets kanoniska Chat-byggare är uppdaterad till Engine 1.6.27. `runtime.chat_zip.bundle_distribution_engine: false` gör att vanlig Chat ZIP inte längre får med offline-byggmotorn. GPT Byggarens egna projekt kan fortfarande välja `true`. Bygg och validera distributionerna i GitHub Actions; genererade ZIP-filer ska inte checkas in.
