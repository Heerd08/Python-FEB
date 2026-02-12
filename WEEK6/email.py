# 2. Filter Valid Email Domains

# Problem Statement
# You are given a list of email addresses. Return a list of usernames (part before @) whose email domain belongs to a given set of allowed domains.

# Input

# emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
# allowed_domains = {"gmail.com"}


# Output

# ["alice", "carol"]


emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
allowed_domains = {"gmail.com"}

# Step 1: Filter emails with allowed domains
valid_emails = list(filter(
    lambda email: email.split("@")[1] in allowed_domains,
    emails
))

# Step 2: Extract usernames (before @)
usernames = list(map(lambda email: email.split("@")[0], valid_emails))

print("Valid Usernames:", usernames)
