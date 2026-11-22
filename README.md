# AutoTaskX — Industrial Textile Intelligence Platform
## Interactive Technical Slide Presentation

A premium, interactive, 16:9 widescreen HTML slide-based technical presentation explaining the complete **AutoTaskX** platform architecture.

Designed for technical interviewers, engineering leadership, and industrial technology partners.

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
| `→` / `Space` / `PageDown` / `Enter` | Next Slide |
| `←` / `PageUp` / `Backspace` | Previous Slide |
| `Home` | Jump to Slide 01 (Cover) |
| `End` | Jump to Slide 22 (Conclusion) |
| `O` (or Overview button) | Toggle 22-Slide Navigator Grid Modal |
| `N` (or Notes button) | Toggle Presenter Engineering Notes Drawer |
| `F` (or Full button) | Toggle Widescreen Fullscreen Mode |
| `Esc` | Close Overview Modal / Notes Drawer |

---

### Slide Deck Structure (22 Slides)

1. **Slide 01 — Cover**: AutoTaskX Industrial Textile Intelligence Platform, "From Physical Factory Operations to Intelligent Digital Manufacturing", Stack badges, Presenter credentials (`Sheikh Shamiul Shakib`).
2. **Slide 02 — The Industrial Problem**: "Textile Manufacturing Generates More Data Than It Can Effectively Use" — Fragmented floor, slow lab trials (24-72h), subjective manual inspection, ERP drift. Grounded in a 150-page BUTEX textile engineering thesis.
3. **Slide 03 — The AutoTaskX Vision**: "One Connected Intelligence Layer for the Entire Textile Factory" — Connecting Color Science, Visual Quality Inspection, Production Intelligence, Textile OS, and Enterprise ERP.
4. **Slide 04 — Platform Overview**: Five Integrated Modules (01 Color Formulation, 02 Visual Quality Inspection, 03 Production Intelligence, 04 Textile OS, 05 ERP Integration).
5. **Slide 05 — Feature 01: Color Formulation**: Kubelka-Munk Absorption Matrix ($K/S = (1-R_\lambda)^2 / 2R_\lambda$), Non-Negative Least Squares (NNLS), Triple Input Ingestion Channels, and 8-step recipe pipeline.
6. **Slide 06 — Feature 01: Lab Hardware IoT & MQTT**: Spectrophotometers, automatic chemical dispensers, precision weighing balances, and live JSON telemetry streams over EMQX.
7. **Slide 07 — Feature 02: Industrial Camera Integration**: Basler racer 2 L (R2L16384-60cc) Line Scan Camera (16,384 x 2 px, 60 kHz line rate, CoaXPress 2.0 CXP-12) with authentic lab vision gantry setup.
8. **Slide 08 — Feature 02: Dual Data Pipeline Architecture**: Decoupling heavyweight raw TIFF image storage (Direct S3 via pre-signed URLs) from lightweight IoT telemetry (MQTT v5 via EMQX).
9. **Slide 09 — Feature 02: Inspection Sequence & Real-Time HUD**: 7-stage sequence diagram and live fabric inspection canvas with bounding box defect overlays (Warp Float, Oil Stain) and 99.4% defect recall.
10. **Slide 10 — Feature 03: Production Intelligence**: Live factory OEE (86.4%), RFT (94.2%), and real-time fleet table monitoring Fong's Jet dyeing vessels and Monforts stenters at 124ms intervals.
11. **Slide 11 — Feature 03: Industrial IoT Protocol Taxonomy**: Modbus TCP/RTU, OPC UA, LwM2M over CoAP (IPSO 3303 & 3323 objects), and standardized MQTT v5 topic hierarchy.
12. **Slide 12 — Feature 03: AI Production Analyst & Anomaly Detection**: Conversational natural-language query simulator translating inquiries into validated TimescaleDB SQL queries, plus dual-tier anomaly engine.
13. **Slide 13 — Feature 03: Predictive Maintenance & Bottleneck Analysis**: FFT vibration spectral harmonics for bearing defect frequencies and 8-stage textile manufacturing flow with Stenter bottleneck detection.
14. **Slide 14 — Feature 03: Resource Intelligence & Multi-Mill Benchmarking**: Specific utility consumption (0.42 kWh/kg electricity, 48.5 L/kg water) and Gazipur vs Narayanganj cluster comparison with row-level security.
15. **Slide 15 — Feature 04: Textile OS**: Unified industrial operating system connecting 5 device classes (Environmental, Machine, Textile Equipment, Lab, Vision) with centralized device registry and LWT.
16. **Slide 16 — Feature 04: TimescaleDB Time-Series Engine**: PostgreSQL 16 + TimescaleDB hypertables, 1-day chunk intervals, 7-day columnar compression (92% disk reduction), and continuous aggregates.
17. **Slide 17 — Feature 04: Live Industrial Telemetry Console**: Real-time updating HTML5 Canvas waveform monitor for chamber temperature, liquor pressure, and fabric speed, plus live digital twin gauges.
18. **Slide 18 — Feature 05: ERP Integration — Enterprise Interoperability**: Non-invasive enterprise data bridge supporting Datatex NOW, SAP S/4HANA (PP/QM), Infor M3, and Generic REST.
19. **Slide 19 — Feature 05: Bidirectional Synchronization & Schema Mapping**: Flow A (Top-Down ERP orders) vs Flow B (Bottom-Up shopfloor reality), field mapping table, and transactional outbox.
20. **Slide 20 — Feature 05: Interactive Mill Console & Live Dispatch Stream**: Terminal dispatch stream showing live SAP and Datatex transaction events, ACK latencies, and enterprise security governance.
21. **Slide 21 — Complete End-to-End System Architecture**: Comprehensive 7-layer industrial diagram spanning physical shopfloor to digital twin presentation.
22. **Slide 22 — Measurable Outcomes & Technical Discussion**: Validated benchmarks (<25ms latency, 0.32 dE00, 99.4% recall, 60% faster lab dips, 0% clipboard errors), technical discussion prompts, and presenter info.

---

### Key Technical Assets Included
- `index.html`: Complete standalone presentation.
- `styles.css`: Enterprise industrial SaaS styling, typography, responsive 16:9 canvas scaling.
- `app.js`: Slide navigation, keyboard listener, overview grid, presenter notes drawer, live canvas telemetry generator, and interactive query simulators.
- `logo.svg` & `logo-white.svg`: Official AutoTaskX vector logo assets.
- `Textile Inspection Vision Lab.png`: Authentic industrial machine vision lab gantry testbed.
- `textile_factory_floor.png`: Authentic textile weaving and warping mill floor photo.
- `autotaskx_ui_hero.png`: Authentic AutoTaskX control environment screenshot.
