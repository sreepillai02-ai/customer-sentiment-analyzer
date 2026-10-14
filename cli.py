"""
Command Line Interface (CLI) runner for batch sentiment analysis.
Processes customer feedback datasets with VADER sentiment engine.
"""

import argparse
import sys
import os
import io
import pandas as pd

# Ensure Windows terminal can print unicode safely
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from src.preprocessor import clean_social_text
from src.sentiment import SentimentAnalyzer
from src.insights import generate_sentiment_insights

def main():
    parser = argparse.ArgumentParser(description="SocialSense - Customer Feedback Sentiment CLI")
    parser.add_argument("--input", "-i", type=str, default="data/sample_social_feedback.csv", help="Path to input CSV or Excel file")
    parser.add_argument("--output", "-o", type=str, default="output_sentiment_results.csv", help="Path to output CSV file")
    parser.add_argument("--text-col", "-t", type=str, default="feedback_text", help="Column name containing text/review")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)

    print(f"\n[1/3] Loading input dataset from {args.input}...")
    if args.input.endswith(".xlsx") or args.input.endswith(".xls"):
        df = pd.read_excel(args.input)
    else:
        df = pd.read_csv(args.input)

    if args.text_col not in df.columns:
        candidates = [c for c in df.columns if any(k in c.lower() for k in ["text", "feedback", "review", "tweet"])]
        if candidates:
            args.text_col = candidates[0]
            print(f"Notice: Using column '{args.text_col}'")
        else:
            args.text_col = df.columns[0]
            print(f"Notice: Defaulting to first column '{args.text_col}'")

    print(f"[2/3] Running social cleaning & VADER sentiment analysis on {len(df)} records...")
    analyzer = SentimentAnalyzer()
    cleaned = [clean_social_text(str(t)) for t in df[args.text_col]]
    sentiments = analyzer.analyze_batch(df[args.text_col].astype(str).tolist())

    df['cleaned_text'] = cleaned
    df['sentiment_label'] = [s['label'] for s in sentiments]
    df['compound_score'] = [s['compound'] for s in sentiments]
    df['pos_score'] = [s['pos'] for s in sentiments]
    df['neu_score'] = [s['neu'] for s in sentiments]
    df['neg_score'] = [s['neg'] for s in sentiments]
    df['subjectivity'] = [s['subjectivity'] for s in sentiments]
    df['confidence'] = [s['confidence'] for s in sentiments]

    # Generate insights
    insights = generate_sentiment_insights(df)
    print("\n" + "="*52)
    print("        CUSTOMER SENTIMENT EXECUTIVE SUMMARY        ")
    print("="*52)
    print(f"Total Feedback Analyzed:   {insights['total_reviews']}")
    print(f"Net Sentiment Score (NSS):  {insights['net_sentiment_score']}%")
    print(f"Positive Sentiment:        {insights['positive_pct']}%")
    print(f"Neutral Sentiment:         {insights['neutral_pct']}%")
    print(f"Negative Sentiment:        {insights['negative_pct']}%")
    print(f"Average Compound Score:    {insights['avg_compound']} (-1.0 to +1.0)")
    print("-"*52)
    for action in insights['action_items']:
        clean_action = action.encode('ascii', errors='replace').decode('ascii')
        print(f" * {clean_action}")
    print("="*52)

    print(f"\n[3/3] Saving detailed output to {args.output}...")
    df.to_csv(args.output, index=False)
    print("Done! Sentiment analysis completed successfully.\n")

if __name__ == "__main__":
    main()
