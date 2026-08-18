from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import io

# Enable UTF-8 for Windows
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
except:
    pass

app = Flask(__name__)
CORS(app)

# Global Data Store
data_store = {"status": 0, "latitude": 0.0, "longitude": 0.0, "crash_alert": False}

@app.route('/')
def home():
    return send_from_directory('.', 'dashboard.html')

@app.route('/update', methods=['POST'])
def update_status():
    global data_store
    try:
        data = request.get_json(force=True)
        
        if not data:
            return jsonify({"error": "No JSON received"}), 400

        print(f"[RECEIVED] Data from transmitter: {data}")

        status = int(data.get("status", 0))
        latitude = float(data.get("latitude", 0.0))
        longitude = float(data.get("longitude", 0.0))

        if status == -1:
            data_store["crash_alert"] = True
            print(f"[CRASH ALERT] Location: Lat={latitude}, Lon={longitude}")
        else:
            data_store["crash_alert"] = False

        data_store["status"] = status
        data_store["latitude"] = latitude
        data_store["longitude"] = longitude

        print(f"[UPDATED] Data store: {data_store}")
        return jsonify({"message": "Success"}), 200

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def get_status():
    print("[GET] Sending current status to receiver")
    return jsonify(data_store)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  SMART HELMET SERVER STARTING")
    print("="*50)
    app.run(host='0.0.0.0', port=5000, debug=True)
