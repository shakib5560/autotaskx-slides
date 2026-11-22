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
| `End` | Jump to Slide 17 (Conclusion) |
| `O` (or Overview button `⊞`) | Toggle 17-Slide Thumbnail Grid Modal |
| `N` (or Notes button `Notes`) | Toggle 30-Second Presenter Speaking Guide |
| `F` (or Fullscreen button `⛶`) | Toggle 16:9 Fullscreen Mode |
| `Esc` | Close Overview Modal / Notes Drawer |

---

### Slide Deck Structure (17 Slides)

1. **Slide 01 — Introduction**: "Making Textile Manufacturing Smarter, Connected, and More Efficient" — AutoTaskX central platform introduction, 4 core pillars, live mill status card, presenter credentials (`Sheikh Shamiul Shakib · Software Engineer · BUTEX Alumnus`).
2. **Slide 02 — The Actual Problem**: "What Problems Do Textile Factories Face Today?" — Manual Work, Disconnected Machines, Missing Information, and Delayed Decisions with a Before vs After comparison strip.
3. **Slide 03 — Our Solution**: "One Platform to Connect the Entire Factory" — 5 integrated modules: Color Formulation, Visual Quality Inspection, Production Intelligence, Textile OS, and ERP Integration with authentic industrial imagery.
4. **Slide 04 — How AutoTaskX Works**: "From the Factory Floor to One Digital Dashboard" — The grand 6-step journey: Physical Machines → Sensors & Cameras → Connection System → AutoTaskX Platform → Database Storage → Live Dashboard.
5. **Slide 05 — Feature 01: Color Formulation**: "Calculate and Manage Dye Recipes More Easily" — 6-step lab workflow with real-world 100 kg cotton navy knit batch recipe calculation and laboratory validation disclaimer.
6. **Slide 06 — Feature 02: Visual Quality Inspection**: "Inspect Fabric Using Industrial Cameras or Smartphones" — Two sources (Basler racer 2 L line-scan camera vs Textile OS smartphone), 5-step image workflow, and S3 Cloud Storage vs PostgreSQL separation.
7. **Slide 07 — Feature 03: Production Intelligence**: "Know What Is Happening Inside Your Factory" — Real-world Stenter Frame #02 temperature control scenario (185.5°C normal vs 190°C alert) and live executive production monitor.
8. **Slide 08 — Feature 04: Textile OS**: "Connect Your Physical Factory to AutoTaskX" — Hardware-to-software bridge supporting temperature, pressure, vibration, PLCs, and energy meters with a 5-step connection sequence.
9. **Slide 09 — How a Physical Sensor Connects**: "Let's Follow One Sensor" — Deep dive tracing a single 185.5°C reading with an interactive pulse animation (`Animate Reading Pulse` button) moving through Machine → Sensor → Gateway → Network → AutoTaskX → Live Screen.
10. **Slide 10 — How Devices Communicate: MQTT**: "How Do Machines Send Information to AutoTaskX?" — The digital post office analogy (EMQX messaging broker) and the critical rule: MQTT for small sensor telemetry (< 1 KB) vs direct HTTPS S3 upload for heavy inspection images.
11. **Slide 11 — Where Does the Data Go?**: "Every Type of Information Has Its Own Storage" — Three specialized storage containers: PostgreSQL (structured business records), TimescaleDB (continuous time-series measurements), and AWS S3 (heavy image files).
12. **Slide 12 — How Data Reaches the Dashboard**: "From a Physical Reading to a Live Dashboard" — 5-step delivery pipeline with real-time WebSockets and the practical difference between Current Data (what's happening now) vs Historical Data (what happened earlier).
13. **Slide 13 — ERP Integration**: "AutoTaskX Works With Your Existing Business Software" — Two-way enterprise highway connecting shopfloor execution with Datatex NOW, SAP S/4HANA, and Infor M3 with a Before vs After comparison.
14. **Slide 14 — Complete Factory Workflow**: "How Everything Works Together" — Grand 4-zone master architecture map: Zone 1 (Physical Mill), Zone 2 (Connection Layer), Zone 3 (AutoTaskX Core & Storage), Zone 4 (Delivery & Enterprise).
15. **Slide 15 — What Does the Factory Owner Get?**: "One Place to Understand the Entire Factory" — Executive HUD summary (24 active machines, 99.2% right-first-time quality, zero critical alerts) and 4 measurable business outcomes.
16. **Slide 16 — Future Possibilities**: "Where Can AutoTaskX Go Next?" — Realistic 5-stage roadmap: Connect More Machines → Automated Inspection → Historical Analytics → Predictive Maintenance → Autonomous Adjustments.
17. **Slide 17 — Closing & Discussion**: "Connecting Every Part of Textile Manufacturing" — Core platform value statement, 4 pillars recap, presenter signature card (`Sheikh Shamiul Shakib`), and open floor for technical questions.

---

### Built With
- Pure HTML5 / Modern CSS (16:9 widescreen stage scaling)
- Vanilla JavaScript (zero external runtime dependencies, fast loading)
- Dark Industrial Color Palette (`#0B132B`, `#111C38`, `#0E172E`, `#080D1C`)
- Vector SVG Brand Identity & Local Industrial Assets
