<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Lexicon</title>
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #f2f2f7;
      --surface: rgba(255,255,255,0.72);
      --text-primary: #1d1d1f;
      --text-secondary: #6e6e73;
      --text-tertiary: #aeaeb2;
      --accent: #0071e3;
      --green: #34c759;
      --separator: rgba(0,0,0,0.08);
      --shadow-md: 0 8px 32px rgba(0,0,0,0.08);
      --radius: 18px;
      --radius-sm: 12px;
    }

    html { -webkit-font-smoothing: antialiased; }

    body {
      background: var(--bg);
      color: var(--text-primary);
      font-family: 'Lato', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 64px 20px 100px;
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background:
        radial-gradient(ellipse at 20% 20%, rgba(0,113,227,0.04) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 80%, rgba(0,113,227,0.03) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    /* ── Header ── */
    header {
      text-align: center;
      margin-bottom: 32px;
      position: relative;
      z-index: 1;
      animation: fadeUp 0.6s ease both;
      background: rgba(255,255,255,0.45);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid rgba(255,255,255,0.8);
      border-radius: var(--radius);
      padding: 24px 48px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06), inset 0 1px 0 rgba(255,255,255,0.9);
    }

    .logo {
      font-family: 'Lato', sans-serif;
      font-size: 2.4rem;
      font-weight: 300;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--text-primary);
    }

    header p {
      color: var(--text-secondary);
      font-size: 0.88rem;
      margin-top: 6px;
      font-weight: 300;
    }

    /* ── Card ── */
    .card {
      background: var(--surface);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid rgba(255,255,255,0.8);
      border-radius: var(--radius);
      padding: 40px;
      width: 100%;
      max-width: 660px;
      box-shadow: var(--shadow-md);
      position: relative;
      z-index: 1;
      animation: fadeUp 0.6s ease 0.1s both;
    }

    /* ── Empty / Loading states ── */
    .empty-state, .loading {
      text-align: center;
      padding: 56px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

    .loading { display: none; }

    .empty-state p, .loading p {
      color: var(--text-secondary);
      font-size: 0.95rem;
      font-weight: 300;
    }

    .loading-spinner {
      width: 28px;
      height: 28px;
      border: 2px solid var(--separator);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }

    @keyframes spin { to { transform: rotate(360deg); } }

    /* ── Word content ── */
    #word-content { display: none; }

    .word-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 10px;
    }

    .word-pos {
      font-size: 0.72rem;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 1.2px;
      font-weight: 500;
      background: rgba(0,113,227,0.08);
      padding: 3px 10px;
      border-radius: 20px;
    }

    .pronunciation {
      font-size: 0.85rem;
      color: var(--text-tertiary);
      font-weight: 300;
    }

    .word-title {
      font-size: 3.2rem;
      font-weight: 300;
      color: var(--text-primary);
      letter-spacing: -0.5px;
      line-height: 1.1;
      margin-bottom: 20px;
    }

    .definition {
      font-size: 1rem;
      line-height: 1.75;
      color: var(--text-secondary);
      font-weight: 300;
      margin-bottom: 32px;
      padding-bottom: 28px;
      border-bottom: 1px solid var(--separator);
    }

    .section-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--text-tertiary);
      font-weight: 500;
      margin-bottom: 14px;
    }

    .examples {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 32px;
    }

    .example {
      font-size: 0.92rem;
      color: var(--text-primary);
      line-height: 1.65;
      font-weight: 300;
      padding: 12px 16px;
      background: rgba(0,0,0,0.025);
      border-radius: var(--radius-sm);
      border-left: 2px solid rgba(0,113,227,0.25);
    }

    .meta-row {
      display: flex;
      gap: 24px;
      flex-wrap: wrap;
      padding: 20px;
      background: rgba(0,0,0,0.02);
      border-radius: var(--radius-sm);
      margin-bottom: 32px;
    }

    .meta-block { flex: 1; min-width: 160px; }
    .meta-value { font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5; font-weight: 300; }
    .mistake-value { font-size: 0.88rem; color: #bf4800; line-height: 1.5; font-weight: 300; }

    /* ── Try section ── */
    .try-section {
      border-top: 1px solid var(--separator);
      padding-top: 28px;
    }

    .try-section > p {
      font-size: 0.88rem;
      color: var(--text-secondary);
      margin-bottom: 12px;
      font-weight: 300;
    }

    textarea {
      width: 100%;
      padding: 14px 16px;
      border: 1px solid var(--separator);
      border-radius: var(--radius-sm);
      font-family: 'Lato', sans-serif;
      font-size: 0.92rem;
      font-weight: 300;
      color: var(--text-primary);
      background: rgba(255,255,255,0.6);
      resize: none;
      height: 80px;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
      display: block;
    }

    textarea:focus {
      border-color: rgba(0,113,227,0.4);
      box-shadow: 0 0 0 3px rgba(0,113,227,0.08);
    }

    textarea::placeholder { color: var(--text-tertiary); }

    /* ── Button row ── */
    .btn-row {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-top: 16px;
      flex-wrap: wrap;
    }

    /* Glass button base */
    .glass-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 11px 26px;
      background: rgba(255,255,255,0.6);
      backdrop-filter: blur(16px) saturate(180%);
      -webkit-backdrop-filter: blur(16px) saturate(180%);
      color: var(--accent);
      border: 1px solid rgba(255,255,255,0.95);
      border-radius: 980px;
      font-family: 'Lato', sans-serif;
      font-size: 0.88rem;
      font-weight: 500;
      cursor: pointer;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08), inset 0 1px 0 rgba(255,255,255,0.9);
      transition: all 0.2s ease;
      -webkit-appearance: none;
      appearance: none;
      white-space: nowrap;
    }

    .glass-btn:hover {
      background: rgba(255,255,255,0.85);
      box-shadow: 0 4px 20px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,1);
      transform: translateY(-1px);
    }

    .glass-btn:active { transform: translateY(0); box-shadow: 0 1px 6px rgba(0,0,0,0.08); }
    .glass-btn:disabled { opacity: 0.45; cursor: not-allowed; transform: none; }

    /* Save button variant — green tint */
    .glass-btn.save {
      color: #1a7f37;
      background: rgba(52,199,89,0.12);
      border-color: rgba(52,199,89,0.3);
      box-shadow: 0 2px 12px rgba(52,199,89,0.1), inset 0 1px 0 rgba(255,255,255,0.8);
    }

    .glass-btn.save:hover {
      background: rgba(52,199,89,0.2);
      box-shadow: 0 4px 20px rgba(52,199,89,0.15), inset 0 1px 0 rgba(255,255,255,0.9);
    }

    .glass-btn.save.saved {
      color: #1a7f37;
      opacity: 0.6;
      cursor: default;
      transform: none;
    }

    /* ── Feedback ── */
    .feedback-box {
      margin-top: 16px;
      padding: 16px 18px;
      border-radius: var(--radius-sm);
      display: none;
      animation: fadeUp 0.3s ease both;
    }

    .feedback-box.correct   { background: rgba(52,199,89,0.08);  border: 1px solid rgba(52,199,89,0.2); }
    .feedback-box.partial   { background: rgba(255,159,10,0.08); border: 1px solid rgba(255,159,10,0.2); }
    .feedback-box.incorrect { background: rgba(255,69,58,0.06);  border: 1px solid rgba(255,69,58,0.15); }

    .feedback-status { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.2px; font-weight: 700; margin-bottom: 6px; color: var(--text-secondary); }
    .feedback-text { font-size: 0.9rem; line-height: 1.65; color: var(--text-primary); font-weight: 300; margin-bottom: 6px; }
    .feedback-improved { font-size: 0.85rem; color: var(--text-secondary); font-style: italic; font-weight: 300; }

    /* ── Bottom action row ── */
    .bottom-row {
      margin-top: 24px;
      display: none;
      justify-content: center;
      gap: 12px;
      position: relative;
      z-index: 1;
      animation: fadeUp 0.6s ease 0.2s both;
      flex-wrap: wrap;
    }

    .outline-btn {
      display: inline-flex;
      align-items: center;
      padding: 11px 24px;
      background: transparent;
      color: var(--text-secondary);
      border: 1px solid var(--separator);
      border-radius: 980px;
      font-family: 'Lato', sans-serif;
      font-size: 0.85rem;
      font-weight: 400;
      cursor: pointer;
      transition: all 0.2s ease;
      -webkit-appearance: none;
      appearance: none;
    }

    .outline-btn:hover {
      color: var(--accent);
      border-color: rgba(0,113,227,0.3);
      background: rgba(0,113,227,0.04);
    }

    /* ── Saved words panel ── */
    .saved-panel {
      background: var(--surface);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid rgba(255,255,255,0.8);
      border-radius: var(--radius);
      padding: 32px 40px;
      width: 100%;
      max-width: 660px;
      box-shadow: var(--shadow-md);
      position: relative;
      z-index: 1;
      margin-top: 24px;
      display: none;
      animation: fadeUp 0.4s ease both;
    }

    .saved-panel h2 {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--text-tertiary);
      font-weight: 500;
      margin-bottom: 16px;
    }

    .saved-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .saved-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(0,113,227,0.07);
      border: 1px solid rgba(0,113,227,0.15);
      border-radius: 980px;
      font-size: 0.85rem;
      color: var(--accent);
      font-weight: 400;
    }

    .saved-tag button {
      background: none;
      border: none;
      color: var(--text-tertiary);
      cursor: pointer;
      font-size: 0.8rem;
      padding: 0;
      line-height: 1;
      -webkit-appearance: none;
    }

    .saved-tag button:hover { color: #bf4800; }

    .no-saved {
      font-size: 0.88rem;
      color: var(--text-tertiary);
      font-weight: 300;
      font-style: italic;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(16px); }
      to   { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">Lexicon</div>
    <p>One word a day, thoughtfully learned.</p>
  </header>

  <div class="card">

    <!-- Empty state -->
    <div class="empty-state" id="empty-state">
      <p>Ready to learn a new word?</p>
      <button class="glass-btn" onclick="loadWord()">Get my word →</button>
    </div>

    <!-- Loading state -->
    <div class="loading" id="loading">
      <div class="loading-spinner"></div>
      <p>Finding your word…</p>
    </div>

    <!-- Word content -->
    <div id="word-content">
      <div class="word-meta">
        <span class="word-pos" id="pos"></span>
        <span class="pronunciation" id="pronunciation"></span>
      </div>
      <div class="word-title" id="word"></div>
      <div class="definition" id="definition"></div>

      <div class="section-label">Examples</div>
      <div class="examples" id="examples"></div>

      <div class="meta-row">
        <div class="meta-block">
          <div class="section-label">Synonyms</div>
          <div class="meta-value" id="synonyms"></div>
        </div>
        <div class="meta-block">
          <div class="section-label">Common Mistake</div>
          <div class="mistake-value" id="mistake"></div>
        </div>
      </div>

      <div class="try-section">
        <p>Write your own sentence using this word:</p>
        <textarea id="user-sentence" placeholder="Type your sentence here…"></textarea>
        <div class="btn-row">
          <button class="glass-btn" id="check-btn" onclick="checkSentence()">Check my sentence →</button>
          <button class="glass-btn save" id="save-btn" onclick="saveWord()">+ Save word</button>
        </div>
        <div class="feedback-box" id="feedback-box">
          <div class="feedback-status" id="feedback-status"></div>
          <div class="feedback-text" id="feedback-text"></div>
          <div class="feedback-improved" id="feedback-improved"></div>
        </div>
      </div>
    </div>

  </div>

  <!-- Bottom actions -->
  <div class="bottom-row" id="bottom-row">
    <button class="outline-btn" onclick="toggleSaved()">My saved words</button>
    <button class="outline-btn" onclick="loadWord()">New word →</button>
  </div>

  <!-- Saved words panel -->
  <div class="saved-panel" id="saved-panel">
    <h2>Saved Words</h2>
    <div class="saved-list" id="saved-list"></div>
  </div>

  <script>
    let currentWord = '';
    let seenWords = [];
    let savedWords = JSON.parse(localStorage.getItem('lexicon-saved') || '[]');
    let savedPanelOpen = false;

    function persistSaved() {
      localStorage.setItem('lexicon-saved', JSON.stringify(savedWords));
    }

    function renderSavedPanel() {
      const list = document.getElementById('saved-list');
      if (savedWords.length === 0) {
        list.innerHTML = '<span class="no-saved">No saved words yet.</span>';
      } else {
        list.innerHTML = savedWords.map(w => `
          <span class="saved-tag">
            ${w}
            <button onclick="removeWord('${w}')" title="Remove">✕</button>
          </span>
        `).join('');
      }
    }

    function toggleSaved() {
      const panel = document.getElementById('saved-panel');
      savedPanelOpen = !savedPanelOpen;
      panel.style.display = savedPanelOpen ? 'block' : 'none';
      if (savedPanelOpen) renderSavedPanel();
    }

    function saveWord() {
      if (!currentWord || savedWords.includes(currentWord)) return;
      savedWords.push(currentWord);
      persistSaved();
      const btn = document.getElementById('save-btn');
      btn.textContent = '✓ Saved';
      btn.classList.add('saved');
      btn.disabled = true;
      if (savedPanelOpen) renderSavedPanel();
    }

    function removeWord(word) {
      savedWords = savedWords.filter(w => w !== word);
      persistSaved();
      renderSavedPanel();
      // Re-enable save button if current word was removed
      if (word === currentWord) {
        const btn = document.getElementById('save-btn');
        btn.textContent = '+ Save word';
        btn.classList.remove('saved');
        btn.disabled = false;
      }
    }

    async function loadWord() {
      document.getElementById('empty-state').style.display = 'none';
      document.getElementById('loading').style.display = 'flex';
      document.getElementById('word-content').style.display = 'none';
      document.getElementById('feedback-box').style.display = 'none';
      document.getElementById('user-sentence').value = '';
      document.getElementById('bottom-row').style.display = 'none';

      // Reset save button
      const saveBtn = document.getElementById('save-btn');
      saveBtn.textContent = '+ Save word';
      saveBtn.classList.remove('saved');
      saveBtn.disabled = false;

      try {
        const res = await fetch('/api/word?seen=' + encodeURIComponent(seenWords.join(',')));
        const json = await res.json();
        if (!json.success) throw new Error(json.error);

        const d = json.data;
        currentWord = d.word;
        if (!seenWords.includes(currentWord)) seenWords.push(currentWord);

        document.getElementById('word').textContent = d.word;
        document.getElementById('pos').textContent = d.part_of_speech;
        document.getElementById('pronunciation').textContent = d.pronunciation;
        document.getElementById('definition').textContent = d.definition;
        document.getElementById('synonyms').textContent = d.synonyms;
        document.getElementById('mistake').textContent = d.common_mistake;

        const examplesEl = document.getElementById('examples');
        examplesEl.innerHTML = '';
        d.examples.forEach(ex => {
          const div = document.createElement('div');
          div.className = 'example';
          div.textContent = ex;
          examplesEl.appendChild(div);
        });

        // If already saved, reflect that
        if (savedWords.includes(currentWord)) {
          saveBtn.textContent = '✓ Saved';
          saveBtn.classList.add('saved');
          saveBtn.disabled = true;
        }

        document.getElementById('loading').style.display = 'none';
        document.getElementById('word-content').style.display = 'block';
        document.getElementById('bottom-row').style.display = 'flex';

      } catch (err) {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('empty-state').style.display = 'flex';
        document.getElementById('empty-state').innerHTML =
          `<p style="color:#bf4800">Something went wrong: ${err.message}</p>
           <button class="glass-btn" onclick="loadWord()">Try again →</button>`;
      }
    }

    async function checkSentence() {
      const sentence = document.getElementById('user-sentence').value.trim();
      if (!sentence) return;

      const btn = document.getElementById('check-btn');
      btn.disabled = true;
      btn.textContent = 'Checking…';

      try {
        const res = await fetch('/api/check', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ word: currentWord, sentence })
        });
        const json = await res.json();
        if (!json.success) throw new Error(json.error);

        const d = json.data;
        const box = document.getElementById('feedback-box');
        const status = (d.correct || '').toLowerCase();

        box.className = 'feedback-box ' + (status === 'yes' ? 'correct' : status === 'partially' ? 'partial' : 'incorrect');
        document.getElementById('feedback-status').textContent =
          status === 'yes' ? '✓ Correct' : status === 'partially' ? '◐ Partially correct' : '✕ Not quite';
        document.getElementById('feedback-text').textContent = d.feedback;
        document.getElementById('feedback-improved').textContent =
          d.improved !== 'Great job!' ? `Suggestion: ${d.improved}` : '';
        box.style.display = 'block';

      } catch (err) {
        alert('Error: ' + err.message);
      } finally {
        btn.disabled = false;
        btn.textContent = 'Check my sentence →';
      }
    }
  </script>
</body>
</html>