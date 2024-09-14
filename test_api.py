import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API with a response as of 2024-09-13
    response = requests.get(url)

    if response.status_code == 200:
        print("Success:", response.json())
        with open("results.txt", "w") as f:
            f.write(str(response.json()))
    else:
        print("Failed to retrieve data:", response.status_code)

if __name__ == "__main__":
    main()
