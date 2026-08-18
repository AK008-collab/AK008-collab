# Smart Helmet — Source Code

This directory contains the web/backend portion of the Smart Helmet prototype supplied for the project portfolio.

## Included

- `app.py` — Flask API server and in-memory data store
- `requirements.txt` — Python dependencies
- `templates/dashboard.html` — live dashboard client
- `templates/index.html` — GPS live-location map client
- `static/style.css` — frontend styling

## API

### `POST /update`

Receives helmet telemetry as JSON.

Example:

```json
{
  "status": 1,
  "latitude": 11.9795,
  "longitude": 79.832199
}
```

A status of `-1` is treated by the current prototype as a crash-alert condition.

### `GET /status`

Returns the latest stored status, latitude, longitude and crash-alert flag.

## Run locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python app.py
```

The Flask server listens on port `5000`.

## Architecture

```text
ESP8266 / ESP32
       |
       | HTTP POST /update
       v
   Flask Server
       |
       +---- GET /status ----> Web Dashboard
       |
       +---- GPS data -------> Live Map
```

## Important note

This is prototype software. The current backend uses an in-memory data store and CORS is enabled for development. A production deployment should add authentication, input validation, persistent storage, HTTPS and appropriate access controls.
