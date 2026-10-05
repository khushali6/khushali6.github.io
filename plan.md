# Khushali Pariyal — AI Engineer Portfolio

## Product direction
A premium, responsive one-page portfolio that positions Khushali Pariyal as an AI Engineer and Agentic AI Engineer. It uses the provided Webflow site as a structural reference for confident editorial storytelling: bold hero, selected work, capabilities, process, proof points, factual credibility, profile, and contact. It does not copy the reference's imagery, identity, copy, or testimonials.

## Design direction

- **Design movement:** Editorial systems design — the warmth and pacing of a premium creative portfolio paired with the precision of an AI infrastructure diagram.
- **Core principles:** (1) evidence before adjectives, (2) calm hierarchy with energetic details, (3) human warmth inside technical systems, (4) motion that clarifies rather than decorates.
- **Color philosophy:** Warm ivory gives the site a human, tactile base; near-black ink creates authority and legibility; cobalt/electric blue signals intelligence and acts as the ownable signature accent; mint highlights live system states and success metrics.
- **Layout paradigm:** A vertical editorial narrative with asymmetric split panels, horizontal proof rails, sticky section labels, and long-form case-study cards instead of a centered grid of equal modules.
- **Signature elements:** (1) cobalt orbital system diagrams built from SVG nodes and routes, (2) monospace metadata labels and index marks, (3) blue/mint metric pills and signal bars that feel like live telemetry.
- **Interaction philosophy:** Hovering a project reveals its system signal and makes the real external link obvious; navigation anchors feel like a control surface; motion is quick, low-amplitude, and respects reduced-motion preferences.
- **Animation:** Hero orbital diagram floats subtly; headline and meta reveal upward on load; sections use IntersectionObserver fade/translate reveals; project cards lift 6px and animate a signal line; buttons use a short color sweep; metrics count in through opacity/translate only (no distracting numeric tweening).
- **Typography system:** `Space Grotesk` for display and interface headlines, `DM Mono` for labels, project metadata, and technical annotations, with system sans fallbacks for resilience. Headline hierarchy is oversized and tight; body text is compact and generous in line-height.
- **Brand essence:** Production AI systems that turn ambiguity into dependable decisions and working software — for teams that need intelligent systems shipped, not just demoed. Personality: precise, kinetic, grounded.
- **Brand voice:** Direct, specific, quietly confident. Example lines: “I build AI systems that keep moving after the demo.” “From messy inputs to decisions your team can trust.”
- **Wordmark & logo:** A custom `K/` signal mark made from a diagonal slash and two offset nodes, paired with the `KP` wordmark and a small `AI SYSTEMS` label.
- **Signature brand color:** Cobalt Signal `#315CFF`.

## Information architecture

1. Sticky header with logo, anchor navigation, and collaboration CTA.
2. Hero: positioning statement, concise summary, proof metrics, and original orbital AI-system visual.
3. Selected work: public GitHub-grounded projects — Meadow, SignVerse, Intentroute, NeuralCraft, and CoFoundry — with factual descriptions and real links.
4. Capabilities: verified expertise grouped into systems, intelligence, and delivery tracks.
5. Process: frame, architect, prototype, evaluate, ship, iterate.
6. Proof: resume-backed impact rail with the major metrics only.
7. Factual credibility: TCS role and impact in an editorial statement layout; no fabricated client quotes.
8. About: short career narrative and education line.
9. Contact: collaboration CTA, email, GitHub, LinkedIn, and footer metadata.

## Implementation

- Use a small, readable vanilla HTML/CSS/JS implementation with no server or database dependency.
- Serve from `0.0.0.0:3000` using a minimal Node server and keep all visible project data in `app.js`.
- Use CSS/SVG for original system visuals and decorative motifs; no third-party headshots or copied reference imagery.
- Add `public/manus-routes.json` with the single `/` route.
- Keep external links limited to the verified public GitHub repositories, the supplied LinkedIn profile, email, and the available CoFoundry Vercel URL.
- Use responsive breakpoints for tablet and mobile, a mobile menu toggle, visible keyboard focus states, and a `prefers-reduced-motion` override.
- Use project metadata and measurable claims from the attached resume and authenticated GitHub connector test only; avoid inventing outcomes for GitHub repositories.

## Project structure

- `index.html` — semantic page structure and section content.
- `styles.css` — full design system, responsive layout, animation, and diagrams.
- `app.js` — project data, reveal/menu interactions, current-year label, and lightweight visual behavior.
- `server.mjs` — static preview server on port 3000.
- `public/manus-routes.json` — WebDev route manifest.
- `app.config.ts` — project logo metadata.
- `plan.md` / `TODO.md` — approved design and delivery scope.
