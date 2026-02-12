"""
Filter Valid Email Domains
Problem Statement:
Return usernames whose domain is in allowed domains.
"""

def get_domain(email):
    return email.split("@")[1]

def is_allowed_domain(email, allowed_domains):
    return get_domain(email) in allowed_domains

def get_username(email):
    return email.split("@")[0]

def filter_valid_emails(emails, allowed_domains):

    def email_filter(email):
        return is_allowed_domain(email, allowed_domains)

    # Filter valid emails
    valid_emails = list(filter(email_filter, emails))
    print(valid_emails)

    # Extract usernames
    usernames = list(map(get_username, valid_emails))

    return usernames


def main():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
    allowed_domains = {"gmail.com"}

    result = filter_valid_emails(emails, allowed_domains)
    print(f"Valid usernames: {result}")


if __name__ == "__main__":
    main()
