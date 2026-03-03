# Changelog

> SOT system version: **2.5.0** (as of `workflow-registry.yaml`)
> Entries organized by git commit date. SOT internal module versions noted in parentheses where applicable.

## 2026-03-01

### 4-Layer Quality Defense (L2b + L3)
- Add `validate_report_quality.py` — L2b cross-reference QC (13 checks: QC-001~013)
- Add `quality-reviewer.md` — L3 semantic depth review (3-pass LLM sub-agent)
- Fix skeleton contamination in report generator

---

## 2026-02-24

### WF4: Multi&Global-News Environmental Scanning (Quadruple Workflow)
- Add WF4 orchestrator (`multiglobal-news-scan-orchestrator.md`) and 5 exclusive workers
- Add `news_direct_crawler.py` — 43 direct news sites, 11 languages, 3-level retry architecture
- Add `news_signal_processor.py` — FSSF/Three Horizons/Tipping Point adapted for multilingual news
- Add `sources-multiglobal-news.yaml` — 17 KR + 20 EN + 7 other language sites
- Add WF4 report skeleton pair (KO/EN)
- SOT updated: WF4 definition, SOT-051~054 validation, 9 checkpoints

### Documentation
- Update all root documentation for Quadruple Workflow System

---

## 2026-02-06

### WF3: Naver News Environmental Scanning (Triple Workflow)
- Add WF3 orchestrator (`naver-scan-orchestrator.md`) and 4 exclusive workers
- Add `naver_crawler.py` — CrawlDefender 7-strategy anti-blocking cascade
- Add `naver_signal_processor.py` — FSSF 8-type classification, Three Horizons, Tipping Point detection
- Add `sources-naver.yaml` — 6 Naver News sections with STEEPs mapping
- Add WF3 report skeleton pair (KO/EN)

### Standard Signal Format
- Add standard signal processor for WF3 with `items[]` array format

### Weekly Meta-Analysis
- Add weekly report skeleton and meta-analysis workflow
- 7-day signal evolution analysis across all workflows

---

## 2026-02-04

### Initial Release (Dual Workflow System)

All foundational modules committed as a single consolidated release.

#### Core Infrastructure
- SharedContextManager with field-level selective loading
- RecursiveArchiveLoader with time-based filtering and index building
- `entity_extractor.py` for automatic named entity extraction
- Unit tests and integration tests

#### WF2: arXiv Academic Deep Scanning
- Add WF2 orchestrator (`arxiv-scan-orchestrator.md`)
- arXiv extracted from WF1 into independent WF2
- 14-day lookback, 50 results per category, 30+ arXiv categories

#### Bilingual Pipeline (SOT internal: v2.8.0)
- Add `bilingual_resolver.py`, `skeleton_mirror.py`, `translation_validator.py`
- Reports generated in EN → validated → translated to KO
- EN skeleton auto-generated from KO skeleton via deterministic transformation
- `translation-terms.yaml` for STEEPs term preservation

#### Temporal Consistency (SOT internal: v2.2.0)
- Add `temporal_anchor.py` — deterministic T₀ generation and scan window arithmetic
- Add `temporal_gate.py` — programmatic post-collection time range enforcement
- Add `report_metadata_injector.py` — temporal metadata injection into reports
- Add `report_statistics_engine.py` — deterministic placeholder computation
- "계산은 Python이, 판단은 LLM이" principle established

#### Signal Evolution Tracking (SOT internal: v2.3.0)
- Add `signal_evolution_tracker.py` — cross-day signal matching (NEW/RECURRING/STRENGTHENING/WEAKENING/FADED/TRANSFORMED)
- Jaro-Winkler title matching + keyword vector similarity
- Evolution index as persistent file separate from database.json
- Cross-workflow thread correlation for integration step
- SOT direct reading (v2.3.1): all thresholds read from registry by Python

#### Signal Evolution Timeline Map (SOT internal: v2.4.0)
- Add `timeline_map_generator.py` — 7-day Korean markdown timeline map
- Cross-WF correlation visualization in integrated reports

#### Source Exploration (SOT internal: v2.5.0)
- Add `source_explorer.py`, `exploration_gate.py`, `exploration_merge_gate.py`, `frontier_selector.py`
- Gap-directed (alpha) and random serendipitous (beta) discovery agents
- Independent evaluator agent for candidate scoring

#### Dedup Gate (SOT internal: v2.6.0–v2.9.0)
- Add `dedup_gate.py` — 4-stage cascade: URL → Topic Fingerprint → Jaro-Winkler → Entity Jaccard
- Deterministic Python pre-filter before LLM dedup-filter agent
- Cross-scan duplicate detection with 30-day lookback
