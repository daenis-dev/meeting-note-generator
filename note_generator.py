from openai import OpenAI
import os
import re

class NoteGenerator:
    
    def get_notes_for_transcription_file(self, file_name):
        summaries = {}

        transcript = self.clean_vtt(self.load_file(file_name))

        transcript_sections = self.divide_transcript_into_groups_of_four_thousand_characters(transcript)

        for idx, transcript_section in enumerate(transcript_sections):
            summaries[idx + 1] = self.get_summary_for_transcript_section(transcript_section)

        output_file_name = file_name.replace('.vtt', '') + '_summary.txt'
        with open(output_file_name, 'w', encoding='utf-8') as f:
            for idx, summary in summaries.items():
                f.write(f"{idx}) {summary}\n\n")
        
        return [summary for _, summary in sorted(summaries.items())]


    def clean_vtt(self, raw_text):
        raw_text = raw_text.replace("WEBVTT", "").strip()
        
        cleaned_text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', raw_text)
        
        lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
        return '\n'.join(lines)
    
    def load_file(self, file_name):
        with open('transcripts/' + file_name, 'r', encoding='utf-8') as f:
            return f.read()
    
    def divide_transcript_into_groups_of_four_thousand_characters(self, file):
        chunk_size = 4000
        return [file[i:i + chunk_size] for i in range(0, len(file), chunk_size)]
    
    def get_summary_for_transcript_section(self, transcript_section):
        prompt = f"Summarize the following meeting transcript section in 2-3 sentences:\n\n{transcript_section}"

        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides concise summaries of meeting transcript sections."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()
