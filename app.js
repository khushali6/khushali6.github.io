const projects = [
  {
    name: 'Meadow',
    type: 'LOCAL-FIRST AGENT',
    description: 'A local-first agent that turns a request into finished, tested code by driving a coding engine phase by phase.',
    tags: ['TypeScript', 'Agents', 'Code systems'],
    url: 'https://github.com/khushali6/Meadow',
    accent: 'signal'
  },
  {
    name: 'SignVerse',
    type: 'ACCESSIBLE VISION',
    description: 'A cross-platform communication app exploring sign-language-to-text and voice conversion, learning resources, and community chat.',
    tags: ['Flutter', 'TFLite', 'Accessibility'],
    url: 'https://github.com/khushali6/SignVerse_Project',
    accent: 'signal'
  },
  {
    name: 'Intentroute',
    type: 'INTENT ROUTING',
    description: 'A Python exploration of routing user intent toward the right path, tool, or next action.',
    tags: ['Python', 'NLP', 'Routing'],
    url: 'https://github.com/khushali6/Intentroute',
    accent: 'signal'
  },
  {
    name: 'NeuralCraft',
    type: 'AI PRODUCT SURFACE',
    description: 'An AI product landing-page concept built around the promise of intelligence that works at scale.',
    tags: ['React', 'Product', 'AI'],
    url: 'https://github.com/khushali6/NeuralCraft',
    accent: 'signal'
  },
  {
    name: 'CoFoundry',
    type: 'STARTUP INTELLIGENCE',
    description: 'A startup discovery and hiring radar powered by TinyFish Web Agent API, with enrichment, jobs, team, and outreach flows.',
    tags: ['JavaScript', 'Web agents', 'Vercel'],
    url: 'https://co-foundry.vercel.app',
    github: 'https://github.com/khushali6/CoFoundry',
    accent: 'signal'
  }
];

const projectGrid = document.querySelector('#project-grid');
if (projectGrid) {
  projectGrid.innerHTML = projects.map((project, index) => `
    <article class="project-card reveal">
      <div class="card-top"><span class="card-number">0${index + 1}</span><span>${project.type}</span></div>
      <div class="signal" aria-hidden="true"></div>
      <div class="card-body"><h3>${project.name}</h3><p>${project.description}</p></div>
      <div class="card-foot"><div class="card-tags">${project.tags.map(tag => `<span>${tag}</span>`).join('')}</div><a class="card-link" href="${project.url}" target="_blank" rel="noreferrer" aria-label="Open ${project.name}">↗</a></div>
    </article>
  `).join('');
}

const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
menuToggle?.addEventListener('click', () => {
  const isOpen = nav.classList.toggle('is-open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.querySelector('em').textContent = isOpen ? 'Close' : 'Menu';
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('is-open');
  menuToggle?.setAttribute('aria-expanded', 'false');
  if (menuToggle) menuToggle.querySelector('em').textContent = 'Menu';
}));

const revealItems = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: .12, rootMargin: '0px 0px -30px' });
revealItems.forEach(item => revealObserver.observe(item));

document.querySelector('#year').textContent = new Date().getFullYear();
