(() => {
  const btn = document.getElementById('langBtn');
  if (!btn) return;
  const params = new URLSearchParams(window.location.search);
  const forced = params.get('lang');
  const stored = localStorage.getItem('lang');
  const state = { lang: forced || stored || 'en' };

  const applyLang = () => {
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
    applyLang();
  });

  // Default to English regardless of browser language
  applyLang();

  // Apple-like reveal on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.18 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();
