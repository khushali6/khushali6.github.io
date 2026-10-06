(function () {
  'use strict';
  var USER = 'khushali6';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* mobile nav */
  var burger = document.querySelector('.burger');
  var menu = document.querySelector('.nav ul');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
    menu.addEventListener('click', function (e) { if (e.target.tagName === 'A') menu.classList.remove('open'); });
  }

  /* reveal on scroll */
  var rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    rv.forEach(function (n) { io.observe(n); });
  } else rv.forEach(function (n) { n.classList.add('in'); });

  /* count-up numbers: <span data-count="75" data-suffix="%"> */
  function count(el) {
    var end = parseFloat(el.dataset.count), suf = el.dataset.suffix || '', pre = el.dataset.prefix || '';
    if (reduce) { el.textContent = pre + end + suf; return; }
    var t0 = null, dur = 1100;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + Math.round(end * eased) + suf;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { count(e.target); co.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (n) { co.observe(n); });
  }
  document.querySelectorAll('.metric').forEach(function (m) {
    m.addEventListener('mouseenter', function () { var c = m.querySelector('[data-count]'); if (c) count(c); });
  });

  /* animated flows: highlight each step in turn while visible / hovered */
  document.querySelectorAll('.flow').forEach(function (f) {
    var steps = f.querySelectorAll('li:not(.arr)');
    if (!steps.length) return;
    var i = -1, timer = null;
    function tick() {
      i = (i + 1) % (steps.length + 1);
      steps.forEach(function (s, k) { s.classList.toggle('on', k === i); s.classList.toggle('done', k < i); });
    }
    function start() { if (timer || reduce) return; tick(); timer = setInterval(tick, 700); }
    function stop() { clearInterval(timer); timer = null; }
    var host = f.closest('.feature, .card, .loop, .cs-sec, .sys') || f;
    host.addEventListener('mouseenter', start);
    host.addEventListener('mouseleave', stop);
    host.addEventListener('focusin', start);
    host.addEventListener('focusout', stop);
    if ('IntersectionObserver' in window) {
      var fo = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { start(); setTimeout(stop, 4800); } else stop(); });
      }, { threshold: 0.6 });
      fo.observe(f);
    }
  });

  /* interactive architecture explorer */
  document.querySelectorAll('.arch').forEach(function (a) {
    var btns = a.querySelectorAll('button'), panels = a.querySelectorAll('[data-panel]');
    function show(id) {
      btns.forEach(function (b) { b.setAttribute('aria-selected', b.dataset.target === id); });
      panels.forEach(function (p) { p.hidden = p.dataset.panel !== id; });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.target); }); });
    if (btns[0]) show(btns[0].dataset.target);
  });

  /* ---------- GitHub API ---------- */
  function cached(url) {
    var key = 'gh:' + url;
    try {
      var c = JSON.parse(sessionStorage.getItem(key) || 'null');
      if (c && Date.now() - c.t < 600000) return Promise.resolve(c.d);
    } catch (e) {}
    return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    }).then(function (d) {
      try { sessionStorage.setItem(key, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {}
      return d;
    });
  }
  function ago(iso) {
    var d = Math.floor((Date.now() - new Date(iso)) / 864e5);
    if (d < 1) return 'today'; if (d < 30) return d + 'd ago';
    if (d < 365) return Math.floor(d / 30) + 'mo ago';
    return Math.floor(d / 365) + 'y ago';
  }
  var star = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 .6l2.2 4.8 5.2.6-3.9 3.5 1.1 5.2L8 12l-4.6 2.7 1.1-5.2L.6 6l5.2-.6z"/></svg>';
  var git = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0a8 8 0 00-2.5 15.6c.4.1.5-.2.5-.4v-1.4c-2.2.5-2.7-1-2.7-1-.4-.9-.9-1.2-.9-1.2-.7-.5.1-.5.1-.5.8.1 1.2.8 1.2.8.7 1.3 1.9.9 2.4.7.1-.5.3-.9.5-1.1-1.8-.2-3.6-.9-3.6-4 0-.9.3-1.6.8-2.1-.1-.2-.4-1 .1-2.1 0 0 .7-.2 2.2.8a7.500 7.500 0 014 0c1.500-1 2.200-.8 2.200-.8.400 1.100.2 1.900.1 2.100.5.6.8 1.300.8 2.100 0 3.100-1.900 3.800-3.700 4 .3.3.6.8.6 1.500v2.200c0 .2.1.5.6.4A8 8 0 008 0z"/></svg>';

  /* featured project meta strips: <div data-repo="Meadow"> */
  document.querySelectorAll('[data-repo]').forEach(function (el) {
    cached('https://api.github.com/repos/' + USER + '/' + el.dataset.repo).then(function (r) {
      var bits = [];
      if (r.language) bits.push('<span><i class="dot"></i>' + r.language + '</span>');
      bits.push('<span>' + star + ' ' + r.stargazers_count + '</span>');
      bits.push('<span>' + git + ' updated ' + ago(r.pushed_at) + '</span>');
      el.innerHTML = bits.join('');
    }).catch(function () { el.hidden = true; });
  });

  /* live repository grid: <div id="repos"> */
  var grid = document.getElementById('repos');
  if (grid) {
    var status = document.getElementById('repos-status');
    var skip = { 'khushali6.github.io': 1, 'khushali6': 1 };
    cached('https://api.github.com/users/' + USER + '/repos?per_page=100&sort=pushed&type=owner').then(function (list) {
      var shown = list.filter(function (r) { return !r.fork && !r.private && !skip[r.name] && r.description; })
        .sort(function (a, b) { return new Date(b.pushed_at) - new Date(a.pushed_at); })
        .slice(0, 9);
      if (!shown.length) throw new Error('empty');
      grid.innerHTML = shown.map(function (r) {
        var d = (r.description || '').replace(/[<>&]/g, function (c) { return { '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]; });
        var n = r.name.replace(/[<>&]/g, '');
        return '<a class="repo" href="' + r.html_url + '" target="_blank" rel="noopener"><h4>' + n + '</h4><p>' + d + '</p><div class="m">' +
          (r.language ? '<span><i class="dot"></i>' + r.language + '</span>' : '') +
          '<span>' + star + ' ' + r.stargazers_count + '</span><span>' + ago(r.pushed_at) + '</span></div></a>';
      }).join('');
      if (status) status.textContent = 'Live from the GitHub API · ' + list.length + ' public repositories';
    }).catch(function () {
      grid.hidden = true;
      if (status) status.innerHTML = 'GitHub API is unavailable right now — browse everything at <a href="https://github.com/' + USER + '">github.com/' + USER + '</a>.';
    });
  }
})();
