"""
SocialSense: Customer Feedback Sentiment Analyzer in Social Media Analytics
Interactive Web Application Dashboard with Executive Metrics, Live Post Analyzer, and Basic Guidance.
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from src.preprocessor import clean_social_text
from src.sentiment import SentimentAnalyzer
from src.insights import generate_sentiment_insights

# Configure Streamlit page settings
st.set_page_config(
    page_title="SocialSense - Customer Sentiment Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Cache analyzer for fast re-renders
@st.cache_resource
def get_sentiment_analyzer():
    return SentimentAnalyzer()

@st.cache_data
def load_default_data():
    sample_path = os.path.join("data", "sample_social_feedback.csv")
    if os.path.exists(sample_path):
        return pd.read_csv(sample_path)
    return pd.DataFrame()

sentiment_analyzer = get_sentiment_analyzer()

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/analytics.png", width=90)
    st.markdown("## **SocialSense**")
    st.caption("Customer Feedback Sentiment Analytics")
    st.divider()

    # Data Source Selection
    st.markdown("### 📁 Data Source")
    data_option = st.radio(
        "Select Input Source:",
        ["Built-in Sample Social Data", "Upload CSV / Excel File"],
        index=0
    )

    df_raw = None
    if data_option == "Built-in Sample Social Data":
        df_raw = load_default_data()
        st.success(f"Loaded {len(df_raw)} sample social media posts.")
    else:
        uploaded_file = st.file_uploader("Upload feedback file", type=["csv", "xlsx"])
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df_raw = pd.read_csv(uploaded_file)
                else:
                    df_raw = pd.read_excel(uploaded_file)
                st.success(f"Uploaded {len(df_raw)} records.")
            except Exception as e:
                st.error(f"Error reading file: {e}")

    st.divider()
    st.markdown("### ℹ️ Engine Details")
    st.markdown("""
    - **Model**: VADER (*Valence Aware Dictionary and sEntiment Reasoner*)
    - **Subjectivity**: TextBlob Polarity
    - **Valence Range**: -1.0 to +1.0
    - **Thresholds**:
      - Positive: $\ge +0.05$
      - Neutral: $-0.05$ to $+0.05$
      - Negative: $\le -0.05$
    """)

# --- MAIN DASHBOARD HEADER ---
st.markdown('<div class="main-title">💬 Customer Feedback Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Mining real-time customer sentiment, emotion valence, and brand health metrics across social media channels.</div>', unsafe_allow_html=True)

# Navigation Tabs
tab_overview, tab_single, tab_data, tab_about = st.tabs([
    "📊 Executive Sentiment Dashboard", 
    "⚡ Real-Time Post Analyzer", 
    "📋 Data Explorer", 
    "📖 How to Use (Basic Guide)"
])

# Process Batch Data if available
if df_raw is not None and not df_raw.empty:
    text_column_candidates = [c for c in df_raw.columns if any(k in c.lower() for k in ["feedback", "text", "tweet", "review", "comment", "content"])]
    text_col = text_column_candidates[0] if text_column_candidates else df_raw.columns[0]

    with st.spinner("Analyzing sentiments across social posts..."):
        cleaned_texts = [clean_social_text(str(t)) for t in df_raw[text_col]]
        sentiment_results = sentiment_analyzer.analyze_batch(df_raw[text_col].astype(str).tolist())
        
        df_analyzed = df_raw.copy()
        df_analyzed['cleaned_text'] = cleaned_texts
        df_analyzed['sentiment_label'] = [s['label'] for s in sentiment_results]
        df_analyzed['compound_score'] = [s['compound'] for s in sentiment_results]
        df_analyzed['subjectivity'] = [s['subjectivity'] for s in sentiment_results]
        df_analyzed['pos_score'] = [s['pos'] for s in sentiment_results]
        df_analyzed['neu_score'] = [s['neu'] for s in sentiment_results]
        df_analyzed['neg_score'] = [s['neg'] for s in sentiment_results]
        df_analyzed['confidence'] = [s['confidence'] for s in sentiment_results]

        insights = generate_sentiment_insights(df_analyzed)

    color_map = {'Positive': '#22C55E', 'Neutral': '#94A3B8', 'Negative': '#EF4444'}

    # ================= TAB 1: EXECUTIVE DASHBOARD =================
    with tab_overview:
        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
        kpi1.metric("Total Social Posts", f"{len(df_analyzed):,}")
        kpi2.metric(
            "Net Sentiment (NSS)", 
            f"{insights['net_sentiment_score']}%", 
            delta=f"{insights['net_sentiment_score']}%",
            delta_color="normal" if insights['net_sentiment_score'] >= 0 else "inverse"
        )
        kpi3.metric("Positive Sentiment", f"{insights['positive_pct']}%", "👍")
        kpi4.metric("Neutral Sentiment", f"{insights['neutral_pct']}%", "😐")
        kpi5.metric("Negative Sentiment", f"{insights['negative_pct']}%", "👎")

        # Business Insights Alerts
        st.markdown("#### 💡 Key Sentiment Takeaways")
        insight_cols = st.columns(len(insights['action_items']))
        for i, item in enumerate(insights['action_items']):
            with insight_cols[i % len(insight_cols)]:
                st.info(item)

        st.markdown("---")

        # Visualizations Row
        col_c1, col_c2 = st.columns([1, 1])

        with col_c1:
            st.markdown("##### 🍩 Overall Sentiment Distribution")
            fig_pie = px.pie(
                df_analyzed, 
                names='sentiment_label', 
                color='sentiment_label',
                color_discrete_map=color_map,
                hole=0.45
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False, height=340)
            st.plotly_chart(fig_pie, use_container_width=True)

        with col_c2:
            st.markdown("##### 🌐 Sentiment by Social Channel")
            if 'platform' in df_analyzed.columns:
                plat_sent = df_analyzed.groupby(['platform', 'sentiment_label']).size().reset_index(name='count')
                fig_bar = px.bar(
                    plat_sent,
                    x='platform',
                    y='count',
                    color='sentiment_label',
                    barmode='group',
                    color_discrete_map=color_map,
                    labels={'platform': 'Social Platform', 'count': 'Post Count', 'sentiment_label': 'Sentiment'}
                )
                fig_bar.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=340)
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.write("Upload a dataset with a 'platform' column to view channel breakdown.")

        # Row 2: Timeline & Top Sentiment Keywords
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("##### 📅 Sentiment Compound Score Trend")
            if 'date' in df_analyzed.columns:
                df_time = df_analyzed.copy()
                df_time['date'] = pd.to_datetime(df_time['date'], errors='coerce')
                df_time = df_time.dropna(subset=['date']).sort_values('date')
                df_time_agg = df_time.groupby('date')['compound_score'].mean().reset_index()
                
                fig_time = px.line(
                    df_time_agg, 
                    x='date', 
                    y='compound_score', 
                    markers=True,
                    labels={'compound_score': 'Avg Valence (-1 to +1)', 'date': 'Date'}
                )
                fig_time.add_hline(y=0.0, line_dash="dash", line_color="grey")
                fig_time.update_layout(height=300, margin=dict(t=10, b=10, l=10, r=10))
                st.plotly_chart(fig_time, use_container_width=True)
            else:
                st.write("Add a 'date' column to visualize sentiment timeline.")

        with col_t2:
            st.markdown("##### 🔑 Top Distinctive Keywords")
            k_col1, k_col2 = st.columns(2)
            with k_col1:
                st.markdown("**🟢 Positive Drivers**")
                for w in insights['top_positive_words']:
                    st.markdown(f"- `{w}`")
            with k_col2:
                st.markdown("**🔴 Negative Complaints**")
                for w in insights['top_negative_words']:
                    st.markdown(f"- `{w}`")

    # ================= TAB 3: DATA EXPLORER =================
    with tab_data:
        st.markdown("#### 📋 Analyzed Customer Feedback Records")
        
        f1, f2, f3 = st.columns(3)
        with f1:
            sent_filter = st.multiselect("Filter by Sentiment", options=df_analyzed['sentiment_label'].unique(), default=list(df_analyzed['sentiment_label'].unique()))
        with f2:
            plat_options = df_analyzed['platform'].unique() if 'platform' in df_analyzed.columns else []
            plat_filter = st.multiselect("Filter by Platform", options=plat_options, default=list(plat_options))
        with f3:
            search_query = st.text_input("Search feedback text", "")

        df_filtered = df_analyzed[df_analyzed['sentiment_label'].isin(sent_filter)]
        if 'platform' in df_analyzed.columns and plat_filter:
            df_filtered = df_filtered[df_filtered['platform'].isin(plat_filter)]

        if search_query:
            df_filtered = df_filtered[df_filtered[text_col].str.contains(search_query, case=False, na=False)]

        display_cols = [text_col, 'sentiment_label', 'compound_score', 'subjectivity', 'confidence']
        if 'platform' in df_analyzed.columns:
            display_cols.insert(1, 'platform')

        st.dataframe(df_filtered[display_cols], use_container_width=True, height=380)

        csv_data = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Analyzed Sentiment Data as CSV",
            data=csv_data,
            file_name="social_feedback_sentiment_results.csv",
            mime="text/csv"
        )

# ================= TAB 2: REAL-TIME SINGLE POST ANALYZER =================
with tab_single:
    st.markdown("#### ⚡ Real-Time Social Media Post Analyzer")
    st.caption("Paste any tweet, comment, or review to instantly analyze emotional valence, emoji intensity, and subjectivity.")

    sample_post = st.selectbox(
        "Or try a ready-made sample:",
        [
            "Select a sample post or write your own...",
            "Ordered 5 days ago and still no tracking info! Customer support is completely unresponsive 😡📦",
            "Obsessed with this product! Incredible build quality, premium packaging, and fast delivery ✨🚀",
            "Does anyone know if this service includes cloud backups or is that an extra monthly fee?",
            "Battery died after just 2 weeks of light usage. Defective unit, extremely disappointed with this purchase."
        ]
    )

    default_text = "" if sample_post.startswith("Select a sample") else sample_post
    user_input = st.text_area("Social Media Feedback Text:", value=default_text, height=110, placeholder="E.g., Loving the speedy delivery, but customer support took 2 hours to answer!")

    if st.button("🚀 Analyze Post", type="primary") or user_input:
        if user_input.strip():
            res = sentiment_analyzer.analyze_single(user_input)

            st.markdown("---")
            res_c1, res_c2, res_c3, res_c4 = st.columns(4)
            badge_color = "#22C55E" if res['label'] == "Positive" else ("#EF4444" if res['label'] == "Negative" else "#94A3B8")
            
            with res_c1:
                st.markdown(f"### Sentiment: <span style='color:{badge_color}'>{res['label']}</span>", unsafe_allow_html=True)
                st.caption(f"Confidence: {res['confidence'] * 100:.1f}%")

            with res_c2:
                st.metric("Compound Score", f"{res['compound']}", delta=f"{res['compound']}")
                st.caption("Range: -1.0 (Most Negative) to +1.0 (Most Positive)")

            with res_c3:
                st.metric("Subjectivity", f"{res['subjectivity'] * 100:.1f}%")
                st.caption("0% = Pure Fact, 100% = Pure Opinion")

            with res_c4:
                dominant_comp = "Positive" if res['pos'] > res['neg'] else ("Negative" if res['neg'] > res['pos'] else "Neutral")
                st.metric("Dominant Valence", dominant_comp)
                st.caption("Based on word & emoji weights")

            # Score details & Gauge
            g1, g2 = st.columns([1, 1])
            with g1:
                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=res['compound'],
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Sentiment Gauge (-1.0 to +1.0)"},
                    gauge={
                        'axis': {'range': [-1, 1]},
                        'bar': {'color': badge_color},
                        'steps': [
                            {'range': [-1, -0.05], 'color': "#FEE2E2"},
                            {'range': [-0.05, 0.05], 'color': "#F1F5F9"},
                            {'range': [0.05, 1], 'color': "#DCFCE7"}
                        ],
                    }
                ))
                fig_gauge.update_layout(height=260, margin=dict(t=30, b=10, l=20, r=20))
                st.plotly_chart(fig_gauge, use_container_width=True)

            with g2:
                st.markdown("##### 🧩 Text & Valence Decomposition")
                st.write(f"**Cleaned Text:** `{clean_social_text(user_input)}`")
                st.write(f"**Positive Component:** `{res['pos']}`")
                st.write(f"**Neutral Component:** `{res['neu']}`")
                st.write(f"**Negative Component:** `{res['neg']}`")
        else:
            st.warning("Please enter some text to analyze.")

# ================= TAB 4: HOW TO USE (BASIC & SIMPLE GUIDE) =================
with tab_about:
    st.markdown("### 📖 How to Use This Website: Simple Step-by-Step Guide")
    st.write("Here is how to use the website in 4 easy steps:")

    # Step 1
    with st.container(border=True):
        st.markdown("#### 1️⃣ Step 1: Look at the Left Sidebar")
        st.markdown("""
        - The website automatically loads **30 sample customer reviews** (from Twitter, Reddit, Instagram, and Facebook).
        - If you want to test your own file, select **'Upload CSV / Excel File'** and choose your spreadsheet.
        """)

    # Step 2
    with st.container(border=True):
        st.markdown("#### 2️⃣ Step 2: View the Dashboard (Tab 1)")
        st.markdown("""
        - Look at the top numbers to see:
          - **Total Posts Analyzed**
          - **Net Sentiment Score (NSS)**: Shows if customers are mostly happy (Positive %) or mostly complaining (Negative %).
        - Look at the **Donut Chart** to see the percentage of Positive (Green), Neutral (Grey), and Negative (Red) reviews.
        - Check the **Channel Bar Chart** to see which platform (like Twitter or Instagram) has the most complaints.
        """)

    # Step 3
    with st.container(border=True):
        st.markdown("#### 3️⃣ Step 3: Test Any Sentence Live (Tab 2)")
        st.markdown("""
        - Click on the **'⚡ Real-Time Post Analyzer'** tab.
        - Type any review or customer comment in the box (e.g. *"Great product, loved it! 🚀"*).
        - Click **'🚀 Analyze Post'**.
        - The website immediately shows:
          - Whether it is **Positive 😊**, **Negative 😡**, or **Neutral 😐**.
          - A colorful **Speedometer Gauge** showing how positive or negative the sentence is.
        """)

    # Step 4
    with st.container(border=True):
        st.markdown("#### 4️⃣ Step 4: Search & Download Data (Tab 3)")
        st.markdown("""
        - Click on the **'📋 Data Explorer'** tab.
        - You can filter by sentiment (e.g., view only negative complaints).
        - Type in the search box to find specific words like *"delivery"* or *"battery"*.
        - Click **'📥 Download Analyzed Sentiment Data as CSV'** to save the results to your computer.
        """)

    # Quick Presentation Downloads
    st.markdown("---")
    st.markdown("#### 📥 Download Presentation Slides")
    st.caption("You can download the presentation slides for your project presentation / viva below:")
    
    col_dl1, col_dl2 = st.columns(2)
    ppt_path = os.path.join("presentation", "Social_Media_Sentiment_Topic_Analysis_Presentation.pptx")
    pdf_path = os.path.join("presentation", "Social_Media_Sentiment_Topic_Analysis_Presentation.pdf")
    
    with col_dl1:
        if os.path.exists(ppt_path):
            with open(ppt_path, "rb") as f:
                st.download_button(
                    label="📥 Download Presentation (.pptx)",
                    data=f.read(),
                    file_name="Social_Media_Sentiment_Analysis_Presentation.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True
                )
        else:
            st.write("Run `generate_ppt.bat` to build the PPTX file.")

    with col_dl2:
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download Presentation (.pdf)",
                    data=f.read(),
                    file_name="Social_Media_Sentiment_Analysis_Presentation.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.write("Run `generate_pdf.bat` to build the PDF file.")
