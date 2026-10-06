#!/usr/bin/env python3
"""Generates the static site. Run: python3 tools/build.py"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://khushali6.github.io"
EMAIL, GH, LI = "khushalipariyal@gmail.com", "https://github.com/khushali6", "https://linkedin.com/in/khushalipariyal"

def e(s): return html.escape(s, quote=True)
def tags(ts): return '<p class="tags">%s</p>' % ''.join('<span>%s</span>' % e(t) for t in ts)
def flow(steps, cls=""):
    return '<ol class="flow %s" aria-label="Workflow">%s</ol>' % (cls, '<li class="arr" aria-hidden="true"></li>'.join('<li>%s</li>' % e(s) for s in steps))

NAV = [("Work", "/#work"), ("Experience", "/#experience"), ("Stack", "/#stack"), ("About", "/#about"), ("Workbench", "/workbench/"), ("Contact", "/#contact")]
THEME_DOTS = [("paper", "#f6f4ee"), ("night", "#141413"), ("nord", "#5e81ac"), ("gruvbox", "#b8bb26")]

def page(title, desc, path, body, cur=None, og=None):
    nav = ''.join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if cur == n else '', n) for n, h in NAV)
    dots = ''.join('<button data-t="%s" aria-label="%s theme" aria-pressed="false" style="background:%s"></button>' % (t, t, c) for t, c in THEME_DOTS)
    url = SITE + path
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Khushali Pariyal">
<meta property="og:title" content="{e(og or title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Khushali Pariyal","jobTitle":"AI Engineer","url":"{SITE}/","sameAs":["{GH}","{LI}"]}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="bar">
<a class="brand" href="/">khushali pariyal</a>
<nav aria-label="Primary"><ul>{nav}</ul></nav>
<div class="themes" role="group" aria-label="Theme">{dots}</div>
<button class="burger" aria-label="Menu" aria-expanded="false">menu</button>
</div></header>
<main id="main">
{body}
</main>
<script src="/assets/app.js" defer></script>
</body>
</html>
'''

def contact():
    return f'''<section class="contact" id="contact"><div class="col">
<h2>Have something <em>interesting</em> to build?</h2>
<p>I'm always interested in problems where the obvious solution isn't another chatbot.</p>
<div class="big"><a href="mailto:{EMAIL}"><span>Email</span><span>{EMAIL}</span></a><a href="{GH}" target="_blank" rel="noopener"><span>GitHub</span><span>khushali6 ↗</span></a><a href="{LI}" target="_blank" rel="noopener"><span>LinkedIn</span><span>khushalipariyal ↗</span></a></div>
<p class="who">Khushali Pariyal<br>AI Engineer · Agentic AI · RAG · Multimodal AI</p>
</div></section>'''

def shot(slug, alt, cap_name):
    """Real screenshot if assets/shots/<slug>.jpg exists on the live site; otherwise a UI sketch."""
    return f'''<figure class="shot"><img src="/assets/shots/{slug}.jpg" data-fallback="/assets/img/{slug}.svg" alt="{e(alt)}" width="1200" height="800" loading="lazy" onerror="this.onerror=null;this.src=this.dataset.fallback" onload="if(this.src.indexOf('/shots/')>-1)this.closest('figure').classList.add('live')"><figcaption><span class="c-sketch">UI sketch · {cap_name}</span><span class="c-live">Live product · {cap_name}</span></figcaption></figure>'''

# ------------------------------------------------------------------ DATA
P = {
 "meadow": dict(name="Meadow", kicker="Agentic coding system", head="Your coding environment, from your pocket.",
   line="A local-first agent that turns a request into finished, tested code by driving a coding engine phase by phase.",
   stack=["Agentic AI","MCP","Tool calling","TypeScript","Human-in-the-loop"], repo="Meadow", gh="https://github.com/khushali6/Meadow", live=None,
   steps=["Plan","Build","Test","Review","Merge"], alt="Meadow demo: a Telegram conversation that plans, builds and tests a habit-tracker app"),
 "casora": dict(name="Casora", kicker="AI decision intelligence", head="Real estate research without the broker maze.",
   line="Search, compare and understand homes across India — with the evidence shown, and “verify first” when it isn't there.",
   stack=["LLM","Semantic search","Investment analytics","Full-stack"], repo=None, gh=None, live="https://casora-nine.vercel.app/",
   steps=["Ask","Search","Verify","Compare","Decide"], alt="Casora: natural-language property search with a decision panel"),
 "splitmate": dict(name="SplitMate", kicker="Multimodal AI", head="Take a photo. Split the bill.",
   line="OCR + VLMs read the receipt. A deterministic engine does the math. The LLM never touches the numbers.",
   stack=["OCR","VLM","Gemini API","Debt graph","Full-stack"], repo=None, gh=None, live="https://splitmate-two-iota.vercel.app/",
   steps=["Receipt","AI","Structure","Math","Split"], alt="SplitMate: receipt, extracted items, math engine and settlements"),
 "laya": dict(name="Laya", kicker="Creative AI experiment", head="What happens when AI gets a meme brain?",
   line="A playful experiment in character-driven content generation. Built because AI should be fun too.",
   stack=["LLM workflows","Creative AI"], repo=None, gh=None, live="https://layameme.vercel.app/",
   steps=["Idea","AI","Meme"], alt="Laya meme cards"),
}

SYS = [
 ("Requirements → software", "75% faster feature turnaround",
  "An autonomous agentic system that turns stakeholder requirements into shipped software: architecture flow, code generation, automated review and deployment. Documents go through Textract OCR into an OpenSearch vector index, orchestrated event-driven with EventBridge and Lambda.",
  ["AWS Bedrock","AgentCore","RAG","Textract","OpenSearch","EventBridge","Lambda"]),
 ("ADAS test generation", "70% less manual test creation · 2× coverage",
  "A GenAI RAG pipeline that generates ADAS test cases from NCAP specification documents: multimodal ingestion (text, tables, images), chunking, embeddings, FAISS retrieval, LLM inference, and agentic validation loops to cut hallucination.",
  ["Multimodal RAG","FAISS","LLM","Validation loops"]),
 ("AI code review", "80% less manual review effort",
  "LLM-powered developer tooling for automated code review, static analysis, architectural validation and security vulnerability detection inside CI/CD, raising pre-merge defect detection.",
  ["DeepSeek","CI/CD","Static analysis","Security"]),
 ("Computer-vision inspection", "18–22% better precision/recall",
  "Railway inspection models: DeepLabV3 for segmentation and PatchCore for anomaly detection across multi-camera pipelines processing 20K+ images per cycle. Stable Diffusion generated synthetic data for robustness under changing light and weather.",
  ["DeepLabV3","PatchCore","Stable Diffusion","PyTorch"]),
]

WB = [
 ("crop-raid-guard", "Night camera footage in, signed crop-loss evidence out.", "crop-raid-guard"),
 ("Intentroute", "LangGraph + MCP agent that turns fuzzy requests (“I'm bloated”) into verified, structured orders.", "Intentroute"),
 ("CoFoundry", "Startup discovery and hiring radar built on the TinyFish web-agent API.", "CoFoundry"),
 ("NeuralCraft", "Landing-page experiments in React.", "NeuralCraft"),
 ("Movie-Mania", "Movie recommender: content-based, collaborative and demographic filtering.", "Movie-Mania"),
 ("DailyInsight", "Django app serving categorised news from the Inshorts API.", "DailyInsight"),
 ("SignVerse", "Flutter app (SSIP project).", "SignVerse"),
]

LEARNED = [
 ("SplitMate", "let the model read the receipt. Don't let it calculate the bill.", "/splitmate/"),
 ("Meadow", "the interesting part of an agent is what happens after it fails.", "/meadow/"),
 ("Casora", "if the data isn't there, “I don't know” is a feature.", "/casora/"),
 ("TCS", "measure the system, not the demo: correctness, recovery, latency, cost.", "/#experience"),
]

# ------------------------------------------------------------------ HOME
def home():
    m = P["meadow"]
    meadow = f'''<article class="feat">
<figure class="player"><video data-auto muted loop playsinline preload="none" poster="/assets/media/meadow-3.jpg" aria-label="{e(m["alt"])}"><source src="/assets/media/meadow-demo.mp4" type="video/mp4"></video>
<figcaption><span>Real product demo · from the Meadow README</span><span>Telegram → plan → build → test</span></figcaption></figure>
<div class="t"><h3>Meadow</h3><span class="k">{m["kicker"].upper()} · BETA · MIT</span></div>
<p class="d">{e(m["line"])} Each phase gets its own git branch and checks that can actually fail.</p>
<p class="pull">The interesting part isn't that an LLM writes code. It's what happens when the code it writes is wrong.</p>
{tags(m["stack"])}
<p class="go"><a class="p" href="/meadow/">Read the build →</a><a href="{m["gh"]}" target="_blank" rel="noopener">GitHub ↗</a><span class="meta" data-repo="Meadow"></span></p>
</article>'''
    def card(k):
        p = P[k]
        links = f'<a class="p" href="/{k}/">Read the build →</a><a href="{p["live"]}" target="_blank" rel="noopener">Live ↗</a>'
        return f'''<article class="pcard">{shot(k, p["alt"], p["name"])}<h3>{p["name"]}</h3><p class="k">{p["kicker"].upper()}</p><p class="d">{e(p["line"])}</p>{tags(p["stack"])}<p class="go">{links}</p></article>'''
    l = P["laya"]
    laya = f'''<article class="row"><div><h3>Laya</h3><p class="k">{l["kicker"].upper()}</p></div><span class="chipmeme">idea → AI → meme</span><p>{e(l["line"])}</p><p class="go" style="margin:0"><a class="p" href="/laya/">Read the build →</a><a href="{l["live"]}" target="_blank" rel="noopener">Live ↗</a></p></article>'''
    sys = ''.join(f'<details class="sys"><summary><b>{t}</b><span class="m">{m_}</span></summary><div class="in"><p>{e(d)}</p>{tags(st)}</div></details>' for t, m_, d, st in SYS)
    learned = ''.join(f'<li><b>{a}</b>{e(b)} <a href="{u}">→</a></li>' for a, b, u in LEARNED)
    wb = ''.join(f'<li><a href="https://github.com/khushali6/{r}" target="_blank" rel="noopener"><b>{n}</b><span>{e(d)}</span><em data-live="{r}"></em></a></li>' for n, d, r in WB[:5])
    body = f'''
<div class="col hero">
<p class="hello">Khushali Pariyal · AI engineer · Gandhinagar, India</p>
<h1>I build AI systems that <em>actually do things.</em></h1>
<p class="intro">AI engineer. I build agents, RAG systems, multimodal tools and occasionally things I probably didn't need to build.</p>
<p class="now">Right now: agents, AI products, and systems that turn messy information into useful decisions.</p>
<p class="links"><a href="#work">Work ↓</a><a href="{GH}" target="_blank" rel="noopener">GitHub ↗</a><a href="{LI}" target="_blank" rel="noopener">LinkedIn ↗</a><a href="mailto:{EMAIL}">Email</a></p>
<dl class="facts"><div><dt>Experience</dt><dd>2+ years of production AI at TCS</dd></div><div><dt>Shipped</dt><dd>4+ projects, idea to working software</dd></div><div><dt>Focus</dt><dd>Agents · RAG · multimodal · LLMOps</dd></div></dl>
</div>

<section id="work"><div class="wide">
<h2 class="sh">Selected work</h2>
<p class="lead">Four things I'm proud I actually finished.</p>
{meadow}
<div class="pair">{card("casora")}{card("splitmate")}</div>
{laya}
</div></section>

<section id="experience"><div class="col">
<h2 class="sh">Experience</h2>
<div class="job"><h3>Tata Consultancy Services</h3><p class="k">AI Engineer (Systems Engineer) · Gandhinagar · Aug 2024 — present</p></div>
{sys}
<p class="note">Described at a high level — no confidential employer or customer details. <a href="/work/">More on the production work →</a></p>
<ul class="small" style="margin-top:34px">
<li><span>Project Intern, TCS — YOLO traffic-sign MLOps on Azure (~30 FPS, &gt;90% accuracy)</span><span>2024</span></li>
<li><span>Web Development Intern, Infolabz — Django news API</span><span>2023</span></li>
<li><span>Microsoft Engage mentee — movie recommender</span><span>2022</span></li></ul>
</div></section>

<section id="stack"><div class="col">
<h2 class="sh">Stack</h2>
<p class="stackline">I work mostly with <b>Python</b>, <b>TypeScript</b>, <b>AWS</b>, <b>Bedrock</b>, <b>LangGraph</b>, <b>MCP</b>, <b>OpenSearch</b>, <b>PostgreSQL</b>, <b>FastAPI</b> and <b>Docker</b> — and whatever the problem requires.</p>
<details class="more"><summary>everything else I've used</summary><dl>
<dt>agents</dt><dd>LangChain · tool calling · multi-agent · agent harness engineering</dd>
<dt>llm / rag</dt><dd>OpenAI · Gemini · DeepSeek · Ollama · embeddings · FAISS · vector search</dd>
<dt>backend</dt><dd>Django · Node.js · REST · MongoDB · Redis</dd>
<dt>cloud</dt><dd>Azure · Lambda · EventBridge · Textract · AgentCore</dd>
<dt>ml / vision</dt><dd>PyTorch · YOLO · DeepLabV3 · PatchCore · Stable Diffusion · OCR · VLM</dd>
<dt>languages</dt><dd>Java · JavaScript · SQL · C++ · C</dd></dl></details>
<ul class="learn">{learned}</ul>
</div></section>

<section id="about"><div class="col about">
<h2 class="sh">About</h2>
<p>I started with ML and computer vision, somehow ended up building agents, and now I have a habit of turning random “what if…” ideas into working products.</p>
<p>The last 2+ years have been agentic AI, RAG, multimodal systems and computer vision — mostly at TCS, and the rest on projects outside work. I like the messy part of AI engineering: deciding what the model should do, what it absolutely shouldn't, how it uses tools, how it recovers when it's wrong, and how you know it helped.</p>
<p>I build projects because I usually learn more by shipping something than by reading another framework's documentation.</p>
<p class="school">B.E. Computer Engineering — Government Engineering College Gandhinagar, 2021–24 · CGPA 8.37<br>Diploma in IT — Government Polytechnic for Girls Ahmedabad, 2018–21 · CGPA 9.69</p>
</div></section>

<section id="workbench"><div class="col">
<h2 class="sh">Workbench</h2>
<p class="lead">The weird stuff. Not everything deserves a case study.</p>
<ul class="wb">{wb}</ul>
<p class="go"><a class="p" href="/workbench/">Open the workbench →</a><a href="{GH}?tab=repositories" target="_blank" rel="noopener">All repositories ↗</a></p>
</div></section>
{contact()}
'''
    return page("Khushali Pariyal — AI Engineer | Agentic AI, RAG & Generative AI",
                "Khushali Pariyal is an AI Engineer building agentic AI systems, RAG pipelines, multimodal AI and AI products.", "/", body)

# ------------------------------------------------------------------ CASE PAGES
def archexplorer(nodes):
    b = ''.join(f'<button role="tab" data-target="n{i}" aria-selected="false">{e(t)}</button>' for i, (t, _, _) in enumerate(nodes))
    p = ''.join(f'<div data-panel="n{i}" hidden><h3>{e(t)}</h3><p>{d}</p>{("<div class=term>%s</div>" % c) if c else ""}</div>' for i, (t, d, c) in enumerate(nodes))
    return f'<p>Click through the pipeline.</p><div class="arch"><div class="nodes" role="tablist" aria-label="Pipeline stages">{b}</div><div class="panel">{p}</div></div>'

def case(k, c, prev, nxt):
    p = P[k]
    ul = lambda it: '<ul>%s</ul>' % ''.join(f'<li>{x}</li>' for x in it)
    dec = ''.join(f'<div class="decision"><h3>{e(q)}</h3><p>{a}</p></div>' for q, a in c["decisions"])
    fails = ''.join(f'<div class="fail"><b>{e(a)}</b> {e(b)}</div>' for a, b in c["failures"])
    links = []
    if p["live"]: links.append(f'<a class="p" href="{p["live"]}" target="_blank" rel="noopener">Live demo ↗</a>')
    if p["gh"]: links.append(f'<a class="p" href="{p["gh"]}" target="_blank" rel="noopener">Source on GitHub ↗</a>')
    if not links: links.append(f'<a href="{GH}" target="_blank" rel="noopener">GitHub ↗</a>')
    media = c.get("media") or shot(k, p["alt"], p["name"])
    meta = f'<span data-repo="{p["repo"]}"></span>' if p["repo"] else ''
    sec = lambda h, inner: f'<section class="cs-sec"><h2>{h}</h2>{inner}</section>'
    body = f'''<article class="cs"><div class="wide" style="padding-top:56px">
<div class="col" style="padding:0"><a class="back" href="/#work">← work</a>
<p class="hello" style="margin-top:22px">{p["kicker"]}</p>
<h1>{e(p["head"])}</h1>
<p class="intro">{e(c["intro"])}</p>
<p class="facts2"><span><b>{e(c["type"])}</b></span><span>{e(c["role"])}</span>{meta}</p></div>
{media}
</div>
<div class="col">
{sec("Overview", c["overview"])}
{sec("How it works", ul(c["how"]) + c["arch"])}
{sec("What I built", ul(c["built"]))}
{sec("The interesting decisions", dec)}
{sec("Where it breaks", fails)}
{sec("Results", c["results"])}
{sec("What I'd build next", ul(c["next"]))}
<section class="cs-sec"><h2>Try it</h2><p class="go">{''.join(links)}</p></section>
<div class="pager"><a href="{prev[1]}"><small>← PREVIOUS</small>{prev[0]}</a><a href="{nxt[1]}" style="text-align:right"><small>NEXT →</small>{nxt[0]}</a></div>
</div></article>
{contact()}'''
    return page(f'{p["name"]} — {p["head"]} | Khushali Pariyal', p["line"], f"/{k}/", body, cur="Work")

MEADOW_MEDIA = '''<figure class="player" style="margin-top:34px"><video data-auto muted loop playsinline controls preload="none" poster="/assets/media/meadow-3.jpg" aria-label="Meadow demo"><source src="/assets/media/meadow-demo.mp4" type="video/mp4"></video><figcaption><span>Real demo from the Meadow README</span><span>one Telegram message → a tested app</span></figcaption></figure>'''
MEADOW_STILLS = '''<div class="stills"><figure><img src="/assets/media/meadow-3.jpg" alt="Meadow demo frame: send one message" loading="lazy" width="1280" height="720"><figcaption>01 · Request</figcaption></figure><figure><img src="/assets/media/meadow-11.jpg" alt="Meadow demo frame: plan awaiting approval" loading="lazy" width="1280" height="720"><figcaption>03 · Build, phase by phase</figcaption></figure><figure><img src="/assets/media/meadow-15.jpg" alt="Meadow demo frame: report with real browser tests" loading="lazy" width="1280" height="720"><figcaption>04 · Report, with real browser tests</figcaption></figure><figure><img src="/assets/media/meadow-20.jpg" alt="Meadow title card" loading="lazy" width="1280" height="720"><figcaption>Runs on your own computer · MIT</figcaption></figure></div>'''

C = {}
C["meadow"] = dict(type="Open source · beta · MIT", role="Designed and built end to end", media=MEADOW_MEDIA,
 intro="Describe what you want. Meadow plans it, builds it phase by phase with a real coding engine, tests every step, and reports back on Telegram.",
 overview="<p>Meadow runs on your own computer. You send a request from a dashboard or Telegram — text, voice or a <span class='mono'>PLAN.md</span> — approve the plan, and Meadow drives a coding engine (the Cursor CLI is the most tested; Codex CLI, Gemini CLI or any command-line tool also work) until every phase passes its checks. Code, memory and keys stay on your machine.</p><div class='callout'>The interesting part isn't that an LLM writes code. It's what happens when the code it writes is wrong.</div><p style='margin-top:1.2em'>I wanted to work on the part <em>around</em> the model: the harness that decides what it may touch, checks what it produced, and puts a human back in the loop. A single long agent session drifts, mixes unrelated changes and leaves little evidence — so Meadow breaks the work into phases that can each fail on their own.</p>",
 how=["<b>Request.</b> Meadow classifies it (new app, feature, bug, question) and asks up to five short questions.","<b>Spec and plan.</b> It writes <span class='mono'>SPEC.md</span> and a phased <span class='mono'>PLAN.md</span>. Every phase has at least one check that can actually fail.","<b>Approval.</b> Nothing touches code until you approve — on the dashboard or with one tap on Telegram.","<b>Build.</b> Each phase runs on its own branch; guards inspect the diff, checks run, and failures go back to the engine with the real error, up to three attempts.","<b>Merge.</b> Only passing work is committed and fast-forwarded onto main, with a summary, diff stats and screenshots.","<b>Browser tests.</b> For web apps, Meadow starts the app, clicks through each main user flow in a headless browser and sends desktop and mobile screenshots."],
 arch=archexplorer([
  ("Request → spec → plan","Text, voice or a PLAN.md becomes a specification and a phased plan. Phases are the unit of work, approval and rollback.","<span class='c'># PLAN.md</span><br>1. scaffold &amp; schema<br>2. api routes<br>3. auth flow<br>4. dashboard ui"),
  ("Supervisor","A supervisor model (Ollama, FreeLLMAPI or Claude) reviews failures, reports progress over Telegram, and lets independent phases run in parallel.",None),
  ("Coding engine","The engine does all the editing, headless, one phase at a time. The agent model only plans and summarises.",None),
  ("Tools / MCP","Every tool has a risk level. Writes and risky commands wait for approval, every call lands in an audit log, and secrets never appear in prompts, logs or the UI.","<span class='b'>tool</span> fs.write src/auth/session.ts<br><span class='b'>gate</span> approval required: shell.exec<br><span class='g'>audit</span> recorded"),
  ("Git branch","Each phase runs on <span class='mono'>meadow/phase-&lt;id&gt;-&lt;slug&gt;</span>, so work is isolated, reviewable and reversible.",None),
  ("Checks + tests","Checks (<span class='mono'>cmd</span>, <span class='mono'>file_exists</span>, <span class='mono'>http</span>) decide whether a phase may merge.","<span class='r'>✗ expected 401, got 200</span><br>→ real error returned to the engine (attempt 2/3)"),
  ("CodeAtlas","A local knowledge graph of services, APIs, tables, releases and incidents, so Meadow can answer “why did payments start failing after v2.4?” with cited evidence.",None)]) + MEADOW_STILLS,
 built=["The harness: branch-per-phase execution, guard checks, test runs and the retry loop.","The supervisor agent, Telegram control surface and parallel execution of independent phases.","Tool calling and MCP integration with approval gates and audit logs.","CodeAtlas, the local knowledge graph, plus a search index and notes per project.","Headless-browser flow tests with desktop and mobile screenshots.","A cross-platform setup script (<span class='mono'>startup.sh</span> / <span class='mono'>startup.ps1</span>) and a <span class='mono'>meadow doctor</span> command."],
 decisions=[("Why does every phase get its own git branch?","So each phase is independently checkable and reversible. A failing phase can't contaminate the rest, and merging becomes a decision made on evidence rather than a side-effect of the agent finishing."),
  ("Why send the real error back instead of “try again”?","A retry without information repeats the same mistake. The actual failing output gives the engine something concrete to fix — which is what a developer would do."),
  ("Why approval gates and audit logs?","Give agents tools, not superpowers. The agent acts through explicit, inspectable tools, a human can veto risky actions, and there's a record of what happened."),
  ("Why local-first?","Code, memory and keys stay on your machine, and Meadow never signs in for you or reads <span class='mono'>.env</span> files.")],
 failures=[("A phase keeps failing.","After three attempts it stops and tells you why. You can retry with a hint, skip, or roll back — it never merges."),("The checks are weak.","Meadow verifies what the checks measure, so a weak check proves little. That's why plans must include checks that can fail."),("Beyond localhost.","Browser screenshots work for web apps on localhost only.")],
 results="<p>Meadow is open source (MIT) and in <b>beta</b>. CI tests every commit on macOS, Linux and Windows with Node 22.16, 24 and 26. I haven't published success-rate benchmarks yet, so there are no made-up numbers here.</p>",
 next=["An evaluation suite: success rate and retries across a fixed set of tasks.","Smarter supervisor policies for when to stop retrying and escalate.","Claude Code as a first-class engine (it's listed as coming soon)."])

C["casora"] = dict(type="Deployed product", role="Designed and built end to end",
 intro="Casora turns messy real-estate information into structured decisions for buyers and investors.",
 overview="<p>Casora is an AI-powered real-estate research platform for searching, comparing and understanding homes across India, using verified listings and neighbourhood-level price intelligence — replacing broker-driven discovery with data-backed decisions.</p><div class='callout'>Don't invent a number just because the model can.</div><p style='margin-top:1.2em'>Listings are noisy, prices are hard to compare, and a language model will happily produce a confident-sounding figure that isn't grounded in anything. In a decision this large, an invented number is worse than none.</p>",
 how=["<b>Ask</b> in natural language: “3 BHK in Bengaluru under ₹2 Cr”, or “80 lakh se kam in Ahmedabad”.","<b>Understand</b> the query and pull out hard filters — city, BHK, budget.","<b>Retrieve</b> candidates with semantic search plus those filters.","<b>Verify</b> against evidence: price trends and comparable listings.","<b>Compare</b> properties and localities.","<b>Decide</b>: scoring and ranking produce an explainable recommendation — buy, buy at the right price, verify first, or compare."],
 arch=flow(["Query","Understanding","Hard filters","Retrieval","Evidence","Analysis","Decision layer","Explanation"], "vertical"),
 built=["Natural-language, mixed-language query handling.","Semantic search over listings with hard filters.","The investment decision layer: scoring and ranking over price trends, comparable listings and predictive analytics.","Grounded conversational discovery with LLMs and prompt engineering.","The full-stack product, deployed on Vercel."],
 decisions=[("Why does it refuse to invent missing property information?","Because trust is the product. If the evidence isn't there, the right answer is “verify first”, not a plausible guess."),("Why separate retrieval from the decision layer?","Retrieval finds evidence; the decision layer weighs it. Keeping them apart makes recommendations explainable and testable."),("Why hard filters before semantic search?","Budget and BHK are constraints, not preferences. They shouldn't be traded away for a better semantic match.")],
 failures=[("Missing data.","If a listing or locality lacks evidence, Casora says so and suggests verifying rather than filling the gap."),("Ambiguous queries.","Vague or conflicting requests should lead to a clarifying question, not a silent assumption.")],
 results="<p>Casora is live. I don't quote user numbers or market statistics here, and the product makes no unsupported claims about live property data.</p>",
 next=["More cities and locality coverage.","Backtesting recommendations against historical data.","Shareable side-by-side comparison reports."])

C["splitmate"] = dict(type="Deployed product", role="Designed and built end to end",
 intro="An AI expense-sharing product that understands receipts and turns them into structured expenses and fair settlements.",
 overview="<p>Upload a receipt image or PDF. SplitMate extracts line items, quantities, taxes and service charges, lets you say who had what, and works out a fair, minimal set of settlements.</p><div class='callout'>The model understands the receipt. Code handles the money.</div><p style='margin-top:1.2em'>Reading a receipt is ambiguous and visual — exactly what VLMs are good at. Splitting it is pure arithmetic — exactly what they're not. I wanted to build the version that treats those two jobs differently.</p>",
 how=["<b>Receipt in</b> — image or PDF.","<b>OCR + VLM</b> extract line items, quantities, taxes and service charges into structured data.","<b>Human review</b> — confirm or correct the extracted items.","<b>Assign</b> who had what.","<b>Deterministic calculation</b> — totals, proportional tax and rounding, reconciled to the receipt total.","<b>Debt graph</b> — reduce everyone's balances to the minimum number of settlements."],
 arch=flow(["Receipt","OCR + VLM","Structured items","Who had what?","Deterministic math","Minimum settlements"], "vertical") + "<p style='margin-top:14px;color:var(--mute)'>Use AI where there's ambiguity. Use deterministic code where correctness matters.</p>",
 built=["The extraction pipeline with OCR and Vision-Language Models (Gemini).","The human-in-the-loop review workflow.","A deterministic math engine: totals, proportional tax, rounding, reconciliation.","A debt-graph algorithm that minimises the number of group settlements.","Configurable LLM endpoints — bring your own AI.","The full-stack web app, deployed on Vercel."],
 decisions=[("Why doesn't the LLM calculate the bill?","LLMs can be subtly wrong at arithmetic. A deterministic engine gives exact, testable, reproducible totals and can be reconciled against the printed total."),("Why a human review step?","Extraction can misread a quantity or a line. Showing structured items before any math catches errors at the cheapest point."),("Why a debt graph?","Settling every pairwise debt is noisy. Collapsing balances into a graph and reducing it gives the fewest transfers.")],
 failures=[("Blurry or cropped receipts.","Low-confidence items are flagged for review instead of silently trusted."),("Totals don't reconcile.","Reconciliation catches mismatches between computed and printed totals before anyone is asked to pay.")],
 results="<p>SplitMate is live and works end to end from receipt to settlement plan. No usage statistics — I haven't published any.</p>",
 next=["Multi-currency and saved groups.","An evaluation set of receipts to measure extraction accuracy per model.","A friendlier mobile capture flow."])

C["laya"] = dict(type="Personal experiment", role="Built for fun",
 intro="A playful AI experiment exploring character-driven content generation and creative AI workflows.",
 overview="<p>Laya is a character with opinions, an LLM workflow, and a lot of questionable humour. Not everything has to be enterprise architecture — small, silly experiments are how I try new workflows, and they keep me honest about what's actually delightful to use.</p><div class='memes' style='display:grid;gap:10px;margin-top:22px'><span class='chipmeme' style='transform:rotate(-1deg)'>when the prompt works first try</span><span class='chipmeme' style='transform:rotate(1deg)'>me reading the logs at 2 AM</span><span class='chipmeme' style='transform:rotate(-.5deg)'>AI: “I'm sure this is correct”</span></div>",
 how=["<b>Idea</b> in.","<b>AI</b> shapes it through a character-driven workflow.","<b>Meme</b> out, ready to share."],
 arch=flow(["Idea","AI","Meme"]),
 built=["The concept, character and prompt workflow.","The web experience, deployed on Vercel."],
 decisions=[("Why a character?","A consistent voice makes generated content feel authored rather than random.")],
 failures=[("Not funny.","Sometimes. That's the experiment.")],
 results="<p>It exists, it's live, and it makes me laugh. No metrics — this one is purely for fun.</p>",
 next=["More characters and templates.","Remix and share flows."])

# ------------------------------------------------------------------ WORK + WORKBENCH
def work_page():
    sys = ''.join(f'<section class="cs-sec"><h2>{t}</h2><p class="facts2" style="margin:0 0 12px"><b>{m}</b></p><p>{e(d)}</p>{tags(st)}</section>' for t, m, d, st in SYS)
    earlier = '''<ul><li><b>Traffic-sign MLOps</b> (TCS project intern, Jan–May 2024). Automated an end-to-end pipeline on Azure with GitLab CI/CD to train, version and deploy a YOLO-based model for real-time traffic-sign and speed-limit detection — ~30 FPS inference and &gt;90% detection accuracy.</li><li><b>News API</b> (Infolabz, 2023). A Django RESTful API aggregating articles across categories in real time.</li><li><b>Movie recommender</b> (Microsoft Engage, 2022). Content-based and collaborative filtering with ranking, under mentorship from Microsoft engineers.</li></ul>'''
    body = f'''<div class="col" style="padding-top:56px"><a class="back" href="/#experience">← experience</a>
<p class="hello" style="margin-top:22px">Tata Consultancy Services · Aug 2024 — present</p>
<h1>When the model has to work in the real world.</h1>
<p class="intro">Selected production AI systems, described at a high level. No confidential employer or customer details; the metrics are the ones from my resume.</p>
{sys}
<section class="cs-sec"><h2>Earlier work</h2>{earlier}</section>
<div class="pager"><a href="/laya/"><small>← PREVIOUS</small>Laya</a><a href="/workbench/" style="text-align:right"><small>NEXT →</small>Workbench</a></div></div>
{contact()}'''
    return page("Production AI at TCS | Khushali Pariyal", "Production AI systems: agentic requirements-to-software, ADAS test generation, AI code review and computer-vision inspection.", "/work/", body, cur="Experience")

def workbench_page():
    rows = ''.join(f'<li><a href="https://github.com/khushali6/{r}" target="_blank" rel="noopener"><b>{n}</b><span>{e(d)}</span><em data-live="{r}"></em></a></li>' for n, d, r in WB)
    tl = [("2022","Microsoft Engage — a movie recommender (content-based + collaborative filtering)."),("2023","Django news API at Infolabz. First time shipping a backend people could actually call."),("Jan 2024","TCS intern: YOLO traffic-sign detection with an MLOps pipeline on Azure."),("Aug 2024","TCS AI engineer: computer vision, then RAG, then agents."),("Now","Meadow, Casora, SplitMate, Laya — and whatever I build next at 2 AM.")]
    t = ''.join(f'<li><b>{a}</b><span>{e(b)}</span></li>' for a, b in tl)
    body = f'''<div class="col" style="padding-top:56px"><a class="back" href="/">← home</a>
<p class="hello" style="margin-top:22px">The experimental layer</p>
<h1>Workbench.</h1>
<p class="intro">Things I built at 2 AM, older experiments, and anything that didn't deserve a full case study. Descriptions are written by me; the “updated” numbers come live from the GitHub API.</p>
<section><h2 class="sh">Poke around</h2><div class="tw" id="term"><div class="out"></div><form autocomplete="off"><span class="pr">$</span><input aria-label="Terminal input" spellcheck="false" autocapitalize="off"></form></div></section>
<section><h2 class="sh">Archive</h2><ul class="wb">{rows}</ul><p class="go"><a href="{GH}?tab=repositories" target="_blank" rel="noopener">All public repositories ↗</a></p></section>
<section><h2 class="sh">How it got here</h2><ul class="tl">{t}</ul></section></div>
{contact()}'''
    return page("Workbench | Khushali Pariyal", "Experiments, older projects and things Khushali Pariyal built at 2 AM.", "/workbench/", body, cur="Workbench")

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

write("/", home())
order = ["meadow", "casora", "splitmate", "laya"]
names = {"meadow": "Meadow", "casora": "Casora", "splitmate": "SplitMate", "laya": "Laya"}
for i, k in enumerate(order):
    prev = ("Home", "/") if i == 0 else (names[order[i - 1]], f"/{order[i-1]}/")
    nxt = ("Production work at TCS", "/work/") if i == len(order) - 1 else (names[order[i + 1]], f"/{order[i+1]}/")
    write("/" + k, case(k, C[k], prev, nxt))
write("/work", work_page())
write("/workbench", workbench_page())
urls = ["/", "/meadow/", "/casora/", "/splitmate/", "/laya/", "/work/", "/workbench/"]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built")
