import os
import requests 


def scrape_linkedin_profile():
    '''
    This function scrapes a linkedin profile and returns the following information:
    '''
    response = requests.get("https://gist.githubusercontent.com/arvindkc/8fac136752fbcdc6ca3da9df6307eb8d/raw/085905a6b4af0a6b6e3fcf2fca1fe8ec2da6a60c/gistfile1.txt")
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

    
