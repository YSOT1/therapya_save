# Therapya

## Overview
Therapya: Your Moroccan Dialect Speech Coach that utilizes the Whisper speech recognition model to transcribe audio recordings and provide feedback on pronunciation accuracy. The application is built using FastAPI and integrates with Supabase for audio file storage.

## Features
- Upload audio recordings for pronunciation analysis.
- Transcribe audio to text using the Whisper model.
- Compare transcriptions against expected sentences.
- Provide feedback on pronunciation, including tips for improvement.

## Technologies Used
- **FastAPI**: A modern web framework for building APIs with Python.
- **Whisper**: An automatic speech recognition (ASR) model developed by OpenAI.
- **Supabase**: An open-source Firebase alternative for database and storage.
- **Python**: The programming language used for backend development.
- **JavaScript/TypeScript**: For the frontend (if applicable).

## Installation

### Prerequisites
- Python 3.7 or higher
- Node.js (if you have a frontend)
- A Supabase account for database and storage

### Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add the following variables:

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
FRONTEND_URL=http://localhost:3000  # Adjust as necessary
UPLOAD_DIR=./temp_uploads  # Directory for temporary uploads

## Running the Application
To start the FastAPI server, run:
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Upload Audio
- **POST** `/upload_audio`
  - **Parameters**: 
    - `file`: The audio file to upload.
    - `email`: User's email for file identification.
  - **Response**: Returns the public URL of the uploaded audio.

### Analyze Pronunciation
- **POST** `/analyze`
  - **Parameters**: 
    - `file`: The audio file to analyze.
    - `expected_sentence`: The expected sentence for comparison.
  - **Response**: Returns the transcription and feedback on pronunciation.

## Frontend
If you have a frontend application, ensure it is set up to communicate with the backend API. Adjust the API URLs as necessary based on your deployment.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenAI for the Whisper model.
- Supabase for providing a robust backend solution.
