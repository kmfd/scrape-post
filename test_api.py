import requests
import time
import os
import subprocess

def main():
    # Print the current working directory
    print("Current Working Directory:", os.getcwd())

    # List installed packages
    print("Installed packages:")
    subprocess.run(["pip", "list"])

    # List directory contents
    print("Directory contents:")
    for item in os.listdir('.'):
        print(item)

    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    response = requests.get(url)

    # Prepare log details
    timestamp_unix = int(time.time())
    timestamp_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_unix))
    response_validity = response.status_code == 200
    bytesize = len(response.content)  # Size in bytes

    # Write to latest_response.txt
    try:
        with open("latest_response.txt", "w") as response_file:
            if response_validity:
                response_file.write(f"{timestamp_unix} - {timestamp_readable} - Success: Response received. Size: {bytesize} bytes, Valid: {response_validity}\n")
            else:
                response_file.write(f"{timestamp_unix} - {timestamp_readable} - Failure: No response received or failed to retrieve data. Valid: {response_validity}\n")
    except Exception as e:
        print("Error writing to file:", e)

    # Print log message to console
    print(f"Run Details: {timestamp_unix}, {timestamp_readable}, Valid: {response_validity}, Size: {bytesize} bytes\n")

    if response_validity:
        print("Success:", response.json())
    else:
        print("Failed to retrieve data:", response.status_code)

if __name__ == "__main__":
    main()



# import requests
# import time

# def main():
    # url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    # response = requests.get(url)

    # # Prepare log details
    # timestamp_unix = int(time.time())
    # timestamp_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_unix))
    # response_validity = response.status_code == 200
    # bytesize = len(response.content)  # Size in bytes

    # # Write to latest_response.txt
    # with open("latest_response.txt", "w") as response_file:
        # if response_validity:
            # response_file.write(f"{timestamp_unix} - {timestamp_readable} - Success: Response received. Size: {bytesize} bytes, Valid: {response_validity}\n")
        # else:
            # response_file.write(f"{timestamp_unix} - {timestamp_readable} - Failure: No response received or failed to retrieve data. Valid: {response_validity}\n")

    # # Print log message to console
    # print(f"Run Details: {timestamp_unix}, {timestamp_readable}, Valid: {response_validity}, Size: {bytesize} bytes\n")

    # if response_validity:
        # print("Success:", response.json())
    # else:
        # print("Failed to retrieve data:", response.status_code)

# if __name__ == "__main__":
    # main()
