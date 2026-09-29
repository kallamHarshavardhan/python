# ============================================================
# class_notes.py — Python Class & Object Notes
# Author  : Harsha Vardhan
# Topic   : OOP — Class and Object
# ============================================================

# ── WHAT IS CLASS ───────────────────────────────────────────
# CLASS  → Blueprint / Recipe / Mold
#          Written ONCE
#          Does NOTHING by itself until object is created

# ── WHAT IS OBJECT ──────────────────────────────────────────
# OBJECT → Actual thing made FROM the class
#          Can make MANY objects from ONE class
#          Output appears ONLY when object calls a method

# ── SYNTAX ──────────────────────────────────────────────────

# class ClassName:
#     def __init__(self, property1, property2):
#         self.property1 = property1      # what it HAS
#         self.property2 = property2
#
#     def method(self):                   # what it DOES
#         print("something")

# ── 3 RULES ─────────────────────────────────────────────────

# 1. CLASS   → recipe/blueprint → written ONCE
# 2. OBJECT  → actual thing made FROM class → make MANY
# 3. self    → refers to THAT specific object
#              user1.name is Harsha
#              user2.name is Rohit
#              self knows WHICH one you mean

# ── __init__ ────────────────────────────────────────────────

# __init__ → runs AUTOMATICALLY when object is created
# Like activating LinkedIn account as soon as it is created
# Stores all properties the object HAS

# ── PROPERTIES vs METHODS ───────────────────────────────────

# Properties → what it HAS  (name, role, company, skills, email)
# Methods    → what it DOES (login, view_profile, get_user)

# ── QUICK REFERENCE ─────────────────────────────────────────

# class      → Blueprint
# object     → Thing made from blueprint
# __init__   → Auto-runs when object is created
# self       → Refers to that specific object
# properties → what it HAS
# methods    → what it DOES

# ── IMPORT RULE ─────────────────────────────────────────────

# from filename import ClassName
# from oop     import LinkedInProfile
#      ↑                    ↑
#   file name           class name
#  (no .py)          (exact spelling)

# ── 3 FILES RULE ────────────────────────────────────────────

# oop.py           → CLASS only    → blueprint
# Import_class.py  → OBJECTS only  → creates + calls methods
# class_notes.py   → NOTES only    → learning reference

# ── CALLING RULE ────────────────────────────────────────────

# CLASS  in oop.py          → defines WHAT to do  (no output)
# OBJECT in Import_class.py → actually DOES it    (output!) ✅

# ── METHOD CALLING RULE ─────────────────────────────────────

# Normal method  → user1.method()         → only needs self
# Connect method → user1.connect(user2)   → needs other user too

# ── CONNECT RULE ────────────────────────────────────────────

# If you need connect → add connect method in oop.py
#                     → create user2 object in Import_class.py
#                     → call user1.connect(user2) at the bottom

# ── OUTPUT RULE ─────────────────────────────────────────────

# class defined   → NO output   (just blueprint)
# object created  → NO output   (just stored)
# method called   → OUTPUT ✅   (appears here only!)

# ============================================================
# REAL LIFE ANALOGY
# ============================================================

# CLASS  = LinkedIn Profile Blueprint
#           defines → name, role, company, skills, email
#                     login(), view_profile(), get_user()
#
# OBJECT = Actual User Profiles made from blueprint
#           user1 → Harsha Vardhan · QA Engineer  · ProcessQ
#           user2 → Rohit Kumar    · DevOps Eng   · Infosys
#           user3 → Priya Singh    · Python Dev   · TCS
#           user4 → Ravi Teja      · Cloud Eng    · Wipro
#
# Same blueprint → Different user profiles! ✅

# ============================================================
# MISTAKES TO AVOID
# ============================================================

# ❌ Missing colon after def
# def get_user(self)       → WRONG
# def get_user(self):      → CORRECT ✅

# ❌ Using property not defined in __init__
# def get_user(self):
#     print(self.email)    → ERROR if email not in __init__!
# Always define in __init__ first ✅

# ❌ Wrong function name when calling
# result = num_of_days()   → WRONG (parameter not function!)
# result = day_of_units()  → CORRECT ✅

# ❌ Hyphen in file name when importing
# from Import-class import  → ERROR!
# from Import_class import  → CORRECT (use underscore) ✅

# ============================================================
# MY LEARNING PROGRESS
# ============================================================

# ✅ Functions
# ✅ Conditionals (if / elif / else)
# ✅ try / except
# ✅ while loop
# ✅ Class and Object
# ✅ Multiple Objects
# ✅ Import between files
# ✅ Splitting code into multiple files