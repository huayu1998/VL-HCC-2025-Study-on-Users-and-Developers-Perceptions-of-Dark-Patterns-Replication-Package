"""GitHub Dark Pattern Data Collection

Utilizes the PyGitHub API located at
    https://pygithub.readthedocs.io/en/stable/index.html

# Description
#### A Python program to mine dark patterns related issues on GitHub to analyze the developer's activities on Dark Pattern with the PyGitHub API 

# Requires GitHub API Access Token
"""

from github import Github
import csv

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("REPLACE YOUR TOKEN HERE")

# Public Web Github
gh = Github(auth=auth)

def search_issues_and_save_to_csv(query, filename, start_page, end_page):
    """
    Search for issues with the given query and save the results to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Title', 'URL', 'Repository', 'State', 'Comments', 'Creator Email'])

        issues = gh.search_issues(query)
        
        for page_number in range(start_page, end_page):
            print(f"Processing page: {page_number}")
            page_has_issues = False
            for issue in issues.get_page(page_number):
                # Check if the issue was created by dependabot
                if issue.user.login.lower() == "dependabot[bot]" or issue.user.login.lower() == "dependabot-preview[bot]":
                    continue  # Skip this issue
                # ImgBot[bot]
                
                # Attempt to fetch publicly visible email
                email = issue.user.email if issue.user.email else "Not Available"
                
                # Write issue details to CSV, including the creator's email
                writer.writerow([issue.title, issue.html_url, issue.repository.full_name, issue.state, issue.comments, email])
                page_has_issues = True

            if not page_has_issues:
                print("No more issues found.")
                break
def main():
    # Define your search query, including quotes for an exact match
    query = '"dark pattern" in:title,body,comments'
    filename = "github_issues_dark_pattern_1_40.csv"

    # Due to the pages access limitation, please replace the start and end page numbers
    # for every run. Examples: 1-25, 26-50, 51-75, etc.
    start_page = 1
    end_page = 25 
    search_issues_and_save_to_csv(query, filename, start_page, end_page)
    print(f"Issues saved to {filename}")

    # Get the rate limit to check the rate left before the next run
    print('Rate limit/hour:',gh.get_rate_limit().core.limit) # Rate limit per hour
    print('Rate used:',gh.get_rate_limit().core.limit - gh.rate_limiting[0]) # Rate used
    print('Rate remaining:',gh.get_rate_limit().core.remaining) # Rate remaining
    print('Rate reset time:',gh.get_rate_limit().core.reset) # Rate reset time
    # Unix timestamp indicating when rate limiting will reset
    print('Rate reset time in Unix timestamp:',gh.rate_limiting_resettime)
    
    # Return true or pass
    pass

if __name__ == "__main__":
    main()
