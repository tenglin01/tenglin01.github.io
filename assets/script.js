(() => {
  const btn = document.getElementById('langBtn');
  if (!btn) return;
  const defaultLang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  const state = { lang: localStorage.getItem('lang') || defaultLang };
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
  apply();
})();
