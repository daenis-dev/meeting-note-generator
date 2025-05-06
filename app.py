from flask import Flask, request, jsonify
from flask_cors import CORS
from note_generator import NoteGenerator

app = Flask(__name__)
CORS(app)

@app.route('/generate-meeting-notes', methods=['GET'])
def generate_meeting_notes():
    note_generator = NoteGenerator()
    note_generator.get_notes_for_transcription_file(request.args.get('file-name'))

    return jsonify({"message": "Request successful"}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)