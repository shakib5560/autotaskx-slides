/**
 * AutoTaskX — Industrial Textile Intelligence Platform
 * Simplified Keynote Slide Deck Presentation Engine (17 Slides)
 */

(function () {
  'use strict';

  // --- DOM Elements & Presentation State ---
  const stageScaler = document.getElementById('stage-scaler');
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length || 18;
  let currentSlide = 1;
  let isFullscreen = false;

  const progressBar = document.getElementById('progress-bar');
  const slideIndicator = document.getElementById('slide-indicator');
  const categoryIndicator = document.getElementById('slide-category-indicator');

  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnOverview = document.getElementById('btn-overview');
  const btnNotes = document.getElementById('btn-notes');
  const btnFullscreen = document.getElementById('btn-fullscreen');

  const overviewModal = document.getElementById('overview-modal');
  const btnCloseOverview = document.getElementById('btn-close-overview');
  const overviewBackdrop = document.getElementById('overview-backdrop');
  const overviewGrid = document.getElementById('overview-grid');

  const notesDrawer = document.getElementById('notes-drawer');
  const btnCloseNotes = document.getElementById('btn-close-notes');
  const notesContent = document.getElementById('notes-content');

  // --- Presenter Notes Data (Natural Conversational English) ---
  const PRESENTER_NOTES = {
    1: `<strong>What to say (30-45s):</strong><br>
        "Good morning. Today I'm presenting AutoTaskX — a software platform designed to connect every part of a textile factory. Right now, textile mills have high-tech dyeing jets, stenters, and laboratories, but they operate as disconnected islands. AutoTaskX brings them all into one intelligent, easy-to-use digital ecosystem."<br><br>
        <strong>What the visual means:</strong><br>
        The left side shows our four core pillars (smart chemistry, machine vision, live telemetry, and ERP bridge). The right card shows an active mill HUD from Gazipur running 24 connected machines.<br><br>
        <strong>Why it matters:</strong> Sets the stage immediately as an industrial software engineer who understands both software architecture and physical factory reality.`,

    2: `<strong>What to say (30-45s):</strong><br>
        "Let's look at the actual reality inside a modern textile factory. Despite millions of dollars in equipment, four big problems persist: operators still calculate dye recipes with pen and paper; machines operate completely disconnected; quality inspection photos get lost in personal phones; and managers only find out about fabric damage hours after thousands of meters are ruined."<br><br>
        <strong>Real-world example:</strong><br>
        If a stenter chamber overheats by just 10°C, 500 meters of cotton can turn yellow before anyone notices on the floor.<br><br>
        <strong>Why it matters:</strong> Grounds the entire presentation in real operational pain points, not theoretical abstractions.`,

    3: `<strong>What to say (30-45s):</strong><br>
        "Our answer is AutoTaskX. Rather than replacing physical factory machines, AutoTaskX provides five modular tools that share one central database: Color Formulation for the dye lab; Visual Quality Inspection for flaw detection; Production Intelligence for real-time speed and temperature; Textile OS to connect physical sensors; and ERP Integration to sync with existing business software."<br><br>
        <strong>What the visual means:</strong><br>
        Five clean module cards showing what each department uses. Every card has a clear industrial photo showing real equipment.<br><br>
        <strong>Why it matters:</strong> Shows that AutoTaskX is a comprehensive platform, not just a single one-off script.`,

    4: `<strong>What to say (30-45s):</strong><br>
        "Here is the complete journey of how AutoTaskX works from the shopfloor to the screen. First, physical machines run. Sensors and cameras capture physical reality. An industrial gateway collects those signals. AutoTaskX backend receives and organizes them. The database saves the history. And finally, the live dashboard displays real-time readings to managers. The entire journey happens in under 25 milliseconds."<br><br>
        <strong>What the visual means:</strong><br>
        A 6-step horizontal flow chart that is easy for the interviewer to visualize and remember.<br><br>
        <strong>Why it matters:</strong> Demonstrates end-to-end full stack architecture from hardware to user interface.`,

    5: `<strong>What to say (30-45s):</strong><br>
        "Feature 01 is Color Formulation. In textile dyeing, calculating chemical recipes for 100 kg of cotton fabric takes significant trial-and-error. With AutoTaskX, the lab technician enters the fabric type, weight, and target shade. The system calculates exact dye grams per kilogram and total quantities for the dispensary."<br><br>
        <strong>Real-world example:</strong><br>
        The right card shows an exact recipe for a 100 kg deep navy knit batch: 1,850g of Reactive Blue and 420g of Reactive Red with 600 liters of water.<br><br>
        <strong>Important note:</strong> Always clarify to the interviewer that software recipes are computational estimates that require standard lab beaker validation.`,

    6: `<strong>What to say (30-45s):</strong><br>
        "Feature 02 is Visual Quality Inspection. Fabric defects can be captured from two sources: continuous line-scan cameras like the Basler racer 2L mounted above an inspection frame, or smartphone cameras used by floor operators for spot checks. When an image is captured, the heavy photograph goes straight to AWS S3 Cloud Storage, while defect tags and locations are saved in our database."<br><br>
        <strong>What the visual means:</strong><br>
        Shows the contrast between automated 16K line scanning and flexible mobile spot-checking.<br><br>
        <strong>Why it matters:</strong> Demonstrates clean cloud architecture by keeping heavy images out of transactional databases.`,

    7: `<strong>What to say (30-45s):</strong><br>
        "Now let's look at the true engineering depth behind Feature 02. This sequence diagram illustrates how we handle high-frequency image acquisition without bottlenecking the system. When the Basler line-scan camera sends raw lines via CoaXPress, our Edge PC buffers them into a full TIFF image. Notice the parallel execution phase: the Edge PC requests a pre-signed S3 URL from FastAPI, and uploads the 20MB TIFF image directly to AWS S3 while concurrently emitting camera telemetry over MQTT. FastAPI never handles heavy image bytes in memory — it only persists metadata in PostgreSQL and notifies the Next.js frontend via WebSockets."<br><br>
        <strong>Technical highlights:</strong><br>
        Direct S3 offloading, parallel MQTT event distribution, and secure presigned GET delivery to the browser.<br><br>
        <strong>Why it matters:</strong> Proves production-grade distributed systems design to senior technical interviewers.`,

    8: `<strong>What to say (30-45s):</strong><br>
        "Feature 03 is Production Intelligence. First, here is how we solve machine problems: every machine sends live heat and speed over MQTT to our Digital Twin, our backend checks safe limits, and if heat gets too high, it turns red and sends an SMS in 3 seconds. Now here is what actually happened: on Stenter Line 03, the safe limit was 185°C, and the heat suddenly jumped to 192°C. Before AutoTaskX, hundreds of meters would burn. With our 3-second alert, the supervisor lowered the heat right away and saved the whole batch."<br><br>
        <strong>What the visual means:</strong><br>
        Left side shows our 4-step solution and the real Stenter Line 03 incident; right side shows live machine heat and status.<br><br>
        <strong>Why it matters:</strong> Clear problem-solving story showing exact backend protection in real production.`,

    9: `<strong>What to say (30-45s):</strong><br>
        "Feature 04 is Textile OS — the physical nervous system of the platform. Different factory machines use different physical wires, serial cables, or network ports. Textile OS uses industrial IoT gateways to read physical signals from temperature probes, pressure sensors, and power meters, converting them all into one unified software format."<br><br>
        <strong>What the visual means:</strong><br>
        The left side shows the physical devices we support. The right side shows the 5 simple steps to wire, configure, and connect any sensor.<br><br>
        <strong>Why it matters:</strong> Proves hands-on engineering knowledge of how software touches physical industrial hardware.`,

    10: `<strong>What to say (30-45s):</strong><br>
        "Let's trace one single sensor reading step by step. On Stenter #02, a PT100 temperature probe reads 185.5°C. The gateway reads that electrical voltage and creates a small data packet. It sends it over the factory network. AutoTaskX validates it and writes it to TimescaleDB. The dashboard screen immediately shows 185.5°C with a green status. You can click 'Animate Reading Pulse' to see the packet travel."<br><br>
        <strong>Interactive demo:</strong> Click the button in the top right to watch the packet pulse across all 6 nodes.<br><br>
        <strong>Why it matters:</strong> Clear, confident explanation of the complete data pipeline in plain English.`,

    11: `<strong>What to say (30-45s):</strong><br>
        "How do 50 machines talk to AutoTaskX without slowing down? We use MQTT. Think of MQTT as a digital post office: machines drop off small, lightweight telegrams, and the messaging server delivers them instantly. Most importantly, we follow a strict architecture rule: MQTT is only for small sensor numbers (under 1 KB). Large 20 MB fabric photos are uploaded separately via HTTPS directly to cloud storage."<br><br>
        <strong>Why it matters:</strong> Shows architectural maturity by decoupling high-frequency sensor telemetry from heavy file storage.`,

    12: `<strong>What to say (30-45s):</strong><br>
        "Where does all this factory information go? We use three specialized storage containers: PostgreSQL for organized business records like recipes and user accounts; TimescaleDB for continuous second-by-second measurements like temperature and pressure; and AWS S3 for large inspection photographs."<br><br>
        <strong>What the visual means:</strong><br>
        Three clean containers with everyday examples of what each one stores.<br><br>
        <strong>Why it matters:</strong> Explains database choices simply without confusing technical jargon.`,

    13: `<strong>What to say (30-45s):</strong><br>
        "Here is how data reaches the screen. A sensor reading is forwarded via MQTT, saved in TimescaleDB, and WebSockets push the update to the browser instantly without reloading the page. Notice the difference between Current Data (what is happening right now this second) and Historical Data (what happened over the last 8-hour shift)."<br><br>
        <strong>What the visual means:</strong><br>
        Contrasts live real-time dials for operators with historical trend lines for plant managers.<br><br>
        <strong>Why it matters:</strong> Demonstrates understanding of different user personas and real-time frontend engineering.`,

    14: `<strong>What to say (30-45s):</strong><br>
        "Textile factories already have enterprise software like SAP, Datatex NOW, or Infor. AutoTaskX does not replace them — it connects them to the shopfloor. The ERP sends work orders and customer recipes down to AutoTaskX, and AutoTaskX sends actual meters produced and chemical quantities consumed back up. No more manual paper data entry."<br><br>
        <strong>Before vs After:</strong><br>
        Before: Paper logs typed into ERP 2 days later with mistakes. After: Automated inventory sync as soon as fabric leaves the machine.`,

    15: `<strong>What to say (30-45s):</strong><br>
        "This slide brings everything together in one complete architecture map: Zone 1 is the physical factory with dye labs, cameras, and machines. Zone 2 is the gateway and network connection layer. Zone 3 is the AutoTaskX core with our backend and three specialized databases. Zone 4 is the live web interface and two-way ERP integration."<br><br>
        <strong>What the visual means:</strong><br>
        A 4-zone master blueprint summarizing the entire system.<br><br>
        <strong>Why it matters:</strong> Proves you can architect and explain an end-to-end industrial software solution.`,

    16: `<strong>What to say (30-45s):</strong><br>
        "What does the factory owner or general manager actually get? Instead of walking across noisy production floors and deciphering paper logs, they see complete reality on one screen: 24 active machines, 99.2% right-first-time quality, zero active temperature alerts, and 42,500 meters completed today. That means faster decisions, lower costs, and zero paperwork delays."<br><br>
        <strong>Why it matters:</strong> Ties all the technical engineering directly back to concrete business value and ROI.`,

    17: `<strong>What to say (30-45s):</strong><br>
        "Where can AutoTaskX go next? We have a phased, realistic roadmap: Stage 1 connects more legacy machines; Stage 2 expands automated AI defect classification; Stage 3 introduces deep historical recipe analytics; Stage 4 adds predictive maintenance warnings; and Stage 5 enables closed-loop autonomous machine adjustments."<br><br>
        <strong>Why it matters:</strong> Shows strategic product vision and honest engineering integrity about current vs future capabilities.`,

    18: `<strong>What to say (30-45s):</strong><br>
        "To conclude: AutoTaskX transforms disconnected textile factory operations into one unified, intelligent manufacturing platform. My name is Sheikh Shamiul Shakib, Backend Software Engineer and Computer Science graduate from BUBT. Thank you for your time, and I am very happy to answer any technical questions."<br><br>
        <strong>Why it matters:</strong> Professional, crisp, confident finish opening the floor for technical interview questions.`
  };

  // --- Dynamic 16:9 Stage Scaler ---
  function updateStageScale() {
    if (!stageScaler) return;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const targetWidth = 1920;
    const targetHeight = 1080;

    const scaleX = windowWidth / targetWidth;
    const scaleY = windowHeight / targetHeight;
    const scale = Math.min(scaleX, scaleY);

    stageScaler.style.transform = `scale(${scale})`;
  }

  // --- URL Hash Helper ---
  function getSlideFromHash() {
    const hash = window.location.hash;
    const match = hash.match(/#?(?:slide-)?(\d+)/i);
    if (match) {
      const num = parseInt(match[1], 10);
      if (num >= 1 && num <= totalSlides) return num;
    }
    return 1;
  }

  // --- Slide Navigation Engine ---
  function showSlide(index) {
    if (index < 1) index = 1;
    if (index > totalSlides) index = totalSlides;

    currentSlide = index;

    slides.forEach((slide, idx) => {
      const dataSlide = parseInt(slide.getAttribute('data-slide'), 10);
      const slideNum = !isNaN(dataSlide) ? dataSlide : (idx + 1);
      slide.classList.remove('active', 'prev');
      if (slideNum === currentSlide) {
        slide.classList.add('active');
        const cat = slide.getAttribute('data-category') || 'AUTOTASKX';
        if (categoryIndicator) categoryIndicator.textContent = cat;
      } else if (slideNum < currentSlide) {
        slide.classList.add('prev');
      }
    });

    // Update Progress Bar
    if (progressBar) {
      const progress = totalSlides > 1 ? ((currentSlide - 1) / (totalSlides - 1)) * 100 : 100;
      progressBar.style.width = `${progress}%`;
    }

    // Update Indicator
    if (slideIndicator) {
      const formattedCur = String(currentSlide).padStart(2, '0');
      const formattedTot = String(totalSlides).padStart(2, '0');
      slideIndicator.textContent = `${formattedCur} / ${formattedTot}`;
    }

    // Update URL hash without polluting browser history
    try {
      if (window.location.hash !== `#slide-${currentSlide}`) {
        history.replaceState(null, '', `#slide-${currentSlide}`);
      }
    } catch (e) {}

    // Update Presenter Notes
    updateNotesContent();

    // Update Overview Grid Active State
    updateOverviewActiveThumb();
  }

  function nextSlide() {
    if (currentSlide < totalSlides) {
      showSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      showSlide(currentSlide - 1);
    }
  }

  // --- Presenter Notes Drawer ---
  function toggleNotes() {
    if (!notesDrawer) return;
    notesDrawer.classList.toggle('drawer-hidden');
  }

  function updateNotesContent() {
    if (!notesContent) return;
    const noteHtml = PRESENTER_NOTES[currentSlide] || '<strong>Slide Notes:</strong><br>No specific notes for this slide.';
    notesContent.innerHTML = noteHtml;
  }

  // --- Overview Modal Engine ---
  function initOverviewGrid() {
    if (!overviewGrid) return;
    overviewGrid.innerHTML = '';

    slides.forEach((slide, idx) => {
      const dataSlide = parseInt(slide.getAttribute('data-slide'), 10);
      const slideNum = !isNaN(dataSlide) ? dataSlide : (idx + 1);
      const titleElem = slide.querySelector('h1, h2, h3, [class*="-title"], [class*="-heading"]') || slide.querySelector('.cover-subtitle');
      const titleText = titleElem ? titleElem.textContent.replace(/\s+/g, ' ').trim() : `Slide ${slideNum}`;
      const category = slide.getAttribute('data-category') || 'OVERVIEW';

      const thumb = document.createElement('div');
      thumb.className = 'thumb-card';
      thumb.setAttribute('data-target-slide', slideNum);

      thumb.innerHTML = `
        <span class="thumb-num">SLIDE ${String(slideNum).padStart(2, '0')}</span>
        <h4 class="thumb-title">${titleText}</h4>
        <span class="thumb-cat">${category}</span>
      `;

      thumb.addEventListener('click', () => {
        showSlide(slideNum);
        closeOverview();
      });

      overviewGrid.appendChild(thumb);
    });

    updateOverviewActiveThumb();
  }

  function updateOverviewActiveThumb() {
    const thumbs = document.querySelectorAll('.thumb-card');
    thumbs.forEach(t => {
      const target = parseInt(t.getAttribute('data-target-slide'), 10);
      if (target === currentSlide) {
        t.classList.add('active-thumb');
      } else {
        t.classList.remove('active-thumb');
      }
    });
  }

  function toggleOverview() {
    if (!overviewModal) return;
    if (overviewModal.classList.contains('modal-hidden')) {
      overviewModal.classList.remove('modal-hidden');
      updateOverviewActiveThumb();
    } else {
      closeOverview();
    }
  }

  function closeOverview() {
    if (overviewModal) overviewModal.classList.add('modal-hidden');
  }

  // --- Fullscreen Toggle ---
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.warn(err));
      isFullscreen = true;
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
        isFullscreen = false;
      }
    }
  }

  // --- Slide 09 Interactive Pulse Animation ---
  function initPulseAnimation() {
    const pulseBtn = document.getElementById('btn-pulse-packet');
    if (!pulseBtn) return;

    pulseBtn.addEventListener('click', () => {
      const nodes = [
        document.getElementById('tn-1'),
        document.getElementById('tn-2'),
        document.getElementById('tn-3'),
        document.getElementById('tn-4'),
        document.getElementById('tn-5'),
        document.getElementById('tn-6')
      ];

      const pulses = [
        document.getElementById('pulse-1'),
        document.getElementById('pulse-2'),
        document.getElementById('pulse-3'),
        document.getElementById('pulse-4'),
        document.getElementById('pulse-5')
      ];

      // Reset
      nodes.forEach(n => n && n.classList.remove('active-glow'));
      pulses.forEach(p => p && p.classList.remove('pulsing'));

      // Sequence chain animation
      nodes.forEach((node, i) => {
        setTimeout(() => {
          if (node) node.classList.add('active-glow');
          if (i > 0 && pulses[i - 1]) pulses[i - 1].classList.add('pulsing');

          setTimeout(() => {
            if (node) node.classList.remove('active-glow');
            if (i > 0 && pulses[i - 1]) pulses[i - 1].classList.remove('pulsing');
          }, 450);
        }, i * 380);
      });
    });
  }

  // --- Slide 03 Interactive Ecosystem Pulse ---
  function initSlide3Animation() {
    const triggerBtn = document.getElementById('s03-trigger-pulse');
    const cards = [
      document.getElementById('s03-card-1'),
      document.getElementById('s03-card-2'),
      document.getElementById('s03-card-3'),
      document.getElementById('s03-card-4'),
      document.getElementById('s03-card-5')
    ];

    function runWave() {
      cards.forEach(c => c && c.classList.remove('pulse-active'));
      cards.forEach((card, idx) => {
        setTimeout(() => {
          if (card) {
            card.classList.add('pulse-active');
            setTimeout(() => {
              card.classList.remove('pulse-active');
            }, 650);
          }
        }, idx * 160);
      });
    }

    if (triggerBtn) {
      triggerBtn.addEventListener('click', runWave);
    }

    cards.forEach(card => {
      if (card) {
        card.addEventListener('click', () => {
          card.classList.add('pulse-active');
          setTimeout(() => card.classList.remove('pulse-active'), 800);
        });
      }
    });
  }

  // --- Slide 04 Interactive Packet Pulse ---
  function initSlide4Animation() {
    const triggerBtn = document.getElementById('s04-trigger-pulse');
    if (!triggerBtn) return;

    triggerBtn.addEventListener('click', () => {
      const cards = [
        document.getElementById('s04-card-1'),
        document.getElementById('s04-card-2'),
        document.getElementById('s04-card-3'),
        document.getElementById('s04-card-4'),
        document.getElementById('s04-card-5'),
        document.getElementById('s04-card-6')
      ];

      cards.forEach(c => c && c.classList.remove('pulse-glow'));

      cards.forEach((card, idx) => {
        setTimeout(() => {
          if (card) {
            card.classList.add('pulse-glow');
            setTimeout(() => {
              card.classList.remove('pulse-glow');
            }, 600);
          }
        }, idx * 180);
      });
    });
  }

  // --- Keyboard Event Listeners ---
  function handleKeyDown(e) {
    // If overview modal open, Escape closes it
    if (overviewModal && !overviewModal.classList.contains('modal-hidden')) {
      if (e.key === 'Escape' || e.key === 'o' || e.key === 'O') {
        closeOverview();
        return;
      }
    }

    switch (e.key) {
      case 'ArrowRight':
      case ' ': // Spacebar
      case 'PageDown':
        e.preventDefault();
        nextSlide();
        break;

      case 'ArrowLeft':
      case 'Backspace':
      case 'PageUp':
        e.preventDefault();
        prevSlide();
        break;

      case 'Home':
        e.preventDefault();
        showSlide(1);
        break;

      case 'End':
        e.preventDefault();
        showSlide(totalSlides);
        break;

      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      case 'o':
      case 'O':
        e.preventDefault();
        toggleOverview();
        break;

      case 'n':
      case 'N':
        e.preventDefault();
        toggleNotes();
        break;

      case 'g':
      case 'G':
        e.preventDefault();
        window.open('guide.html', '_blank');
        break;

      case 'Escape':
        if (notesDrawer && !notesDrawer.classList.contains('drawer-hidden')) {
          notesDrawer.classList.add('drawer-hidden');
        }
        break;

      default:
        break;
    }
  }

  // --- Initialization ---
  function init() {
    updateStageScale();
    window.addEventListener('resize', updateStageScale);
    window.addEventListener('orientationchange', updateStageScale);

    document.addEventListener('keydown', handleKeyDown);

    if (btnNext) btnNext.addEventListener('click', nextSlide);
    if (btnPrev) btnPrev.addEventListener('click', prevSlide);
    if (btnOverview) btnOverview.addEventListener('click', toggleOverview);
    if (btnNotes) btnNotes.addEventListener('click', toggleNotes);
    if (btnFullscreen) btnFullscreen.addEventListener('click', toggleFullscreen);

    if (btnCloseOverview) btnCloseOverview.addEventListener('click', closeOverview);
    if (overviewBackdrop) overviewBackdrop.addEventListener('click', closeOverview);
    if (btnCloseNotes) btnCloseNotes.addEventListener('click', () => notesDrawer.classList.add('drawer-hidden'));

    initOverviewGrid();
    initPulseAnimation();
    initSlide3Animation();
    initSlide4Animation();

    // Show initial slide based on URL hash (default slide 1)
    const initialSlide = getSlideFromHash();
    showSlide(initialSlide);

    // Support browser back/forward and hash links
    window.addEventListener('hashchange', () => {
      const target = getSlideFromHash();
      if (target !== currentSlide) {
        showSlide(target);
      }
    });

    // Touch swipe navigation for mobile devices
    let touchStartX = 0;
    let touchStartY = 0;
    const stage = document.getElementById('app-container');
    if (stage) {
      stage.addEventListener('touchstart', (e) => {
        if (e.changedTouches && e.changedTouches.length === 1) {
          touchStartX = e.changedTouches[0].clientX;
          touchStartY = e.changedTouches[0].clientY;
        }
      }, { passive: true });
      stage.addEventListener('touchend', (e) => {
        if (!e.changedTouches || e.changedTouches.length !== 1) return;
        if (overviewModal && !overviewModal.classList.contains('modal-hidden')) return;
        if (notesDrawer && !notesDrawer.classList.contains('drawer-hidden')) return;
        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy) * 1.4) {
          if (dx < 0) nextSlide();
          else prevSlide();
        }
      }, { passive: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
