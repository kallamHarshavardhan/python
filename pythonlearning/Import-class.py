# ============================================================
# Import_class.py — Objects File
# This file IMPORTS class from oop.py
# CREATES objects and CALLS all methods
# ============================================================

# ── IMPORT ──────────────────────────────────────────────────
# Borrowing LinkedInProfile class from oop.py
from oop import LinkedInProfile    # ✅ oop.py has the class

# ── CREATING OBJECTS ─────────────────────────────────────────
# Same blueprint used for all 4 users
# Each user is a separate object with different data

# Object 1 → Harsha Vardhan
user1 = LinkedInProfile(
    name    = "Harsha Vardhan",
    role    = "QA Engineer → DevOps Learner",
    company = "ProcessQ India LLP",
    skills  = ["Manual Testing", "Ansible", "AWS", "Python"],
    email   = "harshavardhanr419@gmail.com"
)

# Object 2 → Rohit Kumar
user2 = LinkedInProfile(
    name    = "Rohit Kumar",
    role    = "DevOps Engineer",
    company = "Infosys",
    skills  = ["Docker", "Kubernetes", "Jenkins", "AWS"],
    email   = "rohit@gmail.com"
)

# Object 3 → Priya Singh
user3 = LinkedInProfile(
    name    = "Priya Singh",
    role    = "Python Developer",
    company = "TCS",
    skills  = ["Python", "Django", "SQL", "REST API"],
    email   = "priya@gmail.com"
)

# Object 4 → Ravi Teja
user4 = LinkedInProfile(
    name    = "Ravi Teja",
    role    = "Cloud Engineer",
    company = "Wipro",
    skills  = ["AWS", "Terraform", "Linux", "Docker"],
    email   = "ravi@gmail.com"
)

# ── CALLING METHODS ──────────────────────────────────────────
# Nothing runs until we call methods here
# Each user → login, view_profile, get_user

# ── User 1 Output ────────────────────────────────────────────
user1.login()           # prints welcome message
user1.view_profile()    # prints full profile
user1.get_user()        # prints name + email

print()                 # empty line

# ── User 2 Output ────────────────────────────────────────────
user2.login()
user2.view_profile()
user2.get_user()

print()                 # empty line

# ── User 3 Output ────────────────────────────────────────────
user3.login()
user3.view_profile()
user3.get_user()

print()                 # empty line

# ── User 4 Output ────────────────────────────────────────────
user4.login()
user4.view_profile()
user4.get_user()

# ============================================================
# SUMMARY
# ============================================================

# oop.py          → has CLASS      → blueprint only
# Import_class.py → has OBJECTS    → creates + calls methods
# from oop import LinkedInProfile  → borrows class from oop.py

# ── RULE ─────────────────────────────────────────────────────
# CLASS  in oop.py          → defines WHAT to do  (no output)
# OBJECT in Import_class.py → actually DOES it    (output!) ✅