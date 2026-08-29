import pandas as pd

#ques 1
roll_no = "01024160001"

# Fixed FAQ entries
faq_data = [
    {
        "category": "account",
        "question": "How do I reset my password?",
        "answer": "Click on 'Forgot Password' on the login page and follow the instructions.",
        "keywords": ["password", "reset", "login"]
    },
    {
        "category": "billing",
        "question": "How can I download my invoice?",
        "answer": "You can download your invoice from the Billing section of your account.",
        "keywords": ["invoice", "billing", "download"]
    },
    {
        "category": "general",
        "question": "How can I contact customer support?",
        "answer": "You can contact customer support through the Help or Support section.",
        "keywords": ["support", "help", "contact"]
    },
    {
        "category": "account",
        "question": "How do I update my registered email address?",
        "answer": "Go to Account Settings and update your email address under Profile Information.",
        "keywords": ["email", "account", "profile"]
    }
]

# Get last two digits
last_two_digits = [int(d) for d in roll_no[-2:]]

categories = ["billing", "account", "general"]

# Create 2 personalized FAQ entries
for d in last_two_digits:
    category = categories[d % 3]

    if category == "billing":
        question = "How can I update my billing information?"
        answer = "Open the Billing section in your account and update your payment details."
        keywords = ["billing", "payment", "details"]

    elif category == "account":
        question = "How do I update my registered mobile number?"
        answer = "Go to Account Settings and replace your existing mobile number with the new one."
        keywords = ["mobile", "account", "profile"]

    else:
        question = "How can I change my notification preferences?"
        answer = "Open Settings and select your preferred notification options."
        keywords = ["notifications", "settings", "preferences"]

    faq_data.append({
        "category": category,
        "question": question,
        "answer": answer,
        "keywords": keywords
    })


df = pd.DataFrame(faq_data)

print(df)

#ques 2
def score_hypothesis(query, df):
    query_words = set(query.lower().split())
    results = []

    for _, row in df.iterrows():
        question_words = set(row["question"].lower().split())
        keyword_words = set(k.lower() for k in row["keywords"])

        # Match query words with question and keywords
        question_matches = query_words.intersection(question_words)
        keyword_matches = query_words.intersection(keyword_words)

        # Calculate score
        score = (
            len(question_matches) * 0.3 +
            len(keyword_matches) * 0.7
        )

        if score > 0:
            results.append({
                "category": row["category"],
                "question": row["question"],
                "answer": row["answer"],
                "confidence": round(score, 2)
            })

    # Rank by confidence (highest first)
    results.sort(key=lambda x: x["confidence"], reverse=True)

    return pd.DataFrame(results)


# Example queries
query = "How do I update my mobile number?"

results = score_hypothesis(query, df)

print(results)


#ques 3
def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]


# Call the function using the category of one personalized entry
category_name = df.iloc[4]["category"]

result = same_category(category_name, df)

print("Category:", category_name)
print("Questions belonging to this category:")
print(result)


#ques 4
# Roll number configuration
roll_number = "1024160001"

# Pick the first entry (index 0) and define the new keyword directly
entry_index = 0
new_keyword = "yearly"

# Append the new keyword to entry 0's existing keywords
df.loc[entry_index, "keywords"] += f" {new_keyword}"

# Save the updated DataFrame to CSV with your roll number
file_name = f"{roll_number}_faq_data.csv"
df.to_csv(file_name, index=False)

# Display result
print(f"Updated entry {entry_index} keywords: {df.loc[entry_index, 'keywords']}")
print(f"File saved as: {file_name}")


#ques 5
category_counts = df.groupby("category").size()
print(category_counts)

#ques 6
def score_query_with_ties(query: str, faq_df: pd.DataFrame) -> pd.DataFrame:
    ranked = score_query(query, faq_df)
    
    if ranked.empty:
        print(f"No match found for query: '{query}'")
        return ranked
    
    max_score = ranked["score"].max()
    top_matches = ranked[ranked["score"] == max_score]
    
    if len(top_matches) > 1:
        print(f"Tie detected! {len(top_matches)} entries matched with score {max_score}:")
    else:
        print(f"Single best match with score {max_score}:")
        
    return top_matches[["question", "category", "score"]]

# Demonstration 1: Query producing a tie (matches both fee entries)
print("--- Query with Tie ---")
print(score_query_with_ties("fee", df))

# Demonstration 2: Query producing a single top match
print("\n--- Query without Tie ---")
print(score_query_with_ties("reset password", df))

