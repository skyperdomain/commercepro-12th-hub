import json
import datetime

STUDY_POOL = [
    {
        "subject": "Business Studies",
        "topic": "Principles of Management — Scientific Management",
        "title": "Daily Case Study: Functional Foremanship",
        "content": "<p class='text-sm text-slate-600 dark:text-slate-300 mb-3'><strong>Case Scenario:</strong> Production Manager Rahul noticed low productivity due to lack of specialized supervision. Which technique of Taylor solves this issue?</p><div class='p-4 rounded-xl bg-violet-50 dark:bg-violet-950/50 border border-violet-200 text-sm space-y-1'><p class='font-bold text-violet-700 dark:text-violet-400'>Topper Answer:</p><p><strong>Functional Foremanship</strong>. Taylor proposed 8 specialized bosses to separate planning from execution.</p></div>"
    },
    {
        "subject": "Economics",
        "topic": "Macroeconomics — National Income Aggregates",
        "title": "Daily Numerical Focus: Real GDP vs Nominal GDP",
        "content": "<p class='text-sm text-slate-600 dark:text-slate-300 mb-3'><strong>Question:</strong> If Real GDP is ₹500 and Price Index (GDP Deflator) is 125, calculate Nominal GDP.</p><div class='p-4 rounded-xl bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-200 text-sm space-y-1'><p class='font-bold text-emerald-700 dark:text-emerald-400'>Formula & Calculation:</p><p>GDP Deflator = (Nominal GDP / Real GDP) × 100</p><p>125 = (Nominal GDP / 500) × 100  ➜  Nominal GDP = <strong>₹625</strong></p></div>"
    },
    {
        "subject": "Accountancy",
        "topic": "Company Accounts — Forfeiture of Shares",
        "title": "Daily Journal Entry Focus: Forfeiture at Premium",
        "content": "<p class='text-sm text-slate-600 dark:text-slate-300 mb-3'><strong>Rule Breakdown:</strong> When shares issued at a premium are forfeited and premium was NOT received, Securities Premium Account must be debited!</p><div class='p-4 rounded-xl bg-indigo-50 dark:bg-indigo-950/50 border border-indigo-200 text-sm font-mono text-xs space-y-1'><p>Share Capital A/c ... Dr (Called-up value)</p><p>Securities Premium A/c ... Dr (Unpaid premium)</p><p>&nbsp;&nbsp;To Share Forfeiture A/c (Amount received)</p><p>&nbsp;&nbsp;To Unpaid Calls A/c (Amount due)</p></div>"
    }
]

today_str = datetime.date.today().strftime("%Y-%m-%d")

try:
    with open('daily-content.json', 'r') as f:
        data = json.load(f)
except Exception:
    data = []

day_number = datetime.date.today().timetuple().tm_yday
selected_item = STUDY_POOL[day_number % len(STUDY_POOL)]

if not any(item.get('date') == today_str for item in data):
    new_entry = {
        "date": today_str,
        "subject": selected_item["subject"],
        "topic": selected_item["topic"],
        "title": selected_item["title"],
        "content": selected_item["content"]
    }
    data.append(new_entry)

    with open('daily-content.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Added daily content for {today_str}")
else:
    print(f"Content for {today_str} already exists.")