# scrape-post
Web Scraper via GitHub Actions to GitHub Pages - Demo

## What does this do?
This is a demo of a web scraper that uses Python and GitHub Actions to automate the process of making the request and then publishing the scraped data to a GitHub repository. The scraper, which runs on GitHub's servers, fetches data from a specified API or website and commits the results to the repository.
The Action which causes this is set to run whenever there is a commit to the repo, and it can also be triggered manually.

## How does this work?
The scraper is implemented in Python and is triggered by GitHub Actions. When changes are pushed to the main branch or when manually triggered, the action runs the scraper, collects the data, and commits the results back to the repository. This allows for continuous integration and deployment of the scraped data.

This scripted action occurs on GitHub's servers. The request to the website or API therefore originates from GitHub. Neat! Per GitHub:

> **About GitHub-hosted runners**  
> GitHub offers hosted virtual machines to run workflows. The virtual machine contains an environment of tools, packages, and settings available for GitHub Actions to use.

- Reference: About GitHub-hosted runners - [https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners) 

## Why do we want this?
This lets us get info without having to check the source directly. We can do all kinds of things to the data before publishing. That this does not take place on our own machine means reliability, potential cost savings, and possibly avoiding limitations such as annoying or broken interfaces.

## Summary of how to set this up yourself

### 1. Create the Repository
1. Go to GitHub and create a new repository.
2. Set the repository to private if desired.
3. Enable workflows to write to the repository so that the scraper can push the JSON response. 
   - Navigate to **Settings -> Actions -> General -> Workflow permissions** and choose **Read and write permissions**.
   - Reference: Permission Denied to GitHub Actions Bot - [https://stackoverflow.com/questions/73687176/permission-denied-to-github-actionsbot-the-requested-url-returned-error-403](https://stackoverflow.com/questions/73687176/permission-denied-to-github-actionsbot-the-requested-url-returned-error-403)

### 2. Create the Python File
Create a Python file (e.g., `test_api.py`) that contains the logic for your web scraper. This file should include the necessary libraries (we used Python's `requests`) to fetch and parse the data you want to scrape.

### 3. Create the GitHub Action YAML File
Create a new directory called `.github/workflows` in your repository and add a YAML file (e.g., `python-curl.yml`).
(Github will offer to do this for you when you go to Actions if you have not yet created an Action.)

To see what this should look like please have a look at the default file which GitHub suggests, and see `python-curl.yml` in this repo which is fit for our purposes. You can find many other examples of these for various purposes online.

### Action and Python Versions
Note specifically in ours:
- `checkout@v4`
- `setup-python@v5`

These are the latest at this time; you can see what is latest on the action's page listed in GitHub's marketplace.
- Reference: Checkout Action - [https://github.com/marketplace/actions/checkout](https://github.com/marketplace/actions/checkout)
- Reference: Setup Python Action - [https://github.com/marketplace/actions/setup-python](https://github.com/marketplace/actions/setup-python)

`python-version: '3.8'` is used here, but you can use your preferred version or whatever is needed for the task.

### YAML Run
`run: python test_api.py`
We indicate on this line our Python file to run.

### GitHub Commit Actions
- git add latest_response.txt and results.txt (These are the two files we have chosen to log results to. They are hardcoded here so be sure to ensure the changes you want to capture are similarly added to the commit. You could commit the whole directory but that would not be tidy, would it?)
- Note we use GitHub's credentials here, and `secrets.GITHUB_TOKEN` is automatically created and used when we enter it this way.
- Reference: About the GitHub Token Secret https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#about-the-github_token-secret

## Quality of life improvements present
Beyond the bare minimim of what we've outlined above, we added a few minor checks to the github actions file that are logged in the job results.
- check working dir path and contents
- check installed pip packages
- git diff before commit

# Additional thoughts

## Other resources related to this

## Other projects with this type of functionality
