# Python app to show Metadata Info from Kubernetes Pod

This is a simple Python web application that renders a webpage with a background color specified by the environment variable `BG_COLOR`.

## Project Structure

```
my-python-web-app
├── app
│   ├── __init__.py
│   ├── main.py
│   └── templates
│       └── index.html
├── .env
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```
   pip install -r app/requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app/main.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8080`.

## Docker
Docker Buildx is a CLI plugin that extends the Docker command with the full support of the features provided by Moby BuildKit builder toolkit.

```bash
# Enable Docker Buildx:
docker buildx create --use

# Build the Docker image using Buildx:
docker buildx build --platform linux/amd64,linux/arm64 -t josefloressv/metadata-pod --push .

# Run the Docker container:
docker run -d -p 8080:8080 --name metadata-pod --env-file .env josefloressv/metadata-pod

```