import os
import requests 


def scrape_linkedin_profile():
    '''
    This function scrapes a linkedin profile and returns the following information:
    '''
    response = requests.get("https://gist.githubusercontent.com/arvindkc/008a717bb4688d3fe7b38a69ed2fa2b2/raw/900d312017e9ec36edac29b2a23d6baa3480772d/gistfile1.txt")
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

    
