"""
PowerPoint Presentation Generator for:
Customer Feedback Sentiment Analyzer in Social Media Analytics.
Generates an 10-slide presentation (.pptx) with clear speaker notes.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="presentation/Social_Media_Sentiment_Topic_Analysis_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)  # 16:9 widescreen layout

    # Color Palette Definitions
    COLOR_PRIMARY = RGBColor(15, 23, 42)        # Deep Slate / Navy (#0F172A)
    COLOR_ACCENT = RGBColor(37, 99, 235)        # Electric Blue (#2563EB)
    COLOR_TEXT_DARK = RGBColor(30, 41, 59)     # Slate 800
    COLOR_CARD_BG = RGBColor(241, 245, 249)    # Light Slate 100
    COLOR_WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text="SOCIAL MEDIA ANALYTICS & NLP"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.4))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]
        p_c.text = category_text.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_ACCENT

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_PRIMARY

    def add_card(slide, left, top, width, height, title, body_bullets, border_color=None):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = COLOR_CARD_BG
        shape.line.color.rgb = border_color if border_color else RGBColor(226, 232, 240)
        shape.line.width = Pt(1.5)

        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)
        tf.margin_bottom = Inches(0.3)

        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_PRIMARY
        p_title.space_after = Pt(8)

        for bullet in body_bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"• {bullet}"
            p_b.font.size = Pt(12.5)
            p_b.font.color.rgb = COLOR_TEXT_DARK
            p_b.space_after = Pt(5)

    # ------------------ SLIDE 1: TITLE SLIDE ------------------
    slide1 = prs.slides.add_slide(prs.slide_layouts[6])
    bg_box = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg_box.fill.solid()
    bg_box.fill.fore_color.rgb = COLOR_PRIMARY
    bg_box.line.color.rgb = COLOR_PRIMARY

    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(3.5))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "NATURAL LANGUAGE PROCESSING • SOCIAL MEDIA ANALYTICS"
    p_badge.font.size = Pt(13)
    p_badge.font.bold = True
    p_badge.font.color.rgb = RGBColor(96, 165, 250)
    p_badge.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "Customer Feedback Sentiment Analyzer"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_after = Pt(12)

    p2 = tf1.add_paragraph()
    p2.text = "Mining Real-Time Emotional Valence, Brand Perception, and Net Sentiment from Social Media Streams"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(203, 213, 225)
    p2.space_after = Pt(36)

    p_meta = tf1.add_paragraph()
    p_meta.text = "Project Submission  |  Ready-to-Deploy Codebase & Live Dashboard"
    p_meta.font.size = Pt(13)
    p_meta.font.color.rgb = RGBColor(148, 163, 184)

    slide1.notes_slide.notes_text_frame.text = (
        "Welcome everyone. Today I am presenting my project: Customer Feedback Sentiment Analyzer in Social Media Analytics. "
        "We will explore how customer comments and reviews are analyzed to understand sentiment and brand health."
    )

    # ------------------ SLIDE 2: PROBLEM STATEMENT ------------------
    slide2 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide2, "Problem Statement & Industry Motivation")
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "Massive Unstructured Noise", [
        "Millions of customer comments and tweets are posted daily on Twitter/X, Reddit, and Instagram.",
        "Manual inspection is impossible, slow, expensive, and subjective.",
        "Customer escalations can quickly snowball into viral PR crises."
    ])
    add_card(slide2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "Informal Social Language", [
        "Social posts feature slang, contractions, and abbreviations ('pls', 'can't', 'u').",
        "Heavy sentiment is carried by emojis (😡, 🚀) and capitalization ('TERRIBLE').",
        "Traditional dictionary lookup tools fail on micro-texts and sarcasm."
    ])
    add_card(slide2, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "Lack of Quantified Metrics", [
        "Businesses struggle to quantify overall customer happiness.",
        "Need for a standardized metric like Net Sentiment Score (NSS).",
        "Requires real-time visibility across different social media channels."
    ])
    slide2.notes_slide.notes_text_frame.text = (
        "Traditional manual monitoring cannot keep pace with social media. Customer posts are short, full of slang, and emotive."
    )

    # ------------------ SLIDE 3: PROJECT OBJECTIVES ------------------
    slide3 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide3, "Project Objectives & Scope")
    add_card(slide3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Core Technical Goals", [
        "Develop an automated sentiment pipeline calibrated specifically for social media text.",
        "Preserve emotive cues like emojis (😡, ❤️) and all-caps emphasis during preprocessing.",
        "Calculate continuous compound scores [-1.0 to +1.0] and classify into Positive, Neutral, Negative.",
        "Measure Subjectivity (0.0 to 1.0) to distinguish factual queries from personal opinions."
    ])
    add_card(slide3, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Practical Deliverables", [
        "Interactive Streamlit Web Dashboard for real-time post analysis and visual insights.",
        "Automated Net Sentiment Score (NSS = % Positive - % Negative) calculation.",
        "Comparative sentiment breakdown across social platforms (Twitter, Reddit, Instagram).",
        "Batch CSV upload and headless CLI mode for automated reports."
    ])
    slide3.notes_slide.notes_text_frame.text = (
        "Our objective was to build a clean, accurate, and practical sentiment analyzer tailored for social media."
    )

    # ------------------ SLIDE 4: SYSTEM ARCHITECTURE ------------------
    slide4 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide4, "System Architecture Pipeline")
    steps = [
        ("Step 1: Ingestion", ["Social media post streams", "CSV and Excel uploads", "Interactive user inputs"]),
        ("Step 2: Preprocessing", ["Strip URLs and @mentions", "Expand informal slang & contractions", "Preserve emojis and case"]),
        ("Step 3: Sentiment Engine", ["VADER valence dictionary", "Punctuation & modifier rules", "Compound score calculation"]),
        ("Step 4: Insights & Dashboard", ["Streamlit web dashboard", "Net Sentiment Score (NSS)", "Channel comparisons & CSV export"])
    ]
    for idx, (step_title, bullets) in enumerate(steps):
        left_pos = Inches(0.8 + idx * 2.95)
        add_card(slide4, left_pos, Inches(1.8), Inches(2.8), Inches(5.0), step_title, bullets)

    slide4.notes_slide.notes_text_frame.text = (
        "Here is the streamlined 4-stage pipeline: from raw ingestion to social cleaning, VADER sentiment classification, and the dashboard layer."
    )

    # ------------------ SLIDE 5: PREPROCESSING ------------------
    slide5 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide5, "Data Preprocessing Optimized for Social Text")
    add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Noise Cleaning Techniques", [
        "User Mentions & URLs: Removes noisy @usernames and web links (http/https).",
        "Hashtags: Strips the '#' symbol while keeping the word (e.g. '#awesome' -> 'awesome').",
        "Contractions & Slang: Standardizes informal language ('can't' -> 'cannot', 'u' -> 'you', 'pls' -> 'please').",
        "Unicode Normalization: Resolves special character encodings and HTML entities."
    ])
    add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Emotional Signal Preservation", [
        "Emoji Retention: Keeps emojis ('😡', '🚀', '🔥') because they encode over 75% of emotion in micro-texts.",
        "Capitalization Retention: 'GREAT' carries significantly more positive weight than 'great'.",
        "Punctuation Retention: Multiple exclamation marks ('!!!') amplify intensity.",
        "Result: Clean text that retains full psychological valence."
    ])
    slide5.notes_slide.notes_text_frame.text = (
        "Unlike standard NLP which destroys emojis and capitalization, our preprocessor preserves emotional signals."
    )

    # ------------------ SLIDE 6: SENTIMENT ENGINE ------------------
    slide6 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide6, "Sentiment Analysis Engine (VADER)")
    add_card(slide6, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Why VADER for Social Media?", [
        "VADER: Valence Aware Dictionary and sEntiment Reasoner.",
        "Specifically trained on social media text, micro-blogs, and user reviews.",
        "Rule-based, fast, and does not require heavy GPU hardware or 5GB language models.",
        "Generalizes well across diverse social media platforms."
    ])
    add_card(slide6, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Heuristic Rules in Action", [
        "Punctuation Booster: 'Good' (0.44) vs 'Good!!!' (0.64).",
        "Capitalization Booster: 'great' (0.62) vs 'GREAT' (0.75).",
        "Degree Modifiers: 'slightly disappointed' vs 'extremely disappointed'.",
        "Conjunction Flipping: 'Good UI BUT slow checkout' accurately prioritizes the negative clause."
    ])
    slide6.notes_slide.notes_text_frame.text = (
        "VADER relies on five generalizable linguistic heuristics that make it exceptionally accurate on social media comments."
    )

    # ------------------ SLIDE 7: MATHEMATICAL NORMALIZATION ------------------
    slide7 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide7, "Mathematical Formulation & Classification")
    add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Compound Valence Calculation", [
        "VADER normalizes the sum of lexical ratings into a continuous Compound Score:",
        "Compound = sum(valence) / sqrt(sum(valence)^2 + alpha)",
        "Alpha is a normalization constant (default = 15).",
        "Output range: strictly bounded between -1.0 (Most Negative) and +1.0 (Most Positive)."
    ])
    add_card(slide7, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Classification Thresholds & Subjectivity", [
        "Industry-Standard Thresholds:",
        "   • Positive Sentiment: Compound Score >= +0.05",
        "   • Neutral Sentiment:  -0.05 < Compound Score < +0.05",
        "   • Negative Sentiment: Compound Score <= -0.05",
        "Subjectivity Score (TextBlob):",
        "   • Measures 0.0 (Pure Objective Fact) to 1.0 (Personal Opinion)."
    ])
    slide7.notes_slide.notes_text_frame.text = (
        "The compound score provides a continuous, normalized metric that makes it easy to set clear thresholds."
    )

    # ------------------ SLIDE 8: BUSINESS METRICS & NSS ------------------
    slide8 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide8, "Business Intelligence & Net Sentiment Score (NSS)")
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "Net Sentiment Score (NSS)", [
        "NSS = (% Positive) - (% Negative)",
        "Ranges from -100% to +100%.",
        "Acts as a real-time social proxy for Net Promoter Score (NPS).",
        "Provides an instant benchmark for marketing campaigns."
    ])
    add_card(slide8, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "Cross-Platform Analysis", [
        "Compares customer satisfaction across Twitter, Reddit, and Instagram.",
        "Detects which platform hosts the most vocal complaints.",
        "Helps allocate customer support resources efficiently."
    ])
    add_card(slide8, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "Keyword Drivers", [
        "Extracts top distinct positive drivers (e.g. 'fast', 'sleek', 'loving').",
        "Identifies top complaint drivers (e.g. 'delayed', 'crashed', 'broken').",
        "Provides actionable takeaways for product teams."
    ])
    slide8.notes_slide.notes_text_frame.text = (
        "Net Sentiment Score translates individual sentiment scores into an executive KPI that leadership can track over time."
    )

    # ------------------ SLIDE 9: TECH STACK ------------------
    slide9 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide9, "Technology Stack & Repository Layout")
    add_card(slide9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Core Technologies", [
        "Python 3.10+: Core programming language with modular architecture.",
        "VADER Sentiment: Social-media-specific sentiment analysis engine.",
        "TextBlob: Subjectivity and polarity evaluation.",
        "Streamlit: Reactive web dashboard with live post tester.",
        "Plotly Express: Interactive donut charts, timelines, and bar graphs.",
        "Pandas & NumPy: Data manipulation and batch processing."
    ])
    add_card(slide9, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Repository Structure", [
        "src/preprocessor.py -> Social media cleaning & emoji handling",
        "src/sentiment.py    -> VADER & TextBlob sentiment engines",
        "src/insights.py     -> Net Sentiment Score (NSS) calculation",
        "app.py              -> Streamlit Web Dashboard",
        "cli.py              -> Headless batch processing CLI",
        "tests/              -> Automated test suite (unittest)",
        "data/               -> Realistic social feedback dataset"
    ])
    slide9.notes_slide.notes_text_frame.text = (
        "The project is engineered with a clean, modular structure following standard software engineering practices."
    )

    # ------------------ SLIDE 10: CONCLUSION & VIVA SUMMARY ------------------
    slide10 = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide10, "Conclusion & Project Outcomes")
    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Key Achievements", [
        "Built a fast, reliable sentiment analyzer tailored for social media.",
        "Solved informal language challenges (emojis, slang, capitalization).",
        "Delivered a live interactive web app and executive dashboard.",
        "Full unit test suite passing with 100% success rate.",
        "Open-source ready with comprehensive GitHub documentation."
    ])
    add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Future Scope", [
        "Live Social API Streaming: Connect directly to Twitter/X API v2 and Reddit PRAW.",
        "Multilingual Sentiment: Incorporate XLM-RoBERTa for 50+ languages.",
        "Aspect-Based Sentiment (ABSA): Sentence-level breakdown for multi-feature products.",
        "Auto-Reply Generator: LLM-powered response drafts for support teams."
    ])
    slide10.notes_slide.notes_text_frame.text = (
        "In conclusion, the Customer Feedback Sentiment Analyzer provides an effective, lightweight solution for social media analytics. Thank you, and I look forward to your questions."
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"Successfully generated PowerPoint presentation at: {output_path}")

if __name__ == "__main__":
    create_deck()
