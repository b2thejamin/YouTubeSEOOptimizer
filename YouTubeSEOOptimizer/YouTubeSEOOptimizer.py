def get_category_rules():
    """
    Define rule-based keyword boosters and power words for each category.
    Returns a dictionary containing SEO rules for different video categories.
    """
    rules = {
        'gaming': {
            'power_words': ['INSANE', 'EPIC', 'ULTIMATE', 'BEST', 'PRO', 'CRAZY', 'LEGENDARY'],
            'hooks': ['Gameplay', 'Guide', 'Tips', 'Walkthrough', 'Tutorial', 'Review'],
            'keywords': [
                'gaming', 'gameplay', 'walkthrough', 'tutorial', 'guide', 'tips',
                'tricks', 'best moments', 'highlights', 'epic', 'funny moments',
                'pro player', 'strategy', 'build', 'meta', 'update', 'patch',
                'review', 'let\'s play', 'stream highlights', 'compilation'
            ],
            'description_intro': 'Welcome to this amazing gaming video! In this episode, we dive deep into',
            'cta': 'Don\'t forget to LIKE, SUBSCRIBE, and hit the BELL for more gaming content!'
        },
        'streaming': {
            'power_words': ['LIVE', 'VIRAL', 'TRENDING', 'EXCLUSIVE', 'REACT', 'SHOCKING'],
            'hooks': ['Stream Highlights', 'Best Moments', 'Clips', 'Reaction', 'Stream'],
            'keywords': [
                'stream', 'streaming', 'live', 'twitch', 'highlights', 'best moments',
                'clips', 'funny', 'reaction', 'chat', 'donation', 'subscriber',
                'emotes', 'streamer', 'gaming stream', 'irl stream', 'talk show',
                'q&a', 'community', 'subscriber special', 'charity stream'
            ],
            'description_intro': 'Check out these incredible moments from the stream! Today we',
            'cta': 'Follow the stream and join the community! Like and subscribe for daily highlights!'
        },
        'tech': {
            'power_words': ['NEW', 'REVOLUTIONARY', 'TESTED', 'HONEST', 'DETAILED', 'COMPLETE'],
            'hooks': ['Review', 'Unboxing', 'Comparison', 'Tutorial', 'Guide', 'Analysis'],
            'keywords': [
                'tech', 'technology', 'review', 'unboxing', 'tutorial', 'guide',
                'comparison', 'vs', 'specs', 'features', 'hands-on', 'first look',
                'analysis', 'benchmark', 'performance', 'setup', 'tips', 'tricks',
                'how to', 'explained', 'worth it', 'buy or skip', 'latest', 'new'
            ],
            'description_intro': 'In this tech video, we take a comprehensive look at',
            'cta': 'Subscribe for more tech reviews and tutorials! Drop your questions in the comments!'
        },
        'fitness': {
            'power_words': ['TRANSFORM', 'POWERFUL', 'EFFECTIVE', 'PROVEN', 'QUICK', 'INTENSE'],
            'hooks': ['Workout', 'Training', 'Exercise', 'Routine', 'Challenge', 'Tips'],
            'keywords': [
                'fitness', 'workout', 'exercise', 'training', 'gym', 'home workout',
                'bodybuilding', 'weight loss', 'muscle gain', 'cardio', 'strength',
                'routine', 'diet', 'nutrition', 'tips', 'motivation', 'transformation',
                'beginner', 'advanced', 'full body', 'abs', 'legs', 'arms', 'chest'
            ],
            'description_intro': 'Get ready for an amazing fitness journey! In this video, we cover',
            'cta': 'SUBSCRIBE for weekly workout videos! Share your progress in the comments!'
        },
        'general': {
            'power_words': ['AMAZING', 'MUST-SEE', 'INCREDIBLE', 'TOP', 'BEST', 'AWESOME'],
            'hooks': ['Guide', 'Tips', 'Tutorial', 'Review', 'How To', 'Explained'],
            'keywords': [
                'tutorial', 'guide', 'tips', 'tricks', 'how to', 'explained',
                'review', 'top', 'best', 'compilation', 'list', 'beginner',
                'advanced', 'complete', 'full', 'step by step', 'easy', 'quick',
                'detailed', 'ultimate', 'everything you need', 'comprehensive'
            ],
            'description_intro': 'Welcome! In this video, we explore',
            'cta': 'Like, Subscribe, and Comment your thoughts below! More content coming soon!'
        }
    }
    return rules


def clean_and_capitalize(text):
    """
    Clean and capitalize text for title formatting.
    Removes extra spaces and capitalizes properly.
    """
    # Remove extra spaces
    text = ' '.join(text.split())
    # Capitalize first letter of each word (title case)
    return text.title()


def optimize_title(base_title, category, rules):
    """
    Rule-based title optimization.
    Adds power words and hooks based on category rules.
    Ensures title stays under 70 characters for SEO.
    """
    # Clean the base title
    base_title = clean_and_capitalize(base_title)
    
    # Get category-specific rules
    if category in rules:
        power_words = rules[category]['power_words']
        hooks = rules[category]['hooks']
    else:
        # Default to general if category not found
        power_words = rules['general']['power_words']
        hooks = rules['general']['hooks']
    
    # Rule 1: Check if title already has a power word
    has_power_word = False
    for word in power_words:
        if word.lower() in base_title.lower():
            has_power_word = True
            break
    
    # Rule 2: Add power word if not present and space allows
    if not has_power_word:
        # Try to add a power word at the beginning
        for power_word in power_words:
            test_title = f"{power_word} {base_title}"
            if len(test_title) <= 70:
                base_title = test_title
                break
    
    # Rule 3: Check if title has a category hook
    has_hook = False
    for hook in hooks:
        if hook.lower() in base_title.lower():
            has_hook = True
            break
    
    # Rule 4: Try to add hook if not present and space allows
    if not has_hook and len(base_title) < 50:
        # Try to add hook at the end
        for hook in hooks:
            test_title = f"{base_title} - {hook}"
            if len(test_title) <= 70:
                base_title = test_title
                break
    
    # Rule 5: Ensure title doesn't exceed 70 characters
    if len(base_title) > 70:
        base_title = base_title[:67] + "..."
    
    return base_title


def generate_tags(base_title, category, rules):
    """
    Generate 15-30 relevant tags based on category and title.
    Uses rule-based keyword extraction and category boosters.
    """
    tags = []
    
    # Rule 1: Get category-specific keywords
    if category in rules:
        category_keywords = rules[category]['keywords'].copy()
    else:
        category_keywords = rules['general']['keywords'].copy()
    
    # Rule 2: Add the category itself as first tag
    tags.append(category)
    
    # Rule 3: Extract words from title (3+ characters)
    title_words = base_title.lower().split()
    for word in title_words:
        # Clean punctuation
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if len(cleaned_word) >= 3 and cleaned_word not in tags:
            tags.append(cleaned_word)
    
    # Rule 4: Add category-specific keywords
    for keyword in category_keywords:
        if keyword not in tags:
            tags.append(keyword)
        # Stop if we have enough tags
        if len(tags) >= 30:
            break
    
    # Rule 5: Generate phrase combinations from title
    if len(tags) < 20:
        for i in range(len(title_words) - 1):
            phrase = f"{title_words[i]} {title_words[i+1]}"
            cleaned_phrase = ''.join(char if char.isalnum() or char == ' ' else '' for char in phrase)
            if cleaned_phrase and cleaned_phrase not in tags:
                tags.append(cleaned_phrase)
            if len(tags) >= 30:
                break
    
    # Rule 6: Ensure we have at least 15 tags
    fallback_tags = ['video', 'youtube', 'content', 'new', 'latest', 'trending', 
                     'popular', 'viral', 'watch', 'subscribe', 'channel', 'entertainment',
                     'quality', 'hd', '2026']
    
    for tag in fallback_tags:
        if len(tags) >= 15:
            break
        if tag not in tags:
            tags.append(tag)
    
    return tags[:30]  # Return maximum 30 tags


def generate_description(title, category, rules):
    """
    Generate a starter description with introduction, timestamps, and call-to-action.
    Uses rule-based templates based on category.
    """
    description = ""
    
    # Rule 1: Add introduction based on category
    if category in rules:
        intro = rules[category]['description_intro']
        cta = rules[category]['cta']
    else:
        intro = rules['general']['description_intro']
        cta = rules['general']['cta']
    
    description += f"{intro} {title}.\n\n"
    
    # Rule 2: Add timestamp section
    description += "⏱️ TIMESTAMPS:\n"
    description += "0:00 - Introduction\n"
    description += "0:30 - Main Content\n"
    description += "5:00 - Key Points\n"
    description += "8:00 - Conclusion\n\n"
    
    # Rule 3: Add social media section
    description += "🔗 CONNECT WITH US:\n"
    description += "• Subscribe: [Your Channel Link]\n"
    description += "• Instagram: [Your Instagram]\n"
    description += "• Twitter: [Your Twitter]\n"
    description += "• Discord: [Your Discord]\n\n"
    
    # Rule 4: Add hashtags based on category
    description += "📌 HASHTAGS:\n"
    if category == 'gaming':
        description += "#Gaming #Gameplay #GamingCommunity #VideoGames\n\n"
    elif category == 'streaming':
        description += "#Stream #Streaming #LiveStream #StreamHighlights\n\n"
    elif category == 'tech':
        description += "#Tech #Technology #TechReview #Gadgets\n\n"
    elif category == 'fitness':
        description += "#Fitness #Workout #FitnessMotivation #Health\n\n"
    else:
        description += "#YouTube #Content #Video #Tutorial\n\n"
    
    # Rule 5: Add call-to-action
    description += f"💬 {cta}\n\n"
    
    # Rule 6: Add generic footer
    description += "---\n"
    description += f"© 2026 - All Rights Reserved\n"
    description += f"Video optimized for: {category.upper()}\n"
    
    return description


def display_results(title, tags, description):
    """
    Display the optimized results in a formatted manner.
    """
    print("\n" + "="*70)
    print("✅ OPTIMIZATION COMPLETE!")
    print("="*70)
    
    print(f"\n📺 OPTIMIZED TITLE ({len(title)} characters):")
    print(f"   {title}")
    
    print(f"\n🏷️  TAGS ({len(tags)} tags):")
    # Display tags in rows of 3
    for i in range(0, len(tags), 3):
        row_tags = tags[i:i+3]
        print(f"   {' | '.join(row_tags)}")
    
    print(f"\n📝 VIDEO DESCRIPTION STARTER:")
    print("-" * 70)
    # Display description with proper indentation
    for line in description.split('\n'):
        print(f"   {line}")
    print("-" * 70)


def get_user_input():
    """
    Get and validate user input for category and title.
    Returns tuple of (category, title) or None if user wants to quit.
    """
    print("\n" + "="*70)
    print("🎬 YOUTUBE SEO OPTIMIZER - RULE-BASED AI")
    print("="*70)
    print("\nAvailable categories: gaming, streaming, tech, fitness, general")
    print("Type 'quit' to exit the program.\n")
    
    # Get category
    category = input("Enter video category: ").strip().lower()
    
    # Rule: Check if user wants to quit
    if category == 'quit':
        return None
    
    # Rule: Validate category, default to 'general' if invalid
    valid_categories = ['gaming', 'streaming', 'tech', 'fitness', 'general']
    if category not in valid_categories:
        print(f"⚠️  Category '{category}' not recognized. Using 'general' instead.")
        category = 'general'
    
    # Get title
    title = input("Enter base title idea: ").strip()
    
    # Rule: Check if user wants to quit
    if title.lower() == 'quit':
        return None
    
    # Rule: Validate title is not empty
    if not title:
        print("⚠️  Title cannot be empty. Using default title.")
        title = "My Awesome Video"
    
    return category, title


def main():
    """
    Main program loop - handles user interaction and orchestrates optimization.
    """
    print("\n" + "*"*70)
    print("*" + " "*68 + "*")
    print("*" + "  YOUTUBE SEO OPTIMIZER - RULE-BASED AI SYSTEM".center(68) + "*")
    print("*" + "  Pure Python | No Machine Learning | Rule-Based Only".center(68) + "*")
    print("*" + " "*68 + "*")
    print("*"*70)
    
    # Load rule-based system
    rules = get_category_rules()
    
    # Main loop - continue until user types 'quit'
    while True:
        # Get user input
        user_input = get_user_input()
        
        # Rule: Exit if user wants to quit
        if user_input is None:
            print("\n👋 Thank you for using YouTube SEO Optimizer! Goodbye!")
            break
        
        category, base_title = user_input
        
        # Apply rule-based optimizations
        print("\n⚙️  Applying rule-based optimization...")
        
        # Step 1: Optimize title
        optimized_title = optimize_title(base_title, category, rules)
        
        # Step 2: Generate tags
        tags = generate_tags(base_title, category, rules)
        
        # Step 3: Generate description
        description = generate_description(optimized_title, category, rules)
        
        # Step 4: Display results
        display_results(optimized_title, tags, description)
        
        # Ask if user wants to optimize another video
        print("\n" + "="*70)
        continue_choice = input("\nOptimize another video? (yes/quit): ").strip().lower()
        if continue_choice == 'quit' or continue_choice == 'q' or continue_choice == 'no':
            print("\n👋 Thank you for using YouTube SEO Optimizer! Goodbye!")
            break


# Entry point - run the program
if __name__ == "__main__":
    main()