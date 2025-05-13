# VL-HCC-2025-Study-on-Users-and-Developers-Perceptions-of-Dark-Patterns-Replication-Package

Python scripts to collect the Dark Patterns data on GitHub &amp; Data files and data analysis to understand the user's and developers' perceptions of Dark Patterns in Online Environments and Software Development

## Description of the folder contents in this repository:

**Note:** DP refers to Dark Patterns &amp; non-DP refers to Non Dark Patterns.

**Coding_Scripts**
1. The folder contains the Python scripts used to collect and preprocess DP and non-DP related to GitHub data for further sentiment analysis.
2. The ``dp_filter.py`` file is used to collect the review comments based on the URLs and filter the DP, non-DP, and non-English issues.
3. The ``dp_github_search.py`` file collects information on DP-related issues, including title, body, and comments based on *page numbers*.
4. The ``dp_json_to_csv.py`` file collects information on DP-related issues, including URL, title, html_url, body, created_at, updated_at, state, and comments based on *time range*.
5. The ``preprocess_dp.py`` file preprocess the raw data and run the sentiment analysis on the cleaned data

**GitHub_Sentiment_Analysis**
1. The folder contains the original dark patterns GitHub issues search result file and corresponding sentiment analysis results for the title, body, and review comments.
2. The ``original_dp_issues.csv`` file contains the original non-preprocessed html_url, title, body, created_at, updated_at, state, and comments of the DP and non-DP issues based on the issue's URLs.
3. The ``dp_title.csv`` file contains DP-related Github issues' data and analysis, including URL, title, html_url, and sentiment analysis results for title message using SentiStrength-SE and DEVA.
4. The ``dp_body.csv`` file contains DP-related Github issues' data and analysis, including URL, body, html_url, and sentiment analysis results for body messages using SentiStrength-SE and DEVA.
5. The ``dp_comments.csv`` file contains DP-related Github issues' data and analysis, including URL, body, html_url, and sentiment analysis results for review comments using SentiStrength-SE and DEVA.
6. The ``non_dp_title.csv`` file contains non-DP-related Github issues' data and analysis, including URL, title, html_url, and sentiment analysis results for title message using SentiStrength-SE and DEVA.
4. The ``non_dp_body.csv`` file contains non-DP-related Github issues' data and analysis, including URL, body, html_url, and sentiment analysis results for body messages using SentiStrength-SE and DEVA.
5. The ``non_dp_comments.csv`` file contains non-DP-related Github issues' data and analysis, including URL, body, html_url, and sentiment analysis results for review comments using SentiStrength-SE and DEVA.

**Surveys**
1. This directory contains a copy of the user and developer surveys distributed to end users and OSS developers to further explore their perceptions of dark patterns.
3. The ``User_Survey_Dark_Pattern.pdf`` contains full details of the end-user survey.
4. The ``User_Survey_Results.csv`` contains the original responses from user group participants, open coding, and sentiment analysis results.
6. The ``Developer_Survey_Dark_Pattern.pdf`` contains full details of the developer survey.
7. The ``Developer_Survey_Results.csv`` contains the original responses from developer group participants, open coding, and sentiment analysis results.
