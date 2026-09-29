class LinkedInProfile:

    # __init__ → runs automatically when object is created
    def __init__(self, name, role, company, skills, email):
        self.name    = name
        self.role    = role
        self.company = company
        self.skills  = skills
        self.email   = email

    # method 1
    def login(self):
        print(f"Welcome back {self.name}! You are logged in.")

    # method 2
    def view_profile(self):
        print(f"---- LinkedIn Profile ----")
        print(f"Name    : {self.name}")
        print(f"Role    : {self.role}")
        print(f"Company : {self.company}")
        print(f"Skills  : {', '.join(self.skills)}")
        print(f"--------------------------")

    # method 3
    def get_user(self):
        print(f"{self.name} you can connect me at {self.email}!")


# ── CREATE MULTIPLE USERS ────────────────────────────────────

user1 = LinkedInProfile(
    name    = "Harsha Vardhan",
    role    = "QA Engineer → DevOps Learner",
    company = "ProcessQ India LLP",
    skills  = ["Manual Testing", "Ansible", "AWS", "Python"],
    email   = "harshavardhanr419@gmail.com"
)

user2 = LinkedInProfile(
    name    = "Rohit Kumar",
    role    = "DevOps Engineer",
    company = "Infosys",
    skills  = ["Docker", "Kubernetes", "Jenkins", "AWS"],
    email   = "rohit@gmail.com"
)

user3 = LinkedInProfile(
    name    = "Priya Singh",
    role    = "Python Developer",
    company = "TCS",
    skills  = ["Python", "Django", "SQL", "REST API"],
    email   = "priya@gmail.com"
)

user4 = LinkedInProfile(
    name    = "Ravi Teja",
    role    = "Cloud Engineer",
    company = "Wipro",
    skills  = ["AWS", "Terraform", "Linux", "Docker"],
    email   = "ravi@gmail.com"
)

# ── USE ALL USERS ────────────────────────────────────────────

user1.login()
user1.view_profile()
user1.get_user()

print()

user2.login()
user2.view_profile()
user2.get_user()

print()

user3.login()
user3.view_profile()
user3.get_user()

print()

user4.login()
user4.view_profile()
user4.get_user()
