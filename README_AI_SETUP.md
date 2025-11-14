# AI Image Analysis Setup

This document explains how to set up the AI image analysis feature for the Smart Garbage Management System.

## Prerequisites

1. Python 3.7 or higher
2. Google Gemini API key

## Installation

1. Install required Python packages:
```bash
pip install -r requirements.txt
```

2. Set up your Google Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set it as an environment variable:
     ```bash
     # Windows (PowerShell)
     $env:GEMINI_API_KEY="your_api_key_here"
     
     # Windows (CMD)
     set GEMINI_API_KEY=your_api_key_here
     
     # Linux/Mac
     export GEMINI_API_KEY="your_api_key_here"
     ```
   
   Or edit `ai_image_analyzer.py` and replace `YOUR_API_KEY_HERE` with your actual API key.

## Usage

The AI image analyzer is automatically called by the backend when a user uploads an image in the report submission form.

To test manually:
```bash
python ai_image_analyzer.py path/to/image.jpg
```

## How It Works

1. User uploads an image in the report submission form
2. Frontend sends the image to `/api/analyze-image` endpoint
3. Backend saves the image temporarily and calls the Python script
4. Python script uses Google Gemini Vision API to analyze the image
5. Returns the detected garbage type (plastic, paper, glass, metal, organic, hazardous, or other)
6. Frontend auto-fills the garbage type field with the detected type

## Troubleshooting

- If AI analysis fails, the system defaults to "other" type
- Make sure Python is in your system PATH
- Verify your API key is correct and has proper permissions
- Check that the image file exists and is readable

