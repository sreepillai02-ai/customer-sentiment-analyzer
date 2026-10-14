"""
Standalone PDF Presentation Generator for:
Customer Feedback Sentiment Analyzer in Social Media Analytics.
Generates an 10-slide 16:9 widescreen presentation in PDF format.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

# Color Palette
BG_DARK = "#0F172A"       # Deep Slate / Navy
BG_LIGHT = "#F8FAFC"      # Slate 50
CARD_BG = "#FFFFFF"       # White cards
CARD_BORDER = "#E2E8F0"   # Light border
PRIMARY_BLUE = "#2563EB"  # Electric blue
ACCENT_BLUE = "#38BDF8"   # Sky blue
TEXT_DARK = "#1E293B"     # Slate 800
TEXT_MUTED = "#64748B"    # Slate 500
TEXT_WHITE = "#FFFFFF"
COLOR_GREEN = "#16A34A"   # Green 600
COLOR_RED = "#DC2626"     # Red 600
COLOR_AMBER = "#D97706"   # Amber 600

def draw_header(ax, title, category="SOCIAL MEDIA ANALYTICS & NLP", slide_num=1):
    ax.text(0.06, 0.92, category.upper(), fontsize=10, fontweight='bold', color=PRIMARY_BLUE, transform=ax.transAxes)
    ax.text(0.06, 0.86, title, fontsize=20, fontweight='bold', color=TEXT_DARK, transform=ax.transAxes)
    ax.plot([0.06, 0.94], [0.83, 0.83], transform=ax.transAxes, color=CARD_BORDER, linewidth=1.5)
    ax.text(0.06, 0.04, "SocialSense • Customer Sentiment Analyzer", fontsize=9, color=TEXT_MUTED, transform=ax.transAxes)
    ax.text(0.94, 0.04, f"Slide {slide_num} of 10", fontsize=9, fontweight='bold', color=TEXT_MUTED, ha='right', transform=ax.transAxes)

def draw_card(ax, x, y, width, height, title, items, badge="", badge_color=PRIMARY_BLUE, title_color=TEXT_DARK):
    card = patches.FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.015,rounding_size=0.02",
        facecolor=CARD_BG,
        edgecolor=CARD_BORDER,
        linewidth=1.2,
        transform=ax.transAxes,
        zorder=1
    )
    ax.add_patch(card)

    curr_y = y + height - 0.05
    if badge:
        ax.text(x + 0.025, curr_y, badge.upper(), fontsize=8, fontweight='bold', color=badge_color, transform=ax.transAxes, zorder=2)
        curr_y -= 0.04

    ax.text(x + 0.025, curr_y, title, fontsize=13, fontweight='bold', color=title_color, transform=ax.transAxes, zorder=2)
    curr_y -= 0.05

    for item in items:
        ax.text(
            x + 0.025, curr_y, f"• {item}",
            fontsize=9.5,
            color=TEXT_DARK,
            transform=ax.transAxes,
            wrap=True,
            zorder=2,
            linespacing=1.3
        )
        curr_y -= 0.065

def create_presentation_pdf(output_path="presentation/Social_Media_Sentiment_Topic_Analysis_Presentation.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with PdfPages(output_path) as pdf:
        # ------------------ SLIDE 1: TITLE SLIDE ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_DARK)
        ax.axis('off')

        badge_box = patches.FancyBboxPatch(
            (0.08, 0.72), 0.44, 0.05,
            boxstyle="round,pad=0.01,rounding_size=0.015",
            facecolor="#1E293B",
            edgecolor=PRIMARY_BLUE,
            linewidth=1.5,
            transform=ax.transAxes
        )
        ax.add_patch(badge_box)
        ax.text(0.10, 0.735, "NATURAL LANGUAGE PROCESSING • SOCIAL MEDIA ANALYTICS", fontsize=10, fontweight='bold', color=ACCENT_BLUE, transform=ax.transAxes)

        ax.text(0.08, 0.58, "Customer Feedback Sentiment Analyzer", fontsize=34, fontweight='bold', color=TEXT_WHITE, transform=ax.transAxes)
        ax.text(0.08, 0.46, "Mining Real-Time Emotional Valence, Brand Perception, and Net Sentiment from Social Media Streams", fontsize=14, color="#94A3B8", transform=ax.transAxes)

        pills = ["Python 3.10+", "VADER Valence Engine", "TextBlob Subjectivity", "Streamlit Dashboard", "Net Sentiment Score"]
        pill_x = 0.08
        for p in pills:
            p_box = patches.FancyBboxPatch((pill_x, 0.30), 0.155, 0.05, boxstyle="round,pad=0.008,rounding_size=0.01", facecolor="#1E293B", edgecolor="#334155", linewidth=1, transform=ax.transAxes)
            ax.add_patch(p_box)
            ax.text(pill_x + 0.012, 0.315, p, fontsize=9.5, fontweight='bold', color=TEXT_WHITE, transform=ax.transAxes)
            pill_x += 0.175

        ax.text(0.08, 0.14, "Project Submission • Open Source Codebase & Live Web App", fontsize=11, color="#64748B", transform=ax.transAxes)
        pdf.savefig(fig, facecolor=BG_DARK)
        plt.close(fig)

        # ------------------ SLIDE 2: PROBLEM STATEMENT ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Problem Statement & Industry Motivation", slide_num=2)

        draw_card(ax, 0.06, 0.12, 0.27, 0.67, "Massive Unstructured Noise", [
            "Millions of unsolicited customer posts daily.",
            "Manual review is slow, expensive, & subjective.",
            "Human reviewers introduce cognitive fatigue.",
            "Critical complaints trigger rapid PR crises."
        ], badge="Volume Challenge", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.36, 0.12, 0.27, 0.67, "Informal Social Language", [
            "Heavy slang, informal spelling, and jargon.",
            "Strong emotional valence in emojis (😡, 🚀).",
            "Punctuation ('!!!') & ALL-CAPS shift valence.",
            "Standard dictionary parsers miss context."
        ], badge="Linguistic Challenge", badge_color=COLOR_AMBER)

        draw_card(ax, 0.66, 0.12, 0.27, 0.67, "Lack of Quantified Metrics", [
            "No standard real-time benchmark for brand health.",
            "Unclear sentiment variance across channels.",
            "Need for standardized Net Sentiment Score (NSS).",
            "Leadership requires instant visual dashboards."
        ], badge="Business Challenge", badge_color=COLOR_RED)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 3: OBJECTIVES ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Project Objectives & Scope", slide_num=3)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Technical Objectives", [
            "Build an automated sentiment engine calibrated for social text.",
            "Preserve emojis, capitalization, and punctuation signals.",
            "Compute continuous Compound Valence [-1.0 to +1.0].",
            "Classify posts into Positive, Neutral, and Negative.",
            "Derive Subjectivity (0.0 to 1.0) to separate facts from opinions."
        ], badge="Technical Goals", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Practical Deliverables", [
            "Streamlit interactive dashboard with real-time post tester.",
            "Calculation of Net Sentiment Score (NSS = %Pos - %Neg).",
            "Channel comparisons across Twitter, Reddit, and Instagram.",
            "Batch CSV/Excel file processing and report export.",
            "Full unit test suite and clean GitHub repository."
        ], badge="Key Deliverables", badge_color=COLOR_GREEN)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 4: ARCHITECTURE ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Streamlined System Architecture Pipeline", slide_num=4)

        stages = [
            ("Stage 1: Ingestion", ["Twitter/X, Reddit, IG", "CSV & Excel files", "Single post input"], "0.06"),
            ("Stage 2: Cleaning", ["URL & @mention strip", "Emoji preservation", "Contraction expansion"], "0.285"),
            ("Stage 3: Sentiment Core", ["VADER valence lexicon", "Punctuation boosters", "Compound score math"], "0.51"),
            ("Stage 4: Dashboard", ["Streamlit web app", "Net Sentiment KPI cards", "CSV report export"], "0.735")
        ]
        for title, items, pos_x in stages:
            draw_card(ax, float(pos_x), 0.12, 0.205, 0.67, title, items, badge="Pipeline Stage", badge_color=PRIMARY_BLUE)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 5: PREPROCESSING ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Data Preprocessing for Social Media Text", slide_num=5)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Noise Cleaning Techniques", [
            "User Mentions & URLs: Removes raw @usernames and links.",
            "Hashtag Handling: Keeps semantic words while stripping '#'.",
            "Contraction Expansion: 'can't' -> 'cannot', 'u' -> 'you'.",
            "Slang Standardization: 'pls' -> 'please', 'idk' -> 'i do not know'.",
            "Unicode Normalization: Resolves special character encodings."
        ], badge="Noise Reduction", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Preserving Emotional Signals", [
            "Emoji Retention: Keeps '😡', '❤️', '🚀' carrying intense valence.",
            "Capitalization Retention: 'GREAT' scores higher than 'great'.",
            "Punctuation Retention: 'Good!!!' conveys higher enthusiasm.",
            "Result: Retains full psychological meaning of customer posts."
        ], badge="Valence Preservation", badge_color=COLOR_GREEN)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 6: SENTIMENT ENGINE ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Sentiment Analysis Engine (VADER)", slide_num=6)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Why VADER for Social Media?", [
            "VADER: Valence Aware Dictionary and sEntiment Reasoner.",
            "Calibrated specifically for micro-blogs and informal text.",
            "Rule-based, lightning fast, and requires zero heavy GPU memory.",
            "High correlation with human sentiment ratings on social data."
        ], badge="Engine Overview", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Linguistic Heuristics in VADER", [
            "Punctuation amplifier: 'Good' (0.44) vs 'Good!!!' (0.64).",
            "Capitalization amplifier: 'great' (0.62) vs 'GREAT' (0.75).",
            "Degree modifiers: 'slightly late' vs 'extremely late'.",
            "Conjunction flip: 'Good app BUT slow' accurately prioritizes negative."
        ], badge="Heuristic Rules", badge_color=COLOR_AMBER)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 7: MATHEMATICAL NORMALIZATION ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Mathematical Formulation & Classification", slide_num=7)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Compound Valence Calculation", [
            "Normalizes lexical valence ratings into a continuous score:",
            "Compound = sum(valence) / sqrt(sum(valence)^2 + alpha)",
            "Alpha is a normalization constant (default = 15).",
            "Score range: strictly bounded between -1.0 and +1.0."
        ], badge="Formula", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Classification Thresholds & Subjectivity", [
            "Classification Rules:",
            "   • Positive Sentiment: Compound Score >= +0.05",
            "   • Neutral Sentiment:  -0.05 < Compound Score < +0.05",
            "   • Negative Sentiment: Compound Score <= -0.05",
            "Subjectivity Measurement (TextBlob):",
            "   • 0.0 = Objective Fact, 1.0 = Subjective Opinion."
        ], badge="Thresholds", badge_color=COLOR_GREEN)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 8: BUSINESS METRICS ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Executive Metrics & Net Sentiment Score", slide_num=8)

        draw_card(ax, 0.06, 0.12, 0.27, 0.67, "Net Sentiment Score (NSS)", [
            "Formula: % Positive - % Negative.",
            "Ranges between -100% to +100%.",
            "Real-time social proxy for Net Promoter Score (NPS).",
            "Standardized metric for marketing performance."
        ], badge="North-Star Metric", badge_color=COLOR_GREEN)

        draw_card(ax, 0.36, 0.12, 0.27, 0.67, "Cross-Platform Insights", [
            "Compares satisfaction across Twitter, Reddit, and Instagram.",
            "Flags channels with highest complaint concentration.",
            "Directs customer care staff where response is needed."
        ], badge="Channel Benchmarking", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.66, 0.12, 0.27, 0.67, "Keyword Drivers", [
            "Extracts top distinct positive words (e.g. 'fast', 'sleek').",
            "Identifies recurring complaint terms (e.g. 'delayed', 'broken').",
            "Actionable feedback for product teams."
        ], badge="Actionable Drivers", badge_color=COLOR_AMBER)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 9: TECH STACK ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Technology Stack & Repository Layout", slide_num=9)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Core Technologies", [
            "Language: Python 3.10+ (Clean, modular structure).",
            "Web Framework: Streamlit (Reactive UI, custom CSS).",
            "Sentiment Core: VADER Sentiment & TextBlob.",
            "Data Visualization: Plotly Express (Donut, timeline, gauges).",
            "Data Processing: Pandas & NumPy.",
            "Reporting: Automated PowerPoint (.pptx) & PDF (.pdf)."
        ], badge="Tech Stack", badge_color=PRIMARY_BLUE)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Clean Directory Layout", [
            "src/preprocessor.py -> Social media cleaning & emoji handling",
            "src/sentiment.py    -> VADER sentiment intensity engine",
            "src/insights.py     -> Net Sentiment Score (NSS) calculations",
            "app.py              -> Streamlit Web Dashboard",
            "cli.py              -> Headless batch runner",
            "tests/              -> Automated test suite (unittest)"
        ], badge="Modular Layout", badge_color=COLOR_AMBER)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

        # ------------------ SLIDE 10: CONCLUSION ------------------
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_LIGHT)
        ax.axis('off')
        draw_header(ax, "Conclusion & Project Outcomes", slide_num=10)

        draw_card(ax, 0.06, 0.12, 0.42, 0.67, "Key Achievements", [
            "Fast, production-ready sentiment analyzer for social text.",
            "Effectively resolves emojis, slang, and informal language.",
            "Interactive live web app with real-time post tester.",
            "100% unit test pass rate and clean GitHub documentation.",
            "Widescreen presentation decks ready for evaluation."
        ], badge="Project Outcomes", badge_color=COLOR_GREEN)

        draw_card(ax, 0.52, 0.12, 0.42, 0.67, "Future Scope", [
            "Live Social APIs: Ingest real-time tweets via Twitter API v2.",
            "Multilingual Sentiment: Incorporate XLM-RoBERTa for 50+ languages.",
            "Aspect-Based Sentiment: Sentence-level multi-aspect breakdown.",
            "Auto-Response Generator: AI draft responses for support tickets."
        ], badge="Roadmap", badge_color=PRIMARY_BLUE)

        pdf.savefig(fig, facecolor=BG_LIGHT)
        plt.close(fig)

    print(f"Successfully generated presentation PDF at: {output_path}")

if __name__ == "__main__":
    create_presentation_pdf()
