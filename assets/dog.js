/* Tiny brown dog companion. Self-contained, no dependencies.
   Reactions are attached with data-dog-reaction="sniff|sit|excited|run|look" (+ optional data-dog-goto="below"). */
(function () {
  if (!window.matchMedia) return;
  if (!matchMedia('(any-hover: hover)').matches) return; // touch-only devices: no dog

  var W = 36, H = 30;
  var css = '.dog{position:fixed;left:0;top:0;width:' + W + 'px;height:' + H + 'px;z-index:2147483000;pointer-events:none;opacity:0;transition:opacity .3s;will-change:transform;contain:layout style}' +
    '.dog.on{opacity:1}.dog__flip{width:100%;height:100%;transition:transform .18s ease-out}.dog svg{display:block;width:100%;height:100%;overflow:visible}' +
    '.dog *{transform-box:fill-box}' +
    '.d-pose{transform-origin:20% 90%;transition:transform .25s ease}' +
    '.d-torso{transform-origin:50% 100%;animation:d-breathe 3s ease-in-out infinite}' +
    '.d-head{transform-origin:15% 85%;transition:transform .25s ease;animation:d-nod 3.4s ease-in-out infinite}' +
    '.d-tail{transform-origin:90% 90%;animation:d-wag 1.8s ease-in-out infinite}' +
    '.d-eye{transform-origin:50% 50%;animation:d-blink 4.2s infinite}' +
    '.d-leg{transform-origin:50% 0;animation-duration:.5s;animation-iteration-count:infinite;animation-timing-function:ease-in-out;animation-play-state:paused}' +
    '.d-l2,.d-l3{animation-name:d-swing-a}.d-l1,.d-l4{animation-name:d-swing-b}' +
    '.dog[data-s=walk] .d-leg{animation-play-state:running;animation-duration:.55s}' +
    '.dog[data-s=run] .d-leg{animation-play-state:running;animation-duration:.26s}' +
    '.dog[data-s=walk] .d-flip2,.dog[data-s=run] .d-flip2{animation:d-bob .3s ease-in-out infinite}' +
    '.dog[data-s=run] .d-tail{animation-duration:.3s}' +
    '.dog[data-s=sniff] .d-head{animation:d-sniff .45s ease-in-out infinite;transform:rotate(24deg)}' +
    '.dog[data-s=look] .d-head{animation:none;transform:rotate(-14deg)}' +
    '.dog[data-s=sit] .d-pose{transform:rotate(-24deg)}.dog[data-s=sit] .d-head{transform:rotate(18deg);animation:none}' +
    '.dog[data-s=sit] .d-l1,.dog[data-s=sit] .d-l2{animation:none;transform:scaleY(.55)}' +
    '.dog[data-s=excited] .d-tail,.dog[data-s=wag] .d-tail{animation-duration:.16s}' +
    '.dog[data-s=excited] .d-flip2{animation:d-hop .42s ease-in-out infinite}' +
    '.dog[data-s=excited] .d-head{animation:none;transform:rotate(-10deg)}' +
    '@keyframes d-swing-a{0%,100%{transform:rotate(-26deg)}50%{transform:rotate(26deg)}}' +
    '@keyframes d-swing-b{0%,100%{transform:rotate(26deg)}50%{transform:rotate(-26deg)}}' +
    '@keyframes d-bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-1.5px)}}' +
    '@keyframes d-hop{0%,100%{transform:translateY(0)}45%{transform:translateY(-6px)}}' +
    '@keyframes d-breathe{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.035)}}' +
    '@keyframes d-nod{0%,100%{transform:rotate(0)}40%{transform:rotate(-4deg)}70%{transform:rotate(3deg)}}' +
    '@keyframes d-wag{0%,100%{transform:rotate(-14deg)}50%{transform:rotate(14deg)}}' +
    '@keyframes d-blink{0%,93%,100%{transform:scaleY(1)}96%{transform:scaleY(.1)}}' +
    '@keyframes d-sniff{0%,100%{transform:rotate(22deg)}50%{transform:rotate(32deg)}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var SVG = '<svg viewBox="0 0 48 40" aria-hidden="true" focusable="false"><g class="d-flip2"><g class="d-pose">' +
    '<g class="d-tail"><path d="M10 17 C3 14 3 7 6 5" fill="none" stroke="#7a4a22" stroke-width="3.2" stroke-linecap="round"/></g>' +
    '<rect class="d-leg d-l1" x="11" y="25" width="4.2" height="11" rx="2.1" fill="#6b4020"/>' +
    '<rect class="d-leg d-l3" x="29" y="25" width="4.2" height="11" rx="2.1" fill="#6b4020"/>' +
    '<g class="d-torso"><rect x="8" y="14" width="28" height="15" rx="7.5" fill="#9a6233" stroke="#5c3818" stroke-width="1"/>' +
    '<path d="M13 26 Q22 30 31 26" fill="none" stroke="#c58a50" stroke-width="2" stroke-linecap="round"/></g>' +
    '<rect class="d-leg d-l2" x="16" y="25" width="4.2" height="11" rx="2.1" fill="#8a5429"/>' +
    '<rect class="d-leg d-l4" x="34" y="25" width="4.2" height="11" rx="2.1" fill="#8a5429"/>' +
    '<g class="d-head"><rect x="30" y="7" width="15" height="13" rx="6" fill="#a86b38" stroke="#5c3818" stroke-width="1"/>' +
    '<rect x="39" y="12" width="8" height="7" rx="3.4" fill="#c58a50" stroke="#5c3818" stroke-width="1"/>' +
    '<circle cx="46" cy="13.8" r="1.5" fill="#241208"/>' +
    '<path d="M32.5 8 C28 8 27.5 17 31.5 18.5 C34 17 34 11 32.5 8Z" fill="#5c3818"/>' +
    '<circle class="d-eye" cx="39" cy="12" r="1.35" fill="#241208"/></g></g></g></svg>';

  var el = document.createElement('div'); el.className = 'dog'; el.setAttribute('aria-hidden', 'true');
  el.innerHTML = '<div class="dog__flip">' + SVG + '</div>';
  var flip = el.firstChild;
  document.body.appendChild(el);

  var x = innerWidth - 90, y = innerHeight - 70, mx = innerWidth - 40, my = innerHeight - 60, face = 1, state = '', raf = 0, seen = true;
  var react = null;            // {el, kind, goal:{x,y}|null, until, started, done}
  var doneEl = null, clickUntil = 0, lookAt = null, t0 = 0;

  function setState(s) { if (s !== state) { state = s; el.setAttribute('data-s', s); } }
  function setFace(f) { if (f !== face) { face = f; flip.style.transform = 'scaleX(' + f + ')'; } }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  function followGoal() {
    var gx = mx - W - 16; if (mx < W + 40) gx = mx + 18;
    return { x: clamp(gx, 4, innerWidth - W - 4), y: clamp(my + 10, 4, innerHeight - H - 4) };
  }
  function rectGoal(r, below) {
    var gx = clamp(mx - W / 2, r.left, r.right - W);
    var gy = r.bottom + 6; if (gy + H > innerHeight - 2) gy = r.top - H - 6;
    return { x: clamp(gx, 4, innerWidth - W - 4), y: clamp(gy, 4, innerHeight - H - 4) };
  }
  function cardGoal(node) {
    var shot = node.querySelector('.shot') || node, r = shot.getBoundingClientRect();
    var gx = r.right - W - 18, gy = r.bottom + 6;
    if (gy + H > innerHeight - 2) gy = innerHeight - H - 4;
    return { x: clamp(gx, 4, innerWidth - W - 4), y: clamp(gy, 4, innerHeight - H - 4), cx: r.left + r.width / 2 };
  }

  function kick() { if (!raf) raf = requestAnimationFrame(loop); }

  function loop(now) {
    raf = 0;
    var goal, k = 0.1, busy = false;
    if (react && react.kind === 'card') { react.goal = cardGoal(react.el); }
    goal = (react && react.goal) || followGoal();
    if (react && react.goal) k = 0.1;
    // tiny circle for "run"
    if (react && react.kind === 'run' && react.arrived) {
      var a = (now - react.arrived) / 160;
      goal = { x: react.goal.x + Math.cos(a) * 18, y: react.goal.y + Math.sin(a) * 9 }; k = 0.2; busy = true;
    }
    var px = x, py = y;
    var dx0 = goal.x - x, dy0 = goal.y - y;
    var sx = dx0 * k, sy = dy0 * k, sp = Math.hypot(sx, sy);
    if (sp > 26) { sx *= 26 / sp; sy *= 26 / sp; sp = 26; }
    x += sx; y += sy;
    el.style.transform = 'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0)';

    var dist = Math.hypot(goal.x - x, goal.y - y);
    var moving = sp > 0.7;
    if (moving && Math.abs(sx) > 0.25) setFace(sx > 0 ? 1 : -1);

    var s;
    if (now < clickUntil) { s = 'excited'; busy = true; }
    else if (react && !react.done && dist < 6 || (react && react.kind === 'look' && !react.done && !react.goal)) {
      // arrived at (or following with) a reaction
      if (!react.arrived) { react.arrived = now; react.until = now + (react.dur || 1700); }
      var tgt = react.look || mx;
      if (react.kind !== 'run') setFace(tgt > x + W / 2 ? 1 : -1);
      s = { sniff: 'sniff', sit: 'sit', excited: 'excited', wag: 'wag', run: 'run', look: 'look' }[react.kind] || 'look';
      if (react.kind === 'run') busy = true;
      if (react.dur && now > react.until) { react.done = true; doneEl = react.el; s = 'idle'; }
      else if (react.dur) busy = true;
    } else if (moving) {
      s = sp > 6.5 ? 'run' : 'walk';
    } else {
      s = 'idle';
      if (!react || react.done) setFace(mx > x + W / 2 ? 1 : -1);
    }
    setState(s);
    if (moving || busy || (react && !react.done && dist >= 6)) kick();
  }

  function reactionFor(node) {
    var kind = node.getAttribute('data-dog-reaction');
    if (!kind) return null;
    var r = { el: node, kind: kind, goal: null, done: false };
    var isCard = node.classList.contains('case');
    if (node.getAttribute('data-dog-goto') === 'below') { r.goal = rectGoal(node.getBoundingClientRect()); r.kind = 'look'; r.look = node.getBoundingClientRect().left + node.offsetWidth / 2; }
    else if (isCard) { r.kind = kind; r.dur = kind === 'sit' ? 0 : (kind === 'run' ? 1700 : 1900); r.goal = cardGoal(node); r.card = true; }
    else if (kind === 'look') { var b = node.getBoundingClientRect(); r.look = b.left + b.width / 2; if (node.classList.contains('case__go')) r.goal = rectGoal(b); }
    return r;
  }
  function fixCard(r) { if (r && r.card) r.kind = r.kind === 'run' ? 'run' : r.kind; return r; }

  document.addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY;
    if (!seen) { seen = true; x = clamp(mx - W - 16, 0, innerWidth); y = clamp(my + 10, 0, innerHeight); el.classList.add('on'); }
    kick();
  }, { passive: true });

  document.addEventListener('mouseover', function (e) {
    var n = e.target.closest ? e.target.closest('[data-dog-reaction]') : null;
    if (!n || n === doneEl || (react && react.el === n)) return;
    react = fixCard(reactionFor(n)); if (react && react.kind === 'run' && react.card) react.kind = 'run';
    kick();
  }, { passive: true });

  document.addEventListener('mouseout', function (e) {
    var n = e.target.closest ? e.target.closest('[data-dog-reaction]') : null;
    if (!n) return;
    var to = e.relatedTarget;
    if (to && n.contains(to)) return;
    if (react && react.el === n) react = null;
    if (doneEl === n) doneEl = null;
    kick();
  }, { passive: true });


  document.addEventListener('pointerdown', function () { clickUntil = performance.now() + 700; kick(); }, { passive: true });

  el.classList.add('on'); kick();
})();
