## 📝 Setup Instructions

### 📥 Download the Application

1. **Clone the Repository**
   ```bash
   cd ~/projects
   git clone git@github.com:daenis-dev/meeting-note-generator.git
   ```

2. **Obtain an OpenAI API Key**

   - Visit [platform.openai.com](https://platform.openai.com/account/api-keys) to generate your key.

3. **Create a `.env` File**

   In the project root directory:
   ```bash
   cd meeting-note-generator
   touch .env
   ```

   Add the following line to `.env`:
   ```
   OPENAI_API_KEY=your-openai-key
   ```

4. **Install Docker Desktop**

   - [Download Docker](https://www.docker.com/products/docker-desktop) and follow installation instructions for your OS.

---

### 📤 Export the Transcript

1. Open Microsoft Teams and locate your meeting in the **calendar**.
2. Export the transcript file and save it to:
   ```
   ~/projects/meeting-note-generator
   ```
3. Rename the file as:
   ```
   Meeting_Transcript_<Month>_<Day>_<Year>.txt
   ```
   Example:
   ```
   Meeting_Transcript_May_5_2025.txt
   ```

---

### 📦 Copy the Transcript to the Container

- Open the `Dockerfile` and **uncomment the transcript `COPY` line**.
- Ensure the file name in the line matches your transcript name:
  ```Dockerfile
  COPY Meeting_Transcript_May_5_2025.txt .
  ```

---

### ▶️ Run the Application

```bash
docker compose build --no-cache && docker compose up
```

The API will be available at: [http://localhost:8080](http://localhost:8080)