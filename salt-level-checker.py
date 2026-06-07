<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Salt Level Checker</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet" />

  <style>
    /* ─── Reset & Base ────────────────────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:          #f0ece4;
      --panel:       #1c2333;
      --panel-light: #243044;
      --panel-rim:   #0e1520;
      --rim-shine:   #2e4060;
      --amber:       #c8954a;
      --amber-dim:   #7a5a2a;
      --text-light:  #d4cfc5;
      --text-dim:    #6b7a8d;
      --safe:        #4caf7d;
      --safe-glow:   rgba(76, 175, 125, 0.28);
      --danger:      #d9534f;
      --danger-glow: rgba(217, 83, 79, 0.28);
      --warn:        #e0933c;
      --warn-glow:   rgba(224, 147, 60, 0.22);
      --neutral:     #556070;
      --font-display: 'Playfair Display', Georgia, serif;
      --font-mono:    'IBM Plex Mono', 'Courier New', monospace;
    }

    html, body {
      min-height: 100%;
    }

    body {
      background-color: var(--bg);
      background-image:
        radial-gradient(ellipse at 20% 10%, rgba(200,149,74,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 90%, rgba(28,35,51,0.06) 0%, transparent 50%),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
      background-attachment: fixed;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem 1rem;
      font-family: var(--font-mono);
    }

    /* ─── Instrument Panel Card ───────────────────────────────────── */
    .instrument {
      width: 100%;
      max-width: 440px;
      background: var(--panel);
      border-radius: 18px;
      box-shadow:
        0 0 0 1px var(--panel-rim),
        0 0 0 2px var(--rim-shine),
        0 4px 6px rgba(0,0,0,0.3),
        0 20px 60px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.04);
      overflow: hidden;
      position: relative;
    }

    /* Top bezel strip */
    .instrument::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--panel-rim) 0%, var(--amber) 30%, var(--amber-dim) 55%, var(--panel-rim) 100%);
      opacity: 0.9;
    }

    /* ─── Header / Nameplate ──────────────────────────────────────── */
    .nameplate {
      padding: 1.75rem 2rem 1.25rem;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      display: flex;
      align-items: flex-end;
      gap: 1rem;
      position: relative;
    }

    .nameplate-badge {
      width: 36px;
      height: 36px;
      flex-shrink: 0;
      margin-bottom: 2px;
    }

    .nameplate-text {
      flex: 1;
    }

    .nameplate-label {
      font-family: var(--font-mono);
      font-size: 0.6rem;
      font-weight: 500;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--amber);
      margin-bottom: 0.2rem;
    }

    .nameplate-title {
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 1.55rem;
      color: var(--text-light);
      line-height: 1;
      letter-spacing: -0.01em;
    }

    .nameplate-model {
      font-family: var(--font-mono);
      font-size: 0.58rem;
      color: var(--text-dim);
      letter-spacing: 0.12em;
      margin-top: 0.3rem;
    }

    /* ─── Main Body ───────────────────────────────────────────────── */
    .panel-body {
      padding: 1.5rem 2rem 2rem;
    }

    /* ─── Input Row ───────────────────────────────────────────────── */
    .input-section {
      margin-bottom: 1.5rem;
    }

    .input-label {
      display: block;
      font-size: 0.6rem;
      font-weight: 500;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-bottom: 0.5rem;
    }

    .input-row {
      display: flex;
      gap: 0.6rem;
      align-items: stretch;
    }

    .input-wrapper {
      flex: 1;
      position: relative;
    }

    .salt-input {
      width: 100%;
      background: var(--panel-light);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: 8px;
      padding: 0.75rem 3.2rem 0.75rem 1rem;
      font-family: var(--font-mono);
      font-size: 1.05rem;
      font-weight: 400;
      color: var(--text-light);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
      -moz-appearance: textfield;
    }
    .salt-input::-webkit-outer-spin-button,
    .salt-input::-webkit-inner-spin-button { -webkit-appearance: none; }

    .salt-input::placeholder {
      color: var(--text-dim);
      opacity: 0.6;
    }

    .salt-input:focus {
      border-color: var(--amber);
      box-shadow: 0 0 0 3px rgba(200,149,74,0.15), inset 0 1px 3px rgba(0,0,0,0.3);
    }

    .input-unit {
      position: absolute;
      right: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.65rem;
      font-weight: 500;
      letter-spacing: 0.08em;
      color: var(--amber-dim);
      pointer-events: none;
      text-transform: uppercase;
    }

    .check-btn {
      background: var(--amber);
      border: none;
      border-radius: 8px;
      padding: 0 1.25rem;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--panel);
      cursor: pointer;
      transition: background 0.15s, transform 0.1s, box-shadow 0.15s;
      box-shadow: 0 2px 8px rgba(200,149,74,0.3), inset 0 1px 0 rgba(255,255,255,0.2);
      position: relative;
      overflow: hidden;
      white-space: nowrap;
    }

    .check-btn::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, rgba(255,255,255,0.12), transparent);
      pointer-events: none;
    }

    .check-btn:hover {
      background: #d9a55e;
      box-shadow: 0 4px 14px rgba(200,149,74,0.4), inset 0 1px 0 rgba(255,255,255,0.25);
    }

    .check-btn:active {
      transform: translateY(1px);
      box-shadow: 0 1px 4px rgba(200,149,74,0.25);
    }

    /* ─── Gauge ───────────────────────────────────────────────────── */
    .gauge-section {
      margin-bottom: 1.25rem;
    }

    .gauge-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 0.45rem;
    }

    .gauge-label {
      font-size: 0.58rem;
      font-weight: 500;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--text-dim);
    }

    .gauge-reading {
      font-size: 0.95rem;
      font-weight: 300;
      color: var(--text-light);
      transition: color 0.4s;
      font-style: italic;
    }

    .gauge-reading.has-value {
      font-style: normal;
      font-weight: 500;
    }

    .gauge-track {
      height: 8px;
      background: rgba(255,255,255,0.05);
      border-radius: 99px;
      overflow: hidden;
      border: 1px solid rgba(0,0,0,0.25);
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);
      position: relative;
    }

    .gauge-fill {
      height: 100%;
      width: 0%;
      border-radius: 99px;
      transition: width 0.7s cubic-bezier(0.34, 1.2, 0.64, 1), background 0.5s;
      background: var(--neutral);
      position: relative;
    }

    .gauge-fill::after {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 40%;
      background: rgba(255,255,255,0.18);
      border-radius: 99px;
    }

    .gauge-fill.safe {
      background: linear-gradient(90deg, var(--safe) 0%, #6fcf97 100%);
    }

    .gauge-fill.danger {
      background: linear-gradient(90deg, var(--amber) 0%, var(--danger) 100%);
    }

    .gauge-fill.warn {
      background: linear-gradient(90deg, #d9a55e 0%, var(--warn) 100%);
    }

    /* Threshold tick mark */
    .gauge-threshold {
      position: absolute;
      top: -3px;
      bottom: -3px;
      left: 50%;
      width: 2px;
      background: rgba(255,255,255,0.2);
      border-radius: 99px;
      pointer-events: none;
    }

    .gauge-scale {
      display: flex;
      justify-content: space-between;
      margin-top: 0.3rem;
    }

    .gauge-scale span {
      font-size: 0.52rem;
      color: var(--text-dim);
      letter-spacing: 0.05em;
    }

    /* ─── Result Display ──────────────────────────────────────────── */
    .result-card {
      background: var(--panel-light);
      border: 1px solid rgba(255,255,255,0.05);
      border-radius: 10px;
      padding: 1.1rem 1.25rem;
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 0.75rem;
      min-height: 74px;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.25);
      position: relative;
      overflow: hidden;
      transition: box-shadow 0.4s;
    }

    .result-card.glow-safe {
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.25), 0 0 0 1px rgba(76,175,125,0.25), 0 4px 20px var(--safe-glow);
    }

    .result-card.glow-danger {
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.25), 0 0 0 1px rgba(217,83,79,0.25), 0 4px 20px var(--danger-glow);
    }

    .result-card.glow-warn {
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.25), 0 0 0 1px rgba(224,147,60,0.25), 0 4px 20px var(--warn-glow);
    }

    .result-main {
      min-width: 0;
    }

    .result-label {
      font-size: 0.56rem;
      font-weight: 500;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-bottom: 0.25rem;
    }

    .result-value {
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 600;
      color: var(--text-light);
      letter-spacing: -0.02em;
      line-height: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .result-value.placeholder {
      font-size: 1rem;
      font-weight: 300;
      font-style: italic;
      color: var(--text-dim);
      opacity: 0.5;
    }

    /* Status pill */
    .status-pill {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
      flex-shrink: 0;
    }

    .status-dot {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: rgba(255,255,255,0.04);
      border: 2px solid rgba(255,255,255,0.06);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.4s cubic-bezier(0.34, 1.3, 0.64, 1);
      position: relative;
    }

    .status-dot.active-safe {
      background: rgba(76,175,125,0.12);
      border-color: var(--safe);
      box-shadow: 0 0 12px var(--safe-glow), inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .status-dot.active-danger {
      background: rgba(217,83,79,0.12);
      border-color: var(--danger);
      box-shadow: 0 0 12px var(--danger-glow), inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .status-dot.active-warn {
      background: rgba(224,147,60,0.12);
      border-color: var(--warn);
      box-shadow: 0 0 10px var(--warn-glow), inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .status-icon {
      width: 18px;
      height: 18px;
      opacity: 0.25;
      transition: opacity 0.3s, transform 0.4s cubic-bezier(0.34, 1.5, 0.64, 1);
    }

    .status-dot.active-safe   .status-icon,
    .status-dot.active-danger .status-icon,
    .status-dot.active-warn   .status-icon {
      opacity: 1;
      transform: scale(1.05);
    }

    .status-text {
      font-size: 0.58rem;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-dim);
      transition: color 0.3s;
    }

    .status-text.safe   { color: var(--safe); }
    .status-text.danger { color: var(--danger); }
    .status-text.warn   { color: var(--warn); }

    /* ─── Footer ──────────────────────────────────────────────────── */
    .panel-footer {
      padding: 0.85rem 2rem 1.25rem;
      border-top: 1px solid rgba(255,255,255,0.04);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .footer-spec {
      font-size: 0.54rem;
      color: var(--text-dim);
      letter-spacing: 0.1em;
      line-height: 1.7;
    }

    .footer-spec strong {
      color: rgba(212,207,197,0.4);
      display: block;
      font-size: 0.5rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-weight: 500;
    }

    .led-cluster {
      display: flex;
      gap: 5px;
      align-items: center;
    }

    .led {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--panel-rim);
      border: 1px solid rgba(0,0,0,0.4);
      transition: background 0.3s, box-shadow 0.3s;
    }

    .led.on-safe   { background: var(--safe); box-shadow: 0 0 6px var(--safe); }
    .led.on-warn   { background: var(--warn); box-shadow: 0 0 6px var(--warn); }
    .led.on-danger { background: var(--danger); box-shadow: 0 0 6px var(--danger); }
    .led.pulse { animation: ledPulse 1.6s ease-in-out infinite; }

    @keyframes ledPulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }

    /* ─── Enter key hint ──────────────────────────────────────────── */
    .hint {
      text-align: center;
      font-size: 0.53rem;
      color: var(--text-dim);
      letter-spacing: 0.1em;
      margin-top: 0.85rem;
      opacity: 0.5;
    }

    /* ─── Responsive ──────────────────────────────────────────────── */
    @media (max-width: 480px) {
      .instrument { border-radius: 14px; }
      .nameplate  { padding: 1.5rem 1.5rem 1rem; }
      .panel-body { padding: 1.25rem 1.5rem 1.5rem; }
      .panel-footer { padding: 0.75rem 1.5rem 1rem; }
      .nameplate-title { font-size: 1.3rem; }
    }
  </style>
</head>
<body>

  <div class="instrument" role="main">

    <!-- Nameplate -->
    <div class="nameplate">
      <svg class="nameplate-badge" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect width="36" height="36" rx="6" fill="rgba(200,149,74,0.1)" stroke="rgba(200,149,74,0.25)" stroke-width="1"/>
        <path d="M18 8C18 8 11 14 11 20a7 7 0 0014 0C25 14 18 8 18 8z" fill="rgba(200,149,74,0.2)" stroke="#c8954a" stroke-width="1.4" stroke-linejoin="round"/>
        <path d="M15 21.5a3 3 0 006 0" stroke="rgba(200,149,74,0.7)" stroke-width="1.2" stroke-linecap="round" fill="none"/>
        <circle cx="18" cy="20" r="1.5" fill="#c8954a" opacity="0.8"/>
      </svg>
      <div class="nameplate-text">
        <div class="nameplate-label">Analytical Instrument</div>
        <div class="nameplate-title">Salt Level Checker</div>
        <div class="nameplate-model">MODEL SLC-1 &nbsp;·&nbsp; RANGE 0–2000 PPM</div>
      </div>
    </div>

    <!-- Main Body -->
    <div class="panel-body">

      <!-- Input -->
      <div class="input-section">
        <label class="input-label" for="saltInput">Salinity Input</label>
        <div class="input-row">
          <div class="input-wrapper">
            <input
              id="saltInput"
              class="salt-input"
              type="number"
              min="0"
              max="9999"
              step="any"
              placeholder="0.00"
              autocomplete="off"
              aria-label="Salt level in parts per million"
            />
            <span class="input-unit">ppm</span>
          </div>
          <button class="check-btn" id="checkBtn" aria-label="Check salt level">
            Analyze
          </button>
        </div>
      </div>

      <!-- Gauge -->
      <div class="gauge-section" aria-hidden="true">
        <div class="gauge-header">
          <span class="gauge-label">Concentration Level</span>
          <span class="gauge-reading" id="gaugeReading">awaiting input</span>
        </div>
        <div class="gauge-track">
          <div class="gauge-fill" id="gaugeFill"></div>
          <div class="gauge-threshold" style="left: 50%" title="1000 ppm threshold"></div>
        </div>
        <div class="gauge-scale">
          <span>0</span>
          <span>500</span>
          <span>1000 ⬦</span>
          <span>1500</span>
          <span>2000+</span>
        </div>
      </div>

      <!-- Result -->
      <div class="result-card" id="resultCard" aria-live="polite">
        <div class="result-main">
          <div class="result-label">Measurement Reading</div>
          <div class="result-value placeholder" id="resultValue">— — &nbsp;ppm</div>
        </div>
        <div class="status-pill">
          <div class="status-dot" id="statusDot">
            <svg class="status-icon" id="statusIcon" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <circle cx="9" cy="9" r="7.5" stroke="currentColor" stroke-width="1.5"/>
              <path d="M6 9l2 2 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <span class="status-text" id="statusText">—</span>
        </div>
      </div>

      <p class="hint">Press Enter or click Analyze to check</p>
    </div>

    <!-- Footer / spec plate -->
    <div class="panel-footer">
      <div class="footer-spec">
        <strong>Safe Threshold</strong>
        ≤ 1,000 ppm
      </div>
      <div class="footer-spec" style="text-align:center">
        <strong>Unit</strong>
        mg/L (ppm)
      </div>
      <div>
        <div class="led-cluster" aria-hidden="true">
          <div class="led" id="ledSafe"   title="Safe range"></div>
          <div class="led" id="ledWarn"   title="Caution range"></div>
          <div class="led" id="ledDanger" title="Danger range"></div>
        </div>
        <div class="footer-spec" style="text-align:right;margin-top:4px">
          <strong>Status</strong>
          <span id="footerStatus">STANDBY</span>
        </div>
      </div>
    </div>

  </div>

  <script>
    const THRESHOLD = 1000;
    const MAX_GAUGE  = 2000;

    const saltInput   = document.getElementById('saltInput');
    const checkBtn    = document.getElementById('checkBtn');
    const gaugeReading = document.getElementById('gaugeReading');
    const gaugeFill   = document.getElementById('gaugeFill');
    const resultCard  = document.getElementById('resultCard');
    const resultValue = document.getElementById('resultValue');
    const statusDot   = document.getElementById('statusDot');
    const statusIcon  = document.getElementById('statusIcon');
    const statusText  = document.getElementById('statusText');
    const ledSafe     = document.getElementById('ledSafe');
    const ledWarn     = document.getElementById('ledWarn');
    const ledDanger   = document.getElementById('ledDanger');
    const footerStatus = document.getElementById('footerStatus');

    // SVG paths for icons
    const iconPaths = {
      safe:   '<circle cx="9" cy="9" r="7.5" stroke="currentColor" stroke-width="1.5"/><path d="M6 9l2 2 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>',
      danger: '<circle cx="9" cy="9" r="7.5" stroke="currentColor" stroke-width="1.5"/><path d="M9 5.5v4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="9" cy="12.5" r="0.75" fill="currentColor"/>',
      warn:   '<circle cx="9" cy="9" r="7.5" stroke="currentColor" stroke-width="1.5"/><path d="M9 5.5v4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="9" cy="12.5" r="0.75" fill="currentColor"/>',
    };

    function resetLeds() {
      ledSafe.className   = 'led';
      ledWarn.className   = 'led';
      ledDanger.className = 'led';
    }

    function analyze() {
      const raw = saltInput.value.trim();
      const val = parseFloat(raw);

      if (raw === '' || isNaN(val)) {
        // Error state
        resultValue.textContent = 'invalid input';
        resultValue.classList.add('placeholder');
        resultValue.style.color = 'var(--warn)';

        resultCard.className = 'result-card glow-warn';
        statusDot.className  = 'status-dot active-warn';
        statusIcon.innerHTML = iconPaths.warn;
        statusIcon.style.color = 'var(--warn)';
        statusText.textContent  = 'ERROR';
        statusText.className    = 'status-text warn';

        gaugeFill.style.width = '0%';
        gaugeFill.className   = 'gauge-fill';
        gaugeReading.textContent = 'invalid input';
        gaugeReading.classList.remove('has-value');
        gaugeReading.style.color = 'var(--warn)';

        resetLeds();
        ledWarn.className = 'led on-warn pulse';
        footerStatus.textContent = 'ERROR';
        return;
      }

      const clampedPct = Math.min(val / MAX_GAUGE, 1) * 100;
      const formatted  = val.toLocaleString('en-US', { maximumFractionDigits: 2 });

      // Update gauge
      gaugeFill.style.width  = clampedPct + '%';
      gaugeReading.textContent = formatted + ' ppm';
      gaugeReading.classList.add('has-value');
      gaugeReading.style.color = '';

      // Update result value
      resultValue.textContent = formatted + ' ppm';
      resultValue.classList.remove('placeholder');
      resultValue.style.color = '';

      resetLeds();

      if (val <= THRESHOLD) {
        // Safe
        gaugeFill.className  = 'gauge-fill safe';
        resultCard.className = 'result-card glow-safe';
        statusDot.className  = 'status-dot active-safe';
        statusIcon.innerHTML = iconPaths.safe;
        statusIcon.style.color = 'var(--safe)';
        statusText.textContent  = 'SAFE';
        statusText.className    = 'status-text safe';
        ledSafe.className       = 'led on-safe';
        footerStatus.textContent = 'CLEAR';
      } else {
        // Too Salty
        gaugeFill.className  = 'gauge-fill danger';
        resultCard.className = 'result-card glow-danger';
        statusDot.className  = 'status-dot active-danger';
        statusIcon.innerHTML = iconPaths.danger;
        statusIcon.style.color = 'var(--danger)';
        statusText.textContent  = 'HIGH';
        statusText.className    = 'status-text danger';
        ledDanger.className     = 'led on-danger pulse';
        footerStatus.textContent = 'ALERT';
      }
    }

    checkBtn.addEventListener('click', analyze);
    saltInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') analyze();
    });

    // Focus input on load
    saltInput.focus();
  </script>
</body>
</html>
