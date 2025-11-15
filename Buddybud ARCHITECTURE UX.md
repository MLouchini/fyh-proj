# **COMPLETE UX FLOW - Code-Based Architecture**

---

## **ARCHITECTURE OVERVIEW**

**Two User Types:**
1. **Teachers** - Create homework codes with questions/mark schemes
2. **Students** - Enter code, submit answers, get verified

**Flow Split:**
- Teacher Portal: Create homework → Generate code → View student results
- Student Portal: Enter code → Submit answers → Get feedback & interview → See results

---

# **STUDENT FLOW**

---

## **STAGE 1: Welcome & Code Entry**

### **Full Desktop Screen Layout**

**HEADER (Top bar - full width):**
```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Study Session        [My Reviews] [Resources] [Help] │
└─────────────────────────────────────────────────────────────┘
```

**MAIN CONTENT (Split 60/40):**

**LEFT SIDE (60%):**
```
┌─────────────────────────────────────────────┐
│  Ready to submit your homework?             │
│  Enter your homework code to get started    │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │                                       │ │
│  │    Enter Homework Code                │ │
│  │    ┌───────────────────────────────┐  │ │
│  │    │ PHY-2024-A3B7                 │  │ │
│  │    └───────────────────────────────┘  │ │
│  │                                       │ │
│  │    [Load Homework →]                  │ │
│  │                                       │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  Example codes:                             │
│  • PHY-2024-A3B7 (Physics A-Level)         │
│  • CHE-2024-X9P2 (Chemistry GCSE)          │
│                                             │
│  ─────────────────────────────────────────  │
│                                             │
│  What happens next:                         │
│  📝 Submit Your Answers                     │
│  Upload or type your homework responses     │
│                                             │
│  💬 Quick Understanding Check               │
│  Brief chat about your approach             │
│                                             │
│  📊 Get Detailed Feedback                   │
│  See where you excelled and can improve     │
└─────────────────────────────────────────────┘
```

**RIGHT SIDE (40%) - Animated Illustrations:**
```
┌─────────────────────────────────────┐
│                                     │
│     [Floating 3D elements]          │
│                                     │
│   🎓 (gently rotating)              │
│                                     │
│         📚 (bobbing up/down)        │
│                                     │
│    ✨ (twinkling particles)         │
│                                     │
│         💡 (pulsing glow)           │
│                                     │
│  "Join 10,000+ students improving   │
│   their understanding"              │
│                                     │
│  ⭐⭐⭐⭐⭐                            │
│  "This helped me identify gaps      │
│   I didn't know I had!"             │
│  - Sarah, Physics Student           │
│                                     │
│  [Recent activity feed]             │
│  • 23 students completed reviews    │
│    today                            │
│  • Average improvement: 15%         │
│                                     │
└─────────────────────────────────────┘
```

**BACKGROUND:** Subtle gradient (purple-blue) with floating particle effects, abstract geometric shapes slowly drifting

---

## **STAGE 1B: Homework Loaded**

### **After entering valid code:**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Study Session    Homework: PHY-2024-A3B7    [Help]   │
└─────────────────────────────────────────────────────────────┘
```

**TOP BANNER (Full width):**
```
┌───────────────────────────────────────────────────────────┐
│  📋 Physics A-Level Practice Exam                         │
│  Mr. Johnson's Class | Due: Nov 20, 2024                  │
│                                                           │
│  5 Questions • Total: 60 marks • Topics: Mechanics,       │
│  Thermodynamics, Waves, EM, Quantum                       │
└───────────────────────────────────────────────────────────┘
```

**MAIN CONTENT (Split):**

**LEFT SIDE (65%):**
```
┌─────────────────────────────────────────────┐
│  Upload Your Answers                        │
│                                             │
│  You can submit your work in multiple ways: │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │         📄                            │ │
│  │    Drop your answer sheet here        │ │
│  │    or click to browse                 │ │
│  │                                       │ │
│  │    Supports: PDF, Images, DOCX        │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  OR                                         │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │ ⌨️ Type your answers directly        │ │
│  │                                       │ │
│  │ [Click to expand text editor]         │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  [Submit Answers →]                         │
└─────────────────────────────────────────────┘
```

**RIGHT SIDE (35%):**
```
┌──────────────────────────────┐
│ 📖 Question Preview          │
│                              │
│ Q1: Newton's Laws (10 marks) │
│ Q2: Thermodynamics (15)      │
│ Q3: Wave Motion (12)         │
│ Q4: Electromagnetism (13)    │
│ Q5: Quantum Mechanics (10)   │
│                              │
│ ─────────────────            │
│                              │
│ [View Full Questions]        │
│ (Opens in new tab)           │
│                              │
│ ─────────────────            │
│                              │
│ 💡 Tips:                     │
│ • Show your working          │
│ • Label diagrams clearly     │
│ • Include units              │
│                              │
│ [Animated floating           │
│  study icons]                │
└──────────────────────────────┘
```

---

## **STAGE 2: Review in Progress**

### **Full Desktop Screen**

*(SAME AS ORIGINAL - No changes needed)*

**CENTERED HERO SECTION:**
```
┌───────────────────────────────────────────────┐
│                                               │
│           [Animated book opening]             │
│        [Pages turning with sparkles]          │
│                                               │
│      Reviewing your homework...               │
│      this takes about 2 minutes               │
│                                               │
│           [Elegant spinner]                   │
│                                               │
└───────────────────────────────────────────────┘
```

**BOTTOM SECTION - Rotating Tips:**
```
┌───────────────────────────────────────────────┐
│  💡 Tip: Active recall is more effective      │
│     than re-reading                           │
└───────────────────────────────────────────────┘
```

**LEFT SIDE (Subtle):**
```
┌──────────────────┐
│   [Abstract      │
│    animated      │
│    patterns]     │
│                  │
│   [Floating      │
│    formulas:     │
│    F=ma,         │
│    E=mc²]        │
│                  │
│   [Gently        │
│    drifting]     │
└──────────────────┘
```

**RIGHT SIDE (Subtle):**
```
┌──────────────────┐
│   [Animated      │
│    checkmarks    │
│    appearing]    │
│                  │
│   [Progress      │
│    circles       │
│    filling]      │
│                  │
│   [Particles     │
│    flowing]      │
└──────────────────┘
```

**BACKGROUND:** Animated gradient shift, subtle wave patterns moving across screen

---

## **STAGE 3: Initial Feedback Report**

### **Full Desktop Layout**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [← Back] Your Feedback Report          [Download PDF] [Share]│
│ Homework: PHY-2024-A3B7 | Mr. Johnson's Class               │
└─────────────────────────────────────────────────────────────┘
```
Full Desktop Layout
HEADER:
┌─────────────────────────────────────────────────────────────┐
│ [← Back] Your Feedback Report          [Download PDF] [Share]│
└─────────────────────────────────────────────────────────────┘
TOP BANNER (Full width, gradient background):
┌───────────────────────────────────────────────────────────┐
│  🎉 Great effort! You scored 75%                          │
│  That's a solid B grade - well done!                      │
│                                                           │
│  📊 45/60 marks                                           │
│                                                           │
│  [Animated confetti particles falling]                   │
└───────────────────────────────────────────────────────────┘
MAIN CONTENT AREA (Three columns):
LEFT SIDEBAR (20%) - Always visible:
┌──────────────────────┐
│ 📊 Overview          │
│                      │
│ Total: 75%           │
│ Grade: B             │
│                      │
│ ─────────────        │
│                      │
│ Jump to:             │
│ • Q1: Newton's ✓     │
│ • Q2: Thermo ✓       │
│ • Q3: Waves ✓        │
│ • Q4: EM ⚠           │
│ • Q5: Quantum ⚠      │
│                      │
│ ─────────────        │
│                      │
│ 💪 Strengths         │
│ • Force analysis     │
│ • Heat transfer      │
│ • Wave equations     │
│                      │
│ 🎯 Focus On          │
│ • EM fields          │
│ • Quantum concepts   │
│                      │
│ [Quick Links ▼]      │
└──────────────────────┘
CENTER CONTENT (60%) - Scrollable:
┌─────────────────────────────────────────────┐
│ Question 1: Newton's Laws                   │
│ ⭐⭐⭐⭐☆ 8/10 marks                          │
│                                             │
│ [Animated progress bar filling to 80%]      │
│                                             │
│ ✅ What you nailed:                         │
│ • Perfect application of F=ma               │
│ • Clear free-body diagram                   │
│ • Good understanding of force components    │
│                                             │
│ 💡 Room to grow:                            │
│ • Watch calculation errors in part (c)      │
│ • Double-check unit conversions             │
│                                             │
│ [📖 Review Newton's Laws] [Show my answer]  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Question 2: Thermodynamics                  │
│ ⭐⭐⭐⭐⭐ 12/15 marks                         │
│                                             │
│ [Animated progress bar filling to 80%]      │
│                                             │
│ ✅ What you nailed:                         │
│ • Excellent grasp of heat transfer          │
│ • Clear explanation of entropy concept      │
│ • Strong diagram skills                     │
│                                             │
│ 💡 Room to grow:                            │
│ • Could elaborate more on entropy changes   │
│                                             │
│ [📖 Review Thermodynamics] [Show my answer] │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Question 3: Wave Motion                     │
│ ⭐⭐⭐⭐☆ 10/12 marks                         │
│                                             │
│ [Animated progress bar filling to 83%]      │
│                                             │
│ ✅ What you nailed:                         │
│ • Good application of wave equations        │
│ • Formula derivation was clear              │
│ • Correct frequency calculations            │
│                                             │
│ 💡 Room to grow:                            │
│ • Include units in intermediate steps       │
│                                             │
│ [📖 Review Wave Motion] [Show my answer]    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Question 4: Electromagnetism                │
│ ⭐⭐⭐☆☆ 9/13 marks                          │
│                                             │
│ [Animated progress bar filling to 69%]      │
│                                             │
│ ✅ What you nailed:                         │
│ • Correct formula application               │
│ • Good attempt at field direction           │
│                                             │
│ 💡 Room to grow:                            │
│ • Missed relationship between B-field       │
│   and current                               │
│ • Right-hand rule application unclear       │
│                                             │
│ [📖 Review Electromagnetism] [Show my answer]│
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Question 5: Quantum Mechanics               │
│ ⭐⭐⭐☆☆ 6/10 marks                          │
│                                             │
│ [Animated progress bar filling to 60%]      │
│                                             │
│ ✅ What you nailed:                         │
│ • Basic concepts present                    │
│ • Correct equation usage                    │
│                                             │
│ 💡 Room to grow:                            │
│ • Lacks depth in wave-particle duality      │
│ • Explanation of photon behavior unclear    │
│                                             │
│ [📖 Review Quantum Mechanics] [Show my answer]│
└─────────────────────────────────────────────┘
RIGHT SIDEBAR (20%) - Decorative/Animated:
┌──────────────────────────────┐
│ [Animated trophy rotating]   │
│                              │
│ "75% - Well Done!"           │
│                              │
│ [Floating achievement badges]│
│                              │
│ 🏆 Completed Review          │
│ ✨ 5 Questions Analyzed      │
│ 💪 2 Strong Areas            │
│                              │
│ ──────────────               │
│                              │
│ [Abstract animated patterns] │
│ [Particles drifting]         │
│                              │
│ ──────────────               │
│                              │
│ Recent activity:             │
│ ✓ Physics Review - Today     │
│ ✓ Chemistry - 3 days ago     │
│                              │
└──────────────────────────────┘
BOTTOM CALL-TO-ACTION (Full width, distinct section):
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  🎁 Unlock Deeper Insights!                               │
│                                                           │
│  Want personalized feedback on your thinking?             │
│  Let's have a quick 5-minute chat about your approach.    │
│  This helps me understand how you learn so I can give     │
│  you better study tips!                                   │
│                                                           │
│  What happens:                                            │
│  • I'll ask about your approach (2-3 questions)           │
│  • We'll explore key concepts (2-3 questions)             │
│  • You'll get customized learning insights                │
│                                                           │
│  [Animated sparkles around button]                        │
│  [✨ Start My Review Session]  [Skip for now]             │
│                                                           │
│  [Background: Gradient purple-blue with subtle animation] │
└───────────────────────────────────────────────────────────┘
BACKGROUND: Soft gradient, subtle grid pattern, occasional floating particles

---

## **STAGES 4-7: Interview & Final Results**

STAGE 4: Interview Preparation
Full Desktop Layout
CENTERED MODAL (Overlay with blur background):
LEFT SIDE (50%):
┌─────────────────────────────────────────┐
│  👋 Quick Setup                         │
│                                         │
│  This 5-minute session helps me         │
│  understand your thinking better!       │
│                                         │
│  ──────────────────────────────────     │
│                                         │
│  System Check:                          │
│  ✓ Camera detected                      │
│  ✓ Microphone detected                  │
│  ✓ Lighting: Good                       │
│  ⚠ Background noise detected            │
│     Try a quieter space if possible     │
│                                         │
│  ──────────────────────────────────     │
│                                         │
│  I'll ask you to:                       │
│  • Explain your approach (2 questions)  │
│  • Explore concepts (3 questions)       │
│                                         │
│  From topics:                           │
│  • Electromagnetism                     │
│  • Quantum Mechanics                    │
│  • Thermodynamics                       │
│                                         │
│  ──────────────────────────────────     │
│                                         │
│  💡 Tips for success:                   │
│  • Find a quiet spot                    │
│  • Explain like teaching a friend       │
│  • Take your time - no rush             │
│                                         │
│  [Start Review Session →]               │
└─────────────────────────────────────────┘
RIGHT SIDE (50%):
┌─────────────────────────────────────────┐
│                                         │
│     [Live webcam preview - large]       │
│     [Shows student's face]              │
│                                         │
│     [Subtle frame with indicators]      │
│                                         │
│     "You look great! 👍"                │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  [Animated icons floating]              │
│  🎤 💡 📹 ✨                            │
│                                         │
│  "This helps us give you                │
│   personalized feedback"                │
│                                         │
│  [Sample question preview bubble]       │
│  "Walk me through how you               │
│   solved Question 4..."                 │
│                                         │
└─────────────────────────────────────────┘
BACKGROUND: Blurred version of previous screen + dark overlay

STAGE 5: Interview Session
Full Desktop Layout
HEADER (Minimal, top bar):
┌─────────────────────────────────────────────────────────────┐
│  ⚫ ⚫ ⚪ ⚪ ⚪    Question 2 of 5             [Minimize] [Exit]│
└─────────────────────────────────────────────────────────────┘
MAIN SPLIT LAYOUT:
LEFT SIDE (40%) - Video Feed:
┌────────────────────────────────────┐
│                                    │
│                                    │
│     [Large webcam feed]            │
│     [Student's face]               │
│                                    │
│                                    │
│                                    │
│  ──────────────────────────────    │
│                                    │
│  Your Turn to Explain 💬           │
│                                    │
│  [Subtle animated border pulse]    │
└────────────────────────────────────┘
RIGHT SIDE (60%) - Question Display:
FOR PROCESS QUESTIONS:
┌─────────────────────────────────────────┐
│                                         │
│  🔧 YOUR APPROACH                       │
│                                         │
│  Walk me through how you calculated     │
│  the magnetic field strength in Q4.     │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  ▼ Reference: What you wrote            │
│  [Expandable card showing their answer] │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  💭 Think about:                        │
│  • What steps did you take?             │
│  • Which formulas did you use?          │
│  • How did you know which approach?     │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  [Animated floating icons: 📐 📊 ✏️]   │
│                                         │
│                                         │
│                                         │
│          [Next Question →]              │
│                                         │
│  Take your time - explain in your own   │
│  words                                  │
└─────────────────────────────────────────┘
FOR CONCEPT QUESTIONS:
┌─────────────────────────────────────────┐
│                                         │
│  💡 UNDERSTANDING CHECK                 │
│                                         │
│  If we doubled the current in that wire,│
│  what would happen to the magnetic      │
│  field? Why?                            │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  This explores:                         │
│  Relationship between current and       │
│  magnetic field                         │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  💭 Think about:                        │
│  • What's the underlying principle?     │
│  • What equation governs this?          │
│  • Can you visualize what happens?      │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  [Animated diagram: Wire with current   │
│   and magnetic field lines]             │
│                                         │
│                                         │
│          [Next Question →]              │
│                                         │
│  Explain the physics behind it          │
└─────────────────────────────────────────┘
BOTTOM DECORATION:
[Subtle ambient particles floating across bottom of screen]
[Abstract wave pattern animation]
BACKGROUND: Dark gradient (navy to deep purple), creates focus on video and question

TRANSITION BETWEEN QUESTIONS:
Full Screen (2 seconds):
┌───────────────────────────────────────────────┐
│                                               │
│                                               │
│           Great explanation! ✨               │
│                                               │
│         Next question coming up...            │
│                                               │
│         [Animated checkmark growing]          │
│         [Sparkle particles]                   │
│                                               │
│                                               │
└───────────────────────────────────────────────┘

STAGE 6: Post-Interview Processing
Full Desktop Layout
CENTERED CONTENT:
┌───────────────────────────────────────────────┐
│                                               │
│     [Their face thumbnail with sparkles]      │
│                                               │
│   Thanks! Putting together your               │
│   personalized insights...                    │
│                                               │
│   [Elegant loading animation]                 │
│   [Progress circle filling]                   │
│                                               │
└───────────────────────────────────────────────┘
LEFT SIDE (Animated):
┌──────────────────┐
│  [Floating       │
│   transcript     │
│   snippets]      │
│                  │
│  "...magnetic    │
│   field..."      │
│                  │
│  [Fading in/out] │
└──────────────────┘
RIGHT SIDE (Animated):
┌──────────────────┐
│  [Animated       │
│   analysis       │
│   icons]         │
│                  │
│  ✓ Understanding │
│  ✓ Clarity       │
│  ⏳ Depth        │
│                  │
└──────────────────┘
BACKGROUND: Soft animations, particles connecting, subtle glow effects

STAGE 7: Complete Results Dashboard
Full Desktop Layout
HEADER:
┌─────────────────────────────────────────────────────────────┐
│ [← Back] Your Complete Learning Profile    [Download] [Share]│
└─────────────────────────────────────────────────────────────┘
TOP BANNER (Full width, animated gradient):
┌───────────────────────────────────────────────────────────┐
│  📊 YOUR COMPLETE SCORE                                   │
│                                                           │
│  Written Exam: 75% (45/60)                                │
│  Understanding Check: 80% (Great insights!)               │
│                                                           │
│  Overall Assessment: Strong B Grade 🎉                    │
│                                                           │
│  [Animated progress rings showing both scores]            │
│  [Sparkle effects on higher score]                        │
└───────────────────────────────────────────────────────────┘
TAB NAVIGATION (Full width):
┌───────────────────────────────────────────────────────────┐
│  [📝 Written Feedback]  [💬 Understanding Check]  [📈 Study Plan]│
│   ═══════════════                                         │
└───────────────────────────────────────────────────────────┘

TAB 1: WRITTEN FEEDBACK
THREE COLUMN LAYOUT:
LEFT SIDEBAR (20%):
┌──────────────────────┐
│ Quick Nav            │
│                      │
│ • Q1: Newton's ✓     │
│ • Q2: Thermo ✓       │
│ • Q3: Waves ✓        │
│ • Q4: EM ⚠           │
│ • Q5: Quantum ⚠      │
│                      │
│ ─────────────        │
│                      │
│ Filter:              │
│ □ Show all           │
│ □ Needs work only    │
│ □ Strong areas       │
│                      │
│ ─────────────        │
│                      │
│ [Animated            │
│  achievement         │
│  badges]             │
│                      │
│ 🏆 5/5 Reviewed      │
│ ⭐ 75% Score         │
└──────────────────────┘
CENTER CONTENT (55%) - Scrollable:
┌─────────────────────────────────────────────┐
│ Question 1: Newton's Laws                   │
│ ⭐⭐⭐⭐☆ 8/10 marks                          │
│                                             │
│ [Animated progress bar - 80%]               │
│                                             │
│ ✅ What you nailed:                         │
│ • Perfect application of F=ma               │
│ • Clear free-body diagram                   │
│ • Good understanding of force components    │
│                                             │
│ 💡 Room to grow:                            │
│ • Watch calculation errors in part (c)      │
│ • Double-check unit conversions             │
│                                             │
│ [📖 Review Newton's Laws] [Show my answer]  │
└─────────────────────────────────────────────┘

[Same format for all questions...]

┌─────────────────────────────────────────────┐
│ Question 4: Electromagnetism                │
│ ⭐⭐⭐☆☆ 9/13 marks                          │
│                                             │
│ [Animated progress bar - 69%]               │
│                                             │
│ ✅ What you nailed:                         │
│ • Correct formula application               │
│ • Good attempt at field direction           │
│                                             │
│ 💡 Room to grow:                            │
│ • Missed relationship between B-field       │
│   and current                               │
│ • Right-hand rule application unclear       │
│                                             │
│ 💬 From our chat:                           │
│ You explained the calculation well, but     │
│ struggled with the conceptual "why" behind  │
│ the field direction. Let's strengthen this! │
│                                             │
│ [📖 Review Electromagnetism] [Show my answer]│
└─────────────────────────────────────────────┘
RIGHT SIDEBAR (25%) - Interactive & Animated:
┌────────────────────────────────┐
│ [Animated circular chart]      │
│                                │
│     75%                        │
│   Overall                      │
│                                │
│ [Breakdown ring chart:         │
│  showing % per topic]          │
│                                │
│ ──────────────                 │
│                                │
│ 💪 Your Strengths              │
│ • Force analysis               │
│ • Heat transfer                │
│ • Wave equations               │
│                                │
│ [Animated checkmarks           │
│  appearing]                    │
│                                │
│ ──────────────                 │
│                                │
│ 🎯 Focus Areas                 │
│ • EM fields                    │
│ • Quantum concepts             │
│                                │
│ [Pulsing highlight on          │
│  priority items]               │
│                                │
│ ──────────────                 │
│                                │
│ [Floating abstract             │
│  decorative elements]          │
│                                │
│ [Subtle particle effects]      │
│                                │
└────────────────────────────────┘

TAB 2: UNDERSTANDING CHECK
FULL WIDTH HERO CARD:
┌──────────────────────────────────────────────────────────┐
│ 🎯 YOUR LEARNING STRENGTHS                               │
│                                                          │
│ Based on your 5-minute review session                    │
│                                                          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                          │
│ 🔧 Problem-Solving Skills: 85%                          │
│ ████████████████████████░░░░░░░░                         │
│ Excellent! You can apply formulas and follow             │
│ procedures confidently.                                  │
│                                                          │
│ 💡 Conceptual Understanding: 70%                        │
│ ██████████████████░░░░░░░░░░░░░░                         │
│ Good foundation. Let's deepen your grasp of *why*        │
│ things work the way they do.                             │
│                                                          │
│ 🎨 Creative Application: 75%                            │
│ ███████████████████░░░░░░░░░░░░░                         │
│ Nice! You can adapt knowledge to new scenarios with      │
│ some guidance.                                           │
│                                                          │
│ [Animated bars filling on page load]                     │
└──────────────────────────────────────────────────────────┘
TWO COLUMN LAYOUT BELOW:
LEFT COLUMN (50%):
┌─────────────────────────────────────────────┐
│ 📊 WRITTEN vs VERBAL INSIGHTS               │
│                                             │
│ Interesting pattern detected!               │
│                                             │
│ [Animated comparison bars]                  │
│                                             │
│  Written:  ████████████████░░ 75%           │
│  Verbal:   ███████████████████ 80%          │
│                                             │
│ You scored HIGHER when explaining verbally! │
│                                             │
│ This suggests:                              │
│ ✓ You understand concepts well              │
│ ⚠ Work on translating thoughts to paper     │
│                                             │
│ 💡 Recommendation:                          │
│ Practice writing out explanations before    │
│ exams. Try teaching concepts to a friend!   │
│                                             │
│ [📚 Guide: Better Exam Writing] ───→        │
└─────────────────────────────────────────────┘
RIGHT COLUMN (50%):
┌─────────────────────────────────────────┐
│ 🎤 INTERVIEW HIGHLIGHTS                 │
│                                         │
│ What stood out in your explanations:    │
│                                         │
│ ✨ Strong moments:                      │
│ • Thermodynamics entropy explanation    │
│   was excellent                         │
│ • Clear step-by-step thinking on Q1     │
│ • Good use of analogies                 │
│                                         │
│ 💭 Areas to develop:                    │
│ • Magnetic field direction reasoning    │
│ • Wave-particle duality explanation     │
│                                         │
│ [Animated speech bubbles with quotes    │
│  from their responses]                  │
│                                         │
│ "The heat flows from hot to cold        │
│  because..." ✓                          │
│                                         │
└─────────────────────────────────────────┘
BOTTOM SECTION - TOPIC BREAKDOWN (Full width, cards):
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ Thermodynamics   │  │ Electromagnetism │  │ Quantum Mechanics│
│ Written: ⭐⭐⭐⭐⭐ │  │ Written: ⭐⭐⭐☆☆  │  │ Written: ⭐⭐⭐☆☆  │
│ Verbal:  ⭐⭐⭐⭐⭐ │  │ Verbal:  ⭐⭐⭐☆☆  │  │ Verbal:  ⭐⭐⭐☆☆  │
│                  │  │                  │  │                  │
│ You clearly      │  │ This is a genuine│  │ Basic concepts   │
│ understand heat  │  │ gap. Follow      │  │ present

---

---

# **TEACHER FLOW**

---

## **TEACHER DASHBOARD - Landing Page**

### **Full Desktop Layout**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Teacher Portal    [Dashboard] [My Homeworks] [Help]  │
│                                     Mr. Johnson | [Settings] │
└─────────────────────────────────────────────────────────────┘
```

**TOP SECTION - Quick Actions:**
```
┌───────────────────────────────────────────────────────────┐
│  Welcome back, Mr. Johnson! 👋                            │
│                                                           │
│  [+ Create New Homework]     [📊 View All Results]        │
└───────────────────────────────────────────────────────────┘
```

**MAIN CONTENT (Three Columns):**

**LEFT SIDEBAR (20%):**
```
┌──────────────────────┐
│ 📚 My Homeworks      │
│                      │
│ Active (3)           │
│ • Physics Practice   │
│ • Thermo Quiz        │
│ • Wave Motion        │
│                      │
│ Recent (5)           │
│ • EM Fields Test     │
│ • Quantum Basics     │
│ • Forces Review      │
│ • Energy Problems    │
│ • Circuits Lab       │
│                      │
│ Archived (12)        │
│ [View all →]         │
│                      │
│ ─────────────        │
│                      │
│ 📊 Quick Stats       │
│ 156 Total students   │
│ 89% Completion rate  │
│ 76% Avg score        │
└──────────────────────┘
```

**CENTER CONTENT (55%):**
```
┌─────────────────────────────────────────────┐
│ 📋 ACTIVE HOMEWORKS                         │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Physics A-Level Practice Exam           │ │
│ │ Code: PHY-2024-A3B7                     │ │
│ │                                         │ │
│ │ 23/30 students submitted                │ │
│ │ ████████████████░░░░░░░░  77%          │ │
│ │                                         │ │
│ │ Due: Nov 20, 2024                       │ │
│ │ Avg Score: 72% | 5 Questions            │ │
│ │                                         │ │
│ │ [View Results →] [Edit] [Share Code]    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Thermodynamics Quiz                     │ │
│ │ Code: THE-2024-M8K4                     │ │
│ │                                         │ │
│ │ 18/25 students submitted                │ │
│ │ ██████████████░░░░░░░░░░  72%          │ │
│ │                                         │ │
│ │ Due: Nov 18, 2024                       │ │
│ │ Avg Score: 68% | 3 Questions            │ │
│ │                                         │ │
│ │ [View Results →] [Edit] [Share Code]    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Wave Motion Problems                    │ │
│ │ Code: WAV-2024-P5N9                     │ │
│ │                                         │ │
│ │ 30/30 students submitted                │ │
│ │ ████████████████████████  100% ✓       │ │
│ │                                         │ │
│ │ Due: Nov 15, 2024 (Completed)           │ │
│ │ Avg Score: 81% | 4 Questions            │ │
│ │                                         │ │
│ │ [View Results →] [Archive]              │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

**RIGHT SIDEBAR (25%):**
```
┌────────────────────────────────┐
│ 📈 Class Performance           │
│                                │
│ [Animated line chart]          │
│ Showing avg scores over time   │
│                                │
│ This Week:  75% ↗              │
│ Last Week:  71%                │
│                                │
│ ──────────────                 │
│                                │
│ 🎯 Common Struggles            │
│ Based on recent submissions:   │
│                                │
│ • Electromagnetism (58%)       │
│ • Quantum concepts (62%)       │
│ • Complex calculations (65%)   │
│                                │
│ [View detailed analysis]       │
│                                │
│ ──────────────                 │
│                                │
│ 🏆 Top Performers              │
│ 1. Sarah M. - 94%              │
│ 2. James T. - 91%              │
│ 3. Alice K. - 89%              │
│                                │
│ [Animated achievement badges]  │
└────────────────────────────────┘
```

**BACKGROUND:** Clean, professional gradient with subtle grid pattern

---

## **CREATE HOMEWORK PAGE**

### **Full Desktop Layout**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [← Back to Dashboard] Create New Homework          [Preview] │
└─────────────────────────────────────────────────────────────┘
```

**STEP INDICATOR (Top):**
```
┌───────────────────────────────────────────────────────────┐
│  ① Homework Details  →  ② Upload Files  →  ③ Review & Create│
│  ═══════════════                                           │
└───────────────────────────────────────────────────────────┘
```

---

### **STEP 1: HOMEWORK DETAILS**

**MAIN FORM (Center, 70% width):**
```
┌─────────────────────────────────────────────────────────┐
│ 📝 Homework Information                                 │
│                                                         │
│ Homework Title:                                         │
│ ┌───────────────────────────────────────────────────┐   │
│ │ Physics A-Level Practice Exam                     │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Subject:                                                │
│ [Physics ▼]                                             │
│                                                         │
│ Level:                                                  │
│ [A-Level ▼]                                             │
│                                                         │
│ Class/Group:                                            │
│ ┌───────────────────────────────────────────────────┐   │
│ │ Year 13 Physics - Period 4                        │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Due Date:                                               │
│ [Nov 20, 2024 📅]                                       │
│                                                         │
│ Total Marks:                                            │
│ ┌─────┐                                                 │
│ │ 60  │                                                 │
│ └─────┘                                                 │
│                                                         │
│ Number of Questions:                                    │
│ ┌─────┐                                                 │
│ │ 5   │                                                 │
│ └─────┘                                                 │
│                                                         │
│ Instructions for Students (optional):                   │
│ ┌───────────────────────────────────────────────────┐   │
│ │ Show all working. Include units. Use diagrams     │   │
│ │ where appropriate.                                │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│             [Next: Upload Files →]                      │
└─────────────────────────────────────────────────────────┘
```

**RIGHT SIDEBAR (30%):**
```
┌──────────────────────────────┐
│ 💡 Tips                      │
│                              │
│ • Clear titles help students │
│ • Set realistic due dates    │
│ • Include instructions       │
│                              │
│ ──────────────               │
│                              │
│ 📋 What You'll Need:         │
│                              │
│ Step 2:                      │
│ • Question paper (PDF/image) │
│ • Mark scheme/rubric         │
│ • Model answers (optional)   │
│ • Textbook excerpts (opt.)   │
│                              │
│ [Animated checklist icons]   │
└──────────────────────────────┘
```

---

### **STEP 2: UPLOAD FILES**

**STEP INDICATOR:**
```
┌───────────────────────────────────────────────────────────┐
│  ① Homework Details  →  ② Upload Files  →  ③ Review & Create│
│                         ═══════════                        │
└───────────────────────────────────────────────────────────┘
```

**MAIN UPLOAD AREA (Center):**
```
┌─────────────────────────────────────────────────────────┐
│ 📤 Upload Required Files                                │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 1️⃣ Questions Document (Required)                       │
│ The exam paper or problem set students will answer      │
│                                                         │
│ ┌───────────────────────────────────────────────────┐   │
│ │         📄                                        │   │
│ │    Drop question paper here                       │   │
│ │    or click to browse                             │   │
│ │                                                   │   │
│ │    Supports: PDF, DOCX, Images                    │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Status: ✓ physics_exam_questions.pdf uploaded          │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 2️⃣ Mark Scheme / Rubric (Required)                    │
│ How answers should be graded                            │
│                                                         │
│ ┌───────────────────────────────────────────────────┐   │
│ │         📋                                        │   │
│ │    Drop mark scheme here                          │   │
│ │    or click to browse                             │   │
│ │                                                   │   │
│ │    Supports: PDF, DOCX, Images                    │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Status: ✓ mark_scheme.pdf uploaded                     │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 3️⃣ Model Answers (Optional but recommended)           │
│ Example perfect answers for AI comparison               │
│                                                         │
│ ┌───────────────────────────────────────────────────┐   │
│ │         ✏️                                         │   │
│ │    Drop model answers here                        │   │
│ │    or click to browse                             │   │
│ │                                                   │   │
│ │    Supports: PDF, DOCX, Images                    │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Status: ✓ model_answers.pdf uploaded                   │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 4️⃣ Textbook Content (Optional)                        │
│ Relevant textbook pages for deeper understanding        │
│                                                         │
│ ┌───────────────────────────────────────────────────┐   │
│ │         📖                                        │   │
│ │    Drop textbook pages here                       │   │
│ │    or click to browse                             │   │
│ │                                                   │   │
│ │    Supports: PDF, Images                          │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
│ Status: ✓ textbook_ch12.pdf uploaded                   │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ [← Back]                    [Next: Review & Create →]  │
└─────────────────────────────────────────────────────────┘
```

**RIGHT SIDEBAR:**
```
┌──────────────────────────────┐
│ ✅ Upload Progress           │
│                              │
│ Required Files:              │
│ ✓ Questions                  │
│ ✓ Mark Scheme                │
│                              │
│ Optional Files:              │
│ ✓ Model Answers              │
│ ✓ Textbook Content           │
│                              │
│ ──────────────               │
│                              │
│ 💡 Why these files?          │
│                              │
│ Questions: What students     │
│ need to answer               │
│                              │
│ Mark Scheme: How to grade    │
│ their work                   │
│                              │
│ Model Answers: AI compares   │
│ student work to perfect      │
│ examples                     │
│                              │
│ Textbook: Provides context   │
│ for deeper understanding     │
│                              │
│ [Animated file icons         │
│  floating]                   │
└──────────────────────────────┘
```

---

### **STEP 3: REVIEW & CREATE**

**STEP INDICATOR:**
```
┌───────────────────────────────────────────────────────────┐
│  ① Homework Details  →  ② Upload Files  →  ③ Review & Create│
│                                             ═══════════     │
└───────────────────────────────────────────────────────────┘
```

**MAIN REVIEW SECTION (Center, 70%):**
```
┌─────────────────────────────────────────────────────────┐
│ 🔍 Review Your Homework                                 │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 📋 Details                                              │
│ Title: Physics A-Level Practice Exam                    │
│ Subject: Physics | Level: A-Level                       │
│ Class: Year 13 Physics - Period 4                       │
│ Due: Nov 20, 2024                                       │
│ Total Marks: 60 | Questions: 5                          │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 📁 Uploaded Files                                       │
│ ✓ physics_exam_questions.pdf (2.3 MB)                  │
│ ✓ mark_scheme.pdf (1.1 MB)                             │
│ ✓ model_answers.pdf (3.2 MB)                           │
│ ✓ textbook_ch12.pdf (4.8 MB)                           │
│                                                         │
│ [Preview files]                                         │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ 🎯 AI Verification Settings                            │
│                                                         │
│ Interview questions to ask students:                    │
│ [Automatic ●] [Custom ○]                               │
│                                                         │
│ ✓ AI will automatically select 3-5 questions based on: │
│   • Low confidence scores                              │
│   • Conceptual gaps                                    │
│   • Areas needing verification                         │
│                                                         │
│ Number of interview questions: [3-5 ▼]                 │
│                                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                         │
│ Everything looks good?                                  │
│                                                         │
│ [← Back to Edit]          [Create Homework →]          │
└─────────────────────────────────────────────────────────┘
```

**RIGHT SIDEBAR:**
```
┌──────────────────────────────┐
│ ✅ Ready to Create           │
│                              │
│ All required items uploaded  │
│                              │
│ ──────────────               │
│                              │
│ What happens next:           │
│                              │
│ 1. Homework code generated   │
│ 2. Share code with students  │
│ 3. Students submit answers   │
│ 4. AI reviews & interviews   │
│ 5. You see all results       │
│                              │
│ ──────────────               │
│                              │
│ 💾 Save as draft             │
│ Come back to this later      │
│                              │
│ [Animated creation icon]     │
└──────────────────────────────┘
```

---

### **HOMEWORK CREATED SUCCESS PAGE**

**Full Screen Celebration:**
```
┌───────────────────────────────────────────────┐
│                                               │
│           [Animated confetti]                 │
│           [Trophy animation]                  │
│                                               │
│        ✨ Homework Created! ✨                │
│                                               │
│        Your homework code is:                 │
│                                               │
│     ┌─────────────────────────┐               │
│     │   PHY-2024-A3B7         │               │
│     │   [Copy Code]           │               │
│     └─────────────────────────┘               │
│                                               │
│   Share this code with your students          │
│                                               │
│   [📧 Email to Class] [📋 Copy Link]          │
│   [📱 Show QR Code]   [💬 Post to LMS]        │
│                                               │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                               │
│   Quick Actions:                              │
│   [View Homework Details]                     │
│   [Create Another Homework]                   │
│   [Back to Dashboard]                         │
│                                               │
└───────────────────────────────────────────────┘
```

---

## **VIEW HOMEWORK RESULTS PAGE**

### **Full Desktop Layout**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [← Back to Dashboard] Physics A-Level Practice Exam         │
│ Code: PHY-2024-A3B7 | Due: Nov 20, 2024     [Export Results]│
└─────────────────────────────────────────────────────────────┘
```

**TOP SUMMARY BANNER:**
```
┌───────────────────────────────────────────────────────────┐
│  📊 Class Overview                                        │
│                                                           │
│  23/30 students submitted (77%)                           │
│  Average Score: 72% (43/60 marks)                         │
│  Completion Rate: █████████████████░░░░░░░░ 77%          │
│                                                           │
│  [Animated progress bars and stats]                       │
└───────────────────────────────────────────────────────────┘
```

**THREE COLUMN LAYOUT:**

**LEFT SIDEBAR (20%):**
```
┌──────────────────────┐
│ 🎯 Filters           │
│                      │
│ Status:              │
│ ☑ Submitted (23)     │
│ ☑ Pending (7)        │
│ □ Late (0)           │
│                      │
│ Score Range:         │
│ □ 90-100
│ ☑ 80-89% (5)         │
│ ☑ 70-79% (9)         │
│ ☑ 60-69% (6)         │
│ ☑ Below 60% (3)      │
│                      │
│ Interview Status:    │
│ ☑ Completed (20)     │
│ ☑ In Progress (3)    │
│ □ Not Started (0)    │
│                      │
│ ─────────────        │
│                      │
│ Sort By:             │
│ [Score ▼]            │
│                      │
│ [Apply Filters]      │
└──────────────────────┘
```

**CENTER CONTENT (55%) - Student List:**
```
┌─────────────────────────────────────────────────────────┐
│ 👥 STUDENT SUBMISSIONS                                  │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Sarah Mitchell                                      │ │
│ │ ⭐⭐⭐⭐⭐ 94% (56/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 94% | Interview: 96% (Excellent!)          │ │
│ │ Submitted: Nov 15, 2024 10:23 AM                    │ │
│ │                                                     │ │
│ │ Strengths: All topics | No major gaps               │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ James Thompson                                      │ │
│ │ ⭐⭐⭐⭐☆ 87% (52/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 85% | Interview: 89% (Strong)              │ │
│ │ Submitted: Nov 16, 2024 3:45 PM                     │ │
│ │                                                     │ │
│ │ Strengths: Mechanics, Waves                         │ │
│ │ Focus Areas: Electromagnetism                       │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Alice Kim                                           │ │
│ │ ⭐⭐⭐⭐☆ 82% (49/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 80% | Interview: 84% (Good)                │ │
│ │ Submitted: Nov 17, 2024 9:12 AM                     │ │
│ │                                                     │ │
│ │ Strengths: Thermodynamics                           │ │
│ │ Focus Areas: Quantum concepts                       │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ David Chen                                          │ │
│ │ ⭐⭐⭐⭐☆ 78% (47/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 75% | Interview: 81% (Good improvement!)   │ │
│ │ Submitted: Nov 17, 2024 2:30 PM                     │ │
│ │                                                     │ │
│ │ Strengths: Problem-solving skills                   │ │
│ │ Focus Areas: Conceptual understanding               │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Emma Rodriguez                                      │ │
│ │ ⭐⭐⭐☆☆ 71% (43/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 70% | Interview: 72%                       │ │
│ │ Submitted: Nov 17, 2024 8:45 PM                     │ │
│ │                                                     │ │
│ │ Strengths: Basic concepts                           │ │
│ │ Focus Areas: EM fields, Quantum mechanics           │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Michael Brown                                       │ │
│ │ ⭐⭐⭐☆☆ 65% (39/60 marks)                          │ │
│ │                                                     │ │
│ │ Written: 62% | Interview: 68%                       │ │
│ │ Submitted: Nov 18, 2024 11:20 AM                    │ │
│ │                                                     │ │
│ │ ⚠️ Significant gaps in EM and Quantum               │ │
│ │ Recommend: Extra support session                    │ │
│ │                                                     │ │
│ │ [View Full Report] [Message Student]                │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ⏳ PENDING SUBMISSIONS (7 students)                 │ │
│ │                                                     │ │
│ │ • Tom Wilson                                        │ │
│ │ • Lisa Anderson                                     │ │
│ │ • Kevin Lee                                         │ │
│ │ • Maria Garcia                                      │ │
│ │ • Ryan Taylor                                       │ │
│ │ • Sophie Martin                                     │ │
│ │ • Jack Davis                                        │ │
│ │                                                     │ │
│ │ [Send Reminder Email]                               │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

**RIGHT SIDEBAR (25%) - Class Insights:**
```
┌────────────────────────────────────┐
│ 📈 CLASS ANALYTICS                 │
│                                    │
│ [Animated score distribution chart]│
│ Score Distribution:                │
│ 90-100%: ████ 5 students           │
│ 80-89%:  █████ 9 students          │
│ 70-79%:  ████ 6 students           │
│ 60-69%:  ██ 3 students             │
│ <60%:    - 0 students              │
│                                    │
│ ──────────────────                 │
│                                    │
│ 🎯 TOPIC PERFORMANCE               │
│                                    │
│ Q1: Newton's Laws                  │
│ ████████████░░░░  82% avg          │
│                                    │
│ Q2: Thermodynamics                 │
│ ██████████████░░  78% avg          │
│                                    │
│ Q3: Wave Motion                    │
│ █████████████░░░  75% avg          │
│                                    │
│ Q4: Electromagnetism               │
│ ████████░░░░░░░░  58% avg ⚠️       │
│                                    │
│ Q5: Quantum Mechanics              │
│ ██████████░░░░░░  64% avg          │
│                                    │
│ ──────────────────                 │
│                                    │
│ 💡 COMMON STRUGGLES                │
│                                    │
│ • EM field direction (15 students) │
│ • Wave-particle duality (12)       │
│ • Right-hand rule (10)             │
│                                    │
│ 📚 Suggested Actions:              │
│ • Review EM fields in class        │
│ • Extra practice problems          │
│ • 1-on-1 support for 3 students    │
│                                    │
│ ──────────────────                 │
│                                    │
│ 🏆 INTERVIEW INSIGHTS              │
│                                    │
│ Written vs Verbal Performance:     │
│                                    │
│ Higher verbal: 12 students         │
│ (Good understanding, needs         │
│  writing practice)                 │
│                                    │
│ Higher written: 4 students         │
│ (May have received help)           │
│                                    │
│ Consistent: 7 students             │
│ (Strong across both)               │
│                                    │
│ [View detailed analysis]           │
└────────────────────────────────────┘
```

**BACKGROUND:** Clean professional gradient with subtle data visualization patterns

---

## **INDIVIDUAL STUDENT REPORT PAGE**

### **Full Desktop Layout**

**HEADER:**
```
┌─────────────────────────────────────────────────────────────┐
│ [← Back to Class Results] Sarah Mitchell's Report           │
│ Physics A-Level Practice Exam | Code: PHY-2024-A3B7         │
└─────────────────────────────────────────────────────────────┘
```

**TOP STUDENT CARD:**
```
┌───────────────────────────────────────────────────────────┐
│  👤 Sarah Mitchell                                        │
│  Student ID: SM2024 | Year 13 Physics                     │
│                                                           │
│  Overall Score: 94% (56/60 marks) ⭐⭐⭐⭐⭐              │
│  Grade: A*                                                │
│                                                           │
│  Written Exam: 94% | Interview: 96%                       │
│  Submitted: Nov 15, 2024 10:23 AM                         │
│                                                           │
│  [Download Report PDF] [Share with Student] [Message]     │
└───────────────────────────────────────────────────────────┘
```

**TAB NAVIGATION:**
```
┌───────────────────────────────────────────────────────────┐
│  [📝 Written Work]  [💬 Interview]  [📊 Analysis]         │
│   ═══════════                                             │
└───────────────────────────────────────────────────────────┘
```

---

### **TAB 1: WRITTEN WORK**

**TWO COLUMN LAYOUT:**

**LEFT SIDE (70%):**
```
┌─────────────────────────────────────────────┐
│ Question 1: Newton's Laws                   │
│ ⭐⭐⭐⭐⭐ 10/10 marks (100%)                 │
│                                             │
│ [Animated progress bar - 100%]              │
│                                             │
│ ✅ Mark Scheme Points Achieved:             │
│ • Correct application of F=ma (2 marks)     │
│ • Clear free-body diagram (2 marks)         │
│ • Accurate calculations (3 marks)           │
│ • Units included throughout (1 mark)        │
│ • Explanation of reasoning (2 marks)        │
│                                             │
│ 💡 AI Assessment:                           │
│ Excellent work. All criteria met with       │
│ clear working shown. Diagram is             │
│ particularly well-labeled.                  │
│                                             │
│ [View Student's Answer] [View Mark Scheme]  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Question 2: Thermodynamics                  │
│ ⭐⭐⭐⭐⭐ 14/15 marks (93%)                  │
│                                             │
│ [Animated progress bar - 93%]               │
│                                             │
│ ✅ Mark Scheme Points Achieved:             │
│ • Heat transfer equation (3 marks)          │
│ • Entropy concept explained (3 marks)       │
│ • Diagram of system (2 marks)               │
│ • Calculations correct (4 marks)            │
│                                             │
│ ⚠️ Mark Scheme Points Missed:               │
│ • Could elaborate more on entropy           │
│   change direction (1 mark)                 │
│                                             │
│ 💡 AI Assessment:                           │
│ Strong understanding demonstrated.          │
│ Minor omission in entropy explanation       │
│ but core concept is solid.                  │
│                                             │
│ [View Student's Answer] [View Mark Scheme]  │
└─────────────────────────────────────────────┘

[Continues for all 5 questions...]
```

**RIGHT SIDEBAR (30%):**
```
┌────────────────────────────────┐
│ 📊 Written Exam Summary        │
│                                │
│ Total: 56/60 (94%)             │
│                                │
│ [Circular progress chart]      │
│                                │
│ Per Question:                  │
│ Q1: 10/10 ✓                    │
│ Q2: 14/15 ✓                    │
│ Q3: 12/12 ✓                    │
│ Q4: 12/13 ✓                    │
│ Q5: 8/10 ✓                     │
│                                │
│ ──────────────                 │
│                                │
│ 💪 Strengths:                  │
│ • Excellent working shown      │
│ • Clear diagrams               │
│ • Accurate calculations        │
│ • Good explanations            │
│                                │
│ 🎯 Minor Improvements:         │
│ • Entropy change details       │
│ • More depth on Q5             │
│                                │
│ ──────────────                 │
│                                │
│ [Submitted answer sheets]      │
│ [View original PDFs]           │
└────────────────────────────────┘
```

---

### **TAB 2: INTERVIEW**

**VIDEO PLAYBACK SECTION (Top):**
```
┌───────────────────────────────────────────────────────────┐
│ 🎥 INTERVIEW RECORDING                                    │
│                                                           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │                                                     │   │
│ │          [Video player - Sarah's interview]        │   │
│ │                                                     │   │
│ │          Duration: 4:32                            │   │
│ │                                                     │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                           │
│ [▶ Play Full Interview] [Jump to Question 2]              │
│                                                           │
│ Timestamps:                                               │
│ 0:00 - Question 1 (Electromagnetism approach)             │
│ 1:15 - Question 2 (Entropy concept)                       │
│ 2:40 - Question 3 (Wave frequency application)            │
│ 3:50 - Interview complete                                 │
└───────────────────────────────────────────────────────────┘
```

**INTERVIEW ANALYSIS (Below):**
```
┌─────────────────────────────────────────────────────────┐
│ 💬 INTERVIEW QUESTIONS & RESPONSES                      │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Question 1: YOUR APPROACH                           │ │
│ │                                                     │ │
│ │ "Walk me through how you calculated the magnetic   │ │
│ │  field strength in Q4."                            │ │
│ │                                                     │ │
│ │ 📝 Transcript:                                      │ │
│ │ "So I started by identifying that this was a       │ │
│ │  long straight wire, which means I should use      │ │
│ │  B = μ₀I/2πr. I knew the current was 5A and the   │ │
│ │  distance was 10cm, so I converted that to         │ │
│ │  0.1 meters. Then I just plugged in the values..." │ │
│ │                                                     │ │
│ │ [View full transcript] [Watch video clip]          │ │
│ │                                                     │ │
│ │ ✅ AI Assessment: Excellent (96%)                   │ │
│ │                                                     │ │
│ │ Evaluation:                                         │ │
│ │ • Clear step-by-step explanation ✓                 │ │
│ │ • Correct formula selection ✓                      │ │
│ │ • Proper unit conversion mentioned ✓               │ │
│ │ • Confident delivery ✓                             │ │
│ │                                                     │ │
│ │ Alignment with written work: High                   │ │
│ │ (Explanation matches written solution)              │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Question 2: UNDERSTANDING CHECK                     │ │
│ │                                                     │ │
│ │ "Explain entropy in your own words and why it      │ │
│ │  always increases in isolated systems."            │ │
│ │                                                     │ │
│ │ 📝 Transcript:                                      │ │
│ │ "Entropy is basically a measure of disorder in     │ │
│ │  a system. It always increases because...the       │ │
│ │  second law of thermodynamics says that energy     │ │
│ │  naturally spreads out and becomes less useful.    │ │
│ │  Like if you have a hot cup of coffee, it          │ │
│ │  eventually cools down to room temperature         │ │
│ │  because the heat energy disperses..."             │ │
│ │                                                     │ │
│ │ [View full transcript] [Watch video clip]          │ │
│ │                                                     │ │
│ │ ✅ AI Assessment: Excellent (98%)                   │ │
│ │                                                     │ │
│ │ Evaluation:                                         │ │
│ │ • Strong conceptual understanding ✓                │ │
│ │ • Good use of analogy ✓                            │ │
│ │ • Connects to thermodynamic laws ✓                 │ │
│ │ • Clear explanation ✓                              │ │
│ │                                                     │ │
│ │ This addressed the gap from written work!          │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ [Continue for remaining questions...]                   │
└─────────────────────────────────────────────────────────┘
```

**RIGHT SIDEBAR:**
```
┌────────────────────────────────┐
│ 🎤 Interview Summary           │
│                                │
│ Overall Score: 96%             │
│                                │
│ Questions Asked: 3             │
│ Duration: 4m 32s               │
│                                │
│ ──────────────                 │
│                                │
│ Performance Breakdown:         │
│                                │
│ 🔧 Process Questions:          │
│ Q1: 96% - Excellent            │
│                                │
│ 💡 Concept Questions:          │
│ Q2: 98% - Excellent            │
│ Q3: 94% - Excellent            │
│                                │
│ ──────────────                 │
│                                │
│ 🎯 Key Insights:               │
│                                │
│ ✓ Verbal > Written (96% vs 94%)│
│ ✓ Strong conceptual grasp      │
│ ✓ Can explain reasoning        │
│ ✓ Uses analogies effectively   │
│                                │
│ ──────────────                 │
│                                │
│ 📊 Confidence Indicators:      │
│                                │
│ Speech clarity: High           │
│ Hesitation: Minimal            │
│ Self-correction: Appropriate   │
│                                │
│ ──────────────                 │
│                                │
│ Academic Integrity: ✓          │
│ High confidence this is        │
│ student's own work             │
└────────────────────────────────┘
```

---

### **TAB 3: ANALYSIS**

**FULL WIDTH COMPARISON CHART:**
```
┌───────────────────────────────────────────────────────────┐
│ 📊 WRITTEN vs VERBAL PERFORMANCE                          │
│                                                           │
│ [Animated dual-axis chart showing both scores by topic]   │
│                                                           │
│ Newton's Laws:     Written 100% | Verbal 96%  ✓          │
│ Thermodynamics:    Written 93%  | Verbal 98%  ↗          │
│ Wave Motion:       Written 100% | Verbal 94%  ✓          │
│                                                           │
│ Overall: Written 94% | Verbal 96%                         │
│                                                           │
│ Interpretation:                                           │
│ Consistent high performance. Slight verbal advantage      │
│ suggests genuine understanding with excellent             │
│ communication skills.                                     │
└───────────────────────────────────────────────────────────┘
```

**THREE COLUMN INSIGHTS:**

**LEFT COLUMN (33%):**
```
┌─────────────────────────────────┐
│ 💪 STRENGTHS                    │
│                                 │
│ ✓ Exceptional problem-solving   │
│   Able to apply formulas        │
│   correctly and efficiently     │
│                                 │
│ ✓ Strong conceptual foundation  │
│   Deep understanding of         │
│   underlying physics            │
│                                 │
│ ✓ Excellent communication       │
│   Can articulate thinking       │
│   clearly and logically         │
│                                 │
│ ✓ Diagram skills                │
│   Clear, labeled, accurate      │
│   visual representations        │
│                                 │
│ ✓ Attention to detail           │
│   Units, working, formatting    │
│   all carefully done            │
└─────────────────────────────────┘
```

**MIDDLE COLUMN (33%):**
```
┌─────────────────────────────────┐
│ 🎯 GROWTH AREAS                 │
│                                 │
│ Minor improvements:             │
│                                 │
│ • Entropy explanation depth     │
│   (Already addressed in         │
│    interview - now strong!)     │
│                                 │
│ • Quantum concepts              │
│   Good but could go deeper      │
│   on wave-particle duality      │
│                                 │
│ Recommendations:                │
│                                 │
│ 📚 Extension reading:           │
│ • Advanced quantum texts        │
│ • Modern physics applications   │
│                                 │
│ 🎓 Suggested challenges:        │
│ • Olympiad problems             │
│ • Research projects             │
│ • Peer tutoring                 │
└─────────────────────────────────┘
```

**RIGHT COLUMN (33%):**
```
┌─────────────────────────────────┐
│ 🔍 ACADEMIC INTEGRITY           │
│                                 │
│ ✅ High Confidence              │
│                                 │
│ Indicators of authentic work:   │
│                                 │
│ ✓ Written & verbal alignment    │
│   Explanations match written    │
│   solutions consistently        │
│                                 │
│ ✓ Process understanding         │
│   Can explain methodology       │
│   clearly and accurately        │
│                                 │
│ ✓ Conceptual depth              │
│   Demonstrates genuine grasp    │
│   beyond memorization           │
│                                 │
│ ✓ Natural communication         │
│   Confident, unprompted         │
│   explanations                  │
│                                 │
│ Assessment: This is clearly     │
│ the student's own work with     │
│ genuine understanding.          │
└─────────────────────────────────┘
```

**BOTTOM SECTION - TEACHER NOTES:**
```
┌───────────────────────────────────────────────────────────┐
│ 📝 TEACHER NOTES (Private)                                │
│                                                           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Add notes visible only to you...                    │   │
│ │                                                     │   │
│ │ [Click to add private comments about this student]  │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                           │
│ [Save Notes]                                              │
└───────────────────────────────────────────────────────────┘
```

---

---

# **DEVELOPER GUIDE: Backend Architecture & Considerations**

---

## **SYSTEM ARCHITECTURE OVERVIEW**

### **Core Components**

1. **User Management System**
   - Teacher accounts
   - Student accounts (can be anonymous/code-based)
   - Authentication & authorization
   - Role-based access control

2. **Homework Code System**
   - Unique code generation
   - Code validation
   - Code-to-homework mapping
   - Expiration handling (optional)

3. **File Storage & Processing**
   - Document upload handling
   - File type validation
   - OCR for images (if needed)
   - PDF text extraction
   - Storage management

4. **AI Processing Engine**
   - Mark scheme parsing
   - Student answer analysis
   - Comparison algorithms
   - Confidence scoring
   - Interview question generation

5. **Video Interview System**
   - WebRTC or similar for video capture
   - Audio transcription (Speech-to-Text)
   - Video storage
   - Timestamp management

6. **Results & Analytics**
   - Score calculation
   - Performance analytics
   - Comparison algorithms (written vs verbal)
   - Class-level aggregations

---

## **DATABASE SCHEMA CONSIDERATIONS**

### **Key Tables/Collections Needed**

**Teachers Table:**
```
- teacher_id (PK)
- email
- name
- school/institution
- created_at
- settings (JSON: preferences, notifications, etc.)
```

**Students Table (Optional - could be session-based):**
```
- student_id (PK)
- name (optional if anonymous)
- email (optional)
- class_id (FK to classes if needed)
- created_at
```

**Homeworks Table:**
```
- homework_id (PK)
- teacher_id (FK)
- code (unique, indexed)
- title
- subject
- level (A-Level, GCSE, etc.)
- class_name
- due_date
- total_marks
- num_questions
- instructions (text)
- created_at
- status (active, archived, draft)
```

**Homework Files Table:**
```
- file_id (PK)
- homework_id (FK)
- file_type (questions, mark_scheme, model_answers, textbook)
- file_url (S3/cloud storage path)
- file_name
- file_size
- uploaded_at
- processed (boolean - has AI processed it?)
- processing_status (pending, complete, failed)
```

**Submissions Table:**
```
- submission_id (PK)
- homework_id (FK)
- student_id (FK or anonymous identifier)
- student_name
- answer_file_url (S3/cloud storage)
- answer_text (if typed directly)
- submitted_at
- status (pending, analyzing, interview_pending, complete)
```

**Submission Scores Table:**
```
- score_id (PK)
- submission_id (FK)
- question_number
- marks_awarded
- marks_possible
- ai_reasoning (text)
- mark_scheme_points_met (JSON array)
- mark_scheme_points_missed (JSON array)
- confidence_score (0-100)
```

**Interview Sessions Table:**
```
- interview_id (PK)
- submission_id (FK)
- started_at
- completed_at
- duration_seconds
- video_url (S3/cloud storage)
- status (in_progress, completed)
```

**Interview Questions Table:**
```
- interview_question_id (PK)
- interview_id (FK)
- question_number (1, 2, 3, etc.)
- question_type (process, concept, application)
- question_text
- related_homework_question (which Q this relates to)
- timestamp_start (video timestamp)
- timestamp_end (video timestamp)
```

**Interview Responses Table:**
```
- response_id (PK)
- interview_question_id (FK)
- audio_url (S3 storage)
- transcript (full text)
- ai_assessment_score (0-100)
- ai_evaluation (JSON: strengths, weaknesses, alignment)
- confidence_indicators (JSON: clarity, hesitation, etc.)
```

**Analytics Cache Table (Optional but recommended):**
```
- cache_id (PK)
- homework_id (FK)
- cache_type (class_overview, topic_performance, etc.)
- data (JSON)
- generated_at
- expires_at
```

---

## **KEY BACKEND GOALS & CONSIDERATIONS**

### **1. CODE GENERATION & VALIDATION**

**Goals:**
- Generate unique, memorable codes (e.g., PHY-2024-A3B7)
- Fast validation (indexed lookups)
- Prevent collisions
- Optional: Expiration dates

**Considerations:**
- Use format: `[SUBJECT]-[YEAR]-[RANDOM]`
- Index the code field heavily
- Consider short codes (6-8 chars) vs descriptive (12-15 chars)
- Handle case-insensitivity
- Validate on both client and server

**Rate Limiting:**
- Limit code attempts per IP (prevent brute force)
- Track failed validation attempts

---

### **2. FILE UPLOAD & PROCESSING**

**Goals:**
- Handle multiple file types (PDF, DOCX, images)
- Extract text reliably
- Process asynchronously
- Store securely
- Validate file integrity

**Considerations:**

**File Size Limits:**
- Set reasonable limits (e.g., 10MB per file, 50MB total per homework)
- Validate on client AND server
- Provide clear error messages

**File Type Validation:**
- Check MIME types, not just extensions
- Scan for malware/viruses
- Reject executable files

**Text Extraction:**
- PDF: Use libraries like PyPDF2, pdfplumber, or pdf2image + OCR
- DOCX: python-docx, mammoth
- Images: OCR with Tesseract, Google Vision API, or AWS Textract
- Handle multi-column layouts, tables, equations
- Preserve formatting where needed (especially for equations)

**Storage Strategy:**
- Use cloud storage (S3, GCS, Azure Blob)
- Organize by: `homework_id/file_type/filename`
- Generate signed URLs for temporary access
- Implement automatic cleanup for old files
- Consider CDN for frequently accessed files

**Processing Pipeline:**
```
Upload → Virus Scan → Type Validation → Storage → 
Text Extraction → AI Processing → Update Status
```

**Async Processing:**
- Use job queues (Celery, RabbitMQ, SQS)
- Provide progress updates via WebSockets or polling
- Handle failures gracefully with retries
- Log all processing steps for debugging

---

### **3. AI MARKING ENGINE**

**Goals:**
- Parse mark schemes accurately
- Compare student answers to model answers
- Generate detailed, actionable feedback
- Assign confidence scores
- Identify knowledge gaps

**Considerations:**

**Mark Scheme Parsing:**
- Extract marking criteria (bullet points, requirements)
- Identify marks per criterion
- Handle multiple acceptable answers
- Parse mathematical notation
- Understand partial credit rules

**Answer Comparison Algorithm:**
- Semantic similarity (not just keyword matching)
- Use embeddings (OpenAI, sentence-transformers)
- Check for key concepts, not just exact phrases
- Handle different phrasings of correct answers
- Detect calculations vs explanations

**Scoring Strategy:**
```
For each question:
1. Extract mark scheme criteria
2. Parse student answer
3. Compare against model answer (if provided)
4. Check each criterion:
   - Present & correct: Award marks
   - Present but partial: Partial marks (if applicable)
   - Missing: 0 marks
5. Generate reasoning for each decision
6. Calculate confidence score based on:
   - Clarity of answer
   - Completeness
   - Alignment with mark scheme
   - Presence of working/explanation
```

**Confidence Scoring:**
- High (80-100%): Clear match to mark scheme, all criteria met
- Medium (50-79%): Some ambiguity, partial matches
- Low (0-49%): Unclear answer, missing key elements

**Use confidence scores to determine interview questions:**
- Low confidence → Definitely ask in interview
- Medium confidence → Possibly ask (especially for important concepts)
- High confidence → Skip in interview (unless spot-checking)

**AI Model Selection:**
- Use GPT-4 or Claude for complex reasoning
- Fine-tune if budget allows
- Prompt engineering is critical:
  ```
  "You are an experienced physics teacher. Given this mark scheme:
  [MARK_SCHEME]
  
  And this student answer:
  [STUDENT_ANSWER]
  
  Award marks according to the scheme. For each criterion:
  - State if met (✓) or not met (✗)
  - Explain your reasoning
  - Award appropriate marks
  
  Output as JSON..."
  ```

**Error Handling:**
- If AI fails, flag for manual review
- Don't block student progress
- Provide estimated score with caveat
- Retry with different model/prompt

---

### **4. INTERVIEW QUESTION GENERATION**

**Goals:**
- Select 3-5 most relevant questions
- Mix process and concept questions
- Target areas of uncertainty
- Adapt to student level

**Considerations:**

**Selection Algorithm:**
```
1. Analyze all questions from written exam
2. Sort by:
   - Confidence score (lowest first)
   - Topic importance (core concepts prioritized)
   - Question complexity
3. Select questions covering:
   - 2 process questions (from low-confidence areas)
   - 2-3 concept questions (testing understanding)
   - Optional: 1 application question (higher-level thinking)
4. Ensure coverage of different topics (don't ask all from one area)
```

**Question Types:**

**Process Questions:**
- "Walk me through how you solved Q4"
- "What steps did you take in part (b)?"
- "How did you decide which formula to use?"

**Concept Questions:**
- "Explain [concept] in your own words"
- "Why does [phenomenon] happen?"
- "What's the relationship between [X] and [Y]?"

**Application Questions:**
- "What if we changed [parameter] - what would happen?"
- "How would this apply to [real-world scenario]?"
- "Can you think of another situation where this concept applies?"

**Dynamic Question Generation:**
- Use AI to generate custom questions based on:
  - Student's specific errors
  - Mark scheme criteria they missed
  - Related concepts from textbook
- Store generated questions for consistency

**Question Context:**
- Include reference to original written answer
- Provide hints if needed
- Set expectations (e.g., "Explain in 1-2 minutes")

---

### **5. VIDEO INTERVIEW SYSTEM**

**Goals:**
- Capture video/audio reliably
- Transcribe accurately
- Store efficiently
- Enable teacher review
- Maintain student privacy

**Considerations:**

**Video Capture:**
- WebRTC for browser-based recording
- MediaRecorder API
- Alternative: Third-party services (Vonage, Agora, Twilio)
- Handle permissions gracefully
- Test across browsers (Chrome, Firefox, Safari)

**Video Format & Compression:**
- Record in WebM or MP4
- Compress on client before upload (if possible)
- Or compress server-side after upload
- Balance quality vs file size (720p is usually sufficient)

**Chunked Upload:**
- Don't wait for full interview to complete
- Upload in chunks (per question or every 30 seconds)
- Allows recovery from failures
- Provides progress indication

**Storage:**
- Store in S3/GCS with lifecycle policies
- Consider auto-deletion after N days (GDPR compliance)
- Separate storage buckets for active vs archived
- Encrypt at rest and in transit

**Audio Transcription:**
- Use Whisper (OpenAI), Google Speech-to-Text, or AWS Transcribe
- Process asynchronously
- Handle multiple speakers (though usually just student)
- Timestamp each sentence/phrase
- Handle background noise, accents, technical terminology

**Transcription Pipeline:**
```
Video Upload → Extract Audio → Send to STT Service → 
Receive Transcript → Store → Link to Interview Questions
```

**Privacy & Consent:**
- Inform students before recording
- Obtain consent (checkbox or verbal at start)
- Provide option to delete recording after assessment
- Comply with data protection laws (GDPR, COPPA)

**Video Review Interface (for teachers):**
- Seekable video player
- Jump to specific questions
- Highlight key moments
- Display transcript alongside video
- Allow playback speed control

---

### **6. TRANSCRIPTION ANALYSIS & SCORING**

**Goals:**
- Evaluate verbal responses
- Compare to written answers
- Detect understanding vs memorization
- Identify academic integrity concerns

**Considerations:**

**Answer Evaluation Criteria:**

For **Process Questions:**
- Can they explain their methodology? (✓/✗)
- Do they mention correct steps? (✓/✗)
- Can they identify their approach? (✓/✗)
- Does explanation match written work? (✓/✗)

For **Concept Questions:**
- Can they define/explain the concept? (✓/✗)
- Do they understand underlying principles? (✓/✗)
- Can they give examples/analogies? (✓/✗)
- Is explanation accurate? (✓/✗)

For **Application Questions:**
- Can they transfer knowledge to new scenarios? (✓/✗)
- Do they make correct predictions? (✓/✗)
- Can they justify their reasoning? (✓/✗)

**Scoring Algorithm:**
```
For each interview question:
1. Extract transcript for that question
2. Send to AI with:
   - Original homework question
   - Student's written answer
   - Mark scheme
   - Evaluation criteria
3. AI returns:
   - Score (0-100)
   - Evaluation notes (what was good/bad)
   - Alignment with written work (high/medium/low)
4. Store results
```

**AI Prompt Example:**
```
"You are evaluating a student's verbal explanation.

Written Answer: [STUDENT_WRITTEN_ANSWER]
Verbal Response: [TRANSCRIPT]
Mark Scheme: [MARK_SCHEME]

Assess:
1. Does the verbal explanation match the written answer?
2. Does it demonstrate genuine understanding?
3. Can they articulate the reasoning clearly?
4. Rate 0-100 based on:
   - Accuracy (40%)
   - Clarity (30%)
   - Depth (30%)

Return JSON with score, strengths, weaknesses, and alignment."
```

**Red Flags for Academic Integrity:**
- Written answer perfect, but can't explain verbally
- Contradictions between written and verbal
- Overly formal/textbook language in writing, casual/confused verbally
- Can't remember their own methodology
- Significant hesitation on basic questions

**However:**
- Don't auto-flag - provide data for teacher judgment
- Consider test anxiety, language barriers
- Some students are better writers than speakers (and vice versa)

---

### **7. RESULTS AGGREGATION & ANALYTICS**

**Goals:**
- Fast dashboard loading
- Insightful class-level analytics
- Identify struggling students/topics
- Actionable recommendations

**Considerations:**

**Caching Strategy:**
- Pre-calculate class statistics
- Update cache when new submission completes
- Use Redis or similar for fast access
- Set reasonable TTL (e.g., 5 minutes)

**Class-Level Metrics to Calculate:**
```
- Submission rate (%)
- Average score (written, interview, overall)
- Score distribution (histogram data)
- Per-question performance
- Per-topic performance
- Common struggles (most-missed criteria)
- Written vs verbal performance patterns
- Top performers
- Students needing support
```

**Student-Level Metrics:**
```
- Overall score
- Per-question breakdown
- Strengths (topics with 80%+)
- Growth areas (topics with <70%)
- Written vs verbal comparison
- Academic integrity confidence
- Submission timestamp
```

**Performance Optimization:**
- Index heavily-queried fields (homework_id, student_id, etc.)
- Use database views for complex aggregations
- Consider materialized views that refresh periodically
- Paginate large result sets
- Lazy-load detailed data

**Real-Time Updates:**
- Use WebSockets to push updates to teacher dashboard
- When student completes: Update "23/30 submitted" counter
- When analysis completes: Update class statistics
- Avoid polling - use event-driven architecture

---

### **8. NOTIFICATION SYSTEM**

**Goals:**
- Keep teachers informed
- Remind students of deadlines
- Alert on completion
- Provide status updates

**Considerations:**

**Notification Types:**

For **Teachers:**
- Homework code generated
- Student submitted homework
- Analysis complete for student
- All students completed
- Deadline approaching with pending submissions
- Urgent: Student needs support (low score + struggled in interview)

For **Students:**
- Homework code received (if email provided)
- Submission received
- Analysis in progress
- Feedback ready
- Interview required
- Deadline reminder

**Delivery Channels:**
- Email (primary)
- In-app notifications
- SMS (optional, premium feature)
- LMS integration (Canvas, Moodle, Google Classroom)

**Implementation:**
- Queue-based (SQS, RabbitMQ)
- Use email service (SendGrid, Mailgun, AWS SES)
- Template-based (parameterized messages)
- Unsubscribe options
- Rate limiting (don't spam)

---

### **9. SECURITY & PRIVACY**

**Goals:**
- Protect student data
- Secure file storage
- Prevent cheating/gaming
- Comply with regulations

**Considerations:**

**Authentication & Authorization:**
- Teacher login: Email/password + 2FA
- Student access: Code-based (no login required) OR optional accounts
- JWT tokens for session management
- Role-based permissions (teacher can only see their homeworks)

**Data Encryption:**
- HTTPS everywhere (TLS 1.2+)
- Encrypt files at rest (S3 encryption)
- Encrypt sensitive DB fields (student names, emails if stored)

**Access Control:**
- Teachers can only access their own homeworks
- Students can only access submissions via valid code
- Video recordings: Signed URLs with expiration
- API rate limiting

**Privacy Compliance:**
- GDPR: Right to deletion, data portability
- COPPA: Parental consent for under-13
- FERPA (if US schools): Protect education records
- Clear privacy policy
- Data retention policies (auto-delete after X months)

**Anti-Cheating Measures:**
- Randomize interview question order
- Time-limit code entry (optional)
- Flag suspicious patterns:
  - Multiple submissions from same IP
  - Identical answers from different students
  - Perfect written + terrible interview
- Don't show mark scheme to students

**Audit Logging:**
- Track all file uploads
- Log all AI processing
- Record interview sessions
- Monitor for abuse

---

### **10. SCALABILITY & PERFORMANCE**

**Goals:**
- Handle 1000+ concurrent students
- Process homeworks quickly
- Keep costs reasonable
- Maintain reliability

**Considerations:**

**Horizontal Scaling:**
- Stateless API servers (can add more instances)
- Load balancer (ALB, NGINX)
- Separate services:
  - Web API
  - File processing workers
  - AI processing workers
  - Transcription workers
  - Analytics workers

**Database Scaling:**
- Read replicas for analytics queries
- Connection pooling
- Query optimization (EXPLAIN plans)
- Consider sharding if huge scale (probably not needed)

**File Processing:**
- Distributed job queue (SQS, RabbitMQ)
- Multiple worker instances
- Priority queues (urgent homeworks first)
- Retry logic with exponential backoff

**AI API Rate Limits:**
- OpenAI, Anthropic have rate limits
- Queue requests
- Batch where possible
- Consider caching common mark schemes
- Fallback to alternative models if rate limited

**Cost Optimization:**
- Use spot instances for workers (if cloud-based)
- Compress videos before storage
- Auto-delete old files
- Cache expensive computations
- Monitor AI API usage (biggest cost driver)

**Monitoring & Alerting:**
- Track key metrics:
  - API response times
  - Queue depths
  - Error rates
  - AI processing times
  - Storage usage
- Set up alerts for anomalies
- Use tools like DataDog, New Relic, CloudWatch

---

### **11. ERROR HANDLING & EDGE CASES**

**Goals:**
- Graceful degradation
- Clear error messages
- Recovery mechanisms
- User-friendly experience

**Considerations:**

**Common Failures:**

**AI Processing Fails:**
- Retry with different prompt
- Fall back to simpler model
- Flag for manual review
- Don't block student progress
- Show estimated score with caveat

**File Upload Fails:**
- Allow retry
- Resume from last chunk (if chunked upload)
- Validate client-side first
- Clear error message ("File too large" not "Error 413")

**Transcription Fails:**
- Retry transcription service
- Try alternative service
- Allow manual transcript entry
- Flag interview as "needs review"
- Don't penalize student

**Video Recording Issues:**
- Detect browser compatibility issues upfront
- Fallback to audio-only if video fails
- Allow re-recording if student not satisfied
- Provide clear troubleshooting steps

**Edge Cases:**

**Student submits blank/corrupted file:**
- Detect during processing
- Notify student immediately
- Allow resubmission
- Don't count as attempt if deadline hasn't passed

**Multiple students use same answer:**
- Flag for teacher review
- Show similarity percentage
- Don't auto-penalize (could be group work, allowed collaboration)
- Provide evidence for teacher decision

**Student disconnects during interview:**
- Save progress (answered questions so far)
- Allow resume from last question
- Don't require full restart

**Code expires/already used:**
- Clear message: "This code has expired" vs "Invalid code"
- Allow teacher to extend deadline
- Generate new code if needed

**Teacher uploads wrong file:**
- Allow file replacement before students submit
- Notify students if files change after submissions
- Version control for homework files

---

### **12. TEACHER EXPERIENCE OPTIMIZATIONS**

**Goals:**
- Minimize teacher workload
- Provide actionable insights
- Enable quick grading
- Support intervention

**Considerations:**

**Bulk Actions:**
- Send reminders to all pending students
- Download all submissions as ZIP
- Export results to CSV/Excel
- Batch message students

**Smart Recommendations:**
```
AI suggests:
- "3 students struggling with EM - recommend review session"
- "Class average on Q4 is 58% - revisit this topic"
- "5 students showed verbal >> written - offer writing workshop"
- "Sarah Mitchell ready for extension work"
```

**Customizable Reports:**
- Choose which metrics to display
- Filter by student, topic, score range
- Sort by various criteria
- Save report templates

**Integration with LMS:**
- Export grades directly to Canvas, Moodle, etc.
- Sync student rosters
- Link resources

**Override Capabilities:**
- Teacher can adjust AI-given scores
- Add manual notes
- Flag for re-review
- Mark as special circumstances

---

### **13. STUDENT EXPERIENCE OPTIMIZATIONS**

**Goals:**
- Clear guidance
- Low friction
- Encouraging feedback
- Learning-focused

**Considerations:**

**Progressive Disclosure:**
- Don't show everything at once
- Guide step-by-step
- Clear progress indicators
- Celebrate small wins

**Mobile Optimization:**
- Code entry works on phones
- File upload from camera
- Responsive layouts
- Touch-friendly buttons

**Accessibility:**
- Screen reader compatible
- Keyboard navigation
- High contrast mode
- Captions for videos (if instructional)

**Feedback Timing:**
- Show immediate feedback where possible
- Don't make students wait unnecessarily
- Set expectations ("Results in 2-3 minutes")
- Allow early access if teacher approves

**Learning Resources:**
- Link directly to relevant textbook sections
- Embed video explanations
- Provide practice problems
- Connect to Khan Academy, etc.

---

### **14. TESTING STRATEGY**

**Goals:**
- Ensure reliability
- Catch bugs early
- Validate AI accuracy
- Stress test system

**Considerations:**

**Unit Tests:**
- Code generation/validation
- File parsing
- Score calculation
- API endpoints

**Integration Tests:**
- Upload → Processing → Results pipeline
- AI marking accuracy
- Transcription → Analysis pipeline
- Notification delivery

**Load Testing:**
- Simulate 1000 students submitting simultaneously
- Concurrent video uploads
- Database query performance
- AI API rate limit handling

**AI Validation:**
- Create test set of 100 student answers
- Have human experts grade them
- Compare AI grades to human grades
- Measure accuracy, precision, recall
- Iterate on prompts to improve

**User Acceptance Testing:**
- Beta test with real teachers/students
- Collect feedback
- Identify UX issues
- Measure completion rates

---

### **15. DEPLOYMENT & DEVOPS**

**Goals:**
- Reliable deployments
- Zero downtime
- Easy rollbacks
- Monitoring

**Considerations:**

**Infrastructure:**
- Cloud provider: AWS, GCP, or Azure
- Use managed services where possible:
  - RDS/Cloud SQL for database
  - S3/GCS for storage
  - Lambda/Cloud Functions for workers (or ECS/GKE for containers)
  - API Gateway for API management

**CI/CD Pipeline:**
- GitHub Actions, GitLab CI, or Jenkins
- Automated testing on commit
- Staging environment for testing
- Blue-green deployment for zero downtime

**Database Migrations:**
- Use migration tool (Alembic, Flyway)
- Test migrations on staging first
- Backup before production migration
- Rollback plan

**Monitoring:**
- Application logs (CloudWatch, Stackdriver)
- Error tracking (Sentry)
- Performance monitoring (New Relic, DataDog)
- Uptime monitoring (Pingdom, UptimeRobot)

**Backup & Disaster Recovery:**
- Automated DB backups daily
- Point-in-time recovery enabled
- File storage versioning
- Regular restore testing
- Document recovery procedures

---

## **DEVELOPMENT PHASES**

### **Phase 1: MVP (8-12 weeks)**
- Teacher account creation
- Homework creation with file uploads
- Code generation
- Student code entry & answer submission
- Basic AI marking (without interviews)
- Simple results display

### **Phase 2: Interview System (6-8 weeks)**
- Video recording interface
- Audio transcription
- Interview question generation
- Verbal response analysis
- Written vs verbal comparison

### **Phase 3: Analytics & Polish (4-6 weeks)**
- Teacher dashboard with class analytics
- Detailed student reports
- Notifications system
- Export/download features
- Mobile optimization

### **Phase 4: Advanced Features (Ongoing)**
- LMS integrations
- Advanced AI features (adaptive questioning)
- Mobile apps
- Gamification
- Extended subject support

---

## **TECHNOLOGY STACK RECOMMENDATIONS**

**Backend:**
- **Language:** Python (Flask/FastAPI) or Node.js (Express)
- **Database:** PostgreSQL (relational) + Redis (caching)
- **File Storage:** AWS S3 or Google Cloud Storage
- **AI APIs:** OpenAI GPT-4, Anthropic Claude, or both
- **Transcription:** OpenAI Whisper or Google Speech-to-Text
- **Queue:** Celery + Redis, or AWS SQS

**Frontend:**
- **Framework:** React or Vue.js
- **UI Library:** Tailwind CSS (as in the mockups)
- **State Management:** Redux or Zustand
- **Video:** WebRTC, MediaRecorder API
- **Charts:** Recharts or Chart.js

**Infrastructure:**
- **Hosting:** AWS, GCP, or Azure
- **CDN:** CloudFront or CloudFlare
- **Monitoring:** DataDog or New Relic
- **Error Tracking:** Sentry

---

## **CRITICAL SUCCESS FACTORS**

1. **AI Accuracy:** Must match human grading 85%+ of the time
2. **Speed:** Results within 3 minutes of submission
3. **Reliability:** 99.5%+ uptime during school hours
4. **Security:** Zero data breaches, GDPR compliant
5. **UX:** Students complete interview 90%+ of the time
6. **Value:** Teachers save time vs traditional marking

---

This guide provides the architectural foundation and key considerations for building this system. The focus is on reliability, scalability, and user experience while maintaining academic integrity through intelligent AI-powered verification.