(() => {
  const btn = document.getElementById('langBtn');
  if (!btn) return;
  const params = new URLSearchParams(window.location.search);
  const forced = params.get('lang');
  const stored = localStorage.getItem('lang');
  const state = { lang: forced || stored || 'en' };

  const apply = () => {
    document.documentElement.lang = state.lang;
    document.querySelectorAll('[data-lang]').forEach(el => {
      el.classList.toggle('hidden', el.dataset.lang !== state.lang);
    });
    btn.textContent = state.lang === 'en' ? '中文' : 'English';
    btn.setAttribute('aria-pressed', state.lang === 'zh');
    localStorage.setItem('lang', state.lang);
  };

  btn.addEventListener('click', () => {
    state.lang = state.lang === 'en' ? 'zh' : 'en';
    apply();
  });

  // Default to English regardless of browser language
  apply();
})();
