(function(){
  const btn = document.querySelector('#langBtn');
  const state = { lang: (localStorage.getItem('lang')||'en') };
  function apply(){
    document.querySelectorAll('[data-lang]').forEach(el=>{
      el.classList.toggle('hidden', el.dataset.lang !== state.lang);
    });
    btn.textContent = state.lang === 'en' ? '中文' : 'English';
    localStorage.setItem('lang', state.lang);
  }
  btn.addEventListener('click', ()=>{ state.lang = state.lang==='en'?'zh':'en'; apply(); });
  apply();
})();
