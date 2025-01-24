# Instagram Mentioned Posts Fetcher

This Python script uses the [Instaloader](https://instaloader.github.io/) library to retrieve Instagram posts by a specific user within a specified date range and filters posts that contain mentions (e.g., `@username`) in their captions.

## Features
- Retrieves all posts from a specified Instagram profile.
- Filters posts by a user-defined date range.
- Identifies posts containing mentions (e.g., `@username`) in their captions.
- Outputs the URLs of all posts with mentions.

## Requirements
- Python 3.6 or later
- `instaloader` library (install via `pip install instaloader`)

## Usage
1. Clone this repository or download the script file.
2. Install the required `instaloader` library:
   ```bash
   pip install instaloader
