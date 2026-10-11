#!/usr/bin/env python3
"""Generate an NI 43-101-styled feasibility study PDF from a content model.

Implements templates/pdf-style.md (house style v1): Letter, sans-serif,
navy cover band, dot-leader TOC, dark-header/zebra tables, section content
per templates/feasibility-study.md.

Usage:
    python3 generate_study_pdf.py --demo [--output out.pdf]
    python3 generate_study_pdf.py --content model.json [--output out.pdf]

The JSON model shape:
    {"title_block": {"title": ..., "project": ..., "location": ..., "level": ...,
                     "effective_date": ..., "report_date": ..., "basis": ...,
                     "issuer": ..., "lead_firm": ..., "qps": [[name, firm], ...]},
     "sections": [{"num": "1", "title": "SUMMARY", "blocks": [
        {"para": "..."}, {"bullets": [...]},
        {"table": {"caption": ..., "headers": [...], "rows": [[...]],
                   "align": "lrr", "source": ...}},
        {"figure_tornado": {"caption": ..., "source": ...,
                            "items": [[label, low, high], ...], "base": x}} ]}]}
Requires: fpdf2 (pip install fpdf2). No network. Deterministic output.
"""

import argparse
import json
import sys

from fpdf import FPDF
from fpdf.enums import TableCellFillMode
from fpdf.fonts import FontFace

NAVY = (29, 45, 79)
TEAL = (0, 107, 127)
INK = (26, 26, 26)
ZEBRA = (242, 242, 242)
GRID = (191, 191, 191)
WHITE = (255, 255, 255)

# Core PDF fonts are latin-1 only, so transliterate wider Unicode to safe
# equivalents. Keeps the script portable (no system-font dependency).
_TRANSLATE = str.maketrans({
    "\u2014": "-", "\u2013": "-", "\u2212": "-",
    "\u2022": "-", "\u00b7": "-",
    "\u2192": "->", "\u2190": "<-",
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2026": "...", "\u2248": "~", "\u2265": ">=", "\u2264": "<=",
    "\u00b2": "2", "\u00b3": "3",
    "\u2082": "2", "\u2083": "3", "\u2084": "4",
    "\u2713": "[x]",
})


def _s(text):
    return text.translate(_TRANSLATE) if isinstance(text, str) else text


class StudyPDF(FPDF):
    def __init__(self, meta):
        super().__init__(format="Letter")
        self.meta = meta
        self.front_matter = True
        self.set_auto_page_break(True, margin=25)
        self.set_margins(25, 25, 25)
        # Sanitize every string rendered through cell/multi_cell (latin-1 cores).
        _cell, _mc = self.cell, self.multi_cell

        def cell(w, h=0, text="", *a, **k):
            return _cell(w, h, _s(text), *a, **k)

        def multi_cell(w, h, text="", *a, **k):
            return _mc(w, h, _s(text), *a, **k)

        self.cell = cell
        self.multi_cell = multi_cell

    # -- chrome ---------------------------------------------------------
    def header(self):
        if self.front_matter or self.page_no() == 1:
            return
        self.set_font("helvetica", "", 9)
        self.set_text_color(*GRID)
        self.cell(0, 6, f"{self.meta['issuer_short']}  |  {self.meta['short_title']}",
                  align="L")
        self.ln(7)
        self.set_draw_color(*GRID)
        self.line(25, self.get_y(), 191, self.get_y())
        self.ln(3)

    def footer(self):
        if self.front_matter or self.page_no() == 1:
            return
        self.set_y(-18)
        self.set_font("helvetica", "", 9)
        self.set_text_color(*GRID)
        self.cell(0, 6, f"DRAFT \u2014 for QP review  |  {self.meta['report_date']}  |  "
                        f"Page {self.page_no()} of {{nb}}", align="C")

    # -- building blocks --------------------------------------------------
    def cover(self, tb):
        self.front_matter = True
        self.add_page()
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 216, 150, style="F")
        self.set_y(28)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(*WHITE)
        self.multi_cell(0, 11, tb["title"], align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font("helvetica", "", 14)
        self.multi_cell(0, 8, f"{tb['project']}\n{tb['location']}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font("helvetica", "B", 13)
        self.cell(0, 8, f"{tb['level']}  \u2014  DRAFT", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_y(160)
        self.set_text_color(*INK)
        self.set_font("helvetica", "", 10)
        for label, value in [("Effective date", tb["effective_date"]),
                             ("Report date", tb["report_date"]),
                             ("Cost / price basis", tb["basis"]),
                             ("Issuer", tb["issuer"]),
                             ("Lead firm", tb["lead_firm"])]:
            self.cell(45, 6, label + ":")
            self.set_font("helvetica", "B", 10)
            self.multi_cell(0, 6, value, new_x="LMARGIN", new_y="NEXT")
            self.set_font("helvetica", "", 10)
        self.ln(4)
        self.set_font("helvetica", "B", 10)
        self.cell(0, 6, "Qualified Persons (certificates TO BE SIGNED)")
        self.set_font("helvetica", "", 10)
        for name, firm in tb["qps"]:
            self.cell(0, 6, f"  \u2022  {name} \u2014 {firm}", new_x="LMARGIN", new_y="NEXT")

    def notices(self):
        self.add_page()
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*NAVY)
        self.cell(0, 9, "Notices", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 10)
        self.set_text_color(*INK)
        for p in [
            "This document is a DRAFT feasibility study prepared for Qualified Person "
            "review. It is not a filed NI 43-101 technical report.",
            "Every technical claim cites its source input document ([Doc ID] + page). "
            "Sections that inputs cannot support are flagged as gaps with work-program "
            "items instead of figures.",
            "Training/reference studies used to shape this template contributed "
            "structure only. No figures herein derive from them.",
        ]:
            self.multi_cell(0, 5.5, p, new_x="LMARGIN", new_y="NEXT")
            self.ln(2)

    def toc(self):
        self.add_page()
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*NAVY)
        self.cell(0, 9, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*INK)
        self.insert_toc_placeholder(self._render_toc, allow_extra_pages=True)

    @staticmethod
    def _render_toc(pdf, outline):
        pdf.set_font("helvetica", "", 10)
        pdf.set_text_color(*INK)
        for sec in outline:
            indent = 5 + sec.level * 8
            pdf.set_x(25 + indent)
            w = 146 - indent
            pdf.cell(w, 6, sec.name)
            pdf.cell(0, 6, str(sec.page_number), align="R",
                     new_x="LMARGIN", new_y="NEXT")

    def lists(self, tables, figures):
        # v1: captions only (page numbers need a second pass — roadmap).
        self.add_page()
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*NAVY)
        self.cell(0, 9, "List of Tables", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 10)
        self.set_text_color(*INK)
        for cap in tables:
            self.cell(0, 6, f"  \u2022  {cap}", new_x="LMARGIN", new_y="NEXT")
        self.ln(6)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*NAVY)
        self.cell(0, 9, "List of Figures", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 10)
        self.set_text_color(*INK)
        for cap in figures:
            self.cell(0, 6, f"  \u2022  {cap}", new_x="LMARGIN", new_y="NEXT")

    def section(self, num, title):
        self.front_matter = False
        self.add_page()
        self.start_section(f"{num}  {title}", level=0)
        self.set_font("helvetica", "B", 16)
        self.set_text_color(*NAVY)
        self.cell(0, 10, f"{num}  {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*TEAL)
        self.set_line_width(0.8)
        self.line(25, self.get_y(), 191, self.get_y())
        self.set_line_width(0.2)
        self.ln(4)
        self.set_text_color(*INK)

    def sub(self, title):
        self.start_section(title, level=1)
        self.set_font("helvetica", "B", 12)
        self.set_text_color(*NAVY)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*INK)
        self.ln(1)

    def para(self, text):
        self.set_font("helvetica", "", 10)
        self.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def bullets(self, items):
        self.set_font("helvetica", "", 10)
        for it in items:
            x = self.get_x()
            self.cell(6, 5.5, "\u2022")
            self.multi_cell(0, 5.5, it, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def spec_table(self, spec):
        self.set_font("helvetica", "B", 9)
        self.set_text_color(*NAVY)
        self.cell(0, 6, spec["caption"], new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*INK)
        aligns = spec.get("align", "")
        with self.table(first_row_as_headings=True,
                         line_height=6,
                         text_align="LEFT" if not aligns else "",
                         width=160,
                         headings_style=FontFace(emphasis="BOLD", color=WHITE,
                                                 fill_color=NAVY),
                         cell_fill_mode=TableCellFillMode.EVEN_ROWS,
                         cell_fill_color=ZEBRA) as t:
            for i, row in enumerate([spec["headers"]] + spec["rows"]):
                tr = t.row()
                for j, datum in enumerate(row):
                    a = aligns[j] if j < len(aligns) else "LEFT"
                    tr.cell(str(datum), align=a)
        if spec.get("source"):
            self.set_font("helvetica", "I", 8)
            self.cell(0, 5, f"Source: {spec['source']}",
                      new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def figure_tornado(self, spec):
        self.set_font("helvetica", "B", 9)
        self.set_text_color(*NAVY)
        self.cell(0, 6, spec["caption"], new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*INK)
        items = spec["items"]
        base = spec.get("base", 0)
        lo = min(i[1] for i in items)
        hi = max(i[2] for i in items)
        span = max(hi - base, base - lo, 1)
        x0, wdt, y = 70, 96, self.get_y() + 2
        self.set_draw_color(*GRID)
        self.line(x0, y - 1, x0 + wdt, y - 1)
        self.line(x0, y + len(items) * 9, x0 + wdt, y + len(items) * 9)
        bx = x0 + wdt / 2
        self.set_draw_color(*NAVY)
        self.line(bx, y - 1, bx, y + len(items) * 9)
        self.set_font("helvetica", "", 8)
        for k, (label, v_lo, v_hi) in enumerate(items):
            yy = y + k * 9
            self.set_xy(25, yy - 1)
            self.cell(43, 6, label)
            xl = bx - (base - v_lo) / span * (wdt / 2)
            xh = bx + (v_hi - base) / span * (wdt / 2)
            self.set_fill_color(*TEAL)
            self.rect(xl, yy, bx - xl, 5, style="F")
            self.set_fill_color(180, 180, 180)
            self.rect(bx, yy, xh - bx, 5, style="F")
            self.set_xy(x0 + wdt + 2, yy - 1)
            self.cell(0, 6, f"{v_lo:+.0f} / +{v_hi - base:.0f}")
        self.set_y(y + len(items) * 9 + 4)
        self.set_font("helvetica", "B", 9)
        self.set_text_color(*NAVY)
        self.cell(0, 6, f"Base case = {spec.get('base_label', base)}; bars = \u00b120% input swing.",
                  new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*INK)
        if spec.get("source"):
            self.set_font("helvetica", "I", 8)
            self.cell(0, 5, f"Source: {spec['source']}",
                      new_x="LMARGIN", new_y="NEXT")
        self.ln(3)


def _san(obj):
    if isinstance(obj, str):
        return _s(obj)
    if isinstance(obj, list):
        return [_san(x) for x in obj]
    if isinstance(obj, dict):
        return {k: _san(v) for k, v in obj.items()}
    return obj


def collect_lists(model):
    tables, figures = [], []
    for s in model["sections"]:
        for b in s.get("blocks", []):
            if "table" in b:
                tables.append(b["table"]["caption"])
            for key in ("figure_tornado",):
                if key in b:
                    figures.append(b[key]["caption"])
    return tables, figures


def build(model, out_path):
    model = _san(model)
    meta = {"issuer_short": model["title_block"].get("issuer_short", "Issuer"),
            "short_title": model["title_block"].get("short_title", "Feasibility Study"),
            "report_date": model["title_block"]["report_date"]}
    pdf = StudyPDF(meta)
    pdf.set_title(f"{model['title_block']['project']} {model['title_block']['level']}")
    pdf.set_author(model["title_block"]["issuer"])
    pdf.cover(model["title_block"])
    pdf.notices()
    pdf.toc()
    tables, figures = collect_lists(model)
    pdf.lists(tables, figures)
    for s in model["sections"]:
        pdf.section(s["num"], s["title"])
        for b in s.get("blocks", []):
            if "sub" in b:
                pdf.sub(b["sub"])
            elif "para" in b:
                pdf.para(b["para"])
            elif "bullets" in b:
                pdf.bullets(b["bullets"])
            elif "table" in b:
                pdf.spec_table(b["table"])
            elif "figure_tornado" in b:
                pdf.figure_tornado(b["figure_tornado"])
    pdf.output(out_path)
    print(f"wrote {out_path} ({pdf.page_no()} pages)")


KESTREL = {
    "title_block": {
        "title": "Preliminary Economic Assessment",
        "project": "Kestrel Ridge Copper-Gold Project",
        "location": "Yukon, Canada  (FICTITIOUS DEMO \u2014 all figures synthetic)",
        "level": "PEA",
        "effective_date": "March 1, 2026",
        "report_date": "March 15, 2026",
        "basis": "Q1-2026 US$",
        "issuer": "Northline Minerals (fictitious)",
        "issuer_short": "Northline",
        "short_title": "Kestrel Ridge PEA",
        "lead_firm": "StudyBot Demo (fictitious compiler)",
        "qps": [["J. Doe, P.Geo (fict.) \u2014 GEO-01/02 (\u00a7\u00a77\u201312, 14)",
                 "Independent (fict.)"],
                ["All other sections \u2014 author of record TO BE SIGNED", ""]],
    },
    "sections": [
        {"num": "1", "title": "SUMMARY", "blocks": [
            {"para": "This Preliminary Economic Assessment evaluates a 12-year open-pit "
                     "copper-gold operation at 15,000 tpd (5.4 Mtpa milled) [MINE-01 p.8]. "
                     "The assessment is preliminary, relies in part on Inferred resources, "
                     "and is not a basis for a production decision."},
            {"table": {"caption": "Table 1-1: PEA Headline Results (Q1-2026 US$)",
                        "headers": ["Item", "Unit", "Value"],
                        "rows": [["Mine life", "years", "12"],
                                 ["Throughput", "tpd", "15,000"],
                                 ["Avg payable Cu", "Mlbs/yr", "52"],
                                 ["Avg payable Au", "koz/yr", "38"],
                                 ["Initial capex", "US$M", "480"],
                                 ["Sustaining capex", "US$M", "120"],
                                 ["Post-tax NPV @ 8%", "US$M", "310"],
                                 ["Post-tax IRR", "%", "19"],
                                 ["Payback", "years", "4.2"]],
                        "align": "lcr",
                        "source": "MINE-01 p.11; COST-01 p.9."}},
            {"para": "Key risks: bench-scale metallurgy only (scale-up risk), conceptual "
                     "tailings with no geotech basis, incomplete hydrogeology, and early-stage "
                     "permitting and engagement. Recommended PFS work program totals "
                     "approximately US$11M (see \u00a726)."}]},
        {"num": "4", "title": "PROPERTY DESCRIPTION AND LOCATION", "blocks": [
            {"para": "100%-owned claims in good standing to 2028 [PROP-01 p.3]. Road and "
                     "airstrip access; subarctic climate with a 10-month operating season "
                     "assumed [PROP-01 p.5]. Minor 1970s trenching is the only historic "
                     "work [PROP-01 p.7]."}]},
        {"num": "7", "title": "GEOLOGICAL SETTING AND MINERALIZATION", "blocks": [
            {"para": "Porphyry copper-gold system over 63 holes (14,200 m) with standard "
                     "logging and sampling [GEO-01 pp.14, 22]. QAQC pass rates within "
                     "tolerance [GEO-02 p.4]. Gap: no QP site visit is on record."}]},
        {"num": "13", "title": "MINERAL PROCESSING AND METALLURGICAL TESTING", "blocks": [
            {"para": "Bench rougher flotation returned 88% Cu and 65% Au recovery to a 26% "
                     "Cu concentrate across 42 variability samples [MET-01 p.6]. "
                     "Gap: no locked-cycle or pilot work; scale-up risk is carried in \u00a725."}]},
        {"num": "14", "title": "MINERAL RESOURCE ESTIMATE", "blocks": [
            {"table": {"caption": "Table 14-1: Pit-Constrained Resources, 15% NSR Cutoff (Feb 28, 2026)",
                        "headers": ["Class", "Mt", "Cu %", "Au g/t"],
                        "rows": [["Measured", "12", "0.90", "0.31"],
                                 ["Indicated", "40", "0.80", "0.28"],
                                 ["Inferred", "25", "0.70", "0.22"]],
                        "align": "lcrr",
                        "source": "GEO-01 p.40 (ID3, pit-constrained; exclusive of reserves, none declared)."}}]},
        {"num": "15", "title": "MINERAL RESERVE ESTIMATE", "blocks": [
            {"para": "No reserves are declared. Correct for a PEA; reserves require PFS-level "
                     "modifying factors."}]},
        {"num": "16", "title": "MINING METHODS", "blocks": [
            {"table": {"caption": "Table 16-1: LOM Production Schedule",
                        "headers": ["Period", "Mined (Mt)", "Milled (Mt)", "Strip ratio"],
                        "rows": [["Pre-production", "9", "\u2014", "\u2014"],
                                 ["Years 1\u20134", "52", "21", "2.5"],
                                 ["Years 5\u20138", "48", "22", "2.2"],
                                 ["Years 9\u201312", "33", "19", "1.7"],
                                 ["Total", "142", "62", "2.2"]],
                        "align": "lrrr",
                        "source": "MINE-01 p.8."}}]},
        {"num": "18", "title": "PROJECT INFRASTRUCTURE", "blocks": [
            {"para": "Grid power assumed via a 40 km spur; conventional valley-fill tailings "
                     "at concept level. Gaps: no utility engagement, no tailings geotech or "
                     "hydrogeology basis [ENV-01 p.9]."}]},
        {"num": "19", "title": "MARKET STUDIES AND CONTRACTS", "blocks": [
            {"para": "January-2026 consensus deck: Cu US$4.25/lb, Au US$2,400/oz, US$ basis "
                     "[MKT-01 p.2]. No offtake or hedging assumed."}]},
        {"num": "20", "title": "ENVIRONMENTAL STUDIES, PERMITTING AND SOCIAL IMPACT", "blocks": [
            {"para": "Baseline studies partial; early engagement commenced [ENV-01 p.3]. "
                     "Gaps: EA pathway undefined, closure cost not estimated."}]},
        {"num": "21", "title": "CAPITAL AND OPERATING COSTS", "blocks": [
            {"table": {"caption": "Table 21-1: Capital Cost Build-Up (US$M, Q1-2026, \u00b140%)",
                        "headers": ["Area", "Initial", "Sustaining"],
                        "rows": [["Mining (fleet + pre-strip)", "150", "60"],
                                 ["Process plant", "190", "25"],
                                 ["Infrastructure / power spur", "70", "10"],
                                 ["Indirect + owners", "70", "5"],
                                 ["Contingency (25%)", "120", "20"],
                                 ["Total", "600", "120"]],
                        "align": "lrr",
                        "source": "COST-01 p.4 (factored estimate)."}},
            {"table": {"caption": "Table 21-2: Operating Cost (US$/t milled)",
                        "headers": ["Area", "US$/t"],
                        "rows": [["Mining", "7.20"],
                                 ["Processing", "8.10"],
                                 ["G&A", "2.10"],
                                 ["Tailings / water", "1.10"],
                                 ["Total", "18.50"]],
                        "align": "lr",
                        "source": "COST-01 p.7."}}]},
        {"num": "22", "title": "ECONOMIC ANALYSIS", "blocks": [
            {"para": "Post-tax NPV at 8% is US$310M with a 19% IRR and 4.2-year payback, "
                     "on 100% equity, no debt, closure excluded (gap). AISC is US$2.10/lb "
                     "CuEq net of gold credits [COST-01 pp.8\u20139]."},
            {"figure_tornado": {"caption": "Figure 22-1: Post-Tax NPV Sensitivity to \u00b120% Input Swings",
                                "source": "COST-01 p.10 (illustrative).",
                                "base": 310, "base_label": "US$310M",
                                "items": [["Cu price", 168, 452],
                                          ["Head grade", 196, 424],
                                          ["Opex", 238, 382],
                                          ["Capex", 262, 358],
                                          ["Recovery", 266, 354]]}}]},
        {"num": "25", "title": "INTERPRETATION AND CONCLUSIONS", "blocks": [
            {"bullets": ["Conceptual economics are positive at the stated deck, with margin "
                         "most exposed to copper price and head grade.",
                         "Scale-up (bench-only met), tailings, hydrogeology, and permitting "
                         "are the material risks; none is characterised beyond concept."]}]},
        {"num": "26", "title": "RECOMMENDATIONS", "blocks": [
            {"table": {"caption": "Table 26-1: PFS Work Program Budget (US$M)",
                        "headers": ["Item", "US$M"],
                        "rows": [["Infill drilling (Inf \u2192 I)", "4.5"],
                                 ["Pilot metallurgy program", "2.0"],
                                 ["Hydrogeotech + tailings PFS", "3.0"],
                                 ["EA baseline completion", "1.5"],
                                 ["Total (unfunded)", "11.0"]],
                        "align": "lr",
                        "source": "Proposed; unfunded."}}]},
        {"num": "27", "title": "REFERENCES", "blocks": [
            {"bullets": ["PROP-01 Claims & tenure memo, 2026-01-15.",
                         "GEO-01/02 Drilling report & QAQC memo, 2025-11-30.",
                         "MET-01 Bench flotation testwork, 2025-09-12.",
                         "MINE-01 Conceptual pits & schedules, 2026-02-03.",
                         "COST-01 Factored capex/opex, 2026-02-20.",
                         "ENV-01 Baseline scoping memo, 2025-08-01.",
                         "MKT-01 Consensus price deck, 2026-01-31."]}]},
    ],
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--demo", action="store_true",
                   help="build the built-in fictitious Kestrel Ridge PEA demo")
    g.add_argument("--content", metavar="MODEL.JSON",
                   help="build from a JSON content model (see module docstring)")
    ap.add_argument("--output", metavar="OUT.PDF", default=None,
                    help="output path (default: <project>-draft.pdf / demo name)")
    args = ap.parse_args(argv)
    if args.demo:
        model = KESTREL
        out = args.output or "Kestrel_Ridge-PEA-DRAFT.pdf"
    else:
        with open(args.content, encoding="utf-8") as f:
            model = json.load(f)
        out = args.output or (model["title_block"]["project"].replace(" ", "_")
                              + "-draft.pdf")
    build(model, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
