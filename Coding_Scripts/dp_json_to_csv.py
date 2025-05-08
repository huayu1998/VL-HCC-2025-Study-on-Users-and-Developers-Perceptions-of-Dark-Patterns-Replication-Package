import csv
import json
import os
import requests
from github import Github

# Initialize the GitHub personal access token for authentication
gh = Github("REPLACE YOUR TOKEN HERE")

def fetch_issues(url):
    """Fetch issues from GitHub API."""
    response = requests.get(url)
    total_count = response.json().get('total_count', 0)  # Default to 0 if 'total_count' is not in the response
    print(f"Total count of search results: {total_count}")
    if response.status_code == 200:
        return response.json()['items']
    else:
        print("Failed to fetch data:", response.status_code)
        return []

"""Filter the issues with the exact phrase 'dark pattern' in the title or body"""
def filter_issues_with_phrase(issues, phrase):
    """Filter issues to exclude bots and include only those with the exact phrase in the title or body."""
    
    # print(issues[0].get('html_url'))
    print("issues before filter: "+str(len(issues)))

    filtered_issues = [
        issue for issue in issues
        # if issue.get('user', {}).get('login', '').lower() not in ["dependabot[bot]", "dependabot-preview[bot]", "imgbot[bot]"]

        if (phrase.lower() in (issue.get('title', '') or '').lower() or phrase.lower() in (issue.get('body', '') or '').lower())
        and issue.get('user', {}).get('login', '').lower() not in ["dependabot[bot]", "dependabot-preview[bot]", "imgbot[bot]"]
    ]

    print("issues after filter: "+str(len(filtered_issues)))
    return filtered_issues

def get_email_by_issue_html_url(html_url):
    # Extract the repository owner, repository name, and issue number from the URL
    path_parts = html_url.split('/')  # Split the URL into parts
    owner = path_parts[3]  # The owner's username is the fourth element
    repo_name = path_parts[4]  # The repository name is the fifth element
    issue_number = int(path_parts[6])  # The issue number is the eighth element
    
    # Fetch the repository
    repo = gh.get_repo(f"{owner}/{repo_name}")
    
    # Fetch the issue by number
    issue = repo.get_issue(number=issue_number)

    # Attempt to fetch publicly visible email
    email = issue.user.email if issue.user.email else "Not Available"
    
    return email

def write_issues_to_csv(issues, filename):
    """Write filtered issues to a CSV file."""
    fields = ['url', 'title', 'html_url', 'body', 'created_at', 'updated_at', 'state', 'comments','email']
    # Check if the file already exists and has content
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

    with open(filename, mode='a', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header only if the file is new or empty
        if not file_exists:
            writer.writerow(fields)
        
        for issue in issues:
            writer.writerow([
                issue['url'],
                issue['title'],
                issue['html_url'],
                issue['body'],
                issue['created_at'],
                issue['updated_at'],
                issue['state'],
                issue['comments'],
                get_email_by_issue_html_url(issue['html_url'])
            ])
    file.close()

def main():
    # The GitHub API URL for fetching issues by time range
    # An example url link for issue search: https://api.github.com/search/issues?q="dark%20pattern"+created:2023-09-01..2024-03-19&page=4&per_page=100
    time_range = '2023-09-01..2024-03-19'
    # Replace the time range to search more issues, examples: 2010-01-01..2019-12-31, 2022-01-01..2023-08-31, etc
    url = 'https://api.github.com/search/issues?q="dark%20pattern"+created:' + time_range + '&page=1&per_page=100'

    # Fetch, filter, and write issues to CSV
    issues = fetch_issues(url)
    filtered_issues = filter_issues_with_phrase(issues, "dark pattern")
    write_issues_to_csv(filtered_issues, "nonbot_dp_output_issues.csv")
    print("Filtered issues have been written to filtered_github_issues.csv")
    
    # Get the rate limit 
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
