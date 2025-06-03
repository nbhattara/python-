import requests

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "Up"
        else:
            return f"Down (Status code: {response.status_code})"
    except requests.RequestException:
        return "Down"

def main():
    websites = input("Enter website URLs separated by commas: ").split(",")

    print("\nWebsite Status Report:")
    for site in websites:
        site = site.strip()
        if not site.startswith("http"):
            site = "https://" + site
        status = check_website_status(site)
        print(f"{site}: {status}")

if __name__ == "__main__":
    main()
