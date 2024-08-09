"""
This script builds out a basic prompt folder structure taxonomy for housing a library of GPT prompts. The script creates 30 categories for storing prompts and each category contains 10 subcategories. The script is non-interactive - the user is not asked to dynamically set these or other parameters. The base_dir parameter should be manually configured for the base of the repository housing the prompt library
"""

import os

categories_and_subcategories = {
    "Technology": ["Linux", "AI", "Cybersecurity", "Cloud Computing", "Networking", "Blockchain", "Programming Languages", "Mobile Development", "DevOps", "Virtualization"],
    "Health and Wellness": ["Nutrition", "Mental Health", "Fitness", "Sleep", "Yoga", "Meditation", "Stress Management", "Diet", "Weight Loss", "Healthy Eating"],
    "Business Strategy": ["Market Analysis", "Competitive Strategy", "Business Planning", "SWOT Analysis", "Risk Management", "Financial Strategy", "Operational Strategy", "Innovation", "Growth Strategy", "Product Development"],
    "Creative Writing": ["Fiction", "Non-fiction", "Poetry", "Screenwriting", "Playwriting", "Character Development", "Plot Development", "Worldbuilding", "Dialogue", "Short Stories"],
    "Marketing": ["SEO", "Content Marketing", "Email Marketing", "Social Media", "Branding", "Market Research", "Advertising", "Public Relations", "Customer Experience", "Influencer Marketing"],
    "Personal Development": ["Time Management", "Goal Setting", "Mindfulness", "Public Speaking", "Self-Discipline", "Productivity", "Leadership", "Confidence Building", "Resilience", "Emotional Intelligence"],
    "Education": ["Teaching Strategies", "Curriculum Development", "Learning Styles", "Educational Psychology", "Assessment Techniques", "Classroom Management", "Online Learning", "Special Education", "Early Childhood Education", "STEM Education"],
    "Finance": ["Personal Finance", "Investing", "Retirement Planning", "Budgeting", "Tax Planning", "Insurance", "Real Estate", "Stock Market", "Cryptocurrency", "Financial Analysis"],
    "Programming": ["Python", "JavaScript", "Java", "C++", "Ruby", "PHP", "R", "Go", "Swift", "Kotlin"],
    "Design": ["Graphic Design", "UI/UX Design", "Web Design", "Logo Design", "Typography", "Color Theory", "Illustration", "Animation", "3D Modeling", "Interior Design"],
    "Science": ["Physics", "Chemistry", "Biology", "Astronomy", "Geology", "Ecology", "Genetics", "Environmental Science", "Meteorology", "Oceanography"],
    "History": ["Ancient History", "Medieval History", "Modern History", "American History", "European History", "Asian History", "African History", "Middle Eastern History", "World Wars", "Historical Figures"],
    "Literature": ["Classic Literature", "Modern Literature", "Poetry", "Drama", "Science Fiction", "Fantasy", "Mystery", "Romance", "Literary Criticism", "Non-fiction"],
    "Music": ["Music Theory", "Composition", "Instrumental", "Vocal", "Genres", "Music History", "Music Production", "Songwriting", "Music Technology", "Music Education"],
    "Art": ["Painting", "Sculpture", "Drawing", "Photography", "Printmaking", "Digital Art", "Art History", "Art Criticism", "Mixed Media", "Ceramics"],
    "Travel": ["Destinations", "Travel Planning", "Cultural Experiences", "Adventure Travel", "Budget Travel", "Travel Photography", "Solo Travel", "Family Travel", "Eco-Tourism", "Luxury Travel"],
    "Food and Cooking": ["Recipes", "Baking", "Grilling", "Vegetarian", "Vegan", "World Cuisines", "Healthy Cooking", "Meal Planning", "Food Photography", "Cooking Techniques"],
    "Sports": ["Football", "Basketball", "Baseball", "Tennis", "Golf", "Soccer", "Swimming", "Cycling", "Running", "Martial Arts"],
    "Language Learning": ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Italian", "Russian", "Arabic", "Portuguese"],
    "Gaming": ["Video Games", "Board Games", "Esports", "Game Development", "VR Gaming", "Gaming Culture", "Retro Gaming", "RPGs", "Strategy Games", "Simulation Games"],
    "Photography": ["Portrait Photography", "Landscape Photography", "Wildlife Photography", "Street Photography", "Macro Photography", "Astrophotography", "Black and White Photography", "Wedding Photography", "Travel Photography", "Photography Techniques"],
    "Movies and TV": ["Film Genres", "Directors", "Actors", "TV Shows", "Documentaries", "Film History", "Screenwriting", "Film Production", "Film Criticism", "Cinematography"],
    "Psychology": ["Cognitive Psychology", "Developmental Psychology", "Behavioral Psychology", "Social Psychology", "Clinical Psychology", "Personality Psychology", "Psychotherapy", "Neuropsychology", "Psychological Disorders", "Positive Psychology"],
    "Environment": ["Climate Change", "Sustainability", "Conservation", "Renewable Energy", "Pollution", "Recycling", "Environmental Policy", "Biodiversity", "Natural Resources", "Green Technology"],
    "Politics": ["Political Theory", "International Relations", "Political History", "Government Systems", "Elections", "Public Policy", "Political Movements", "Political Parties", "Human Rights", "Globalization"],
    "Economics": ["Microeconomics", "Macroeconomics", "Econometrics", "Behavioral Economics", "Development Economics", "International Economics", "Economic Policy", "Labor Economics", "Financial Economics", "Environmental Economics"],
    "Law": ["Criminal Law", "Civil Law", "Constitutional Law", "International Law", "Corporate Law", "Environmental Law", "Human Rights Law", "Intellectual Property", "Family Law", "Employment Law"],
    "Philosophy": ["Ethics", "Metaphysics", "Epistemology", "Logic", "Aesthetics", "Philosophy of Science", "Political Philosophy", "Philosophy of Mind", "Existentialism", "Ancient Philosophy"],
    "Religion": ["Christianity", "Islam", "Judaism", "Buddhism", "Hinduism", "Sikhism", "Religious History", "Religious Philosophy", "Comparative Religion", "Religious Practices"],
    "Crafts and DIY": ["Knitting", "Crocheting", "Woodworking", "Jewelry Making", "Sewing", "Paper Crafts", "Painting", "Home Improvement", "Gardening", "Upcycling"]
}

base_dir = "GPT_Prompt_Library"
os.makedirs(base_dir, exist_ok=True)

for category, subcategories in categories_and_subcategories.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)
    
    for subcategory in subcategories:
        subcategory_path = os.path.join(category_path, subcategory)
        os.makedirs(subcategory_path, exist_ok=True)

print("Folder structure created successfully!")
