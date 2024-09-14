import requests
import time
import json

def main():
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    response = requests.get(url)

    # Prepare log details
    timestamp_unix = int(time.time())
    timestamp_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_unix))
    response_validity = response.status_code == 200
    bytesize = len(response.content)  # Size in bytes

    # Write to latest_response.txt (overwrite)
    try:
        with open("latest_response.txt", "w") as response_file:
            response_file.write(response.text)  # Write the entire response
    except Exception as e:
        print("Error writing to latest_response.txt:", e)

    # Append log details to results.txt
    try:
        with open("results.txt", "a") as results_file:
            if response_validity:
                results_file.write(f"{timestamp_unix} - {timestamp_readable} - Success: Response received. Size: {bytesize} bytes, Valid: {response_validity}\n")
            else:
                results_file.write(f"{timestamp_unix} - {timestamp_readable} - Failure: No response received or failed to retrieve data. Valid: {response_validity}\n")
    except Exception as e:
        print("Error writing to results.txt:", e)

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
