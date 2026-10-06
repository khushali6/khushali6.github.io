#!/usr/bin/env python3
"""Generates the static site (index + case-study pages). Run: python3 tools/build.py"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://khushali6.github.io"
EMAIL, GH, LI = "khushalipariyal@gmail.com", "https://github.com/khushali6", "https://linkedin.com/in/khushalipariyal"
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
GHI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65S8.93 17.38 9 18v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>'
LIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></svg>'
ICONS = {
 "agents": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4M9 14h.01M15 14h.01M2 14h2M20 14h2"/></svg>',
 "rag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3M8 11h6M11 8v6"/></svg>',
 "vision": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
 "product": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m14.7 6.3 3 3L7 20H4v-3zM15 5l1.3-1.3a2.1 2.1 0 0 1 3 3L18 8"/></svg>',
}

def e(s): return html.escape(s, quote=True)
def flow(steps, cls=""):
    return '<ol class="flow %s" aria-label="Workflow">%s</ol>' % (cls, '<li class="arr" aria-hidden="true"></li>'.join('<li>%s</li>' % e(s) for s in steps))
def tags(ts): return '<div class="tags">%s</div>' % ''.join('<span class="tag">%s</span>' % e(t) for t in ts)

NAV = [("Work", "/#work"), ("Projects", "/#projects"), ("About", "/#about"), ("GitHub", "/#github"), ("Contact", "/#contact")]

def page(title, desc, path, body, og_title=None, cur=None):
    nav = ''.join('<li><a class="lnk" href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if cur == n else '', n) for n, h in NAV)
    url = SITE + path
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Khushali Pariyal">
<meta property="og:title" content="{e(og_title or title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f6f2e9">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Khushali Pariyal","jobTitle":"AI Engineer","url":"{SITE}/","sameAs":["{GH}","{LI}"],"knowsAbout":["Agentic AI","RAG","Multimodal AI","Generative AI","LLMOps"]}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
<a class="brand" href="/"><i></i>KHUSHALI</a>
<button class="burger" aria-label="Menu" aria-expanded="false">Menu</button>
<nav aria-label="Primary"><ul>{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap"><span>© 2026 Khushali Pariyal</span><span>Built by hand · projects pulled live from the GitHub API</span></div></footer>
<script src="/assets/app.js" defer></script>
</body>
</html>
'''

def contact_block():
    return f'''<section id="contact" style="padding-bottom:0"><div class="wrap"><div class="contact rv">
<p class="eyebrow" style="color:#cfe6d6">10 — CONTACT</p>
<h2 style="margin-top:18px">Have an interesting <em>AI problem?</em></h2>
<p class="lead">I'm always interested in building things where the obvious solution isn't another chatbot.</p>
<div class="btns"><a class="btn" href="mailto:{EMAIL}">{MAIL} Email me</a><a class="btn ghost" href="{GH}" target="_blank" rel="noopener">{GHI} GitHub</a><a class="btn ghost" href="{LI}" target="_blank" rel="noopener">{LIN} LinkedIn</a></div>
<div class="who"><span><b>Khushali Pariyal</b></span><span>AI Engineer · Agentic AI · RAG · Multimodal AI</span><span>{EMAIL}</span></div>
</div></div></section>'''

# ------------------------------------------------------------------ INDEX
PROJECTS = [
 dict(slug="meadow", name="MEADOW", label="AGENTIC CODING SYSTEM", head="Your coding environment, from your pocket.",
      blurb="Meadow is a local-first agentic coding system that turns a request into a planned, tested and reviewable coding workflow.",
      steps=["Plan","Build","Test","Review","Merge"], tags=["Agentic AI","MCP","Tool Calling","TypeScript","Human-in-the-loop","Harness Engineering"],
      repo="Meadow", gh="https://github.com/khushali6/Meadow", live=None,
      why="The interesting part isn't that an LLM writes code. It's what happens when the code it writes is wrong.", alt="Illustrative Meadow dashboard: phases, a failing test returned to the engine, and an approval gate"),
 dict(slug="casora", name="CASORA", label="AI DECISION INTELLIGENCE", head="Real estate research without the broker maze.",
      blurb="Casora is an AI-powered real-estate research product for searching, comparing and understanding homes across India using verified information and locality-level intelligence.",
      steps=["Ask","Search","Verify","Compare","Decide"], tags=["LLM","Semantic Search","Investment Analytics","Explainable AI","Full-Stack"],
      repo=None, gh=None, live="https://casora-nine.vercel.app/",
      why="Don't invent a number just because the model can.", alt="Illustrative Casora UI: natural-language search, linked listings and a decision panel"),
 dict(slug="splitmate", name="SPLITMATE", label="MULTIMODAL AI", head="Take a photo. Split the bill.",
      blurb="An AI expense-sharing product that understands receipts and turns them into structured expenses and fair settlements.",
      steps=["Receipt","AI","Structure","Math","Split"], tags=["OCR","VLM","Gemini API","Deterministic Engine","Debt Graph","Full-Stack"],
      repo=None, gh=None, live="https://splitmate-two-iota.vercel.app/",
      why="The LLM never does the math.", alt="Illustrative SplitMate UI: receipt, extracted items, math engine and minimum settlements"),
 dict(slug="laya", name="LAYA", label="CREATIVE AI EXPERIMENT", head="What happens when AI gets a meme brain?",
      blurb="A playful AI experiment exploring character-driven content generation and creative AI workflows.",
      steps=["Idea","AI","Meme"], tags=["LLM Workflows","Creative AI","Generative"],
      repo=None, gh=None, live="https://layameme.vercel.app/",
      why="Built because AI should be fun too.", alt="Illustrative Laya meme cards"),
]

def feature(i, p):
    links = f'<a class="btn" href="/{p["slug"]}/">Case study {ARROW}</a>'
    if p["live"]: links += f'<a class="btn ghost" href="{p["live"]}" target="_blank" rel="noopener">Live demo {EXT}</a>'
    if p["gh"]: links += f'<a class="btn ghost" href="{p["gh"]}" target="_blank" rel="noopener">{GHI} GitHub</a>'
    meta = f'<div class="ghmeta" data-repo="{p["repo"]}" aria-label="GitHub stats"></div>' if p["repo"] else ''
    return f'''<article class="feature rv">
<div class="f-text">
<p class="name">0{i} — {p["name"]}</p>
<p class="label">{p["label"]}</p>
<h3>{e(p["head"])}</h3>
<p>{e(p["blurb"])}</p>
<div class="fl">{flow(p["steps"])}</div>
<p class="why">“{e(p["why"])}”</p>
{tags(p["tags"])}
{meta}
<div class="btns" style="margin-top:26px">{links}</div>
</div>
<a href="/{p["slug"]}/" aria-label="{p["name"].title()} case study"><figure class="shot"><img src="/assets/img/{p["slug"]}.svg" alt="{e(p["alt"])}" width="1200" height="800" loading="lazy"><figcaption>ILLUSTRATIVE UI · {p["name"]}</figcaption></figure></a>
</article>'''

PROD = [
 ("REQUIREMENTS → SOFTWARE", ["AWS Bedrock","AgentCore","RAG","Textract","OpenSearch","Lambda","EventBridge"],
  "Built an agentic workflow that takes stakeholder requirements through retrieval, code generation, automated review and deployment.", [(75,"%","faster feature turnaround")]),
 ("ADAS TEST GENERATION", ["Multimodal RAG","FAISS","LLM","Validation Loops"],
  "Generated ADAS test cases from NCAP specification documents containing text, tables and images, with agentic validation loops to reduce hallucination.", [(70,"%","less manual test creation"),(2,"×","test coverage")]),
 ("AI CODE REVIEW", ["LLM","CI/CD","Static Analysis","Security"],
  "Developer tooling for automated code review, architectural validation and security vulnerability detection inside CI/CD pipelines.", [(80,"%","less manual review effort")]),
 ("COMPUTER VISION INSPECTION", ["DeepLabV3","PatchCore","Stable Diffusion","PyTorch"],
  "Multi-camera inspection pipeline processing 20K+ images per cycle, using synthetic data to improve robustness under changing lighting and weather.", [(18,"–22%","precision/recall improvement")]),
]
def prod_cards(link=True):
    out = []
    for t, st, d, ms in PROD:
        m = ''.join(f'<div class="metric"><div class="n"><span data-count="{n}" data-suffix="{s}">0{s}</span></div><div class="t">{e(l)}</div></div>' for n, s, l in ms)
        out.append(f'<article class="card rv"><p class="sm">{t}</p>{tags(st)}<p style="margin-top:18px">{e(d)}</p><div class="metrics">{m}</div></article>')
    return '\n'.join(out)

PRINC = [
 ("01","Don't let the LLM do deterministic work.","If something can be solved reliably with code, I don't ask the model to guess.","SplitMate","/splitmate/"),
 ("02","Give agents tools, not superpowers.","Let the model make decisions, but don't let it invent the state of the world.","Meadow","/meadow/"),
 ("03","Retrieval is not memory.","Searchable knowledge, conversation state, durable facts and past events are different problems.","Agentic / RAG systems","/work/"),
 ("04","Measure the system, not the demo.","A good-looking answer isn't enough. I care about correctness, failure recovery, latency, cost and whether the system actually helps.","Production AI systems","/work/"),
]
STACK = [
 ("AI / AGENTS", ["Python","LangGraph","LangChain","MCP","Tool Calling","Multi-Agent Systems","Agent Harness Engineering","Human-in-the-loop"]),
 ("LLM / RAG", ["AWS Bedrock","OpenAI","Gemini","DeepSeek","Ollama","Embeddings","FAISS","OpenSearch","Vector Search","Semantic Search"]),
 ("BACKEND", ["FastAPI","Django","Node.js","REST APIs","PostgreSQL","MongoDB","Redis"]),
 ("CLOUD", ["AWS","Azure","Lambda","EventBridge","Textract","AgentCore","Docker"]),
 ("ML / VISION", ["PyTorch","YOLO","DeepLabV3","PatchCore","Stable Diffusion","OCR","VLM"]),
 ("LANGUAGES", ["Python","TypeScript","JavaScript","Java","SQL","C++","C"]),
]

def index():
    wb = [("agents","AGENTS","Systems that plan, use tools, maintain state and recover from failures.",["MCP","Tool Calling","Multi-Agent","Human-in-the-loop","Agent Harnesses"]),
          ("rag","RAG & INTELLIGENCE","Systems that retrieve evidence before they make decisions.",["Embeddings","Vector Search","Semantic Search","Hybrid Retrieval","Evaluation"]),
          ("vision","MULTIMODAL AI","Systems that understand documents, images, receipts and real-world visual data.",["OCR","VLM","Computer Vision","Document Understanding"]),
          ("product","AI PRODUCTS","I don't stop at the model. I build the product around it.",["APIs","Databases","Cloud","Frontend","Observability","Deployment"])]
    wbh = ''.join(f'<article class="card rv"><div class="ico">{ICONS[i]}</div><h3 style="font-size:18px;font-family:var(--mono);letter-spacing:.1em">{t}</h3><p>{d}</p>{tags(ts)}</article>' for i, t, d, ts in wb)
    feats = '\n'.join(feature(i + 1, p) for i, p in enumerate(PROJECTS))
    princ = ''.join(f'<article class="card rv"><p class="num">{n}</p><h3>{e(h)}</h3><blockquote>“{e(q)}”</blockquote><p class="ref">Reference · <a href="{u}">{e(r)}</a></p></article>' for n, h, q, r, u in PRINC)
    stack = ''.join(f'<div><h4>{h}</h4><p>{" ".join("<span>%s</span>" % e(x) for x in items)}</p></div>' for h, items in STACK)
    body = f'''
<section class="hero"><div class="wrap">
<p class="eyebrow">AI ENGINEER · AGENTIC AI · RAG · MULTIMODAL AI</p>
<h1>I build AI systems that <em>actually do things.</em></h1>
<p class="lead">AI Engineer building agentic systems, RAG pipelines, multimodal AI and AI products — from the first prototype to production.</p>
<div class="btns"><a class="btn" href="#projects">View my work {ARROW}</a><a class="btn ghost" href="{GH}" target="_blank" rel="noopener">{GHI} GitHub</a><a class="btn ghost" href="{LI}" target="_blank" rel="noopener">{LIN} LinkedIn</a></div>
<div class="proof">
<div><p class="k">2+ YEARS</p><p class="v">Production AI</p><p class="s">Professional AI engineering</p></div>
<div><p class="k">AGENTIC AI</p><p class="v">MCP · Tool Calling</p><p class="s">Multi-Agent</p></div>
<div><p class="k">RAG</p><p class="v">Search · Retrieval</p><p class="s">Evaluation</p></div>
<div><p class="k">AI PRODUCTS</p><p class="v">4+ Shipped Projects</p><p class="s">Idea to working software</p></div>
</div>
<p class="now">Currently building agents, AI products, and systems that turn messy information into useful decisions.</p>
</div></section>

<section id="what" style="border-top:1px solid var(--line)"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>02</b> — WHAT I BUILD</p><h2>I like building the <em>system around</em> the model.</h2></div>
<div class="grid4">{wbh}</div>
</div></section>

<section id="projects" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>03</b> — FEATURED BUILDS</p><h2>Things I've actually <em>shipped.</em></h2><p>A few experiments, products and systems I've built from idea to working software. Screens shown are illustrative mockups of each product's UI.</p></div>
{feats}
</div></section>

<section class="dark" id="meadow-deep"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>04</b> — DEEP DIVE · MEADOW</p><h2>What happens when the agent is <em>wrong?</em></h2><p>Most coding-agent demos stop at “it wrote the code.” Meadow's harness is built for the next ten seconds.</p></div>
<div class="loop">
<div>
{flow(["Request","Spec","Plan","Supervisor","Engine","Tools / MCP","Git branch","Test"],"vertical")}
<p class="pull">If tests <em>pass</em>, the phase merges.<br>If they fail, the <em>real error</em> goes back to the engine — up to 3 fix attempts.</p>
</div>
<div class="term" role="img" aria-label="Example terminal output of a failing test returned to the coding engine">
<span class="c"># phase 3 · branch phase-3-auth · illustrative output</span><br>
<span class="b">engine</span> &gt; implementing session refresh…<br>
<span class="b">guard</span>  &gt; lint ok · types ok<br>
<span class="b">tests</span>  &gt; <span class="r">✗ rejects expired token (expected 401, got 200)</span><br>
<span class="b">harness</span> &gt; attempt 1/3 failed — sending the real error back<br>
<span class="b">engine</span> &gt; patching src/auth/session.ts<br>
<span class="b">tests</span>  &gt; <span class="g">✓ 14 passed</span><br>
<span class="b">approval</span> &gt; merge phase-3-auth? <span class="g">[y]</span><br>
<span class="b">audit</span>  &gt; logged · 4 tool calls · 2 test runs
</div></div>
<div class="chips">
<div class="chip"><b>Branch per phase</b>Every phase is isolated, with its own guard checks and tests.</div>
<div class="chip"><b>Supervisor agent</b>Reviews failures and reports progress over Telegram.</div>
<div class="chip"><b>MCP + approval gates</b>Explicit tools, audit logs, and a human in the loop.</div>
<div class="chip"><b>CodeAtlas</b>Knowledge-graph context so answers can be cited.</div>
<div class="chip"><b>Parallel phases</b>Independent phases run side by side.</div>
<div class="chip"><b>Flow tests</b>Headless-browser runs with desktop and mobile screenshots.</div>
</div>
<div class="btns" style="margin-top:44px"><a class="btn" style="background:var(--bg);color:var(--ink);border-color:var(--bg)" href="/meadow/">Read the Meadow case study {ARROW}</a><a class="btn ghost" style="color:var(--bg);border-color:#5a5a52" href="https://github.com/khushali6/Meadow" target="_blank" rel="noopener">{GHI} Source</a></div>
</div></section>

<section id="work"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>05</b> — PRODUCTION AI @ TCS</p><h2>When the model has to work in the <em>real world.</em></h2><p>Selected production AI systems I've worked on professionally. Described at a high level; no confidential employer or customer details.</p></div>
<div class="prod">{prod_cards()}</div>
<div class="btns" style="margin-top:28px"><a class="btn ghost" href="/work/">All production work {ARROW}</a></div>
</div></section>

<section id="think" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>06</b> — HOW I THINK ABOUT AI</p><h2>Four things I learned by <em>building</em> these systems.</h2></div>
<div class="princ">{princ}</div>
</div></section>

<section id="stack"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>07</b> — ENGINEERING STACK</p><h2>Tools I <em>actually</em> use.</h2><p>Organised by the system they serve, not as a logo wall.</p></div>
<div class="stack rv">{stack}</div>
</div></section>

<section id="github" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
<div class="sec-head"><p class="eyebrow"><b>08</b> — EXPERIMENTS &amp; GITHUB</p><h2>The rest of the <em>workbench.</em></h2><p>Public repositories, fetched live from the GitHub API each time you visit.</p></div>
<div class="repos" id="repos" aria-live="polite"></div>
<p class="status" id="repos-status">Loading repositories from GitHub…</p>
<div class="btns" style="margin-top:22px"><a class="btn ghost" href="{GH}?tab=repositories" target="_blank" rel="noopener">{GHI} All repositories</a></div>
</div></section>

<section id="about"><div class="wrap about">
<div><p class="eyebrow" style="margin-bottom:18px"><b>09</b> — ABOUT</p><h2 style="margin-bottom:30px">A little <em>about me.</em></h2>
<p>I'm an AI Engineer who likes building things that are a little more ambitious than a chatbot.</p>
<p>I've spent the last 2+ years working across agentic AI, RAG, multimodal systems, computer vision and AI products.</p>
<p>I enjoy the messy part of AI engineering — figuring out what the model should do, what it absolutely shouldn't do, how it should use tools, how it should recover when it's wrong, and how to know whether it actually helped.</p>
<p>Outside of work, I build projects because I usually learn more by shipping something than by reading another framework's documentation.</p></div>
<div class="edu" style="align-self:end"><p class="sm" style="margin-top:6px">EDUCATION</p>
<div><b>B.E. Computer Engineering</b><span>Government Engineering College Gandhinagar · CGPA 8.37</span></div>
<div><b>Diploma in Information Technology</b><span>Government Polytechnic for Girls Ahmedabad · CGPA 9.69</span></div></div>
</div></section>
{contact_block()}
'''
    return page("Khushali Pariyal — AI Engineer | Agentic AI, RAG & Generative AI",
                "Khushali Pariyal is an AI Engineer building agentic AI systems, RAG pipelines, multimodal AI and AI products.", "/", body)

# ------------------------------------------------------------------ CASE STUDIES
def cs_sections(secs):
    names = ["What is it?","Why I built it","The problem","How it works","Architecture","What I personally built","Interesting engineering decisions","Failure cases","Results","Screenshots / demo","What I'd build next","GitHub / Live demo"]
    return names

def case_page(p):
    n = cs_sections(None)
    toc = ''.join(f'<a href="#s{i+1}">{i+1:02d} · {nm}</a>' for i, nm in enumerate(n))
    s = p["sections"]
    def sec(i, content): return f'<section class="cs-sec" id="s{i}"><p class="n">{i:02d}</p><h2>{n[i-1]}</h2>{content}</section>'
    ul = lambda items: '<ul>%s</ul>' % ''.join(f'<li>{x}</li>' for x in items)
    decisions = ''.join(f'<div class="decision"><p class="q">QUESTION</p><h3>{e(q)}</h3><p>{a}</p></div>' for q, a in s["decisions"])
    fails = ''.join(f'<div class="fail"><b>{e(a)}</b> {e(b)}</div>' for a, b in s["failures"])
    links = ''
    if p.get("live"): links += f'<a class="btn" href="{p["live"]}" target="_blank" rel="noopener">Live demo {EXT}</a>'
    if p.get("gh"): links += f'<a class="btn ghost" href="{p["gh"]}" target="_blank" rel="noopener">{GHI} GitHub</a>'
    if not links: links = f'<a class="btn ghost" href="{GH}" target="_blank" rel="noopener">{GHI} GitHub profile</a>'
    meta = f'<div class="ghmeta" data-repo="{p["repo"]}" style="margin-top:0"></div>' if p.get("repo") else ''
    shot = p.get("shot")
    shot_html = f'<figure class="shot cs-shot"><img src="/assets/img/{shot}.svg" alt="{e(p["alt"])}" width="1200" height="800"><figcaption>ILLUSTRATIVE UI MOCKUP · {p["name"]} — not a literal screenshot</figcaption></figure>' if shot else ''
    arch = s["arch"]
    body = f'''
<section class="cs-hero" style="padding-bottom:0"><div class="wrap">
<p class="eyebrow"><a href="/#projects" style="text-decoration:none">← ALL PROJECTS</a> &nbsp;·&nbsp; <b>{p["label"]}</b></p>
<h1>{e(p["head"])}</h1>
<p class="lead">{e(p["blurb"])}</p>
{flow(p["steps"], "big")}
<div class="cs-meta"><div><b>Type</b>{e(p["type"])}</div><div><b>Role</b>{e(p["role"])}</div><div><b>Stack</b>{e(", ".join(p["tags"]))}</div>{meta}</div>
{shot_html}
</div></section>
<div class="wrap"><div class="cs-body">
<nav class="toc" aria-label="Case study sections">{toc}</nav>
<div>
{sec(1, s["what"])}
{sec(2, s["why"])}
{sec(3, s["problem"])}
{sec(4, ul(s["how"]))}
{sec(5, arch)}
{sec(6, ul(s["built"]))}
{sec(7, decisions)}
{sec(8, fails)}
{sec(9, s["results"])}
{sec(10, s["demo"])}
{sec(11, ul(s["next"]))}
{sec(12, '<div class="btns">%s</div>' % links)}
</div></div>
<div class="pager"><a href="{p["prev"][1]}"><small>← PREVIOUS</small>{p["prev"][0]}</a><a href="{p["next"][1]}" style="text-align:right"><small>NEXT →</small>{p["next"][0]}</a></div>
</div>
{contact_block()}
'''
    return page(f'{p["name"].title()} — {p["head"]} | Khushali Pariyal', p["blurb"], f'/{p["slug"]}/', body, cur="Projects")

def archexplorer(nodes):
    btns = ''.join(f'<button role="tab" data-target="n{i}" aria-selected="false">{e(t)}</button>' for i, (t, _, _) in enumerate(nodes))
    panels = ''.join(f'<div data-panel="n{i}" hidden><h3>{e(t)}</h3><p>{d}</p>{("<div class=term>%s</div>" % c) if c else ""}</div>' for i, (t, d, c) in enumerate(nodes))
    return f'<p>Click through the pipeline to see what each stage does.</p><div class="arch"><div class="nodes" role="tablist" aria-label="Pipeline stages">{btns}</div><div class="panel">{panels}</div></div>'

MEADOW = dict(slug="meadow", name="MEADOW", label="AGENTIC CODING SYSTEM", head="Your coding environment, from your pocket.",
  blurb="Meadow is a local-first agentic coding system that turns a request into a planned, tested and reviewable coding workflow.",
  steps=["Request","Spec","Plan","Supervisor","Engine","Tools / MCP","Git","Test","Review","Merge"],
  type="Open-source personal project", role="Designed and built end to end", tags=["Agentic AI","MCP","Tool Calling","TypeScript","Harness Engineering"],
  repo="Meadow", gh="https://github.com/khushali6/Meadow", live=None, shot="meadow", alt=PROJECTS[0]["alt"], prev=("Work — Production AI","/work/"), next=("Casora","/casora/"),
  sections=dict(
   what="<p>Meadow is an open-source, local-first agentic system. You give it a request — as text, voice, or a <span class='mono'>PLAN.md</span> — and it writes a specification and a phased plan, then drives a coding engine (Cursor CLI) through the plan one phase at a time, after human-in-the-loop approval from a dashboard or Telegram.</p><div class='callout'>The interesting part isn't that an LLM writes code. It's what happens when the code it writes is wrong.</div>",
   why="<p>Coding agents are easy to demo and much harder to trust. I wanted to work on the part that sits <em>around</em> the model: the harness that decides what it may touch, checks what it produced, and puts a human back in the loop when it matters.</p>",
   problem="<p>A single long agent session tends to drift, mixes unrelated changes together, and leaves little evidence of what it actually did. When something breaks, you can't easily tell which step caused it, and you can't undo one step without undoing everything.</p>",
   how=["<b>Intake.</b> A request arrives as text, voice or PLAN.md.","<b>Spec and plan.</b> Meadow writes a specification and a phased plan for approval.","<b>Approve.</b> A human approves the plan from the dashboard or Telegram.","<b>Run each phase.</b> The coding engine works on its own git branch, with guard checks and tests.","<b>Recover.</b> Failures go back to the engine with the real error, for up to 3 fix attempts.","<b>Merge.</b> Only passing work merges."],
   arch=archexplorer([
    ("Request / Spec / Plan","Text, voice or a PLAN.md becomes a specification and a phased plan. Phases are the unit of work, approval and rollback.","<span class='c'># PLAN.md</span><br>1. scaffold &amp; schema<br>2. api routes<br>3. auth flow<br>4. dashboard ui"),
    ("Supervisor","A supervisor agent (Ollama, FreeLLMAPI or Claude) reviews failures, reports progress over Telegram, and runs independent phases in parallel.",None),
    ("Coding engine","The coding engine (Cursor CLI) does the actual editing, one phase at a time, inside the phase's branch.",None),
    ("Tools / MCP","Tool calling and MCP tools give the agent explicit access to its environment. Approval gates stop uncontrolled actions, and every call lands in an audit log.","<span class='b'>tool</span> fs.write src/auth/session.ts<br><span class='b'>gate</span> approval required: shell.exec<br><span class='g'>audit</span> recorded"),
    ("Git branch","Each phase runs on its own branch, so work is isolated, reviewable and reversible.",None),
    ("Guard + tests","Guard checks and tests decide whether a phase is allowed to merge. Headless-browser flow tests add desktop and mobile screenshots.","<span class='r'>✗ expected 401, got 200</span><br>→ real error returned to the engine"),
    ("Pass → merge · Fail → retry","Pass: the phase merges. Fail: the actual error returns to the engine for another attempt, up to 3 times. Work that still fails does not merge.",None),
    ("CodeAtlas","A knowledge graph of the codebase that gives the agent structured context, so answers can be cited rather than guessed.",None)]),
   built=["The agent harness: branch-per-phase execution, guard checks, test runs and the retry loop.","The supervisor agent and Telegram reporting, including parallel execution of independent phases.","Tool calling and MCP integration with approval gates and audit logs.","The CodeAtlas knowledge graph for cited codebase answers.","Headless-browser flow tests with desktop and mobile screenshots.","Dashboard and Telegram interfaces for approvals."],
   decisions=[("Why does every phase get its own Git branch?","Because it makes every phase independently checkable and reversible. A failing phase can't contaminate the others, and merging becomes a decision made on evidence rather than a side-effect of the agent finishing."),
              ("Why return the real error instead of asking the model to “try again”?","A retry with no information repeats the same mistake. Sending the actual failing output gives the engine something concrete to fix, which is also what a developer would do."),
              ("Why approval gates and audit logs?","Giving agents tools, not superpowers: the agent should act through explicit, inspectable tools, with a human able to veto risky actions and a record of what happened."),
              ("Why local-first?","Your code and keys stay on your machine, and the human stays in control of what is allowed to run.")],
   failures=[("Tests fail repeatedly.","After the allowed fix attempts the phase doesn't merge; the supervisor reviews the failure and a human decides what happens next."),("The engine goes down a wrong path.","The branch-per-phase layout means the damage is contained to one reviewable branch."),("An action needs more trust than the agent has.","The approval gate pauses the run until a human allows or rejects it.")],
   results="<p>Meadow is open source and runs real plan → build → test → merge cycles end to end. I haven't published benchmark numbers for it yet, so I'm not going to quote any here.</p>",
   demo="<p>The mockup above shows the dashboard: phases on the left, a failing test being returned to the engine, an approval gate and the audit log. The source code is on GitHub.</p>",
   next=["An evaluation suite that measures success rate and retries across a fixed set of tasks.","Richer supervisor policies, like when to stop retrying and escalate.","More MCP tools with finer-grained approval rules."]))

CASORA = dict(slug="casora", name="CASORA", label="AI DECISION INTELLIGENCE", head="Real estate research without the broker maze.",
  blurb="Casora is an AI-powered real-estate research product for searching, comparing and understanding homes across India using verified information and locality-level intelligence.",
  steps=["Ask","Search","Verify","Compare","Decide"], type="Deployed personal product", role="Designed and built end to end", tags=["LLM","Semantic Search","Investment Analytics","Explainable AI","Full-Stack"],
  repo=None, gh=None, live="https://casora-nine.vercel.app/", shot="casora", alt=PROJECTS[1]["alt"], prev=("Meadow","/meadow/"), next=("SplitMate","/splitmate/"),
  sections=dict(
   what="<p>Casora turns messy real-estate information into structured decisions for buyers and investors. It lets you search, compare and understand homes across India using verified listings and neighbourhood-level price intelligence.</p>",
   why="<p>Property discovery is often broker-driven and opaque. I wanted to see how far data-backed, explainable decisions could replace guesswork — and to build something where the AI is a product, not a chat box.</p>",
   problem="<p>Listings are noisy, prices are hard to compare, and a language model will happily produce a confident-sounding number that isn't grounded in anything. In a decision this large, an invented figure is worse than no figure.</p>",
   how=["<b>Ask</b> in natural language, e.g. “3 BHK in Bengaluru under ₹2 Cr” or “80 lakh se kam in Ahmedabad”.","<b>Understand</b> the query and extract hard filters such as city, BHK and budget.","<b>Retrieve</b> candidates with semantic search and filtering.","<b>Verify</b> against evidence — price trends and comparable listings.","<b>Compare</b> properties and localities.","<b>Decide</b>: scoring and ranking produce an explainable recommendation."],
   arch=flow(["User query","Query understanding","Hard filters","Retrieval","Evidence","Locality / property analysis","Decision layer","Explainable answer"],"vertical") + "<p style='margin-top:18px'>Outcomes the decision layer can reach: <b>Buy</b> · <b>Buy at the right price</b> · <b>Verify first</b> · <b>Compare</b>.</p>",
   built=["Natural-language and mixed-language query handling.","Semantic search over listings plus hard filters.","The AI investment decision layer: scoring and ranking models over price trends, comparable listings and predictive analytics.","Grounded conversational discovery using LLMs and prompt engineering.","The full-stack web product, deployed on Vercel."],
   decisions=[("Why does the product refuse to invent missing property information?","Because trust is the product. If the evidence isn't there, the right answer is “verify first”, not a plausible-sounding guess."),("Why separate retrieval from the decision layer?","Retrieval finds evidence; the decision layer weighs it. Keeping them apart makes recommendations explainable and easier to test."),("Why hard filters before semantic search?","Budget and BHK are constraints, not preferences. They should never be traded away for a better semantic match.")],
   failures=[("Missing data.","If a listing or locality lacks evidence, Casora surfaces that gap and suggests verifying rather than filling it in."),("Ambiguous queries.","Vague or conflicting requests should lead to a clarification, not a silent assumption.")],
   results="<p>Casora is live. I'm deliberately not quoting user numbers or market statistics here — the site makes no unsupported claims about live property data, and neither does this page.</p>",
   demo="<p>The mockup above is an illustration of the search → evidence → decision experience. Try the real product via the live demo link below.</p>",
   next=["More cities and locality coverage.","Backtesting recommendations against historical data.","Side-by-side comparison views with shareable reports."]))

SPLIT = dict(slug="splitmate", name="SPLITMATE", label="MULTIMODAL AI", head="Take a photo. Split the bill.",
  blurb="An AI expense-sharing product that understands receipts and turns them into structured expenses and fair settlements.",
  steps=["Receipt","OCR + VLM","Items","Confirm","Math","Settle"], type="Deployed personal product", role="Designed and built end to end", tags=["OCR","VLM","Gemini API","Deterministic Engine","Debt Graph","Full-Stack"],
  repo=None, gh=None, live="https://splitmate-two-iota.vercel.app/", shot="splitmate", alt=PROJECTS[2]["alt"], prev=("Casora","/casora/"), next=("Laya","/laya/"),
  sections=dict(
   what="<p>SplitMate is an AI bill-splitting web app. Upload a receipt image or PDF, and it extracts line items, quantities, taxes and service charges, lets you say who had what, and works out a fair, minimal set of settlements.</p><div class='callout'>The model understands the receipt. Code handles the money.</div>",
   why="<p>Splitting a restaurant bill is a perfect small problem for mixing AI and code: reading the receipt is genuinely ambiguous and visual, while splitting it is pure arithmetic. I wanted to build the version that treats those two jobs differently.</p>",
   problem="<p>Receipts are messy, photographed at angles, and full of taxes and service charges. LLMs read them well — but are unreliable at arithmetic, and money is exactly where small errors are unacceptable.</p>",
   how=["<b>Receipt in.</b> An image or PDF.","<b>OCR + VLM</b> extract line items, quantities, taxes and service charges into structured data.","<b>Human review</b> — you confirm or correct the extracted items.","<b>Assign</b> who had what.","<b>Deterministic calculation</b> computes totals, proportional tax and rounding, and reconciles to the receipt total.","<b>Debt graph</b> reduces everyone's balances to the minimum number of settlements."],
   arch=flow(["Receipt","OCR + VLM","Structured items","Who had what?","Deterministic calculation","Minimum settlements"],"vertical")+"<p style='margin-top:18px'>Principle: use AI where there is ambiguity, use deterministic code where correctness matters.</p>",
   built=["The extraction pipeline using OCR and Vision-Language Models (Gemini).","The human-in-the-loop review workflow.","A deterministic math engine: totals, proportional tax, rounding and reconciliation.","A debt-graph algorithm that minimises the number of settlements in a group.","Configurable LLM endpoints — bring your own AI.","The full-stack web app, deployed on Vercel."],
   decisions=[("Why doesn't the LLM calculate the bill?","LLMs are probabilistic and can be subtly wrong on arithmetic. A deterministic engine gives exact, testable, reproducible totals, and can be reconciled against the printed receipt total."),("Why keep a human review step?","Extraction can misread a quantity or a line. Showing the structured items before any math happens catches errors at the cheapest point."),("Why a debt graph?","Settling every pairwise debt is noisy. Collapsing balances into a graph and reducing it gives the fewest transfers.")],
   failures=[("Blurry or cropped receipt.","Low-confidence items are flagged for review instead of silently trusted."),("Totals don't reconcile.","Reconciliation catches mismatches between computed and printed totals before anyone is asked to pay.")],
   results="<p>SplitMate is live and works end to end from receipt to settlement plan. I don't quote usage statistics because I haven't published any.</p>",
   demo="<p>The mockup shows the pipeline hero: receipt on the left, extracted and assigned items in the middle, the math engine and the final settlements on the right. Names and amounts are sample data.</p>",
   next=["Multi-currency support and saved groups.","Evaluation set of receipts to measure extraction accuracy per model.","Offline-friendly capture flow."]))

LAYA = dict(slug="laya", name="LAYA", label="CREATIVE AI EXPERIMENT", head="What happens when AI gets a meme brain?",
  blurb="A playful AI experiment exploring character-driven content generation and creative AI workflows.",
  steps=["Idea","AI","Meme"], type="Personal experiment", role="Built it for fun", tags=["LLM Workflows","Creative AI","Generative"],
  repo=None, gh=None, live="https://layameme.vercel.app/", shot="laya", alt=PROJECTS[3]["alt"], prev=("SplitMate","/splitmate/"), next=("Work — Production AI","/work/"),
  sections=dict(
   what="<p>Laya is a playful AI meme-generation experiment: a character with opinions, an LLM workflow, and a lot of questionable humour. Built because AI should be fun too.</p><div class='memes'><div class='meme'>When the prompt works first try<small>CHARACTER · LAYA</small></div><div class='meme'>Me reading the logs at 2 AM<small>MOOD · SHOCKED</small></div><div class='meme'>AI: “I'm sure this is correct”<small>MOOD · CONFIDENT</small></div></div>",
   why="<p>Not everything has to be enterprise architecture. Small, silly experiments are how I try new workflows, and they keep me honest about what is actually delightful to use.</p>",
   problem="<p>Can an LLM workflow produce content with a consistent character and sense of humour, instead of generic output?</p>",
   how=["<b>Idea</b> in.","<b>AI</b> shapes it through a character-driven workflow.","<b>Meme</b> out, ready to share."],
   arch=flow(["Idea","AI","Meme"]),
   built=["The concept, character and prompt workflow.","The web experience, deployed on Vercel."],
   decisions=[("Why a character?","A consistent voice makes generated content feel authored rather than random.")],
   failures=[("Not funny.","Sometimes. That's the experiment.")],
   results="<p>It exists, it's live, and it makes me laugh. No metrics — this one is purely for fun.</p>",
   demo="<p>The cards above are illustrative samples. The real thing is one click away.</p>",
   next=["More characters and templates.","Remix and share flows."]))

# ------------------------------------------------------------------ WORK PAGE
WORK_SYS = [
 ("REQUIREMENTS → SOFTWARE", ["AWS Bedrock","AgentCore","RAG","Amazon Textract","OpenSearch","EventBridge","Lambda"],
  "Architected an autonomous agentic system that turns stakeholder requirements into shipped software: architecture flow, code generation, automated code review and deployment. Documents are ingested through Textract OCR into an OpenSearch vector database, with event-driven orchestration over EventBridge and Lambda.", [(75,"%","faster feature time-to-market")], ["Requirements","Retrieval","Code gen","Review","Deploy"]),
 ("ADAS TEST GENERATION", ["Multimodal RAG","FAISS","LLM","Agentic validation"],
  "Engineered an end-to-end GenAI RAG pipeline that generates ADAS test cases from NCAP specification documents: multimodal ingestion (text, tables, images), chunking, embeddings, FAISS retrieval, LLM inference and agentic validation loops to reduce hallucination.", [(70,"%","less manual test creation"),(2,"×","test coverage")], ["Ingest","Embed","Retrieve","Generate","Validate"]),
 ("AI CODE REVIEW", ["DeepSeek","CI/CD","Static Analysis","Security"],
  "Deployed an LLM-powered developer tooling platform for automated code review, static analysis, architectural validation and security vulnerability detection in CI/CD pipelines, raising pre-merge defect detection.", [(80,"%","less manual review effort")], ["Commit","Analyse","Review","Report"]),
 ("COMPUTER VISION INSPECTION", ["DeepLabV3","PatchCore","Stable Diffusion","PyTorch"],
  "Built deep learning and computer vision models for railway inspection: DeepLabV3 for segmentation and PatchCore for anomaly detection across multi-camera pipelines processing 20K+ images per cycle. Stable Diffusion generated synthetic data to improve performance under variable lighting and weather.", [(18,"–22%","precision/recall improvement")], ["Capture","Segment","Detect anomalies","Report"]),
]
def work_page():
    sysh = ''
    for t, st, d, ms, fl in WORK_SYS:
        m = ''.join(f'<div class="metric"><div class="n"><span data-count="{n}" data-suffix="{s}">0{s}</span></div><div class="t">{e(l)}</div></div>' for n, s, l in ms)
        sysh += f'<article class="sys rv"><div class="top"><div><p class="sm">PRODUCTION · TCS</p><h3>{t}</h3></div></div>{tags(st)}<p style="margin:20px 0">{e(d)}</p>{flow(fl)}<div class="metrics">{m}</div></article>'
    earlier = ''.join(f'<li>{x}</li>' for x in [
      "<b>Traffic-sign MLOps (TCS project intern).</b> Automated an end-to-end MLOps pipeline on Azure with GitLab CI/CD to train, version and deploy a YOLO-based model for real-time traffic sign and speed-limit detection — ~30 FPS inference and &gt;90% detection accuracy.",
      "<b>News API (Infolabz intern).</b> Engineered a Django RESTful News API for real-time article aggregation across multiple categories.",
      "<b>Movie recommender (Microsoft Engage mentee).</b> Built a movie recommendation system with content-based and collaborative filtering and ranking, under mentorship from Microsoft engineers."])
    body = f'''
<section class="cs-hero"><div class="wrap">
<p class="eyebrow"><a href="/#work" style="text-decoration:none">← HOME</a> &nbsp;·&nbsp; <b>PRODUCTION AI @ TCS</b></p>
<h1>When the model has to work in the real world.</h1>
<p class="lead">Things I built where the model had to work in the real world — as an AI Engineer at Tata Consultancy Services (Aug 2024 – present).</p>
<p class="status">Professional work, described at a high level. No confidential employer or customer information is shown, and the metrics are the ones from my resume.</p>
</div></section>
<section style="padding-top:30px"><div class="wrap">{sysh}
<div class="sys rv"><p class="sm">EARLIER WORK</p><div class="cs-sec" style="padding:0"><ul>{earlier}</ul></div></div>
<div class="pager"><a href="/laya/"><small>← PREVIOUS</small>Laya</a><a href="/meadow/" style="text-align:right"><small>NEXT →</small>Meadow</a></div>
</div></section>
{contact_block()}'''
    return page("Production AI at TCS | Khushali Pariyal", "Selected production AI systems: agentic requirements-to-software, ADAS test generation, AI code review and computer-vision inspection.", "/work/", body, cur="Work")

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

write("/", index())
for p in (MEADOW, CASORA, SPLIT, LAYA): write("/" + p["slug"], case_page(p))
write("/work", work_page())
urls = ["/","/meadow/","/casora/","/splitmate/","/laya/","/work/"]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built")
