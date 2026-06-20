print("--- AI Recommendation Logic Engine Initialized ---")

# 1. Predefined database of items with matching feature tags
content_database = {
    "Advanced Python Programming": ["python", "coding", "software", "development"],
    "Machine Learning Foundations": ["ai", "machine learning", "data", "math"],
    "Web Development Bootcamp": ["html", "css", "javascript", "web design"],
    "Data Science and Analytics": ["data", "python", "statistics", "math"],
    "Introduction to Cloud Computing": ["cloud", "networking", "aws", "infrastructure"]
}

print("Welcome! Let us find the best resources for you.")
print("Available interest tags include: python, coding, ai, machine learning, data, web design, cloud, math\n")

# 2. Take user input for preferences
user_input = input("Enter your interests or skills (separated by commas): ")

# Clean up and split the user input into a clean list of lowercase terms
user_interests = []
for item in user_input.split(","):
    cleaned_term = item.lower().strip()
    if cleaned_term:  # Ensure it's not an empty string
        user_interests.append(cleaned_term)

print(f"\nSearching matches for your profile tags: {user_interests}")
print("-" * 50)

# 3. Match preferences using simple overlapping similarity logic
recommendations = []

for title, tags in content_database.items():
    match_count = 0
    # Check how many user interests overlap with the item's tags
    for interest in user_interests:
        if interest in tags:
            match_count = match_count + 1
            
    # If there is a match, keep track of the item and its score
    if match_count > 0:
        recommendations.append((title, match_count))

# Sort recommendations manually so the highest score comes first
# (Bubble sort style for basic human programming logic)
for i in range(len(recommendations)):
    for j in range(0, len(recommendations) - i - 1):
        if recommendations[j][1] < recommendations[j + 1][1]:
            # Swap items if the next one has a higher match score
            temp = recommendations[j]
            recommendations[j] = recommendations[j + 1]
            recommendations[j + 1] = temp

# 4. Display recommended items to the user
print("\n================ TOP RECOMMENDED FOR YOU ================")
if len(recommendations) == 0:
    print("No direct matches found. Try entering alternative tags next time!")
else:
    for index, (title, score) in enumerate(recommendations):
        print(f"{index + 1}. {title} (Match Score: {score})")
print("==========================================================")