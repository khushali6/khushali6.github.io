(function () {
  'use strict';
  var USER = 'khushali6', reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var THEMES = ['paper', 'night', 'nord', 'gruvbox'];

  /* theme */
  function setTheme(t, save) {
    if (THEMES.indexOf(t) < 0) t = 'paper';
    document.documentElement.setAttribute('data-theme', t);
    document.querySelectorAll('.themes button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.t === t); });
    if (save) try { localStorage.setItem('theme', t); } catch (e) {}
  }
  document.querySelectorAll('.themes button').forEach(function (b) { b.addEventListener('click', function () { setTheme(b.dataset.t, true); }); });
  setTheme(document.documentElement.getAttribute('data-theme') || 'paper');
  window.__setTheme = function (t) { setTheme(t, true); return THEMES.indexOf(t) >= 0; };

  /* mobile nav */
  var burger = document.querySelector('.burger'), menu = document.querySelector('.nav ul');
  if (burger && menu) {
    burger.addEventListener('click', function () { burger.setAttribute('aria-expanded', menu.classList.toggle('open')); });
    menu.addEventListener('click', function (e) { if (e.target.tagName === 'A') menu.classList.remove('open'); });
  }

  /* hero video: play only while visible */
  document.querySelectorAll('video[data-auto]').forEach(function (v) {
    if (!('IntersectionObserver' in window) || reduce) return;
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { v.play().catch(function () {}); } else v.pause(); });
    }, { threshold: 0.4 }).observe(v);
  });

  /* flows */
  document.querySelectorAll('.flow').forEach(function (f) {
    var steps = f.querySelectorAll('li:not(.arr)'), i = -1, timer = null;
    if (!steps.length || reduce) return;
    function tick() { i = (i + 1) % (steps.length + 1); steps.forEach(function (s, k) { s.classList.toggle('on', k === i); s.classList.toggle('done', k < i); }); }
    function start() { if (!timer) { tick(); timer = setInterval(tick, 650); } }
    function stop() { clearInterval(timer); timer = null; }
    f.addEventListener('mouseenter', start); f.addEventListener('mouseleave', stop);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { start(); setTimeout(stop, 4500); } else stop(); }); }, { threshold: 0.8 }).observe(f);
  });

  /* architecture explorer */
  document.querySelectorAll('.arch').forEach(function (a) {
    var btns = a.querySelectorAll('button'), panels = a.querySelectorAll('[data-panel]');
    function show(id) { btns.forEach(function (b) { b.setAttribute('aria-selected', b.dataset.target === id); }); panels.forEach(function (p) { p.hidden = p.dataset.panel !== id; }); }
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.target); }); });
    if (btns[0]) show(btns[0].dataset.target);
  });

  /* GitHub API: enhance server-rendered content with live numbers */
  function ago(iso) {
    var d = Math.floor((Date.now() - new Date(iso)) / 864e5);
    if (d < 1) return 'today'; if (d < 30) return d + 'd ago'; if (d < 365) return Math.floor(d / 30) + 'mo ago';
    return Math.floor(d / 365) + 'y ago';
  }
  function gh(url) {
    var key = 'gh:' + url;
    try { var c = JSON.parse(sessionStorage.getItem(key) || 'null'); if (c && Date.now() - c.t < 600000) return Promise.resolve(c.d); } catch (e) {}
    return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) { try { sessionStorage.setItem(key, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {} return d; });
  }
  var need = document.querySelectorAll('[data-repo], [data-live]');
  if (need.length) {
    gh('https://api.github.com/users/' + USER + '/repos?per_page=100&sort=pushed&type=owner').then(function (list) {
      var by = {}; list.forEach(function (r) { by[r.name.toLowerCase()] = r; });
      need.forEach(function (el) {
        var r = by[(el.dataset.repo || el.dataset.live).toLowerCase()]; if (!r) return;
        el.textContent = (r.language ? r.language + ' · ' : '') + (r.stargazers_count ? '★ ' + r.stargazers_count + ' · ' : '') + 'updated ' + ago(r.pushed_at);
      });
    }).catch(function () {});
  }

  /* little terminal (workbench page) */
  var tw = document.getElementById('term');
  if (tw) {
    var out = tw.querySelector('.out'), input = tw.querySelector('input'), hist = [], hi = 0;
    var C = {
      help: 'commands: about · work · experience · stack · github · contact · theme <paper|night|nord|gruvbox> · whoami · clear',
      whoami: 'khushali — AI engineer. builds agents, RAG systems, multimodal tools.',
      about: 'I started with ML and computer vision, ended up building agents, and keep turning "what if…" ideas into working products.',
      work: 'meadow    agentic coding system → /meadow/\ncasora    AI real-estate decisions → /casora/\nsplitmate receipt → fair split   → /splitmate/\nlaya      meme brain             → /laya/',
      experience: 'TCS · AI Engineer · Aug 2024 — present → /#experience',
      stack: 'python · typescript · aws · bedrock · langgraph · mcp · opensearch · postgresql · fastapi · docker',
      github: 'https://github.com/khushali6',
      contact: 'khushalipariyal@gmail.com · linkedin.com/in/khushalipariyal',
      sudo: 'nice try.', ls: 'meadow  casora  splitmate  laya  work  workbench', pwd: '/home/khushali/workbench'
    };
    function print(t, cls) { var d = document.createElement('div'); d.className = 'l ' + (cls || ''); d.textContent = t; out.appendChild(d); tw.scrollTop = tw.scrollHeight; }
    print('type "help" — nothing here is real except the opinions.');
    tw.addEventListener('click', function () { input.focus(); });
    tw.querySelector('form').addEventListener('submit', function (e) {
      e.preventDefault();
      var v = input.value.trim(); input.value = ''; if (!v) return;
      hist.push(v); hi = hist.length; print('$ ' + v, 'pr');
      var p = v.split(/\s+/), cmd = p[0].toLowerCase();
      if (cmd === 'clear') out.innerHTML = '';
      else if (cmd === 'theme') print(window.__setTheme(p[1]) ? 'theme → ' + p[1] : 'try: paper, night, nord, gruvbox');
      else if (C[cmd]) print(C[cmd]);
      else print('command not found: ' + cmd + ' (try "help")');
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowUp' && hi > 0) { input.value = hist[--hi]; e.preventDefault(); }
      if (e.key === 'ArrowDown') { input.value = hi < hist.length - 1 ? hist[++hi] : ''; hi = Math.min(hi + 1, hist.length); e.preventDefault(); }
    });
  }
})();
