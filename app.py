from flask import Flask, request, jsonify
from flask_cors import CORS
from note_generator import NoteGenerator
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate-meeting-notes', methods=['GET'])
def generate_meeting_notes():
    note_generator = NoteGenerator()
    summaries = note_generator.get_notes_for_transcription_file(request.args.get('file-name'))

    return jsonify({"summaries": summaries}), 200

@app.route('/transcripts/file-names', methods=['GET'])
def get_transcript_file_names():

    transcripts_dir = '/app/transcripts' if os.path.exists('/app/transcripts') else './'

    try:
        file_names = os.listdir(transcripts_dir)
        file_names = [f for f in file_names if os.path.isfile(os.path.join(transcripts_dir, f))]
        return jsonify({"files": file_names}), 200
    except FileNotFoundError:
        return jsonify({"error": f"Directory '{transcripts_dir}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)