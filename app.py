import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="GreeTech Career AI", layout="centered")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ==================================================
# ================= HOME SCREEN ====================
# ==================================================

if st.session_state.page == "home":

    st.title("🚀 GreeTech Career AI")
    st.subheader("Your Smart Career + Job Preparation Assistant")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🚀 Career Ready", use_container_width=True, key="home_career"):
            st.session_state.page = "career"
            st.rerun()

    with col2:
        if st.button("💼 Job Ready", use_container_width=True, key="home_job"):
            st.session_state.page = "job"
            st.rerun()

    with col3:
        if st.button("🌍 Green AI", use_container_width=True, key="home_green"):
            st.session_state.page = "green"
            st.rerun()

# ==================================================
# ================= JOB READY ======================
# ==================================================

elif st.session_state.page == "job":

    st.header("💼 Job Ready")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎯 Interview Prep", use_container_width=True, key="job_interview"):
            st.session_state.page = "interview"
            st.rerun()

    with col2:
        if st.button("📝 Mock Test", use_container_width=True, key="job_mock"):
            st.session_state.page = "mock"
            st.rerun()

    st.markdown("---")

    if st.button("⬅ Back to Home", key="job_back"):
        st.session_state.page = "home"
        st.rerun()

# ==================================================
# ================= INTERVIEW PREP =================
# ==================================================

elif st.session_state.page == "interview":

    st.header("🎯 Interview Preparation Roadmap")
    st.markdown("---")

    role = st.selectbox("Select Your Target Role", [
        "Software Developer",
        "Frontend Developer",
        "Data Science / AI",
        "Non-Tech / HR"
    ])

    st.markdown("---")


    # ================= SOFTWARE =================
    if role == "Software Developer":

        st.subheader("💻 Level 1: Core Foundations")
        st.markdown("✔ Revise Data Structures (Array, Linked List, Stack, Queue)")
        st.markdown("✔ Practice Basic Algorithms (Sorting, Searching)")
        st.markdown("✔ Understand Time & Space Complexity")

        st.subheader("💻 Level 2: Coding Practice")
        st.markdown("✔ Solve 100+ DSA Questions")
        st.markdown("✔ Practice Medium Level Problems")
        st.markdown("✔ Learn Basic System Design")

        st.subheader("💻 Level 3: Mock Interviews")
        st.markdown("✔ Attempt Timed Coding Tests")
        st.markdown("✔ Practice Explaining Your Approach")
        st.markdown("✔ Review Weak Topics")

        st.markdown("### 🔗 Best Preparation Platforms")

        st.markdown("""
        - LeetCode: 
          https://leetcode.com/interview/

        - HackerRank:
          https://www.hackerrank.com/

        - GeeksforGeeks:
           https://www.geeksforgeeks.org/
        """)
    # ================= FRONTEND =================
    elif role == "Frontend Developer":

        st.subheader("🌐 Level 1: Web Fundamentals")
        st.markdown("✔ HTML, CSS Basics")
        st.markdown("✔ JavaScript Fundamentals")
        st.markdown("✔ DOM Manipulation")

        st.subheader("🌐 Level 2: Frameworks")
        st.markdown("✔ React Basics")
        st.markdown("✔ Component Lifecycle")
        st.markdown("✔ API Integration")

        st.subheader("🌐 Level 3: Mock Practice")
        st.markdown("✔ Build Small UI Projects")
        st.markdown("✔ Solve JS Logic Problems")

        st.markdown("### 🔗 Best Preparation Platforms")

        st.markdown("""
        - Frontend Mentor:
          https://www.frontendmentor.io/

        - JavaScript Info: 
         https://javascript.info/

        - CodeWars:
           https://www.codewars.com/
        """)

    # ================= DATA SCIENCE =================
    elif role == "Data Science / AI":

        st.subheader("🤖 Level 1: Foundations")
        st.markdown("✔ Python for Data Science")
        st.markdown("✔ Statistics Basics")
        st.markdown("✔ SQL Practice")

        st.subheader("🤖 Level 2: Machine Learning")
        st.markdown("✔ Supervised Learning")
        st.markdown("✔ Model Evaluation")
        st.markdown("✔ Feature Engineering")

        st.subheader("🤖 Level 3: Mock Case Studies")
        st.markdown("✔ Kaggle Mini Projects")
        st.markdown("✔ ML Interview Questions")

        st.markdown("### 🔗 Best Preparation Platforms")

        st.markdown("""
        - Kaggle:
          https://www.kaggle.com/

        - StrataScratch: 
         https://www.stratascratch.com/

        - Interview Query: 
           https://www.interviewquery.com/
        """)


    # ================= NON TECH =================
    elif role == "Non-Tech / HR":

        st.subheader("🧾 Level 1: Aptitude")
        st.markdown("✔ Quantitative Aptitude")
        st.markdown("✔ Logical Reasoning")
        st.markdown("✔ Verbal Ability")

        st.subheader("🧾 Level 2: Communication")
        st.markdown("✔ HR Questions Practice")
        st.markdown("✔ Mock Self Introduction")

        st.subheader("🧾 Level 3: Mock Round")
        st.markdown("✔ Practice Case Studies")
        st.markdown("✔ Confidence Building")

        st.markdown("### 🔗 Best Preparation Platforms")

        st.markdown("""
        - IndiaBix:
          https://www.indiabix.com/

        - AssessmentDay:
         https://www.assessmentday.co.uk/

        - Pramp:
          https://www.pramp.com/#/
        """)


    st.markdown("---")

    if st.button("⬅ Back to Job Ready", key="back_interview"):
        st.session_state.page = "job"
        st.rerun()

# ==================================================
# ================= MOCK TEST ======================
# ==================================================

elif st.session_state.page == "mock":

    st.header("📝 Role-Based Mock Test Preparation")
    st.markdown("---")

    role = st.selectbox("Select Your Target Role", [
        "Software Developer",
        "Frontend Developer",
        "Data Science / AI",
        "Non-Tech / HR"
    ])

    st.markdown("---")

    # ================= SOFTWARE =================
    if role == "Software Developer":

        st.subheader("💻 Software Developer Mock Tests")

        st.markdown("""
        🔹 DSA Timed Practice  
        🔹 Coding Round Simulation  
        🔹 System Design Basics  
        🔹 Debugging Round  
        """)

        st.markdown("### 🔗 Best Platforms")

        st.markdown("""
        - LeetCode Mock Interview  
          https://leetcode.com/interview/

        - HackerRank Skill Test  
          https://www.hackerrank.com/skills-verification

        - CodeStudio Mock Tests  
          https://www.codingninjas.com/codestudio
        """)

    # ================= FRONTEND =================
    elif role == "Frontend Developer":

        st.subheader("🌐 Frontend Developer Mock Tests")

        st.markdown("""
        🔹 HTML/CSS Practical Tasks  
        🔹 JavaScript Logic Test  
        🔹 React Component Challenges  
        🔹 UI Debugging Round  
        """)

        st.markdown("### 🔗 Best Platforms")

        st.markdown("""
        - Frontend Mentor Challenges  
          https://www.frontendmentor.io/

        - JavaScript Challenges  
          https://www.jschallenger.com/

        - CodeWars Practice  
          https://www.codewars.com/
        """)

    # ================= DATA SCIENCE =================
    elif role == "Data Science / AI":

        st.subheader("🤖 Data Science / AI Mock Tests")

        st.markdown("""
        🔹 Python Coding Test  
        🔹 ML Concept Questions  
        🔹 Case Study Round  
        🔹 SQL + Data Analysis  
        """)

        st.markdown("### 🔗 Best Platforms")

        st.markdown("""
        - Kaggle Competitions  
          https://www.kaggle.com/

        - StrataScratch SQL Practice  
          https://www.stratascratch.com/

        - Interview Query  
          https://www.interviewquery.com/
        """)

    # ================= NON TECH =================
    elif role == "Non-Tech / HR":

        st.subheader("🧾 Non-Technical Mock Tests")

        st.markdown("""
        🔹 Aptitude Test  
        🔹 Communication Round  
        🔹 Case Study Practice  
        🔹 Behavioral Questions  
        """)

        st.markdown("### 🔗 Best Platforms")

        st.markdown("""
        - IndiaBix Aptitude  
          https://www.indiabix.com/

        - AssessmentDay Practice  
          https://www.assessmentday.co.uk/

        - Pramp Mock Interviews  
          https://www.pramp.com/
        """)

    st.markdown("---")

    if st.button("⬅ Back to Job Ready"):
        st.session_state.page = "job"
        st.rerun()

# ==================================================
# ================= GREEN AI DASHBOARD =============
# ==================================================

elif st.session_state.page == "green":

    import datetime
    import random

    # ---------- THEME ----------
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🌿 Green AI Dashboard")
    st.markdown("---")

    today = datetime.date.today()

    if "usage_data" not in st.session_state:
        st.session_state.usage_data = {}

    if today not in st.session_state.usage_data:
        st.session_state.usage_data[today] = 0

    # Increment usage
    st.session_state.usage_data[today] += 1

    st.success(f"📊 Today's Usage Count: {st.session_state.usage_data[today]}")

    st.markdown("---")

    # ================= ECO MODE =================
    st.subheader("⚡ Eco Mode")

    eco_mode = st.toggle("Enable Eco Mode")

    if eco_mode:
        st.success("🌱 Eco Mode Activated (Low Energy Mode)")
        our_ai_usage_percent = random.randint(40, 60)   # Reduced usage
    else:
        st.info("Running in Normal Performance Mode")
        our_ai_usage_percent = random.randint(70, 90)

    # Simulated Normal AI baseline
    normal_ai_usage_percent = 100

    st.markdown("---")
    st.subheader("📊 AI Energy Usage Comparison")

    st.metric("🤖 Normal AI Usage (%)", f"{normal_ai_usage_percent}%")
    st.metric("🌿 Our Green AI Usage (%)", f"{our_ai_usage_percent}%")

    saved_percent = normal_ai_usage_percent - our_ai_usage_percent

    st.metric("♻ Energy Saved (%)", f"{saved_percent}%")

    st.markdown("---")

    if st.button("⬅ Back to Home", key="green_back_btn"):
        st.session_state.page = "home"
        st.rerun()

# ==================================================
# 🚀 CAREER READY SCREEN
# ==================================================

elif st.session_state.page == "career":

    st.header("🚀 Career Ready")

    career = st.selectbox(
        "👉 Choose your career:",
        ["Software Engineer",
         "AI / ML Engineer",
         "Python Developer",
         "DevOps Engineer",
         "Web Developer"]
    )

    skills = st.multiselect(
        "👉 What skills do you already know?",
        ["C", "C++", "Java", "Python",
         "HTML", "JavaScript",
         "R", "SQL", "Bash", "YAML"]
    )

    required = {
        "Software Engineer": ["Python", "Java", "SQL"],
        "AI / ML Engineer": ["Python", "R", "SQL"],
        "Python Developer": ["Python", "SQL"],
        "DevOps Engineer": ["Bash", "YAML", "SQL"],
        "Web Developer": ["HTML", "JavaScript"]
    }

    to_learn = list(set(required.get(career, [])) - set(skills))

    st.markdown("### ✔ Known Skills")
    st.write(skills if skills else "None")

    st.markdown("### ❌ Skills To Learn")
    st.write(to_learn if to_learn else "You are ready!")

    language = st.selectbox(
        "👉 Which language do you want to learn now?",
        ["Python", "HTML", "JavaScript", "R", "SQL", "Bash", "YAML"]
    )

    if st.button("Start Game Mode"):
        st.session_state.learn_lang = language
        st.session_state.level = 1
        st.session_state.page = "game"
        st.rerun()

    if st.button("EXIT"):
        st.stop()


# ==================================================
# 🎮 GAME MODE (MCQ SYSTEM)
# ==================================================

elif st.session_state.page == "game":

    lang = st.session_state.learn_lang
    level = st.session_state.level

    st.title(f"🎮 Game Mode: {lang}")
    st.markdown(f"### Level {level}")

    # ---------------- QUESTIONS ----------------

    if lang == "Python":
        questions = [
            {"q": "What is Python?", "options": ["Programming Language", "Database", "Browser"], "ans": "Programming Language"},
            {"q": "Variable is?", "options": ["Storage Box", "Loop", "Condition"], "ans": "Storage Box"},
            {"q": "Which is loop?", "options": ["for", "print", "input"], "ans": "for"},
            {"q": "Function is?", "options": ["Reusable Code", "Error", "File"], "ans": "Reusable Code"},
            {"q": "Dictionary stores?", "options": ["Key-Value", "Only Number", "Only Text"], "ans": "Key-Value"},
        ]

    elif lang == "HTML":
        questions = [
            {"q": "HTML builds?", "options": ["Structure", "Server", "Database"], "ans": "Structure"},
            {"q": "Biggest heading?", "options": ["h1", "h6", "p"], "ans": "h1"},
            {"q": "Link tag?", "options": ["a", "img", "ul"], "ans": "a"},
        ]

    elif lang == "JavaScript":
        questions = [
            {"q": "JS makes site?", "options": ["Interactive", "Static", "Offline"], "ans": "Interactive"},
            {"q": "Variable keyword?", "options": ["let", "html", "sql"], "ans": "let"},
            {"q": "Event example?", "options": ["onclick", "for", "div"], "ans": "onclick"},
        ]

    elif lang == "R":
        questions = [
            {"q": "R used for?", "options": ["Data Analysis", "Gaming", "Animation"], "ans": "Data Analysis"},
            {"q": "Assignment operator?", "options": ["<-", "=", "=="], "ans": "<-"},
        ]

    elif lang == "SQL":
        questions = [
            {"q": "SELECT does?", "options": ["Fetch Data", "Delete", "Stop"], "ans": "Fetch Data"},
            {"q": "JOIN does?", "options": ["Combine Tables", "Loop", "Break"], "ans": "Combine Tables"},
        ]

    elif lang == "Bash":
        questions = [
            {"q": "ls command?", "options": ["List files", "Delete", "Create"], "ans": "List files"},
            {"q": "cd command?", "options": ["Change directory", "Print", "Loop"], "ans": "Change directory"},
        ]

    else:  # YAML
        questions = [
            {"q": "YAML used for?", "options": ["Configuration", "Game", "AI"], "ans": "Configuration"},
            {"q": "Structure based on?", "options": ["Indentation", "Tags", "Brackets"], "ans": "Indentation"},
        ]

    # ---------------- QUESTION FLOW ----------------

    if level <= len(questions):

        current_q = questions[level - 1]
        answer = st.radio(current_q["q"], current_q["options"])

        if st.button("Submit Answer"):

            if answer == current_q["ans"]:
                st.success("Correct! 🎉")

                if level < len(questions):
                    st.session_state.level += 1
                    st.rerun()
                else:
                    st.success("🎉 You Completed All Levels!")
                    st.markdown("### 💪 You are stronger than yesterday. Build projects daily!")
                    st.balloons()

            else:
                st.error("Wrong Answer. Try Again.")

    if st.button("⬅ Back to Career"):
        st.session_state.page = "career"
        st.rerun()

    if st.button("⬅ Back to Home Screen"):
        st.session_state.page = "home"
        st.rerun()
    
    if st.button("EXIT"):
        st.session_state.page = "home"
        st.rerun()
    