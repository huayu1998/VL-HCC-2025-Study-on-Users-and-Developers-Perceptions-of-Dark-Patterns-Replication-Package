import requests
from github import Github
import pandas as pd
from langdetect import detect

# set up the access token
gh = Github("REPLACE YOUR TOKEN HERE")
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer REPLACE YOUR TOKEN HERE"
}

def get_single_issue_comment_only(issue_url):
    # issue json object
    issue_json = requests.get(issue_url, headers=headers).json()
    comment = ''
    # review comment
    if issue_json.get('comments_url'):
        review_url = issue_json.get('comments_url')
        review_json = requests.get(review_url, headers=headers).json()
        if review_json:
            for review in review_json:
                comment = comment + review.get('body') + '\n' 
    return comment

def get_all_issues_comments_only(inputFile, outputFile):
    # read input csv file and get GitHub API url links
    df = pd.read_csv(inputFile)
    df = df.dropna(subset=['url'])
    df = df.reset_index(drop=False)
    urls = df["url"]
    review_comments = []
    index = 0
    for url in urls: 
        comments = get_single_issue_comment_only(url)
        if comments:
            review_comments.append(comments)
        else:
            review_comments.append('')
        print(str(index) + ": " + url)
        index += 1
    # save the df as a new csv output file
    df['review_comments'] = review_comments
    df.to_csv(outputFile, index=False)
    return 1

def get_single_issue_contents(issue_url):
    # issue json object
    issue_json = requests.get(issue_url, headers=headers).json()
    comments = ''
    # title and body
    title = issue_json.get('title')
    body = issue_json.get('body')
    if title:
        comments = comments + title + '\n'
    if body:
        comments = comments + body + '\n'
    # review comments
    if issue_json.get('comments_url'):
        review_url = issue_json.get('comments_url')
        review_json = requests.get(review_url, headers=headers).json()
        if review_json:
            for review in review_json:
                comments = comments + review.get('body') + '\n' 
    return comments

def get_all_issues_contents(inputFile, outputFile):
    # read input csv file and get GitHub API url links
    df = pd.read_csv(inputFile)
    df = df.dropna(subset=['url'])
    df = df.reset_index(drop=False)
    urls = df["url"]
    review_comments = []
    index = 0
    for url in urls: 
        comments = get_single_issue_contents(url)
        if comments:
            review_comments.append(comments)
        else:
            review_comments.append('')
        print(str(index) + ": " + url)
        index += 1
    # save the df as a new csv output file
    df['filter_contents'] = review_comments
    df.to_csv(outputFile, index=False)
    return 1

def keywords_matched(keywords, inputFile, outputFile):
    # read input csv file and get GitHub API url links
    df = pd.read_csv(inputFile)
    df = df.dropna(subset=['filter_contents'])
    df = df.reset_index(drop=False)
    filter_contents = df["filter_contents"]
    dp_filter_results = []
    num = 1 
    for cur in filter_contents:
        lower_text = cur.lower()
        if any(keyword in lower_text for keyword in keywords):
            num += 1
            # 1 means is dark pattern related
            dp_filter_results.append(1)
        else:
            # 0 means is NOT dark pattern related
            dp_filter_results.append(0)
    print("Total number of dark pattern issues: " + str(num))
    # save the df as a new csv output file
    df['dp_filter_results'] = dp_filter_results
    df.to_csv(outputFile, index=False)
    return 1

def filter_language(inputFile, outputFile):
    # read input csv file and get GitHub API url links
    df = pd.read_csv(inputFile)
    df = df.dropna(subset=['filter_contents'])
    df = df.reset_index(drop=False)
    filter_contents = df["filter_contents"]
    filter_results = df["dp_filter_results"]
    length = len(filter_results)
    num = 0
    file = open("./non_en_nondp_contents.txt", "w")
    # filter the non-en issues using langdetect package
    for index in range(length):
        # check if the issues is dp-related (1) or not dp-related(0)
        content = filter_contents[index]
        # filter out the non-en dp_related (1)
        if filter_results[index] == 1:
            content = filter_contents[index]
            if (detect(content)!='en'):
                num += 1
                file.write(str(num)+": **************************************\n"+content)
                df = df.drop(index=index)
        # filter out the non-en not dp_related (0)
        if filter_results[index] == 0:
            content = filter_contents[index]
            if (detect(content)!='en'):
                num += 1
                file.write(str(num)+": **************************************\n"+content)
                df = df.drop(index=index)

    print("Number of non-en issues: " + str(num))
    file.close()
    # save the df as a new csv output file
    df.to_csv(outputFile, index=False)
    return 1

def main():
    # Define the input and output file names
    inputFile = 'THE_FILE_NAME_OF_ORIGINAL_GITHUB_ISSUES_SEARCH.csv'
    outputFile1 = 'all_issues_contents_output.csv'
    outputFile2 = 'all_issues_comments_output.csv'
    outputFile3 = 'filtered_language_output.csv'

    # Filter the non dark pattern related issues
    keywords = ["dark pattern", "darkpattern", "dark-pattern", "dark_pattern"]
    keywords_matched(keywords, inputFile, 'DARK_PATTERN_FILTER_FILE_NAME.csv')

    # Get the issues title, body, and comments separately
    get_all_issues_contents('DARK_PATTERN_FILTER_FILE_NAME.csv', outputFile1)
    get_all_issues_comments_only('DARK_PATTERN_FILTER_FILE_NAME.csv', outputFile2)
    filter_language('DARK_PATTERN_FILTER_FILE_NAME.csv', outputFile3)

    # Get and print out the rate limit
    url = "https://api.github.com/repos/OwlCarousel2/OwlCarousel2/issues/1459" # An example of issue url
    response = requests.get(url, headers=headers)
    print('X-RateLimit-Limit: ', response.headers.get('X-RateLimit-Limit'), '\n')
    print('X-RateLimit-Used: ', response.headers.get('X-RateLimit-Used'), '\n')
    print('X-RateLimit-Remaining: ', response.headers.get('X-RateLimit-Remaining'), '\n')
    print('X-RateLimit-Reset: ', response.headers.get('X-RateLimit-Reset'), '\n')
    
    # Return true or pass
    pass

if __name__ == "__main__":
    main()
