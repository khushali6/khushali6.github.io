/* Tiny pixel-art brown dog companion. Self-contained, no dependencies.
   Reactions attach through data-dog-reaction="sniff|sit|excited|run|look" (+ optional data-dog-goto="below"). */
(function () {
  if (!window.matchMedia || !matchMedia('(any-hover: hover)').matches) return; // touch-only devices: no dog

  var PX = 2, AW = 16, AH = 14, W = AW * PX, H = AH * PX, COLS = 4;
  var ROW = { idle: 0, walk: 1, run: 2, sniff: 3, look: 4, sit: 5, excited: 6, wag: 7 };
  var DUR = { idle: 1.6, walk: .5, run: .28, sniff: .6, look: 1.4, sit: 1.0, excited: .36, wag: .3 };
  var C = { o: '#2e1a0b', b: '#a4662f', d: '#6e4120', l: '#e0a868', n: '#140b05', e: '#140b05' };

  /* ---------- pixel art: draw each frame onto one sprite sheet ---------- */
  function paint(ctx, ox, oy, f) {
    function P(x, y, w, h, c) { ctx.fillStyle = C[c]; ctx.fillRect(ox + x, oy + y + (f.dy || 0), w, h); }
    var tail = f.tail || 0, hd = f.hd || 0, hx = f.hx || 0;
    if (!f.sit) {
      // tail
      if (tail === 0) { P(0, 2, 2, 1, 'd'); P(0, 3, 1, 3, 'd'); P(1, 5, 1, 1, 'd'); }
      else if (tail === 1) { P(0, 4, 2, 1, 'd'); P(0, 3, 1, 1, 'd'); }
      else { P(1, 5, 1, 1, 'd'); P(0, 6, 2, 1, 'd'); P(0, 7, 1, 2, 'd'); }
      var L = f.legs || [[0, 4], [0, 4], [0, 4], [0, 4]];
      // far legs (darker)
      P(3 + L[0][0], 9, 2, L[0][1] + 1, 'd'); P(9 + L[2][0], 9, 2, L[2][1] + 1, 'd');
      // body
      P(2, 4, 11, 6, 'o'); P(3, 5, 9, 4, 'b'); P(4, 8, 6, 1, 'l'); P(4, 5, 5, 1, 'd');
      // near legs
      P(5 + L[1][0], 9, 2, L[1][1] + 1, 'b'); P(11 + L[3][0], 9, 2, L[3][1] + 1, 'b');
      
    } else {
      P(0, 10 + (tail ? 0 : 0), 3, 1, 'd'); if (tail === 1) P(0, 9, 1, 1, 'd');
      P(1, 6, 7, 7, 'o'); P(2, 7, 5, 5, 'b');
      P(6, 3, 5, 10, 'o'); P(7, 4, 3, 8, 'b'); P(7, 9, 3, 3, 'l');
      P(9, 10, 2, 4, 'd');
    }
    // head
    var y0 = hd + (f.sit ? -1 : 0);
    P(9 + hx, 1 + y0, 7, 7, 'o'); P(10 + hx, 2 + y0, 5, 5, 'b');
    P(9 + hx, 2 + y0, 2, 4, 'd');                       // ear
    P(13 + hx, 4 + y0, 2, 2, 'l'); P(15 + hx, 4 + y0, 1, 1, 'n'); // snout + nose
    if (f.blink) P(12 + hx, 3 + y0, 1, 1, 'd'); else P(12 + hx, 3 + y0, 1, 1, 'e');
  }
  var A = [[0, 4], [0, 4], [0, 4], [0, 4]];
  var WALK1 = [[0, 4], [1, 3], [1, 3], [0, 4]], WALK2 = [[1, 3], [0, 4], [0, 4], [1, 3]];
  var RUN1 = [[-2, 3], [-1, 3], [2, 3], [1, 3]], RUN2 = [[1, 3], [0, 4], [-1, 4], [0, 4]];
  var FRAMES = {
    idle: [{ tail: 0 }, { tail: 1, hd: 0 }, { tail: 2, blink: 1 }, { tail: 1, hd: 1 }],
    walk: [{ legs: WALK1, tail: 1 }, { legs: A, tail: 1, dy: -1 }, { legs: WALK2, tail: 0 }, { legs: A, tail: 0, dy: -1 }],
    run:  [{ legs: RUN1, tail: 2, dy: -1, hx: 1 }, { legs: A, tail: 1, dy: -2, hx: 1 }, { legs: RUN2, tail: 2, dy: -1, hx: 1 }, { legs: A, tail: 1, dy: 0, hx: 1 }],
    sniff:[{ hd: 3, hx: 0, tail: 1 }, { hd: 4, hx: 1, tail: 0 }, { hd: 3, hx: 0, tail: 1 }, { hd: 4, hx: 1, tail: 2 }],
    look: [{ hd: -1, tail: 1 }, { hd: -1, tail: 0, blink: 1 }, { hd: -1, tail: 1 }, { hd: -1, tail: 2 }],
    sit:  [{ sit: 1, tail: 0 }, { sit: 1, tail: 1 }, { sit: 1, tail: 0, blink: 1 }, { sit: 1, tail: 1 }],
    excited: [{ dy: -3, tail: 0, hd: -1, legs: WALK1 }, { dy: 0, tail: 2 }, { dy: -3, tail: 2, hd: -1, legs: WALK2 }, { dy: 0, tail: 0 }],
    wag:  [{ tail: 0 }, { tail: 2 }, { tail: 0 }, { tail: 2 }]
  };
  var names = ['idle', 'walk', 'run', 'sniff', 'look', 'sit', 'excited', 'wag'];
  var sheet = document.createElement('canvas'); sheet.width = AW * COLS; sheet.height = AH * names.length;
  var sx = sheet.getContext('2d');
  names.forEach(function (n, r) { FRAMES[n].forEach(function (f, i) { paint(sx, i * AW, r * AH, f); }); });
  var url = sheet.toDataURL('image/png');

  /* ---------- DOM + styles ---------- */
  var css = '.dog{position:fixed;left:0;top:0;width:' + W + 'px;height:' + H + 'px;z-index:2147483000;pointer-events:none;opacity:0;transition:opacity .3s;will-change:transform}' +
    '.dog.on{opacity:1}.dog__flip{width:100%;height:100%}' +
    '.dog__spr{width:' + W + 'px;height:' + H + 'px;background:url(' + url + ') 0 0/' + (W * COLS) + 'px ' + (H * names.length) + 'px no-repeat;image-rendering:pixelated;image-rendering:crisp-edges;image-rendering:pixelated;animation:d-play 1s steps(' + COLS + ') infinite;filter:drop-shadow(0 1px 0 rgba(0,0,0,.18))}' +
    '@keyframes d-play{from{background-position-x:0}to{background-position-x:-' + (W * COLS) + 'px}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var el = document.createElement('div'); el.className = 'dog'; el.setAttribute('aria-hidden', 'true');
  el.innerHTML = '<div class="dog__flip"><div class="dog__spr"></div></div>';
  var flip = el.firstChild, spr = flip.firstChild;
  document.body.appendChild(el);

  var x = innerWidth - 90, y = innerHeight - 70, mx = x + W + 16, my = y - 10, face = 1, state = '', raf = 0;
  var react = null, doneEl = null, clickUntil = 0;

  function setState(s) {
    if (s === state) return; state = s;
    spr.style.backgroundPositionY = (-ROW[s] * H) + 'px';
    spr.style.animationDuration = DUR[s] + 's';
  }
  function setFace(f) { if (f !== face) { face = f; flip.style.transform = 'scaleX(' + f + ')'; } }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  function followGoal() {
    var gx = mx - W - 16; if (mx < W + 40) gx = mx + 18;
    return { x: clamp(gx, 4, innerWidth - W - 4), y: clamp(my + 10, 4, innerHeight - H - 4) };
  }
  function rectGoal(r) {
    var gx = clamp(mx - W / 2, r.left, r.right - W), gy = r.bottom + 6;
    if (gy + H > innerHeight - 2) gy = r.top - H - 6;
    return { x: clamp(gx, 4, innerWidth - W - 4), y: clamp(gy, 4, innerHeight - H - 4) };
  }
  function cardGoal(node) {
    var r = (node.querySelector('.shot') || node).getBoundingClientRect();
    return { x: clamp(r.right - W - 18, 4, innerWidth - W - 4), y: clamp(r.bottom + 6, 4, innerHeight - H - 4) };
  }
  function kick() { if (!raf) raf = requestAnimationFrame(loop); }

  function loop(now) {
    raf = 0;
    var k = 0.1, busy = false, goal;
    if (react && react.card) react.goal = cardGoal(react.el);
    goal = (react && react.goal) || followGoal();
    if (react && react.kind === 'run' && react.arrived) {
      var a = (now - react.arrived) / 150;
      goal = { x: react.goal.x + Math.cos(a) * 18, y: react.goal.y + Math.sin(a) * 8 }; k = 0.2; busy = true;
    }
    var sx_ = (goal.x - x) * k, sy_ = (goal.y - y) * k, sp = Math.hypot(sx_, sy_);
    if (sp > 26) { sx_ *= 26 / sp; sy_ *= 26 / sp; sp = 26; }
    x += sx_; y += sy_;
    el.style.transform = 'translate3d(' + Math.round(x) + 'px,' + Math.round(y) + 'px,0)';

    var dist = Math.hypot(goal.x - x, goal.y - y), moving = sp > 0.6;
    if (moving && Math.abs(sx_) > 0.25) setFace(sx_ > 0 ? 1 : -1);
    var s;
    if (now < clickUntil) { s = 'excited'; busy = true; }
    else if (react && !react.done && (dist < 6 || (react.kind === 'look' && !react.goal))) {
      if (!react.arrived) { react.arrived = now; react.until = now + (react.dur || 0); }
      if (react.kind !== 'run') setFace((react.look != null ? react.look : mx) > x + W / 2 ? 1 : -1);
      s = { sniff: 'sniff', sit: 'sit', excited: 'excited', wag: 'wag', run: 'run', look: 'look' }[react.kind] || 'look';
      if (react.dur) { if (now > react.until) { react.done = true; doneEl = react.el; s = 'idle'; } busy = true; }
    } else if (moving) s = sp > 6.5 ? 'run' : 'walk';
    else { s = 'idle'; setFace(mx > x + W / 2 ? 1 : -1); }
    setState(s);
    if (moving || busy || (react && !react.done && dist >= 6)) kick();
  }

  function reactionFor(node) {
    var kind = node.getAttribute('data-dog-reaction'); if (!kind) return null;
    var r = { el: node, kind: kind, goal: null, done: false };
    var b = node.getBoundingClientRect();
    if (node.getAttribute('data-dog-goto') === 'below') { r.goal = rectGoal(b); r.kind = 'look'; r.look = b.left + b.width / 2; }
    else if (node.classList.contains('case')) { r.card = true; r.dur = kind === 'sit' ? 0 : (kind === 'run' ? 1800 : 1900); r.goal = cardGoal(node); }
    else if (kind === 'look') { r.look = b.left + b.width / 2; if (node.classList.contains('case__go')) r.goal = rectGoal(b); }
    return r;
  }

  document.addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY; el.classList.add('on'); kick();
  }, { passive: true });
  document.addEventListener('mouseover', function (e) {
    var n = e.target.closest ? e.target.closest('[data-dog-reaction]') : null;
    if (!n || n === doneEl || (react && react.el === n)) return;
    react = reactionFor(n); kick();
  }, { passive: true });
  document.addEventListener('mouseout', function (e) {
    var n = e.target.closest ? e.target.closest('[data-dog-reaction]') : null;
    if (!n || (e.relatedTarget && n.contains(e.relatedTarget))) return;
    if (react && react.el === n) react = null;
    if (doneEl === n) doneEl = null;
    kick();
  }, { passive: true });
  document.addEventListener('pointerdown', function () { clickUntil = performance.now() + 700; kick(); }, { passive: true });
  window.addEventListener('resize', kick);

  setState('idle'); el.classList.add('on'); kick();
})();
