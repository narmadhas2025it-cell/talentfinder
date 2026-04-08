# ---------------- TALENT FINDER APPLICATION ---------------- #

# ---------------- Personality Database ---------------- #

personality_data = {
    "Creative": {
        "strength": "Imaginative, Artistic, Innovative thinker",
        "weakness": "May lack consistency, Easily distracted",
        "careers": ["Graphic Designer", "Content Creator", "Animator"],
        "books": ["Steal Like an Artist", "Big Magic"],
        "platforms": ["Skillshare", "YouTube"]
    },

    "Analytical": {
        "strength": "Logical, Problem solver, Detail oriented",
        "weakness": "Overthinking, Less emotional expression",
        "careers": ["Data Scientist", "Engineer", "Researcher"],
        "books": ["Deep Work", "Atomic Habits"],
        "platforms": ["Coursera", "Kaggle"]
    },

    "Leader": {
        "strength": "Confident, Decision maker, Risk taker",
        "weakness": "Impatient, Dominating sometimes",
        "careers": ["Entrepreneur", "Manager", "Civil Services"],
        "books": ["Start With Why", "Rich Dad Poor Dad"],
        "platforms": ["Udemy", "LinkedIn Learning"]
    },

    "Disciplined": {
        "strength": "Consistent, Focused, Self-controlled",
        "weakness": "May become rigid, Too serious",
        "careers": ["Civil Services", "Defense Officer", "Project Manager"],
        "books": ["The Power of Discipline", "Atomic Habits"],
        "platforms": ["Coursera", "Udemy"]
    },

    "Emotionally Intelligent": {
        "strength": "Empathetic, Good listener, Self-aware",
        "weakness": "Sensitive at times, Over caring",
        "careers": ["Psychologist", "HR Manager", "Counselor"],
        "books": ["Emotional Intelligence 2.0", "The 7 Habits of Highly Effective People"],
        "platforms": ["LinkedIn Learning", "Udemy"]
    },

    "Adaptable": {
        "strength": "Flexible, Learns quickly, Handles change well",
        "weakness": "May lack long-term direction",
        "careers": ["Startup Founder", "Consultant", "Freelancer"],
        "books": ["Who Moved My Cheese", "Mindset"],
        "platforms": ["Skillshare", "YouTube"]
    }
}

# ---------------- Hobby & Subject Career Mapping ---------------- #

hobby_career_map = {
    "drawing": {
        "careers": ["Graphic Designer", "Animator", "Illustrator", "Art Teacher"],
        "books": ["Drawing on the Right Side of the Brain", "Figure Drawing for All It's Worth"],
        "platforms": ["Skillshare", "YouTube", "DeviantArt", "Behance"]
    },
    "sketching": {
        "careers": ["Illustrator", "Storyboard Artist", "Concept Designer"],
        "books": ["Sketching from the Imagination", "Keys to Drawing"],
        "platforms": ["DeviantArt", "Behance", "Instagram Art"]
    },
    "painting": {
        "careers": ["Painter", "Art Teacher", "Gallery Curator"],
        "books": ["The Oil Painting Book", "Watercolor Techniques"],
        "platforms": ["Skillshare", "YouTube Painting", "Pinterest"]
    },
    "calligraphy": {
        "careers": ["Calligrapher", "Designer", "Wedding Stationery Artist"],
        "books": ["Modern Calligraphy", "Mastering Copperplate Calligraphy"],
        "platforms": ["Instagram Calligraphy", "YouTube Tutorials", "Skillshare"]
    },
    "graffiti art": {
        "careers": ["Street Artist", "Muralist", "Urban Designer"],
        "books": ["Graffiti World", "Subway Art"],
        "platforms": ["Instagram Street Art", "YouTube Graffiti", "Pinterest"]
    },
    "sculpting": {
        "careers": ["Sculptor", "Museum Artist", "3D Modeler"],
        "books": ["Modeling the Figure in Clay", "Sculpture Techniques"],
        "platforms": ["YouTube Sculpting", "ArtStation", "Skillshare"]
    },
    "beatboxing": {
        "careers": ["Beatboxer", "Music Performer", "Content Creator"],
        "books": ["The Beatbox Bible"],
        "platforms": ["YouTube Beatboxing", "TikTok", "Instagram Music"]
    },
    "acting": {
        "careers": ["Actor", "Voice Actor", "Drama Teacher"],
        "books": ["An Actor Prepares", "Respect for Acting"],
        "platforms": ["YouTube Acting Tutorials", "IMDB", "Stage32"]
    },


    "pottery": {
        "careers": ["Ceramic Artist", "Pottery Instructor", "Craft Entrepreneur"],
        "books": ["The Pottery Handbook", "Ceramics: A Potter’s Handbook"],
        "platforms": ["YouTube Pottery", "Etsy", "Skillshare"]
    },
    "standup comedy": {
        "careers": ["Comedian", "Writer", "Performer"],
        "books": ["Born Standing Up", "The Comedy Bible"],
        "platforms": ["YouTube Comedy", "Netflix Specials", "Instagram Comedy"]
    },

    "origami": {
        "careers": ["Origami Artist", "Craft Instructor", "Product Designer"],
        "books": ["Origami Design Secrets", "The Complete Book of Origami"],
        "platforms": ["YouTube Origami", "Pinterest", "Instagram Crafts"]
    },
    "comic creation": {
        "careers": ["Comic Artist", "Graphic Novelist", "Storyboard Writer"],
        "books": ["Understanding Comics", "Making Comics"],
        "platforms": ["Webtoon", "Tapas", "DeviantArt"]
    },
    "tattoo designing": {
        "careers": ["Tattoo Artist", "Illustrator", "Body Art Designer"],
        "books": ["Basic Fundamentals of Modern Tattoo", "Tattoo Sourcebook"],
        "platforms": ["Instagram Tattoos", "YouTube Tattoo Art", "Tattoo Forums"]
    },

    "guitar": {
        "careers": ["Guitarist", "Music Teacher", "Performer"],
        "books": ["Guitar Aerobics", "The Guitar Handbook"],
        "platforms": ["YouTube Guitar Lessons", "Ultimate Guitar", "Spotify"]
    },
    "piano": {
        "careers": ["Pianist", "Composer", "Music Teacher"],
        "books": ["Piano Adventures", "The Art of Piano Playing"],
        "platforms": ["YouTube Piano Tutorials", "Flowkey", "Spotify"]
    },
    "violin": {
        "careers": ["Violinist", "Orchestra Performer", "Music Teacher"],
        "books": ["Violin Playing as I Teach It", "Basics of Violin Playing"],
        "platforms": ["YouTube Violin Tutorials", "Violin Lab", "Spotify"]
    },
    "drums": {
        "careers": ["Drummer", "Music Producer", "Performer"],
        "books": ["Stick Control", "Drumming for Beginners"],
        "platforms": ["YouTube Drumming", "Drumeo", "Spotify"]
    },
    "dj mixing": {
        "careers": ["DJ", "Music Producer", "Event Performer"],
        "books": ["How to DJ Right", "The Art of DJing"],
        "platforms": ["SoundCloud", "YouTube DJ Sets", "Mixcloud"]
    },
    "music production": {
        "careers": ["Music Producer", "Sound Engineer", "Composer"],
        "books": ["Mixing Secrets for the Small Studio", "The Recording Engineer’s Handbook"],
        "platforms": ["Ableton Live", "FL Studio", "Logic Pro", "YouTube Music Production"]
    },
    "songwriting": {
        "careers": ["Songwriter", "Lyricist", "Composer"],
        "books": ["Writing Better Lyrics", "Songwriting for Dummies"],
        "platforms": ["YouTube Songwriting", "Spotify", "SoundCloud"]
    },

    "coding": {
        "careers": ["Software Engineer", "Data Scientist", "Web Developer", "AI Researcher"],
        "books": ["Clean Code", "The Pragmatic Programmer", "Introduction to Algorithms"],
        "platforms": ["Coursera", "Udemy", "LeetCode", "GitHub"]
    },
    "reading": {
        "careers": ["Researcher", "Content Creator", "Editor", "Librarian"],
        "books": ["Deep Work", "How to Read a Book", "The Reading Life"],
        "platforms": ["Kindle", "Goodreads", "Audible", "Project Gutenberg"]
    },
    "music": {
        "careers": ["Musician", "Sound Engineer", "Composer", "Music Therapist"],
        "books": ["This Is Your Brain on Music", "Music Theory for Dummies"],
        "platforms": ["Spotify", "SoundCloud", "Bandcamp", "YouTube"]
    },
    "photography": {
        "careers": ["Photographer", "Photojournalist", "Content Creator", "Film Director"],
        "books": ["Understanding Exposure", "The Digital Photography Book"],
        "platforms": ["Instagram", "Flickr", "500px", "Adobe Lightroom"]
    },
    "gaming": {
        "careers": ["Game Developer", "Esports Player", "Game Designer", "Streamer"],
        "books": ["Blood, Sweat, and Pixels", "Reality Is Broken"],
        "platforms": ["Twitch", "Steam", "Discord", "YouTube Gaming"]
    },
    "video games": {
        "careers": ["Game Tester", "Level Designer", "Narrative Designer", "VR Developer"],
        "books": ["The Ultimate History of Video Games", "Game Design Workshop"],
        "platforms": ["Steam", "Epic Games", "PlayStation Network", "Xbox Live"]
    },
    "sports": {
        "careers": ["Athlete", "Coach", "Sports Analyst", "Physiotherapist"],
        "books": ["Relentless", "The Champion’s Mind"],
        "platforms": ["ESPN", "Strava", "Nike Training Club", "YouTube"]
    },
    "football": {
        "careers": ["Football Player", "Coach", "Sports Commentator", "Fitness Trainer"],
        "books": ["Inverting the Pyramid", "The Football Man"],
        "platforms": ["FIFA", "ESPN", "YouTube Football Channels", "Reddit r/soccer"]
    },
    "throwball": {
        "careers": ["Athlete", "Coach", "Sports Instructor", "Recreational Therapist"],
        "books": ["Sports and Games", "The Science of Play"],
        "platforms": ["Local Sports Clubs", "YouTube", "ESPN", "Community Centers"]
    },
    "swimming": {
        "careers": ["Swimmer", "Coach", "Lifeguard", "Physiotherapist"],
        "books": ["Total Immersion", "Swimming Anatomy"],
        "platforms": ["Olympics Channel", "YouTube Swimming Tutorials", "SwimSwam", "Reddit r/Swimming"]
    },
    "eating": {
        "careers": ["Food Critic", "Nutritionist", "Chef", "Food Blogger"],
        "books": ["Salt, Fat, Acid, Heat", "Eat to Live"],
        "platforms": ["Yelp", "Zomato", "Instagram Food Blogs", "YouTube Food Channels"]
    },
    "scrolling": {
        "careers": ["Social Media Manager", "Digital Marketer", "Content Curator", "UX Researcher"],
        "books": ["Hooked", "The Social Media Bible"],
        "platforms": ["Instagram", "TikTok", "Twitter", "Facebook"]
    },
    "watching reels": {
        "careers": ["Influencer", "Content Creator", "Video Editor", "Social Media Strategist"],
        "books": ["Crushing It!", "YouTube Secrets"],
        "platforms": ["Instagram Reels", "TikTok", "YouTube Shorts", "Snapchat Spotlight"]
    },
    "watching mobile": {
        "careers": ["Tech Reviewer", "App Tester", "Digital Wellness Coach", "Content Creator"],
        "books": ["Digital Minimalism", "The Shallows"],
        "platforms": ["YouTube Tech Channels", "Reddit r/Android", "Reddit r/iPhone", "Medium Tech Blogs"]
    },
    "exploring": {
        "careers": ["Explorer", "Travel Writer", "Archaeologist", "Geographer"],
        "books": ["Into the Wild", "Endurance: Shackleton’s Incredible Voyage"],
        "platforms": ["National Geographic", "Lonely Planet", "YouTube Travel Vlogs", "Google Earth"]
    },
    "travelling": {
        "careers": ["Travel Blogger", "Tour Guide", "Photographer", "Cultural Anthropologist"],
        "books": ["Vagabonding", "Lonely Planet Guides"],
        "platforms": ["TripAdvisor", "Expedia", "Airbnb Experiences", "Instagram Travel"]
    },
    "art": {
        "careers": ["Artist", "Curator", "Art Teacher", "Museum Specialist"],
        "books": ["The Story of Art", "Ways of Seeing"],
        "platforms": ["Behance", "DeviantArt", "Instagram Art", "Skillshare"]
    },
    "craft": {
        "careers": ["Craftsperson", "Product Designer", "Artisan", "DIY Blogger"],
        "books": ["The Crafter’s Companion", "Handmade Nation"],
        "platforms": ["Etsy", "Pinterest", "YouTube DIY", "Craftsy"]
    },
    "digital art": {
        "careers": ["Digital Illustrator", "Concept Artist", "Game Designer", "NFT Creator"],
        "books": ["Digital Painting Techniques", "Beginner’s Guide to Digital Painting"],
        "platforms": ["Procreate", "Adobe Photoshop", "ArtStation", "DeviantArt"]
    },
    "magic": {
        "careers": ["Magician", "Illusionist", "Performer", "Entertainer"],
        "books": ["The Royal Road to Card Magic", "Modern Coin Magic"],
        "platforms": ["YouTube Magic Channels", "Reddit r/Magic", "Magic Café Forum", "Instagram Magicians"]
    },
    "listening music": {
        "careers": ["Music Critic", "DJ", "Podcaster", "Content Creator"],
        "books": ["Musicophilia", "This Is Your Brain on Music"],
        "platforms": ["Spotify", "Apple Music", "YouTube Music", "SoundCloud"]
    },
    "reading stories": {
        "careers": ["Author", "Storyteller", "Editor", "Content Creator"],
        "books": ["Storytelling for Writers", "The Hero with a Thousand Faces"],
        "platforms": ["Wattpad", "Goodreads", "Kindle", "Audible"]
    },
    "watching movies": {
        "careers": ["Film Critic", "Director", "Screenwriter", "Cinematographer"],
        "books": ["Save the Cat!", "Adventures in the Screen Trade"],
        "platforms": ["IMDb", "Letterboxd", "Netflix", "YouTube Movies"]
    },
    "watching series": {
        "careers": ["TV Producer", "Actor", "Media Analyst", "Entertainment Journalist"],
        "books": ["Television: Critical Methods and Applications"],
        "platforms": ["Hulu", "Disney+", "Netflix", "YouTube"]
    },
    "watching documentaries": {
        "careers": ["Documentary Filmmaker", "Researcher", "Journalist", "Educator"],
        "books": ["Documentary Storytelling", "Directing the Documentary"],
        "platforms": ["National Geographic", "Netflix Documentaries", "YouTube Docs", "PBS"]
    },
        "reading books": {
        "careers": ["Author", "Editor", "Researcher", "Librarian"],
        "books": ["How to Read a Book", "Deep Work"],
        "platforms": ["Goodreads", "Kindle", "Audible"]
    },
    "writing stories": {
        "careers": ["Writer", "Screenwriter", "Content Creator"],
        "books": ["On Writing", "Bird by Bird"],
        "platforms": ["Wattpad", "Medium", "Substack"]
    },
    "blogging": {
        "careers": ["Blogger", "Content Marketer", "SEO Specialist"],
        "books": ["Blogging for Dummies", "Content Inc."],
        "platforms": ["WordPress", "Medium", "Blogger"]
    },
    "poetry writing": {
        "careers": ["Poet", "Author", "Creative Writing Instructor"],
        "books": ["The Poetry Home Repair Manual", "Writing Poetry"],
        "platforms": ["Poetry Foundation", "Wattpad", "Instagram Poetry"]
    },
    "learning languages": {
        "careers": ["Translator", "Interpreter", "Language Teacher"],
        "books": ["Fluent Forever", "Language Hacking"],
        "platforms": ["Duolingo", "Babbel", "Memrise"]
    },
    "solving puzzles": {
        "careers": ["Puzzle Designer", "Game Developer", "Mathematician"],
        "books": ["The Puzzle Palace", "The Moscow Puzzles"],
        "platforms": ["Puzzle Apps", "YouTube Puzzle Channels", "Reddit r/puzzles"]
    },
    "sudoku": {
        "careers": ["Puzzle Creator", "Game Designer", "Math Educator"],
        "books": ["Sudoku Masterpieces", "The Big Book of Sudoku"],
        "platforms": ["Sudoku.com", "Mobile Sudoku Apps", "YouTube Sudoku"]
    },
    "chess": {
        "careers": ["Chess Player", "Coach", "Analyst"],
        "books": ["My System", "The Art of Chess"],
        "platforms": ["Chess.com", "Lichess", "YouTube Chess"]
    },
    "debate practice": {
        "careers": ["Lawyer", "Politician", "Public Speaker"],
        "books": ["Thank You for Arguing", "The Debater’s Guide"],
        "platforms": ["Debate Clubs", "YouTube Debates", "Toastmasters"]
    },
    "philosophy study": {
        "careers": ["Philosopher", "Professor", "Ethics Consultant"],
        "books": ["Meditations", "The Republic"],
        "platforms": ["Stanford Encyclopedia of Philosophy", "Coursera Philosophy", "YouTube Philosophy"]
    },
    "research reading": {
        "careers": ["Researcher", "Academic", "Analyst"],
        "books": ["The Craft of Research", "How to Read a Paper"],
        "platforms": ["Google Scholar", "ResearchGate", "JSTOR"]
    },
    "app development": {
        "careers": ["App Developer", "Software Engineer", "Product Manager"],
        "books": ["Android Programming for Beginners", "iOS Programming Cookbook"],
        "platforms": ["GitHub", "Stack Overflow", "Udemy"]
    },
    "game development": {
        "careers": ["Game Developer", "Level Designer", "Narrative Designer"],
        "books": ["Game Programming Patterns", "The Art of Game Design"],
        "platforms": ["Unity", "Unreal Engine", "GitHub"]
    },
    "ethical hacking": {
        "careers": ["Cybersecurity Analyst", "Penetration Tester", "Security Consultant"],
        "books": ["The Web Application Hacker’s Handbook", "Hacking: The Art of Exploitation"],
        "platforms": ["HackTheBox", "TryHackMe", "YouTube Cybersecurity"]
    },
    "robotics building": {
        "careers": ["Robotics Engineer", "Automation Specialist", "AI Researcher"],
        "books": ["Robot Building for Beginners", "Introduction to Autonomous Robots"],
        "platforms": ["Arduino", "Raspberry Pi", "YouTube Robotics"]
    },
    "ai experimentation": {
        "careers": ["AI Engineer", "Data Scientist", "Researcher"],
        "books": ["Artificial Intelligence: A Modern Approach", "Deep Learning"],
        "platforms": ["TensorFlow", "PyTorch", "GitHub AI Projects"]
    },
    "3d modeling": {
        "careers": ["3D Artist", "Animator", "Game Designer"],
        "books": ["Blender for Dummies", "Digital Modeling"],
        "platforms": ["Blender", "Maya", "ZBrush"]
    },
    
    "cricket": {
        "careers": ["Cricketer", "Coach", "Sports Analyst", "Commentator"],
        "books": ["Playing It My Way", "The Art of Captaincy"],
        "platforms": ["Cricbuzz", "ESPNcricinfo", "Hotstar"]
    },
    "football": {
        "careers": ["Football Player", "Coach", "Sports Journalist", "Fitness Trainer"],
        "books": ["Inverting the Pyramid", "The Football Man"],
        "platforms": ["FIFA", "ESPN", "YouTube Football"]
    },
    "basketball": {
        "careers": ["Basketball Player", "Coach", "Sports Analyst"],
        "books": ["Eleven Rings", "The Breaks of the Game"],
        "platforms": ["NBA", "ESPN", "YouTube Basketball"]
    },
    "tennis": {
        "careers": ["Tennis Player", "Coach", "Sports Journalist"],
        "books": ["Open", "Winning Ugly"],
        "platforms": ["ATP Tour", "WTA Tour", "YouTube Tennis"]
    },
    "badminton": {
        "careers": ["Badminton Player", "Coach", "Trainer"],
        "books": ["Badminton Handbook", "Winning Badminton Singles"],
        "platforms": ["BWF", "Olympics Channel", "YouTube Badminton"]
    },
    "swimming": {
        "careers": ["Swimmer", "Coach", "Lifeguard"],
        "books": ["Total Immersion", "Swimming Anatomy"],
        "platforms": ["SwimSwam", "Olympics Channel", "YouTube Swimming"]
    },
    "cycling": {
        "careers": ["Cyclist", "Coach", "Sports Scientist"],
        "books": ["The Cyclist’s Training Bible", "It’s All About the Bike"],
        "platforms": ["Strava", "Zwift", "Peloton"]
    },
    "running": {
        "careers": ["Athlete", "Coach", "Fitness Blogger"],
        "books": ["Born to Run", "Running with the Kenyans"],
        "platforms": ["Nike Run Club", "Strava", "Garmin Connect"]
    },
    "trekking": {
        "careers": ["Adventure Guide", "Travel Blogger", "Outdoor Instructor"],
        "books": ["Trekking in the Himalayas", "Wild"],
        "platforms": ["AllTrails", "YouTube Trekking", "Instagram Travel"]
    },
    "rock climbing": {
        "careers": ["Climber", "Instructor", "Adventure Photographer"],
        "books": ["Training for Climbing", "Rock Climbing: Mastering Basic Skills"],
        "platforms": ["Mountain Project", "YouTube Climbing", "Reddit r/climbing"]
    },
    "gym workouts": {
        "careers": ["Fitness Trainer", "Bodybuilder", "Physiotherapist"],
        "books": ["Strength Training Anatomy", "Bigger Leaner Stronger"],
        "platforms": ["Nike Training Club", "YouTube Fitness", "Bodybuilding.com"]
    },
    "yoga": {
        "careers": ["Yoga Instructor", "Wellness Coach", "Therapist"],
        "books": ["Light on Yoga", "The Heart of Yoga"],
        "platforms": ["Yoga with Adriene (YouTube)", "Headspace", "Calm"]
    },
    "martial arts": {
        "careers": ["Martial Artist", "Instructor", "Stunt Performer"],
        "books": ["The Tao of Jeet Kune Do", "Karate-Do: My Way of Life"],
        "platforms": ["Dojo Networks", "YouTube Martial Arts", "UFC Fight Pass"]
    },
    "boxing": {
        "careers": ["Boxer", "Coach", "Sports Commentator"],
        "books": ["The Fight", "Boxing Mastery"],
        "platforms": ["BoxRec", "YouTube Boxing", "ESPN Boxing"]
    },
    "table tennis": {
        "careers": ["Table Tennis Player", "Coach", "Trainer"],
        "books": ["Table Tennis Tactics for Thinkers", "Ping Pong Fever"],
        "platforms": ["ITTF", "YouTube Table Tennis", "Olympics Channel"]
    },
    "pilates": {
        "careers": ["Pilates Instructor", "Fitness Coach", "Wellness Blogger"],
        "books": ["Pilates Anatomy", "Return to Life Through Contrology"],
        "platforms": ["YouTube Pilates", "Instagram Fitness", "Pilates Anytime"]
    },

    "gardening": {
        "careers": ["Horticulturist", "Landscape Designer", "Urban Farmer"],
        "books": ["The Garden Primer", "Gaia’s Garden"],
        "platforms": ["Pinterest Gardening", "YouTube Gardening", "GardenWeb"]
    },
    "bonsai growing": {
        "careers": ["Bonsai Artist", "Botanist", "Gardening Instructor"],
        "books": ["The Bonsai Handbook", "Bonsai Techniques"],
        "platforms": ["YouTube Bonsai", "Pinterest Bonsai", "Instagram Bonsai"]
    },
    "bird watching": {
        "careers": ["Ornithologist", "Wildlife Photographer", "Nature Blogger"],
        "books": ["Birds of the World", "The Sibley Guide to Birds"],
        "platforms": ["eBird", "Audubon", "YouTube Bird Watching"]
    },
    "fishing": {
        "careers": ["Fisherman", "Fishing Guide", "Marine Biologist"],
        "books": ["The Total Fishing Manual", "A River Runs Through It"],
        "platforms": ["YouTube Fishing", "Reddit r/Fishing", "Fishing Forums"]
    },
    "camping": {
        "careers": ["Outdoor Guide", "Travel Blogger", "Adventure Instructor"],
        "books": ["Camping and Woodcraft", "The Ultimate Hiker’s Gear Guide"],
        "platforms": ["AllTrails", "YouTube Camping", "Reddit r/Camping"]
    },
    "hiking": {
        "careers": ["Hiking Guide", "Travel Blogger", "Adventure Photographer"],
        "books": ["Wild", "The Backpacker’s Handbook"],
        "platforms": ["AllTrails", "YouTube Hiking", "Instagram Travel"]
    },
    "stargazing": {
        "careers": ["Astronomer", "Astrophotographer", "Science Communicator"],
        "books": ["Cosmos", "Turn Left at Orion"],
        "platforms": ["NASA", "SkySafari", "YouTube Astronomy"]
    },
    "farming": {
        "careers": ["Farmer", "Agricultural Scientist", "Agri-Entrepreneur"],
        "books": ["The Lean Farm", "Farming for Dummies"],
        "platforms": ["YouTube Farming", "Agri Forums", "Reddit r/farming"]
    },
    "wildlife photography": {
        "careers": ["Wildlife Photographer", "Conservationist", "Documentary Maker"],
        "books": ["The Wildlife Photography Handbook", "Photographing Wildlife"],
        "platforms": ["National Geographic", "YouTube Wildlife Photography", "Instagram Wildlife"]
    },

    "video editing": {
        "careers": ["Video Editor", "Content Creator", "Film Maker"],
        "books": ["In the Blink of an Eye", "The Technique of Film Editing"],
        "platforms": ["Adobe Premiere Pro", "Final Cut Pro", "YouTube"]
    },
    "graphic designing": {
        "careers": ["Graphic Designer", "Brand Designer", "UI/UX Designer"],
        "books": ["Graphic Design School", "Thinking with Type"],
        "platforms": ["Adobe Illustrator", "Canva", "Behance"]
    },
    "crypto trading": {
        "careers": ["Crypto Trader", "Financial Analyst", "Blockchain Consultant"],
        "books": ["Mastering Bitcoin", "The Basics of Bitcoins and Blockchains"],
        "platforms": ["Binance", "Coinbase", "Crypto Twitter"]
    },
    "building pcs": {
        "careers": ["Hardware Engineer", "Tech Reviewer", "PC Builder"],
        "books": ["Build Your Own PC", "Upgrading and Repairing PCs"],
        "platforms": ["PCPartPicker", "YouTube PC Builds", "Reddit r/buildapc"]
    },
    
    "videogaming": {
        "careers": ["Game Tester", "Streamer", "Game Developer", "Esports Player"],
        "books": ["Blood, Sweat, and Pixels", "Reality Is Broken"],
        "platforms": ["Steam", "Twitch", "Discord", "YouTube Gaming"]
    },
    "esports": {
        "careers": ["Professional Gamer", "Coach", "Esports Analyst", "Event Organizer"],
        "books": ["Esports Business Management", "Game On!"],
        "platforms": ["Twitch", "YouTube Esports", "Reddit r/esports"]
    },
    "mobile gaming": {
        "careers": ["App Tester", "Mobile Game Developer", "Content Creator"],
        "books": ["Mobile Game Development with Unity", "Game Design Workshop"],
        "platforms": ["Google Play", "Apple App Store", "YouTube Mobile Gaming"]
    },
    "boardgames": {
        "careers": ["Game Designer", "Board Game Reviewer", "Event Organizer"],
        "books": ["The Board Game Book", "Eurogames"],
        "platforms": ["BoardGameGeek", "YouTube Board Games", "Reddit r/boardgames"]
    },
    "card games": {
        "careers": ["Card Game Designer", "Professional Player", "Content Creator"],
        "books": ["The Ultimate Book of Card Games", "Card Games for One"],
        "platforms": ["YouTube Card Games", "Reddit r/cardgames", "BoardGameGeek"]
    },
    "role playing games": {
        "careers": ["Game Master", "Narrative Designer", "Content Creator"],
        "books": ["Dungeon Master’s Guide", "The Art of Game Design"],
        "platforms": ["D&D Beyond", "Roll20", "YouTube RPG"]
    },
    "watching movies": {
        "careers": ["Film Critic", "Director", "Screenwriter", "Cinematographer"],
        "books": ["Save the Cat!", "Adventures in the Screen Trade"],
        "platforms": ["IMDb", "Letterboxd", "Netflix", "YouTube Movies"]
    },
    "watching web series": {
        "careers": ["TV Producer", "Actor", "Media Analyst"],
        "books": ["Television: Critical Methods and Applications"],
        "platforms": ["Netflix", "Amazon Prime Video", "YouTube Series"]
    },

    "meditation": {
        "careers": ["Mindfulness Coach", "Therapist", "Wellness Instructor"],
        "books": ["The Miracle of Mindfulness", "Wherever You Go, There You Are"],
        "platforms": ["Headspace", "Calm", "Insight Timer"]
    },
    "journaling": {
        "careers": ["Writer", "Therapist", "Content Creator"],
        "books": ["The Artist’s Way", "Journal Therapy"],
        "platforms": ["Pinterest Journaling", "YouTube Journaling", "Instagram Journals"]
    },
    "public speaking": {
        "careers": ["Motivational Speaker", "Trainer", "Politician"],
        "books": ["Talk Like TED", "The Art of Public Speaking"],
        "platforms": ["Toastmasters", "YouTube Public Speaking", "Coursera"]
    },
    "business skills": {
        "careers": ["Entrepreneur", "Business Analyst", "Consultant"],
        "books": ["The Lean Startup", "Good to Great"],
        "platforms": ["Coursera Business", "LinkedIn Learning", "Udemy"]
    },
    "investing": {
        "careers": ["Investor", "Financial Analyst", "Stock Trader"],
        "books": ["The Intelligent Investor", "Rich Dad Poor Dad"],
        "platforms": ["Yahoo Finance", "Bloomberg", "TradingView"]
    },
    "personal branding": {
        "careers": ["Influencer", "Coach", "Entrepreneur"],
        "books": ["Crushing It!", "Building a StoryBrand"],
        "platforms": ["LinkedIn", "Instagram", "YouTube"]
    },
    "leadership training": {
        "careers": ["Manager", "Executive Coach", "Team Leader"],
        "books": ["Leaders Eat Last", "The 21 Irrefutable Laws of Leadership"],
        "platforms": ["Coursera Leadership", "LinkedIn Learning", "YouTube Leadership"]
    },
    "time management": {
        "careers": ["Productivity Coach", "Manager", "Consultant"],
        "books": ["Getting Things Done", "Eat That Frog!"],
        "platforms": ["Trello", "Notion", "YouTube Productivity"]
    },
    "solo traveling": {
        "careers": ["Travel Blogger", "Photographer", "Content Creator"],
        "books": ["Vagabonding", "The Solo Travel Handbook"],
        "platforms": ["TripAdvisor", "Instagram Travel", "YouTube Travel"]
    },
    "backpacking": {
        "careers": ["Adventure Blogger", "Tour Guide", "Photographer"],
        "books": ["Backpacking 101", "The Backpacker’s Handbook"],
        "platforms": ["Lonely Planet", "YouTube Backpacking", "Reddit r/backpacking"]
    },
    "road trips": {
        "careers": ["Travel Blogger", "Photographer", "Content Creator"],
        "books": ["Road Trip USA", "On the Road"],
        "platforms": ["Google Maps", "Instagram Travel", "YouTube Road Trips"]
    },
    "cultural exploration": {
        "careers": ["Anthropologist", "Travel Writer", "Tour Guide"],
        "books": ["Guns, Germs, and Steel", "The Geography of Thought"],
        "platforms": ["National Geographic", "YouTube Culture", "Instagram Travel"]
    },
    "food tourism": {
        "careers": ["Food Blogger", "Chef", "Travel Writer"],
        "books": ["Eat Pray Love", "The World Atlas of Food"],
        "platforms": ["YouTube Food Travel", "Instagram Food", "TripAdvisor"]
    },
    "adventure tourism": {
        "careers": ["Adventure Guide", "Travel Blogger", "Photographer"],
        "books": ["Adventure Tourism Management", "Wild"],
        "platforms": ["YouTube Adventure Travel", "Instagram Adventure", "Lonely Planet"]
    },
    "cooking": {
        "careers": ["Chef", "Food Blogger", "Nutritionist"],
        "books": ["Salt, Fat, Acid, Heat", "The Joy of Cooking"],
        "platforms": ["YouTube Cooking", "Tasty", "Epicurious"]
    },
    "knitting": {
        "careers": ["Textile Designer", "Fashion Entrepreneur", "Craft Instructor"],
        "books": ["Stitch 'n Bitch", "The Principles of Knitting"],
        "platforms": ["Ravelry", "Pinterest Knitting", "YouTube Knitting"]
    },
    "crocheting": {
        "careers": ["Crochet Designer", "Craft Blogger", "Fashion Designer"],
        "books": ["Crochet Every Way Stitch Dictionary", "The Complete Book of Crochet"],
        "platforms": ["Ravelry", "YouTube Crochet", "Instagram Crochet"]
    },
    "woodworking": {
        "careers": ["Carpenter", "Furniture Designer", "Craft Instructor"],
        "books": ["The Complete Manual of Woodworking", "Woodworking Basics"],
        "platforms": ["YouTube Woodworking", "Pinterest DIY", "Reddit r/woodworking"]
    },
    "candle making": {
        "careers": ["Candle Maker", "Craft Entrepreneur", "DIY Blogger"],
        "books": ["The Candlemaker’s Companion", "Candle Making for Beginners"],
        "platforms": ["YouTube Candle Making", "Pinterest Crafts", "Etsy"]
    },
    "soapmaking": {
        "careers": ["Soap Maker", "Cosmetic Entrepreneur", "DIY Blogger"],
        "books": ["The Natural Soap Making Book", "Soap Crafting"],
        "platforms": ["YouTube Soap Making", "Pinterest Soap", "Etsy"]
    },
    "resin art": {
        "careers": ["Resin Artist", "Craft Entrepreneur", "DIY Instructor"],
        "books": ["Resin Jewelry", "Epoxy Resin Art for Beginners"],
        "platforms": ["YouTube Resin Art", "Instagram Resin", "Pinterest Crafts"]
    },
    "dielectronic": {
        "careers": ["Electronics Engineer", "Maker", "Tech Blogger"],
        "books": ["Make: Electronics", "Practical Electronics for Inventors"],
        "platforms": ["Arduino", "Raspberry Pi", "YouTube DIY Electronics"]
    },
    "home decoration": {
        "careers": ["Interior Designer", "DIY Blogger", "Architect"],
        "books": ["Styled", "The Interior Design Handbook"],
        "platforms": ["Pinterest Home Decor", "YouTube DIY Home", "Instagram Decor"]
    },
    "stamp collecting": {
        "careers": ["Philatelist", "Museum Curator", "Historian"],
        "books": ["The World Encyclopedia of Stamps", "Collecting Stamps"],
        "platforms": ["StampWorld", "YouTube Stamp Collecting", "Reddit r/philately"]
    },
    "coin collecting": {
        "careers": ["Numismatist", "Antique Dealer", "Historian"],
        "books": ["The Official Red Book of Coins", "Coin Collecting for Dummies"],
        "platforms": ["NGC Coin", "YouTube Coin Collecting", "Reddit r/coins"]
    },
    "action figure collecting": {
        "careers": ["Toy Reviewer", "Collector", "Content Creator"],
        "books": ["Action Figures: A Collector’s Guide"],
        "platforms": ["YouTube Toy Reviews", "Instagram Collectibles", "Reddit r/actionfigures"]
    },
    "book collecting": {
        "careers": ["Bibliophile", "Rare Book Dealer", "Archivist"],
        "books": ["ABC for Book Collectors", "Rare Books Uncovered"],
        "platforms": ["Goodreads", "Instagram Books", "Reddit r/bookcollecting"]
    },
    "sneaker collecting": {
        "careers": ["Sneaker Reseller", "Fashion Blogger", "Collector"],
        "books": ["Out of the Box: The Rise of Sneaker Culture"],
        "platforms": ["StockX", "GOAT", "Instagram Sneakers"]
    },
    "antique collecting": {
        "careers": ["Antique Dealer", "Museum Curator", "Historian"],
        "books": ["Antiques Handbook", "Collecting Antiques"],
        "platforms": ["eBay Antiques", "YouTube Antiques", "Reddit r/Antiques"]
    },
    "pet training": {
        "careers": ["Dog Trainer", "Animal Behaviorist", "Pet Blogger"],
        "books": ["The Art of Raising a Puppy", "Don’t Shoot the Dog!"],
        "platforms": ["YouTube Pet Training", "Instagram Pets", "Reddit r/dogs"]
    },
    "aquarium keeping": {
        "careers": ["Aquarist", "Marine Biologist", "Pet Blogger"],
        "books": ["The Simple Guide to Freshwater Aquariums", "Aquarium Owner’s Manual"],
        "platforms": ["YouTube Aquariums", "Reddit r/Aquariums", "Instagram Fishkeeping"]
    },
    "dog breeding": {
        "careers": ["Dog Breeder", "Veterinarian", "Pet Blogger"],
        "books": ["The Dog Breeder’s Guide to Success"],
        "platforms": ["YouTube Dog Breeding", "Reddit r/dogs", "Instagram Breeders"]
    },
    "horse-riding": {
        "careers": ["Equestrian", "Horse Trainer", "Sports Instructor"],
        "books": ["Centered Riding", "The Complete Horse Riding Manual"],
        "platforms": ["YouTube Horse Riding", "Equestrian Forums", "Instagram Horses"]
    },
    "birdkeeping": {
        "careers": ["Aviculturist", "Pet Blogger", "Wildlife Educator"],
        "books": ["The Bird Keeper’s Guide", "Parrots for Dummies"],
        "platforms": ["YouTube Bird Keeping", "Instagram Birds", "Reddit r/birding"]
    },
    "drone flying": {
        "careers": ["Drone Pilot", "Aerial Photographer", "Content Creator"],
        "books": ["Drone Photography Basics", "The Drone Pilot’s Handbook"],
        "platforms": ["DJI Forums", "YouTube Drone Flying", "Instagram Drones"]
    },
    "podcasting": {
        "careers": ["Podcaster", "Radio Host", "Content Creator"],
        "books": ["Podcasting for Dummies", "Out on the Wire"],
        "platforms": ["Spotify Podcasts", "Apple Podcasts", "YouTube Podcasts"]
    },
    "vlogging": {
        "careers": ["Vlogger", "Content Creator", "Influencer"],
        "books": ["YouTube Secrets", "Vlog Like a Boss"],
        "platforms": ["YouTube", "Instagram", "TikTok"]
    },
    "content creation": {
        "careers": ["Content Creator", "Influencer", "Digital Marketer"],
        "books": ["Crushing It!", "Content Inc."],
        "platforms": ["YouTube", "Instagram", "TikTok"]
    },
    "nft art creation": {
        "careers": ["NFT Artist", "Digital Entrepreneur", "Crypto Creator"],
        "books": ["NFTs for Beginners", "The NFT Handbook"],
        "platforms": ["OpenSea", "Rarible", "Foundation"]
    },
    "space watching": {
        "careers": ["Astronomer", "Astrophotographer", "Science Communicator"],
        "books": ["Cosmos", "Astrophysics for People in a Hurry"],
        "platforms": ["NASA", "YouTube Astronomy", "Reddit r/space"]
    },
    "urban exploring": {
        "careers": ["Urban Explorer", "Photographer", "Content Creator"],
        "books": ["Access All Areas: A User’s Guide to the Art of Urban Exploration"],
        "platforms": ["YouTube Urbex", "Instagram Urbex", "Reddit r/urbanexploration"]
    },
    "minimalism lifestyle": {
        "careers": ["Minimalism Coach", "Lifestyle Blogger", "Author"],
        "books": ["The Life-Changing Magic of Tidying Up", "Goodbye, Things"],
        "platforms": ["YouTube Minimalism", "Instagram Minimalism", "Reddit r/minimalism"]
    },
    "biohacking": {
        "careers": ["Biohacker", "Health Blogger", "Wellness Entrepreneur"],
        "books": ["Biohackers Handbook", "Superhuman"],
        "platforms": ["YouTube Biohacking", "Reddit r/biohackers", "Instagram Biohacking"]
    },
    "baking": {
        "careers": ["Baker", "Pastry Chef", "Food Blogger"],
        "books": ["The Baking Bible", "Bread Baking for Beginners"],
        "platforms": ["YouTube Baking", "Instagram Baking", "Pinterest Recipes"]
    },
    "cake designing": {
        "careers": ["Cake Designer", "Pastry Chef", "Food Blogger"],
        "books": ["Cake Decorating for Beginners", "The Contemporary Cake Decorating Bible"],
        "platforms": ["YouTube Cake Decorating", "Instagram Cakes", "Pinterest Baking"]
    },
    "chocolate making": {
        "careers": ["Chocolatier", "Pastry Chef", "Food Blogger"],
        "books": ["The Chocolate Bible", "Making Artisan Chocolates"],
        "platforms": ["YouTube Chocolate Making", "Instagram Chocolate", "Pinterest Recipes"]
    },
    "coffee brewing": {
        "careers": ["Barista", "Coffee Blogger", "Cafe Owner"],
        "books": ["The World Atlas of Coffee", "Coffee Obsession"],
        "platforms": ["YouTube Coffee Brewing", "Instagram Coffee", "Reddit r/coffee"]
    },
    "bartending": {
        "careers": ["Bartender", "Mixologist", "Event Manager"],
        "books": ["The Bar Book", "The Craft of the Cocktail"],
        "platforms": ["YouTube Bartending", "Instagram Cocktails", "Pinterest Drinks"]
    },
    "food blogging": {
        "careers": ["Food Blogger", "Content Creator", "Nutritionist"],
        "books": ["Food Blogging for Dummies", "Eat to Live"],
        "platforms": ["WordPress", "Instagram Food", "YouTube Food"]
    },

    "dance": {
        "careers": ["Dancer", "Choreographer", "Dance Instructor", "Performer"],
        "books": ["The Art of Movement", "Dance Anatomy"],
        "platforms": ["YouTube Dance Tutorials", "TikTok", "DancePlug", "Instagram"]
    },
    "meditation": {
        "careers": ["Mindfulness Coach", "Therapist", "Wellness Instructor", "Author"],
        "books": ["The Miracle of Mindfulness", "Wherever You Go, There You Are"],
        "platforms": ["Headspace", "Calm", "Insight Timer", "YouTube"]
    },
    "socializing": {
        "careers": ["Event Planner", "Public Relations Specialist", "Community Manager", "Influencer"],
        "books": ["How to Win Friends and Influence People", "The Charisma Myth"],
        "platforms": ["Meetup", "LinkedIn", "Instagram", "Discord"]
    }
}
subject_career_map = {
    "maths": {
        "careers": ["Engineer", "Data Scientist", "Statistician", "Actuary"],
        "books": ["Mathematics: Its Content, Methods and Meaning", "Introduction to Probability"],
        "platforms": ["Khan Academy", "Coursera", "Brilliant"]
    },
    "physics": {
        "careers": ["Physicist", "Aerospace Engineer", "Research Scientist"],
        "books": ["Concepts of Physics", "Fundamentals of Physics"],
        "platforms": ["MIT OpenCourseWare", "YouTube Physics Girl", "Coursera"]
    },
    "chemistry": {
        "careers": ["Chemist", "Pharmacist", "Chemical Engineer"],
        "books": ["Organic Chemistry by Clayden", "Chemistry: The Central Science"],
        "platforms": ["Khan Academy", "YouTube CrashCourse Chemistry", "edX"]
    },
    "biology": {
        "careers": ["Doctor", "Biotechnologist", "Researcher"],
        "books": ["Campbell Biology", "Molecular Biology of the Cell"],
        "platforms": ["Coursera", "YouTube Amoeba Sisters", "edX"]
    },
    "commerce": {
        "careers": ["Entrepreneur", "Manager", "Accountant", "Financial Analyst"],
        "books": ["Rich Dad Poor Dad", "Principles of Economics"],
        "platforms": ["Udemy", "LinkedIn Learning", "Coursera Business"]
    },
    "economics": {
        "careers": ["Economist", "Policy Analyst", "Financial Consultant"],
        "books": ["Capital in the Twenty-First Century", "Freakonomics"],
        "platforms": ["edX Economics", "Coursera", "Khan Academy"]
    },
    "computer science": {
        "careers": ["Software Engineer", "AI Researcher", "Cybersecurity Specialist"],
        "books": ["Introduction to Algorithms", "Clean Code"],
        "platforms": ["LeetCode", "GitHub", "Udemy"]
    },
    "history": {
        "careers": ["Historian", "Archaeologist", "Museum Curator"],
        "books": ["A People’s History of the United States", "Guns, Germs, and Steel"],
        "platforms": ["Coursera History", "YouTube History Channel", "edX"]
    },
    "geography": {
        "careers": ["Geographer", "Urban Planner", "Environmental Scientist"],
        "books": ["Geography of India", "Human Geography"],
        "platforms": ["National Geographic", "Coursera Geography", "YouTube Geography Now"]
    },
    "political science": {
        "careers": ["Politician", "Policy Analyst", "Diplomat"],
        "books": ["The Republic", "Politics by Aristotle"],
        "platforms": ["Coursera Political Science", "edX", "YouTube CrashCourse Government"]
    },
    "psychology": {
        "careers": ["Psychologist", "Counselor", "Human Resource Specialist"],
        "books": ["Thinking, Fast and Slow", "Psychology by David Myers"],
        "platforms": ["Coursera Psychology", "edX", "YouTube Psych Explained"]
    },
    
    "statistics": {
        "careers": ["Statistician", "Data Analyst", "Actuary"],
        "books": ["Statistics for Engineers", "The Elements of Statistical Learning"],
        "platforms": ["Khan Academy", "Coursera", "edX"]
    },
    "astronomy": {
        "careers": ["Astronomer", "Astrophysicist", "Space Scientist"],
        "books": ["Cosmos", "Astrophysics for People in a Hurry"],
        "platforms": ["NASA", "YouTube Astronomy", "Coursera Astronomy"]
    },
    "geology": {
        "careers": ["Geologist", "Mining Engineer", "Environmental Consultant"],
        "books": ["Earth: An Introduction to Physical Geology", "Principles of Geology"],
        "platforms": ["Coursera Geology", "YouTube Geology", "edX"]
    },
    "zoology": {
        "careers": ["Zoologist", "Wildlife Biologist", "Conservationist"],
        "books": ["Zoology by Miller & Harley", "Animal Behavior"],
        "platforms": ["Coursera Zoology", "National Geographic", "YouTube Wildlife"]
    },
    "botany": {
        "careers": ["Botanist", "Plant Scientist", "Agricultural Researcher"],
        "books": ["Botany for Gardeners", "Plant Physiology"],
        "platforms": ["Coursera Botany", "YouTube Botany", "edX"]
    },
    "environmental science": {
        "careers": ["Environmental Scientist", "Ecologist", "Conservationist"],
        "books": ["Silent Spring", "Our Common Future"],
        "platforms": ["Coursera Environmental Science", "National Geographic", "edX"]
    },

    "sociology": {
        "careers": ["Sociologist", "Social Worker", "Policy Analyst"],
        "books": ["Sociology by Giddens", "The Sociological Imagination"],
        "platforms": ["Coursera Sociology", "YouTube Sociology", "edX"]
    },
    "anthropology": {
        "careers": ["Anthropologist", "Archaeologist", "Cultural Researcher"],
        "books": ["Anthropology: The Basics", "Patterns of Culture"],
        "platforms": ["Coursera Anthropology", "YouTube Anthropology", "edX"]
    },
    "languages": {
        "careers": ["Translator", "Interpreter", "Language Teacher"],
        "books": ["Fluent Forever", "Language Hacking"],
        "platforms": ["Duolingo", "Babbel", "Memrise"]
    },
    "history": {
        "careers": ["Historian", "Archaeologist", "Museum Curator"],
        "books": ["A People’s History of the United States", "Guns, Germs, and Steel"],
        "platforms": ["Coursera History", "YouTube History Channel", "edX"]
    },
    "law": {
        "careers": ["Lawyer", "Judge", "Legal Consultant"],
        "books": ["Black’s Law Dictionary", "Introduction to Law"],
        "platforms": ["Coursera Law", "edX Legal Studies", "YouTube Legal Eagle"]
    },


    "accounting": {
        "careers": ["Accountant", "Auditor", "Financial Analyst"],
        "books": ["Financial Accounting by Libby", "Accounting Made Simple"],
        "platforms": ["LinkedIn Learning", "Coursera Accounting", "Udemy"]
    },
    "business studies": {
        "careers": ["Entrepreneur", "Manager", "Consultant"],
        "books": ["The Lean Startup", "Good to Great"],
        "platforms": ["Coursera Business", "Udemy", "LinkedIn Learning"]
    },
    "economics": {
        "careers": ["Economist", "Policy Analyst", "Financial Consultant"],
        "books": ["Capital in the Twenty-First Century", "Freakonomics"],
        "platforms": ["edX Economics", "Coursera", "Khan Academy"]
    },
    "management": {
        "careers": ["Manager", "Business Consultant", "Project Leader"],
        "books": ["The 7 Habits of Highly Effective People", "Principles of Management"],
        "platforms": ["Coursera Management", "Udemy", "LinkedIn Learning"]
    },
    
    "finearts": {
        "careers": ["Artist", "Designer", "Curator"],
        "books": ["The Story of Art", "Ways of Seeing"],
        "platforms": ["Skillshare", "YouTube Art Channels", "Coursera Arts"]
    },

    "fine arts": {
        "careers": ["Artist", "Designer", "Curator"],
        "books": ["The Story of Art", "Ways of Seeing"],
        "platforms": ["Skillshare", "YouTube Art Channels", "Coursera Arts"]
    },
    "music": {
        "careers": ["Musician", "Composer", "Sound Engineer"],
        "books": ["Music Theory for Dummies", "This Is Your Brain on Music"],
        "platforms": ["Spotify", "YouTube Music", "Coursera Music"]
    },
    "performing arts": {
        "careers": ["Actor", "Dancer", "Theatre Director"],
        "books": ["An Actor Prepares", "Dance Anatomy"],
        "platforms": ["YouTube Performing Arts", "Coursera Theatre", "Skillshare"]
    },
    "design": {
        "careers": ["Graphic Designer", "UI/UX Designer", "Product Designer"],
        "books": ["Thinking with Type", "Graphic Design School"],
        "platforms": ["Adobe Illustrator", "Canva", "Behance"]
    },
    
    "electronics": {
        "careers": ["Electronics Engineer", "Circuit Designer", "Robotics Specialist"],
        "books": ["Electronic Principles", "Practical Electronics for Inventors"],
        "platforms": ["Arduino", "Raspberry Pi", "Coursera Electronics"]
    },
    "mechanical engineering": {
        "careers": ["Mechanical Engineer", "Automotive Designer", "Aerospace Engineer"],
        "books": ["Engineering Mechanics", "Mechanical Engineering Handbook"],
        "platforms": ["MIT OpenCourseWare", "Coursera Mechanical Engineering", "edX"]
    },
    "civil engineering": {
        "careers": ["Civil Engineer", "Urban Planner", "Structural Designer"],
        "books": ["Civil Engineering Reference Manual", "Structural Analysis"],
        "platforms": ["Coursera Civil Engineering", "YouTube Civil Engineering", "edX"]
    },
    "electrical engineering": {
        "careers": ["Electrical Engineer", "Power Systems Analyst", "Electronics Designer"],
        "books": ["Electrical Engineering Fundamentals", "Power System Analysis"],
        "platforms": ["Coursera Electrical Engineering", "edX", "YouTube Electrical Engineering"]
    },
    "biotechnology": {
        "careers": ["Biotechnologist", "Genetic Engineer", "Pharmaceutical Researcher"],
        "books": ["Biotechnology for Beginners", "Molecular Biotechnology"],
        "platforms": ["Coursera Biotechnology", "edX", "YouTube Biotech"]
    },
    "microbiology": {
        "careers": ["Microbiologist", "Lab Technician", "Medical Researcher"],
        "books": ["Microbiology by Prescott", "Medical Microbiology"],
        "platforms": ["Coursera Microbiology", "YouTube Microbiology", "edX"]
    },
    "genetics": {
        "careers": ["Geneticist", "Research Scientist", "Biotech Entrepreneur"],
        "books": ["Genetics: A Conceptual Approach", "Human Genetics"],
        "platforms": ["Coursera Genetics", "YouTube Genetics", "edX"]
    },
    "nutrition": {
        "careers": ["Nutritionist", "Dietitian", "Health Coach"],
        "books": ["Nutrition Essentials", "Eat to Live"],
        "platforms": ["Coursera Nutrition", "YouTube Nutrition", "edX"]
    },

    # Humanities & Arts
    "journalism": {
        "careers": ["Journalist", "Editor", "News Anchor"],
        "books": ["The Elements of Journalism", "On Writing Well"],
        "platforms": ["Coursera Journalism", "YouTube Journalism", "LinkedIn Learning"]
    },
    "media studies": {
        "careers": ["Media Analyst", "Content Creator", "Film Critic"],
        "books": ["Media Studies: A Reader", "Understanding Media"],
        "platforms": ["Coursera Media Studies", "YouTube Media Analysis", "edX"]
    },
    
    
    "hospitality": {
        "careers": ["Hotel Manager", "Chef", "Event Planner"],
        "books": ["Hospitality Management", "The Cornell School of Hotel Administration Handbook"],
        "platforms": ["Coursera Hospitality", "Udemy", "LinkedIn Learning"]
    },
    "tourism": {
        "careers": ["Tour Guide", "Travel Blogger", "Tourism Manager"],
        "books": ["Tourism Management", "The Business of Tourism"],
        "platforms": ["Coursera Tourism", "YouTube Travel", "edX"]
    },
    "fashion design": {
        "careers": ["Fashion Designer", "Stylist", "Fashion Journalist"],
        "books": ["Fashionpedia", "The End of Fashion"],
        "platforms": ["Skillshare Fashion", "Instagram Fashion", "Coursera Fashion"]
    },
    "culinary science": {
        "careers": ["Chef", "Food Scientist", "Nutritionist"],
        "books": ["The Joy of Cooking", "Salt, Fat, Acid, Heat"],
        "platforms": ["YouTube Cooking", "Coursera Culinary Arts", "MasterClass"]
    },
    
    "biochemistry": {
        "careers": ["Biochemist", "Pharmaceutical Scientist", "Lab Researcher"],
        "books": ["Lehninger Principles of Biochemistry", "Biochemistry by Berg"],
        "platforms": ["Coursera Biochemistry", "edX", "YouTube Biochemistry"]
    },
    "ecology": {
        "careers": ["Ecologist", "Conservation Scientist", "Environmental Consultant"],
        "books": ["Ecology by Odum", "The Ecology Book"],
        "platforms": ["Coursera Ecology", "National Geographic", "YouTube Ecology"]
    },
    "statistics": {
        "careers": ["Statistician", "Data Analyst", "Actuary"],
        "books": ["The Elements of Statistical Learning", "Statistics for Engineers"],
        "platforms": ["Khan Academy", "Coursera", "edX"]
    },
    "oceanography": {
        "careers": ["Oceanographer", "Marine Scientist", "Climate Analyst"],
        "books": ["Oceanography: An Invitation to Marine Science"],
        "platforms": ["NOAA", "Coursera Oceanography", "YouTube Ocean Science"]
    },
    "astronomy": {
        "careers": ["Astronomer", "Astrophysicist", "Space Scientist"],
        "books": ["Cosmos", "Astrophysics for People in a Hurry"],
        "platforms": ["NASA", "Coursera Astronomy", "YouTube Astronomy"]
    },
    "archaeology": {
        "careers": ["Archaeologist", "Museum Curator", "Researcher"],
        "books": ["Archaeology: Theories, Methods, and Practice"],
        "platforms": ["Coursera Archaeology", "YouTube Archaeology", "National Geographic"]
    },
    "linguistics": {
        "careers": ["Linguist", "Translator", "Speech Scientist"],
        "books": ["The Power of Babel", "An Introduction to Language"],
        "platforms": ["Coursera Linguistics", "Duolingo", "YouTube Linguistics"]
    },
    "international relations": {
        "careers": ["Diplomat", "Policy Analyst", "International Lawyer"],
        "books": ["International Relations Theories", "The Tragedy of Great Power Politics"],
        "platforms": ["Coursera IR", "edX Global Studies", "YouTube IR"]
    },
    "education": {
        "careers": ["Teacher", "Professor", "Curriculum Designer"],
        "books": ["Pedagogy of the Oppressed", "The Courage to Teach"],
        "platforms": ["Coursera Education", "edX Teaching", "YouTube Teaching"]
    },
    "library science": {
        "careers": ["Librarian", "Archivist", "Information Specialist"],
        "books": ["Foundations of Library and Information Science"],
        "platforms": ["ALA Resources", "Coursera Library Science", "YouTube Libraries"]
    },
    "marketing": {
        "careers": ["Marketing Manager", "Brand Strategist", "Digital Marketer"],
        "books": ["Kotler on Marketing", "Contagious"],
        "platforms": ["Coursera Marketing", "Udemy", "LinkedIn Learning"]
    },
    "finance": {
        "careers": ["Financial Analyst", "Investment Banker", "Portfolio Manager"],
        "books": ["Principles of Corporate Finance", "The Intelligent Investor"],
        "platforms": ["Coursera Finance", "Bloomberg", "Udemy"]
    },
    "supply chain management": {
        "careers": ["Supply Chain Analyst", "Logistics Manager", "Operations Consultant"],
        "books": ["Supply Chain Management: Strategy, Planning, and Operation"],
        "platforms": ["Coursera SCM", "LinkedIn Learning", "Udemy"]
    },
    "human resource management": {
        "careers": ["HR Manager", "Recruiter", "Organizational Consultant"],
        "books": ["Human Resource Management", "Drive"],
        "platforms": ["Coursera HR", "LinkedIn Learning", "Udemy"]
    },
    "hospitality": {
        "careers": ["Hotel Manager", "Chef", "Event Planner"],
        "books": ["Hospitality Management", "The Cornell School of Hotel Administration Handbook"],
        "platforms": ["Coursera Hospitality", "Udemy", "LinkedIn Learning"]
    },
    "tourism": {
        "careers": ["Tour Guide", "Travel Blogger", "Tourism Manager"],
        "books": ["Tourism Management", "The Business of Tourism"],
        "platforms": ["Coursera Tourism", "YouTube Travel", "edX"]
    },
    "fashion design": {
        "careers": ["Fashion Designer", "Stylist", "Fashion Journalist"],
        "books": ["Fashionpedia", "The End of Fashion"],
        "platforms": ["Skillshare Fashion", "Instagram Fashion", "Coursera Fashion"]
    },
    "bioinformatics": {
        "careers": ["Bioinformatician", "Genomics Researcher", "Computational Biologist"],
        "books": ["Bioinformatics: Sequence and Genome Analysis"],
        "platforms": ["Coursera Bioinformatics", "edX", "YouTube Bioinformatics"]
    },
    "nanotechnology": {
        "careers": ["Nanotechnologist", "Materials Scientist", "Researcher"],
        "books": ["Nanotechnology: A Gentle Introduction", "Introduction to Nanoscience"],
        "platforms": ["Coursera Nanotech", "YouTube Nanotechnology", "edX"]
    },
    "climate science": {
        "careers": ["Climate Scientist", "Environmental Analyst", "Policy Advisor"],
        "books": ["The Climate Book", "Climate Change: The Facts"],
        "platforms": ["IPCC Reports", "Coursera Climate Science", "YouTube Climate Change"]
    },
    "robotics": {
        "careers": ["Robotics Engineer", "Automation Specialist", "AI Researcher"],
        "books": ["Robot Building for Beginners", "Introduction to Autonomous Robots"],
        "platforms": ["Arduino", "Raspberry Pi", "Coursera Robotics"]
    },
    "data analytics": {
        "careers": ["Data Analyst", "Business Intelligence Specialist", "Operations Analyst"],
        "books": ["Data Analytics Made Accessible", "Storytelling with Data"],
        "platforms": ["Tableau", "Power BI", "Coursera Data Analytics"]
    },
    "cybersecurity": {
        "careers": ["Cybersecurity Analyst", "Ethical Hacker", "Security Consultant"],
        "books": ["Hacking: The Art of Exploitation", "Cybersecurity Essentials"],
        "platforms": ["HackTheBox", "TryHackMe", "Coursera Cybersecurity"]
    },
    "blockchain": {
        "careers": ["Blockchain Developer", "Crypto Analyst", "FinTech Entrepreneur"],
        "books": ["Mastering Bitcoin", "Blockchain Basics"],
        "platforms": ["Coursera Blockchain", "Udemy Blockchain", "YouTube Crypto"]
    },
    "data science": {
        "careers": ["Data Scientist", "Machine Learning Engineer", "Business Analyst"],
        "books": ["Python for Data Analysis", "Hands-On Machine Learning"],
        "platforms": ["Kaggle", "Coursera Data Science", "edX"]
    },
    "artificial intelligence": {
        "careers": ["AI Engineer", "Research Scientist", "Robotics Specialist"],
        "books": ["Artificial Intelligence: A Modern Approach", "Deep Learning"],
        "platforms": ["TensorFlow", "PyTorch", "Coursera AI"]
    },
    "cybersecurity": {
        "careers": ["Cybersecurity Analyst", "Ethical Hacker", "Security Consultant"],
        "books": ["Hacking: The Art of Exploitation", "Cybersecurity Essentials"],
        "platforms": ["HackTheBox", "TryHackMe", "Coursera Cybersecurity"]
    },
    "blockchain": {
        "careers": ["Blockchain Developer", "Crypto Analyst", "FinTech Entrepreneur"],
        "books": ["Mastering Bitcoin", "Blockchain Basics"],
        "platforms": ["Coursera Blockchain", "Udemy Blockchain", "YouTube Crypto"]
    },
    "public administration": {
        "careers": ["Civil Servant", "Policy Analyst", "Government Officer"],
        "books": ["Public Administration: Understanding Management, Politics, and Law"],
        "platforms": ["Coursera Public Policy", "edX", "YouTube Governance"]
    },
    "physical education": {
        "careers": ["Athlete", "Coach", "Physiotherapist"],
        "books": ["Sports Science Handbook", "The Champion’s Mind"],
        "platforms": ["Nike Training Club", "YouTube Fitness", "Coursera Sports Science"]
    },
    "home science": {
        "careers": ["Nutritionist", "Interior Designer", "Food Scientist"],
        "books": ["Home Science Textbook", "Nutrition Essentials"],
        "platforms": ["YouTube Home Science", "Coursera Nutrition", "Skillshare"]
    },
    "agriculture": {
        "careers": ["Agricultural Scientist", "Farmer", "Agri-Entrepreneur"],
        "books": ["Principles of Agronomy", "The Lean Farm"],
        "platforms": ["YouTube Agriculture", "Coursera Agriculture", "FAO Resources"]
    },
    "medicine": {
        "careers": ["Doctor", "Surgeon", "Medical Researcher"],
        "books": ["Gray’s Anatomy", "Harrison’s Principles of Internal Medicine"],
        "platforms": ["Coursera Medicine", "YouTube Med School Insiders", "edX"]
    },
    "nursing": {
        "careers": ["Nurse", "Healthcare Worker", "Medical Assistant"],
        "books": ["Fundamentals of Nursing", "Essentials of Nursing"],
        "platforms": ["Coursera Nursing", "YouTube Nursing", "edX"]
    },
    "engineering": {
        "careers": ["Mechanical Engineer", "Civil Engineer", "Electrical Engineer"],
        "books": ["Engineering Mechanics", "Introduction to Electrical Engineering"],
        "platforms": ["MIT OpenCourseWare", "Coursera Engineering", "edX"]
    },
    "philosophy": {
        "careers": ["Philosopher", "Professor", "Ethics Consultant"],
        "books": ["Meditations by Marcus Aurelius", "Critique of Pure Reason"],
        "platforms": ["Stanford Encyclopedia of Philosophy", "Coursera Philosophy", "YouTube Philosophy Tube"]
    },
    "literature": {
        "careers": ["Writer", "Editor", "Professor"],
        "books": ["The Norton Anthology of English Literature", "On Writing"],
        "platforms": ["Goodreads", "Coursera Literature", "YouTube Literary Analysis"]
    },
    "law": {
        "careers": ["Lawyer", "Judge", "Legal Consultant"],
        "books": ["Black’s Law Dictionary", "Introduction to Law"],
        "platforms": ["Coursera Law", "edX Legal Studies", "YouTube Legal Eagle"]
    },
    "medicine": {
        "careers": ["Doctor", "Surgeon", "Medical Researcher"],
        "books": ["Gray’s Anatomy", "Harrison’s Principles of Internal Medicine"],
        "platforms": ["Coursera Medicine", "YouTube Med School Insiders", "edX"]
    },
    "arts": {
        "careers": ["Artist", "Designer", "Performer"],
        "books": ["The Story of Art", "Ways of Seeing"],
        "platforms": ["Skillshare", "YouTube Art Channels", "Coursera Arts"]
    },
    "environmental science": {
        "careers": ["Environmental Scientist", "Conservationist", "Ecologist"],
        "books": ["Silent Spring", "Our Common Future"],
        "platforms": ["Coursera Environmental Science", "National Geographic", "edX"]
    }
}
# ---------------- Commands to Add More Data ---------------- #

def add_hobby():
    hobby = input("Enter hobby name: ").lower()
    careers = input("Enter careers (comma separated): ").split(",")
    books = input("Enter books (comma separated): ").split(",")
    platforms = input("Enter platforms (comma separated): ").split(",")
    hobby_career_map[hobby] = {
        "careers": [c.strip() for c in careers],
        "books": [b.strip() for b in books],
        "platforms": [p.strip() for p in platforms]
    }
    print("Hobby added successfully!\n")

def add_subject():
    subject = input("Enter subject name: ").lower()
    careers = input("Enter careers (comma separated): ").split(",")
    books = input("Enter books (comma separated): ").split(",")
    platforms = input("Enter platforms (comma separated): ").split(",")
    subject_career_map[subject] = {
        "careers": [c.strip() for c in careers],
        "books": [b.strip() for b in books],
        "platforms": [p.strip() for p in platforms]
    }
    print("Subject added successfully!\n")

# ---------------- USER INPUT ---------------- #

print("\n------ TALENT FINDER ------\n")

name = input("Enter your name: ")
hobby = input("Enter your hobby: ").lower()
subject = input("Enter your area of interest / subject: ").lower()

scores = {key: 0 for key in personality_data.keys()}

# ---------------- 10 QUESTIONS ---------------- #

questions = [
("1) Important decision?\n1.Decide quickly\n2.Think a lot\n3.Ask others\n4.Avoid\nChoose: ",
 {"1":"Leader","2":"Analytical","3":"Emotionally Intelligent","4":"Adaptable"}),

("2) In group?\n1.Lead\n2.Solve problems\n3.Explain\n4.Quiet\nChoose: ",
 {"1":"Leader","2":"Analytical","3":"Emotionally Intelligent","4":"Creative"}),

("3) If fail?\n1.Try again\n2.Analyze mistake\n3.Feel sad\n4.Stop\nChoose: ",
 {"1":"Disciplined","2":"Analytical","3":"Emotionally Intelligent","4":"Adaptable"}),

("4) Want in life?\n1.Power\n2.Knowledge\n3.Money\n4.Peace\nChoose: ",
 {"1":"Leader","2":"Analytical","3":"Adaptable","4":"Emotionally Intelligent"}),

("5) Stress?\n1.Calm\n2.Overthink\n3.Act fast\n4.Talk\nChoose: ",
 {"1":"Disciplined","2":"Analytical","3":"Leader","4":"Emotionally Intelligent"}),

("6) You are?\n1.Creative\n2.Logical\n3.Caring\n4.Hardworking\nChoose: ",
 {"1":"Creative","2":"Analytical","3":"Emotionally Intelligent","4":"Disciplined"}),

("7) Learn new?\n1.Try\n2.Read\n3.Watch\n4.Friends\nChoose: ",
 {"1":"Leader","2":"Analytical","3":"Creative","4":"Emotionally Intelligent"}),

("8) Risk?\n1.Take\n2.Think\n3.Avoid\n4.Wait\nChoose: ",
 {"1":"Leader","2":"Analytical","3":"Disciplined","4":"Adaptable"}),

("9) People say?\n1.Confident\n2.Smart\n3.Logical\n4.Creative\nChoose: ",
 {"1":"Leader","2":"Emotionally Intelligent","3":"Analytical","4":"Creative"}),

("10) Dream life?\n1.Lead\n2.Settled\n3.Business\n4.Peaceful\nChoose: ",
 {"1":"Leader","2":"Disciplined","3":"Adaptable","4":"Emotionally Intelligent"})
]

for q, mapping in questions:
    ans = input(q)
    if ans in mapping:
        scores[mapping[ans]] += 1

personality = max(scores, key=scores.get)

# ---------------- OUTPUT ---------------- #

print("\n------ RESULT ------")
print("Name:", name)
print("Personality:", personality)
print("Strength:", personality_data[personality]["strength"])
print("Weakness:", personality_data[personality]["weakness"])

# Career Based on Personality
personality_careers = personality_data[personality]["careers"]
print("\nCareer Based on Personality:")
for c in personality_careers:
    print("-", c)

# Career Based on Hobby
hobby_careers = []
print("\nCareer Based on Hobby:")
if hobby in hobby_career_map:
    hobby_careers = hobby_career_map[hobby]["careers"]
    for c in hobby_careers:
        print("-", c)
else:
    print("No data. Use add_hobby() to add.")

# Career Based on Subject
subject_careers = []
print("\nCareer Based on Area of Interest:")
if subject in subject_career_map:
    subject_careers = subject_career_map[subject]["careers"]
    for c in subject_careers:
        print("-", c)
else:
    print("No data. Use add_subject() to add.")

# ---------------- PERFECT MATCH ---------------- #

perfect_match = list(set(personality_careers) & set(hobby_careers) & set(subject_careers))

print("\nPerfect Match Career (Common in All Three Fields):")
if perfect_match:
    for c in perfect_match:
        print("-", c)
else:
    print("No exact common match found. Consider combining skills.")

# ---------------- BOOKS & PLATFORMS SEPARATELY ---------------- #

print("\nBooks Based on Personality:")
for b in personality_data[personality]["books"]:
    print("-", b)

if hobby in hobby_career_map:
    print("\nBooks Based on Hobby:")
    for b in hobby_career_map[hobby]["books"]:
        print("-", b)

if subject in subject_career_map:
    print("\nBooks Based on Subject:")
    for b in subject_career_map[subject]["books"]:
        print("-", b)

print("\nPlatforms Based on Personality:")
for p in personality_data[personality]["platforms"]:
    print("-", p)

if hobby in hobby_career_map:
    print("\nPlatforms Based on Hobby:")
    for p in hobby_career_map[hobby]["platforms"]:
        print("-", p)

if subject in subject_career_map:
    print("\nPlatforms Based on Subject:")
    for p in subject_career_map[subject]["platforms"]:
        print("-", p)

print("\nPlatforms for Perfect Match Career:")
if perfect_match:
    for p in personality_data[personality]["platforms"]:
        print("-", p)
else:
    print("Improve combined skills to get a strong perfect match.")

print("\n------ END ------")
