(() => {
  const btn = document.getElementById('langBtn');
  const params = new URLSearchParams(window.location.search);
  const forced = params.get('lang');
  const stored = localStorage.getItem('lang');
  const state = { lang: forced || stored || 'en' };

  const applyLang = () => {
    document.documentElement.lang = state.lang;
    document.querySelectorAll('[data-lang]').forEach(el => {
      el.classList.toggle('hidden', el.dataset.lang !== state.lang);
    });
    if (btn) {
      btn.textContent = state.lang === 'en' ? '中文' : 'English';
      btn.setAttribute('aria-pressed', state.lang === 'zh');
    }
    localStorage.setItem('lang', state.lang);
  };

  if (btn) {
    btn.addEventListener('click', () => {
      state.lang = state.lang === 'en' ? 'zh' : 'en';
      applyLang();
    });
  }

  const loadComponents = async () => {
    const nodes = document.querySelectorAll('[data-component]');
    await Promise.all([...nodes].map(async (node) => {
      const path = node.dataset.component;
      try {
        const res = await fetch(path, { cache: 'no-cache' });
        if (!res.ok) throw new Error(`Failed ${path}`);
        node.innerHTML = await res.text();
      } catch (err) {
        node.innerHTML = `<p class="text-danger">Failed to load ${path}</p>`;
      }
    }));
    applyLang();
  };

  loadComponents();
})();
