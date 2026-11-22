/**
 * AutoTaskX — Industrial Textile Intelligence Platform
 * Premium Interactive Presentation Engine
 */

(function () {
  'use strict';

  // --- State ---
  let currentSlide = 1;
  const totalSlides = 22;
  let isFullscreen = false;
  let animFrameId = null;

  // --- DOM Elements ---
  const stageScaler = document.getElementById('stage-scaler');
  const slides = document.querySelectorAll('.slide');
  const progressBar = document.getElementById('progress-bar');
  const currentSlideDisplay = document.getElementById('current-slide-num');
  const totalSlideDisplay = document.getElementById('total-slide-num');
  const categoryIndicator = document.getElementById('slide-category-indicator');

  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnOverview = document.getElementById('btn-overview');
  const btnNotes = document.getElementById('btn-notes');
  const btnFullscreen = document.getElementById('btn-fullscreen');

  const overviewModal = document.getElementById('overview-modal');
  const btnCloseOverview = document.getElementById('btn-close-overview');
  const overviewGrid = document.getElementById('overview-grid');

  const notesDrawer = document.getElementById('notes-drawer');
  const btnCloseNotes = document.getElementById('btn-close-notes');
  const notesContent = document.getElementById('notes-content');

  // --- Presenter Notes Data ---
  const presenterNotes = {
    1: `<strong>Title & Executive Position:</strong><br>
        Introduce AutoTaskX as a unified Industrial Textile Intelligence Platform. Emphasize that it bridges real physical factory machinery with enterprise intelligence, targeting textile hubs like Gazipur and Narayanganj. Mention the sub-25ms latency guarantee.`,
    
    2: `<strong>The Industrial Problem:</strong><br>
        Highlight the core problem: modern textile mills generate terabytes of data, but 94% is lost at analog dials and paper clipboards. Mention the 150-page BUTEX thesis foundation, proving deep domain expertise in textile engineering and dyehouse thermodynamics.`,
    
    3: `<strong>Platform Vision:</strong><br>
        Explain that AutoTaskX does NOT rip and replace existing factory equipment. It deploys a non-invasive edge-to-cloud nervous system connecting color chemistry, 16K optical inspection, shopfloor OEE, and SAP/Datatex ERPs.`,
    
    4: `<strong>5 Core Integrated Modules:</strong><br>
        Walk through the 5 modules: 01 Color Formulation, 02 Visual Quality Inspection, 03 Production Intelligence, 04 Textile OS, and 05 ERP Integration. Highlight how they share an ACID-compliant time-series storage core.`,
    
    5: `<strong>Feature 01: Color Formulation Mathematics:</strong><br>
        Detail the Kubelka-Munk absorption/scattering equation (K/S = (1-R)^2 / 2R). Explain how Non-Negative Least Squares (NNLS) calculates exact dye concentrations. Emphasize the industrial notice: algorithmic recipes are verified with lab dips.`,
    
    6: `<strong>Feature 01: Physical Lab IoT Integration:</strong><br>
        Show how spectrophotometers, auto-dispensers, and precision balances connect over RS-232/Modbus into the IoT Gateway, publishing lightweight JSON telemetry over MQTT topic <code>autotaskx/color/...</code>.`,
    
    7: `<strong>Feature 02: Basler Industrial Line-Scan Camera:</strong><br>
        Highlight the Basler racer 2 L (R2L16384-60cc). Explain why area cameras fail on continuous 40 m/min textile rolls: you need true 16K optical width scanned at 60 kHz. Reference the authentic Vision Lab photo with the overhead aluminum gantry.`,
    
    8: `<strong>Feature 02: Dual-Pipeline Architecture:</strong><br>
        Crucial architecture point: Industrial cameras NEVER send heavy TIFF images through MQTT. Pipeline A uploads raw TIFFs directly to AWS S3 using pre-signed URLs; Pipeline B sends lightweight defect bounding box events over MQTT to EMQX.`,
    
    9: `<strong>Feature 02: Sequence & Inspection HUD:</strong><br>
        Walk through the sequence diagram from line capture to S3 and WebSockets. Point out the live HUD with fabric bounding boxes detecting warp floats and oil stains with 99.4% recall.`,
    
    10: `<strong>Feature 03: Production Intelligence OEE:</strong><br>
        Demonstrate real-time factory monitoring. Review OEE (86.4%), RFT (94.2%), and the live fleet table with Fong's Jet dyeing vessels and Monforts stenters updating at 124ms intervals.`,
    
    11: `<strong>Feature 03: Industrial IoT Protocol Taxonomy:</strong><br>
        Explain protocol normalization. Legacy PLCs speak Modbus and OPC UA; LwM2M/CoAP standardizes IPSO 3303 (Temp) and 3323 (Pressure); the Python gateway publishes clean MQTT v5 messages with TLS 1.3.`,
    
    12: `<strong>Feature 03: AI Production Analyst & Anomalies:</strong><br>
        Show conversational AI in action. The model does not hallucinate—it translates natural English into validated TimescaleDB SQL queries. Point out the Monforts Stenter Chamber 04 +6.2°C thermal overshoot anomaly.`,
    
    13: `<strong>Feature 03: Predictive Maintenance & Bottlenecks:</strong><br>
        Explain vibration FFT analysis for bearing BPFI defect frequencies. Walk through the 8-stage manufacturing flow, identifying Stenter drying as the primary bottleneck causing staging delays.`,
    
    14: `<strong>Feature 03: Resource & Multi-Mill Benchmarking:</strong><br>
        Review specific consumption: 0.42 kWh/kg electricity, 48.5 L/kg water. Highlight multi-mill cluster benchmarking between Gazipur and Narayanganj with strict tenant row-level security.`,
    
    15: `<strong>Feature 04: Textile OS Unified Architecture:</strong><br>
        Textile OS connects all 5 device classes: Environmental, Machine, Textile Equipment, Lab, and Vision. Emphasize device health tracking with MQTT Last Will and Testament (LWT).`,
    
    16: `<strong>Feature 04: TimescaleDB Time-Series Engine:</strong><br>
        Explain why PostgreSQL + TimescaleDB: 1-day chunk partitioning, transparent 7-day columnar compression (92% disk reduction), and continuous aggregates delivering sub-25ms query latencies.`,
    
    17: `<strong>Feature 04: Live Industrial Telemetry Console:</strong><br>
        Point to the active real-time waveform canvas. Highlight continuous closed-loop monitoring of vessel temperature (130.4°C) and pressure (2.84 bar).`,
    
    18: `<strong>Feature 05: ERP Integration Strategy:</strong><br>
        Reiterate the core position: AutoTaskX does not replace existing ERP. It provides certified bi-directional connectors for Datatex NOW, SAP S/4HANA (PP/QM), and Infor M3.`,
    
    19: `<strong>Feature 05: Bidirectional Data Flows & Schema Mapping:</strong><br>
        Explain Flow A (top-down work orders & recipes) versus Flow B (bottom-up real-time chemical consumption & meterage). Walk through the schema translation table and transactional outbox.`,
    
    20: `<strong>Feature 05: Interactive Mill Console & Dispatch Stream:</strong><br>
        Demonstrate the terminal stream with live mill dispatch events (PO received, batch mapped, chemical consumption synced to SAP MM with MBLNR document creation).`,
    
    21: `<strong>Complete 7-Layer System Architecture:</strong><br>
        Summarize the full industrial stack: Physical Floor -> Connectivity -> Edge Computing -> EMQX Broker -> Cloud Application -> TimescaleDB/S3 Storage -> Presentation & Digital Twin.`,
    
    22: `<strong>Measurable Outcomes & Technical Discussion:</strong><br>
        Review quantified impacts: <25ms latency, 0.32 dE00, 99.4% defect recall, 60% faster lab dips, 0% clipboard errors. Invite technical questions on edge hardening, TimescaleDB tuning, and CoaXPress 2.0. Open floor for discussion.`
  };

  // --- Overview Titles ---
  const slideTitles = [
    { num: 1, title: "Cover: Industrial Textile Intelligence", cat: "INTRODUCTION" },
    { num: 2, title: "The Industrial Problem & Factory Silos", cat: "THE CHALLENGE" },
    { num: 3, title: "The AutoTaskX Vision & Strategy", cat: "VISION" },
    { num: 4, title: "Five Integrated Modules Ecosystem", cat: "ARCHITECTURE" },
    { num: 5, title: "Feature 01: Precision Color Formulation", cat: "FEATURE 01" },
    { num: 6, title: "Feature 01: Lab Hardware IoT & MQTT", cat: "FEATURE 01" },
    { num: 7, title: "Feature 02: Basler 16K Camera Integration", cat: "FEATURE 02" },
    { num: 8, title: "Feature 02: Dual-Pipeline S3 & MQTT", cat: "FEATURE 02" },
    { num: 9, title: "Feature 02: Sequence & Inspection HUD", cat: "FEATURE 02" },
    { num: 10, title: "Feature 03: Production Intelligence OEE", cat: "FEATURE 03" },
    { num: 11, title: "Feature 03: Protocol Adapters & MQTT", cat: "FEATURE 03" },
    { num: 12, title: "Feature 03: AI Analyst & Anomaly Detection", cat: "FEATURE 03" },
    { num: 13, title: "Feature 03: Predictive Maintenance & Bottlenecks", cat: "FEATURE 03" },
    { num: 14, title: "Feature 03: Utilities & Multi-Mill Ranking", cat: "FEATURE 03" },
    { num: 15, title: "Feature 04: Textile OS Unified System", cat: "FEATURE 04" },
    { num: 16, title: "Feature 04: TimescaleDB Time-Series Engine", cat: "FEATURE 04" },
    { num: 17, title: "Feature 04: Live Waveform Monitor HUD", cat: "FEATURE 04" },
    { num: 18, title: "Feature 05: ERP Interoperability Bridge", cat: "FEATURE 05" },
    { num: 19, title: "Feature 05: Bidirectional Sync & Mapping", cat: "FEATURE 05" },
    { num: 20, title: "Feature 05: Mill Console & Dispatch Stream", cat: "FEATURE 05" },
    { num: 21, title: "Complete 7-Layer Master Architecture", cat: "ARCHITECTURE" },
    { num: 22, title: "Production Impact & Technical Q&A", cat: "CONCLUSION" }
  ];

  // ==========================================================================
  // VIEWPORT AUTO-SCALING (16:9 1920x1080)
  // ==========================================================================
  function handleResize() {
    const targetW = 1920;
    const targetH = 1080;
    const windowW = window.innerWidth;
    const windowH = window.innerHeight;

    const scale = Math.min(windowW / targetW, windowH / targetH);
    stageScaler.style.transform = `scale(${scale})`;
  }

  // ==========================================================================
  // NAVIGATION LOGIC
  // ==========================================================================
  function goToSlide(targetIndex) {
    if (targetIndex < 1) targetIndex = 1;
    if (targetIndex > totalSlides) targetIndex = totalSlides;

    slides.forEach((slide) => {
      const idx = parseInt(slide.dataset.slide, 10);
      if (idx === targetIndex) {
        slide.classList.add('active');
        // Update category indicator
        if (categoryIndicator) {
          categoryIndicator.textContent = slide.dataset.category || 'AUTOTASKX';
        }
      } else {
        slide.classList.remove('active');
      }
    });

    currentSlide = targetIndex;

    // Update Counter
    if (currentSlideDisplay) {
      currentSlideDisplay.textContent = currentSlide.toString().padStart(2, '0');
    }

    // Update Progress Bar
    if (progressBar) {
      const progressPercent = (currentSlide / totalSlides) * 100;
      progressBar.style.width = `${progressPercent}%`;
    }

    // Update Presenter Notes
    updatePresenterNotes();

    // Trigger canvas loop if Slide 17 is active
    if (currentSlide === 17) {
      startCanvasTelemetry();
    } else {
      stopCanvasTelemetry();
    }
  }

  function nextSlide() {
    if (currentSlide < totalSlides) {
      goToSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      goToSlide(currentSlide - 1);
    }
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch((err) => {
        console.warn(`Error attempting to enable fullscreen: ${err.message}`);
      });
      isFullscreen = true;
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
        isFullscreen = false;
      }
    }
  }

  // ==========================================================================
  // SLIDE OVERVIEW MODAL
  // ==========================================================================
  function populateOverview() {
    overviewGrid.innerHTML = '';
    slideTitles.forEach((item) => {
      const card = document.createElement('div');
      card.className = `overview-card ${item.num === currentSlide ? 'active' : ''}`;
      card.innerHTML = `
        <span class="oc-num">SLIDE ${item.num.toString().padStart(2, '0')}</span>
        <h4 class="oc-title">${item.title}</h4>
        <span class="oc-cat">${item.cat}</span>
      `;
      card.addEventListener('click', () => {
        goToSlide(item.num);
        closeOverview();
      });
      overviewGrid.appendChild(card);
    });
  }

  function openOverview() {
    populateOverview();
    overviewModal.classList.remove('modal-hidden');
  }

  function closeOverview() {
    overviewModal.classList.add('modal-hidden');
  }

  // ==========================================================================
  // PRESENTER NOTES
  // ==========================================================================
  function updatePresenterNotes() {
    if (notesContent) {
      notesContent.innerHTML = presenterNotes[currentSlide] || 'No specific notes for this slide.';
    }
  }

  function toggleNotes() {
    notesDrawer.classList.toggle('drawer-hidden');
  }

  // ==========================================================================
  // KEYBOARD NAVIGATION
  // ==========================================================================
  function handleKeyDown(e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case ' ':
      case 'PageDown':
      case 'Enter':
        e.preventDefault();
        nextSlide();
        break;

      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
      case 'Backspace':
        e.preventDefault();
        prevSlide();
        break;

      case 'Home':
        e.preventDefault();
        goToSlide(1);
        break;

      case 'End':
        e.preventDefault();
        goToSlide(totalSlides);
        break;

      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      case 'o':
      case 'O':
        e.preventDefault();
        if (overviewModal.classList.contains('modal-hidden')) {
          openOverview();
        } else {
          closeOverview();
        }
        break;

      case 'n':
      case 'N':
        e.preventDefault();
        toggleNotes();
        break;

      case 'Escape':
        closeOverview();
        notesDrawer.classList.add('drawer-hidden');
        break;
    }
  }

  // ==========================================================================
  // INTERACTIVE AI QUERY SIMULATOR (SLIDE 12)
  // ==========================================================================
  function initAIQuerySimulator() {
    const queryButtons = document.querySelectorAll('.q-btn');
    const resultBox = document.getElementById('ai-query-result');

    const queries = {
      stenter: {
        title: "Stenter Frame MONFORTS-ST-01 (Chamber 4):",
        desc: "Experiencing an abnormal +6.2°C thermal overshoot over the last 45 minutes.",
        metrics: [
          { k: "Observed", v: "191.2°C" },
          { k: "Set Target", v: "185.0°C" },
          { k: "Root Cause", v: "Damper 4 valve actuator sticking at 82% open" }
        ],
        rec: "<strong>AI Operational Recommendation:</strong> Throttle Line Speed from 45 m/min to 38 m/min; dispatch shift technician to inspect pneumatic actuator on Chamber 4."
      },
      downtime: {
        title: "Downtime Variance Analysis (Gazipur Mill 01):",
        desc: "Total unplanned downtime today is 42 minutes vs 118 minutes yesterday (-64% reduction).",
        metrics: [
          { k: "Jet Dyeing", v: "12 min (Batch load)" },
          { k: "Stenter 01", v: "18 min (Filter clean)" },
          { k: "Weaving Looms", v: "12 min (Yarn break)" }
        ],
        rec: "<strong>AI Operational Recommendation:</strong> Preventative lint purge on Stenter filter prior to starting the next French Terry batch #B-4908."
      },
      quality: {
        title: "Right First Time (RFT) Risk Detection:",
        desc: "Dyeing Batch #B-4905 showing pH drift from 5.12 to 5.84 during fixation phase.",
        metrics: [
          { k: "Target pH", v: "5.0 – 5.2" },
          { k: "Current pH", v: "5.84 (Elevated)" },
          { k: "Risk Factor", v: "Uneven dye fixation / shade blotchiness" }
        ],
        rec: "<strong>AI Operational Recommendation:</strong> Automated acetic acid buffer injection (1.2 Liters) recommended immediately to stabilize liquor bath."
      }
    };

    queryButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        queryButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const qKey = btn.dataset.q;
        const data = queries[qKey];
        if (data && resultBox) {
          resultBox.innerHTML = `
            <p class="arb-p"><strong>${data.title}</strong> ${data.desc}</p>
            <div class="arb-metrics">
              ${data.metrics.map(m => `<div>${m.k}: <strong>${m.v}</strong></div>`).join('')}
            </div>
            <div class="arb-rec">${data.rec}</div>
          `;
        }
      });
    });
  }

  // ==========================================================================
  // INTERACTIVE ERP CONFIG TABS (SLIDE 20)
  // ==========================================================================
  function initERPConfigTabs() {
    const tabs = document.querySelectorAll('.ecp-tab');
    const endpointInput = document.querySelector('.ecp-form input[type="text"]');

    const erpEndpoints = {
      'Datatex NOW': 'https://erp-gw.gazipur-mill01.autotaskx.io/datatex/v2',
      'SAP S/4HANA': 'https://s4hana.enterprise.autotaskx.io/sap/opu/odata/sap/PP_ORDER_SRV',
      'Infor M3': 'https://infor-m3.cloud.autotaskx.io/m3api-rest/v2/execute',
      'Generic REST': 'https://api.mill-custom-erp.com/v1/manufacturing'
    };

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const erpName = tab.textContent.trim();
        if (endpointInput && erpEndpoints[erpName]) {
          endpointInput.value = erpEndpoints[erpName];
        }
      });
    });
  }

  // ==========================================================================
  // REAL-TIME CANVAS TELEMETRY WAVEFORM (SLIDE 17)
  // ==========================================================================
  let canvas, ctx;
  let dataPointsTemp = [];
  let dataPointsPress = [];
  let dataPointsSpeed = [];
  const maxPoints = 120;
  let baseTemp = 130.0;
  let basePress = 2.80;
  let baseSpeed = 240.0;

  function initCanvas() {
    canvas = document.getElementById('live-telemetry-canvas');
    if (!canvas) return;
    ctx = canvas.getContext('2d');

    // Fill initial data
    for (let i = 0; i < maxPoints; i++) {
      dataPointsTemp.push(baseTemp + (Math.random() - 0.5) * 0.8);
      dataPointsPress.push(basePress + (Math.random() - 0.5) * 0.08);
      dataPointsSpeed.push(baseSpeed + (Math.random() - 0.5) * 4.0);
    }
  }

  function startCanvasTelemetry() {
    if (!canvas) initCanvas();
    if (!animFrameId) {
      drawCanvasFrame();
    }
  }

  function stopCanvasTelemetry() {
    if (animFrameId) {
      cancelAnimationFrame(animFrameId);
      animFrameId = null;
    }
  }

  let frameCount = 0;
  function drawCanvasFrame() {
    if (!canvas || !ctx) return;

    frameCount++;
    if (frameCount % 6 === 0) { // Update every ~100ms
      // Add next point with slight noise
      const nextTemp = baseTemp + Math.sin(Date.now() / 2000) * 0.4 + (Math.random() - 0.5) * 0.3;
      const nextPress = basePress + Math.cos(Date.now() / 2400) * 0.05 + (Math.random() - 0.5) * 0.03;
      const nextSpeed = baseSpeed + (Math.random() - 0.5) * 2.0;

      dataPointsTemp.shift();
      dataPointsTemp.push(nextTemp);

      dataPointsPress.shift();
      dataPointsPress.push(nextPress);

      dataPointsSpeed.shift();
      dataPointsSpeed.push(nextSpeed);

      // Update text gauges on Slide 17
      const valTemp = document.getElementById('val-temp');
      const valPress = document.getElementById('val-press');
      if (valTemp) valTemp.textContent = nextTemp.toFixed(2);
      if (valPress) valPress.textContent = nextPress.toFixed(2);
    }

    const w = canvas.width;
    const h = canvas.height;

    // Clear background
    ctx.fillStyle = '#0B132B';
    ctx.fillRect(0, 0, w, h);

    // Draw Grid Lines
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
    ctx.lineWidth = 1;
    const gridYCount = 6;
    for (let i = 1; i < gridYCount; i++) {
      const y = (h / gridYCount) * i;
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // Function to draw a line graph
    function drawLine(points, minVal, maxVal, color) {
      ctx.strokeStyle = color;
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const stepX = w / (points.length - 1);
      for (let i = 0; i < points.length; i++) {
        const val = points[i];
        const normalizedY = (val - minVal) / (maxVal - minVal);
        const y = h - (normalizedY * (h - 40) + 20);
        const x = i * stepX;

        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      ctx.stroke();

      // Draw subtle glow under line
      ctx.lineTo(w, h);
      ctx.lineTo(0, h);
      ctx.closePath();
      const grad = ctx.createLinearGradient(0, 0, 0, h);
      grad.addColorStop(0, color.replace(')', ', 0.15)').replace('rgb', 'rgba'));
      grad.addColorStop(1, 'rgba(11, 19, 43, 0)');
      ctx.fillStyle = grad;
      ctx.fill();
    }

    // Draw 3 lines
    drawLine(dataPointsTemp, 128.0, 132.0, 'rgb(239, 68, 68)');
    drawLine(dataPointsPress, 2.60, 3.10, 'rgb(56, 189, 248)');
    drawLine(dataPointsSpeed, 220.0, 260.0, 'rgb(16, 185, 129)');

    if (currentSlide === 17) {
      animFrameId = requestAnimationFrame(drawCanvasFrame);
    }
  }

  // ==========================================================================
  // INITIALIZATION
  // ==========================================================================
  function init() {
    window.addEventListener('resize', handleResize);
    window.addEventListener('keydown', handleKeyDown);

    if (btnPrev) btnPrev.addEventListener('click', prevSlide);
    if (btnNext) btnNext.addEventListener('click', nextSlide);
    if (btnFullscreen) btnFullscreen.addEventListener('click', toggleFullscreen);
    if (btnOverview) btnOverview.addEventListener('click', openOverview);
    if (btnCloseOverview) btnCloseOverview.addEventListener('click', closeOverview);
    if (btnNotes) btnNotes.addEventListener('click', toggleNotes);
    if (btnCloseNotes) btnCloseNotes.addEventListener('click', () => notesDrawer.classList.add('drawer-hidden'));

    if (overviewModal) {
      const backdrop = overviewModal.querySelector('.modal-backdrop');
      if (backdrop) backdrop.addEventListener('click', closeOverview);
    }

    handleResize();
    initAIQuerySimulator();
    initERPConfigTabs();
    initCanvas();
    goToSlide(1);

    console.log("AutoTaskX Presentation Platform initialized. Press 'O' for Overview, 'N' for Notes, 'F' for Fullscreen.");
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
