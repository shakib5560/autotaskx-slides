# AutoTaskX — Industrial Textile Intelligence Platform
## Keynote Technical Interview Presentation (Simplified Story Structure)

A presentation explaining the **AutoTaskX** platform architecture.

Designed for technical interviewers, engineering leadership, and industrial technology partners.

---

### Presentation Philosophy: Problem → Solution → How It Works → Result → Future

Every slide answers a practical question with simple language, tangible real-world examples, and beautiful visual diagrams:
- **What is the actual problem?**
- **Why does a textile factory need this?**
- **What does AutoTaskX do?**
- **How does a physical sensor connect to the system?**
- **How does the information reach the website?**
- **Where is the information stored?**
- **What can the factory owner see?**
- **What happens when a machine reports a problem?**

---

### Deploy to Vercel

This repository is pre-configured as a zero-build static site (`vercel.json` + `.vercelignore`) so it deploys immediately on Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fshakib5560%2Fautotaskx-slides)

1. **Via Vercel Dashboard (GitHub Import):** Go to [vercel.com/new](https://vercel.com/new), import `shakib5560/autotaskx-slides`, leave Build & Output settings at defaults (detected from `vercel.json`), and click **Deploy**.
2. **Via Vercel CLI:**
   ```bash
   npx vercel --prod
   ```
3. Once deployed:
   - `/` serves the 18-slide presentation (`index.html`)
   - `/guide` (or `/guide.html`) serves the fluent English speaker guide with Bangla pronunciation cues (`guide.html`)
   - `/guide/bd` (or `/guide-bd.html`) serves the full Bangla presentation guide (`guide-bd.html`)

---

### Presentation Quickstart

Simply open `index.html` in any modern web browser (Google Chrome, Firefox, Safari, Microsoft Edge):

```bash
# Direct browser launch
xdg-open index.html

# Or serve via local HTTP server
python3 -m http.server 8080
# Navigate to: http://localhost:8080
```

---

### Navigation & Presenter Controls

| Key / Control | Action |
|---|---|
| `→` / `Space` / `PageDown` | Next Slide |
| `←` / `PageUp` / `Backspace` | Previous Slide |
| `Home` | Jump to Slide 01 (Introduction) |
| `End` | Jump to Slide 18 (Conclusion) |
| `O` (or Overview button `⊞`) | Toggle 18-Slide Thumbnail Grid Modal |
| `N` (or Notes button `Notes`) | Toggle 30-Second Presenter Speaking Guide |
| `G` (or Guide link inside Notes) | Open Full Bengali Speech Guide (`guide.html`) |
| `F` (or Fullscreen button `⛶`) | Toggle 16:9 Fullscreen Mode |
| `Esc` | Close Overview Modal / Notes Drawer |

---

### Slide Deck Structure (18 Slides)

1. **Slide 01 — Introduction**: "Making Textile Manufacturing Smarter, Connected, and More Efficient." — AutoTaskX central platform introduction, 4 core pillars, live mill status card, presenter credentials (`Sheikh Shamiul Shakib · Backend Software Engineer · BUBT Alumnus`).
2. **Slide 02 — The Actual Problem**: "Most Textile Factories Still Run on Guesswork." — Manual Work, Disconnected Machines, Missing Information, and Delayed Decisions with a Before vs After comparison strip.
3. **Slide 03 — Our Solution**: "Five Integrated Modules. One Industrial Ecosystem." — Color Formulation, Visual Quality Inspection, Production Intelligence, Textile OS & Digital Twin, and ERP Integration with authentic industrial imagery and interactive ecosystem pulse.
4. **Slide 04 — How AutoTaskX Works**: "From Physical Machine to Live Dashboard." — The grand 6-step journey: Physical Machines → Sensors & Cameras → Connection System → AutoTaskX Platform → Database Storage → Live Dashboard.
5. **Slide 05 — Feature 01: Color Formulation**: "Precise Color Recipes. Calculated in Seconds." — 6-step lab workflow with real-world 100 kg cotton navy knit batch recipe calculation and laboratory validation disclaimer.
6. **Slide 06 — Feature 02: Visual Quality Inspection**: "Every Metre of Fabric. Inspected Automatically." — Two sources (Basler racer 2 L line-scan camera vs Textile OS smartphone), 5-step image workflow, and S3 Cloud Storage vs PostgreSQL separation.
7. **Slide 07 — Feature 02: System Depth**: "From Raw Sensor Lines to Control Panel: Complete Sequence." — High-frequency CoaXPress line-scan acquisition, pre-signed S3 direct offloading, parallel MQTT telemetry, and WebSocket UI updates.
8. **Slide 08 — Feature 03: Production Intelligence**: "See Every Machine. Know Every Problem." — Real-world Stenter Frame #02 temperature control scenario (185.5°C normal vs 190°C alert) and live executive production monitor.
9. **Slide 09 — Feature 04: Textile OS**: "Textile OS & Digital Twin Connect Every Machine." — Hardware-to-software bridge supporting temperature, pressure, vibration, PLCs, and energy meters with a 5-step connection sequence.
10. **Slide 10 — Feature 04: Sensor Deep Dive**: "One Reading. Six Hops. Under 25ms." — Deep dive tracing a single 185.5°C reading moving through Machine → Sensor → Gateway → Network → AutoTaskX → Live Screen.
11. **Slide 11 — Communication Protocol**: "MQTT — The Language Machines Use to Talk." — The digital post office analogy (EMQX messaging broker) and the critical rule: MQTT for small sensor telemetry (< 1 KB) vs direct HTTPS S3 upload for heavy inspection images.
12. **Slide 12 — Storage Architecture**: "Three Databases. Each Does One Job Perfectly." — Three specialized storage containers: PostgreSQL (structured business records), TimescaleDB (continuous time-series measurements), and AWS S3 (heavy image files).
13. **Slide 13 — Dashboard Delivery**: "From Database to Live Screen. Under 25 Milliseconds." — 5-step delivery pipeline with real-time WebSockets and the practical difference between Current Data (what's happening now) vs Historical Data (what happened earlier).
14. **Slide 14 — Feature 05: ERP Integration**: "AutoTaskX Talks to Your Business Software." — Two-way enterprise highway connecting shopfloor execution with Datatex NOW, SAP S/4HANA, and Infor M3 with a Before vs After comparison.
15. **Slide 15 — Complete Architecture**: "Four Zones. One Unified Platform." — Grand 4-zone master architecture map: Zone 1 (Physical Mill), Zone 2 (Connection Layer), Zone 3 (AutoTaskX Core & Storage), Zone 4 (Delivery & Enterprise).
16. **Slide 16 — Business Value**: "Real Numbers. Live Results." — Executive HUD summary (24 active machines, 99.2% right-first-time quality, zero critical alerts) and 4 measurable business outcomes.
17. **Slide 17 — Future Roadmap**: "The Road Ahead for AutoTaskX." — Realistic 5-stage roadmap: Connect More Machines → Automated Inspection → Historical Analytics → Predictive Maintenance → Autonomous Adjustments.
18. **Slide 18 — Conclusion**: "Connecting Every Part of Textile Manufacturing." — Core platform value statement, 4 pillars recap, presenter signature card (`Sheikh Shamiul Shakib`), and open floor for technical questions.

---

### Built With
- Pure HTML5 / Modern CSS (16:9 widescreen stage scaling)
- Vanilla JavaScript (zero external runtime dependencies, fast loading)
- Dark Industrial Color Palette (`#0B132B`, `#111C38`, `#0E172E`, `#080D1C`)
- Vector SVG Brand Identity & Local Industrial Assets
