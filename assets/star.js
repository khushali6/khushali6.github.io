/* Little star companion. Self-contained, no dependencies. Replaces the old dog.
   Follows the pointer with a soft lag, spins gently, perks up over interactive bits
   (anything the old dog reacted to: [data-dog-reaction]) and pops on click. */
(function () {
  if (!window.matchMedia) return;
  if (!matchMedia('(any-hover: hover)').matches) return; // touch-only devices: no star

  var S = 26;                                   // star size in px
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var css = '.star{position:fixed;left:0;top:0;width:' + S + 'px;height:' + S + 'px;z-index:2147483000;pointer-events:none;opacity:0;transition:opacity .3s;will-change:transform;contain:layout style}' +
    '.star.on{opacity:1}' +
    '.star__pop{width:100%;height:100%;transition:transform .22s cubic-bezier(.34,1.56,.64,1)}' +
    '.star svg{display:block;width:100%;height:100%;overflow:visible;filter:drop-shadow(0 0 5px rgba(250,204,0,.7))}' +
    '.star__shape{transform-box:fill-box;transform-origin:50% 50%;animation:star-spin 7s linear infinite,star-twinkle 2.2s ease-in-out infinite}' +
    '.star[data-s=hover] .star__shape{animation-duration:1.6s,.7s}' +
    '.star[data-s=hover] .star__pop{transform:scale(1.45)}' +
    '.star[data-s=click] .star__pop{transform:scale(.7)}' +
    '@keyframes star-spin{to{transform:rotate(360deg)}}' +
    '@keyframes star-twinkle{0%,100%{transform:scale(1)}50%{transform:scale(.86)}}' +
    '@media (prefers-reduced-motion:reduce){.star__shape{animation:none}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  // 5-point star (outer r=11, inner r=4.6, centred in a 24x24 box)
  var pts = [];
  for (var i = 0; i < 10; i++) {
    var a = -Math.PI / 2 + i * Math.PI / 5, r = i % 2 ? 4.8 : 11.5;
    pts.push((12 + Math.cos(a) * r).toFixed(2) + ',' + (12 + Math.sin(a) * r).toFixed(2));
  }
  var SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><g class="star__shape">' +
    '<polygon points="' + pts.join(' ') + '" fill="#facc00" stroke="#161616" stroke-width="1.6" stroke-linejoin="round"/>' +
    '<polygon points="' + pts.join(' ') + '" fill="none" stroke="#fff6bf" stroke-width=".6" stroke-linejoin="round" opacity=".7" transform="translate(12 12) scale(.62) translate(-12 -12)"/>' +
    '</g></svg>';

  var el = document.createElement('div'); el.className = 'star'; el.setAttribute('aria-hidden', 'true');
  el.innerHTML = '<div class="star__pop">' + SVG + '</div>';
  document.body.appendChild(el);

  var mx = innerWidth / 2, my = innerHeight / 2, x = mx, y = my, raf = 0, seen = false;
  var hover = 0, clickUntil = 0, state = '';

  function setState(s) { if (s !== state) { state = s; el.setAttribute('data-s', s); } }
  function goal() { return { x: mx + 14, y: my + 14 }; }  // hangs just off the pointer, bottom-right

  function loop(now) {
    raf = 0;
    var g = goal(), k = reduced ? 1 : 0.2;
    x += (g.x - x) * k; y += (g.y - y) * k;
    el.style.transform = 'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0)';
    setState(now < clickUntil ? 'click' : (hover ? 'hover' : 'idle'));
    if (Math.hypot(g.x - x, g.y - y) > 0.3 || now < clickUntil) raf = requestAnimationFrame(loop);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(loop); }

  document.addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY;
    if (!seen) { seen = true; x = mx + 14; y = my + 14; el.classList.add('on'); }
    kick();
  }, { passive: true });

  document.addEventListener('mouseover', function (e) {
    if (e.target.closest && e.target.closest('[data-dog-reaction]')) { hover = 1; kick(); }
  }, { passive: true });
  document.addEventListener('mouseout', function (e) {
    var n = e.target.closest ? e.target.closest('[data-dog-reaction]') : null;
    if (!n) return;
    var to = e.relatedTarget;
    if (to && n.contains(to)) return;
    hover = 0; kick();
  }, { passive: true });

  document.addEventListener('pointerdown', function () { clickUntil = performance.now() + 220; kick(); }, { passive: true });
  document.addEventListener('mouseleave', function () { el.classList.remove('on'); seen = false; });
})();
