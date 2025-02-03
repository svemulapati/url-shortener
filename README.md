# URL Shortener

This project is a simple URL shortener application built with Python and Flask. It allows users to input a long URL and receive a shortened version.

## Project Structure

```
url-shortener
├── src
│   ├── app.py            # Main application file
│   ├── templates
│   │   └── index.html    # HTML structure for the UI
│   └── static
│       └── styles.css     # CSS styles for the application
├── requirements.txt       # Project dependencies
├── Dockerfile             # Docker configuration
└── README.md              # Project documentation
```

## Setup Instructions

### Using Docker

1. Clone the repository:
   ```
   git clone <repository-url>
   cd url-shortener
   ```

2. Build the Docker image:
   ```
   docker build -t url-shortener .
   ```

3. Run the Docker container:
   ```
   docker run -p 5001:5001 url-shortener
   ```

4. Open your web browser and go to `http://127.0.0.1:5001` to access the URL shortener.

### Without Docker

1. Clone the repository:
   ```
   git clone <repository-url>
   cd url-shortener
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5001` to access the URL shortener.

## Usage

- Enter a long URL in the "Long URL" input field.
- Click the "Shorten" button to generate a shortened URL.
- The shortened URL will be displayed in the second input field.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.