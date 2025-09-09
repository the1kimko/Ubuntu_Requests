import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user to enter an image URL
    url = input("Please enter the image URL: ").strip()

    # Create directory for saving images if not already present
    os.makedirs("Fetched_Images", exist_ok=True)

    try:
        # Fetch the image with a network timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Ensure HTTP OK status

        # Extract filename from URL path
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Generate default filename if none present
        if not filename:
            filename = "downloaded_image.jpg"

        # Path for saving the image file
        filepath = os.path.join("Fetched_Images", filename)

        # Save the image data in binary mode
        with open(filepath, 'wb') as file:
            file.write(response.content)

        # Confirm success to user
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        # Handle network/HTTP related errors gracefully
        print(f"✗ Connection error: {e}")
    except OSError as e:
        # Handle file system related errors gracefully
        print(f"✗ File system error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
