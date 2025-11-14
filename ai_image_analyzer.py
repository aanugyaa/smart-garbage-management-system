#!/usr/bin/env python3
"""
AI Image Analyzer for Smart Garbage Management System
Uses Google Gemini API to analyze garbage images and determine type
"""

import sys
import json
import base64
import os
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: google-generativeai package not installed. Install with: pip install google-generativeai")
    sys.exit(1)

# Configure Gemini API
# Set your API key in environment variable GEMINI_API_KEY or update here
API_KEY = os.getenv('GEMINI_API_KEY', 'YOUR_API_KEY_HERE')

if API_KEY == 'YOUR_API_KEY_HERE':
    print("ERROR: Please set GEMINI_API_KEY environment variable or update the script")
    sys.exit(1)

genai.configure(api_key=API_KEY)

def analyze_garbage_image(image_path):
    """
    Analyze a garbage image and determine the type of garbage.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary with garbage type and confidence
    """
    try:
        # Load the image
        if not os.path.exists(image_path):
            return {"error": "Image file not found", "type": "other"}
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro-vision')
        
        # Read image
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        # Create prompt
        prompt = """Analyze this image and determine what type of garbage/waste is shown. 
        Respond with ONLY one of these types (exactly as written):
        - plastic
        - paper
        - glass
        - metal
        - organic
        - hazardous
        - other
        
        If you cannot clearly identify the type, respond with "other".
        Do not include any explanation, just the type."""
        
        # Analyze image
        response = model.generate_content([prompt, {"mime_type": "image/jpeg", "data": image_data}])
        
        garbage_type = response.text.strip().lower()
        
        # Validate response
        valid_types = ['plastic', 'paper', 'glass', 'metal', 'organic', 'hazardous', 'other']
        if garbage_type not in valid_types:
            garbage_type = 'other'
        
        return {
            "type": garbage_type,
            "confidence": "high" if garbage_type != "other" else "medium"
        }
        
    except Exception as e:
        print(f"Error analyzing image: {str(e)}", file=sys.stderr)
        return {"error": str(e), "type": "other"}

def main():
    """Main function to handle command line input"""
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Image path required", "type": "other"}))
        sys.exit(1)
    
    image_path = sys.argv[1]
    result = analyze_garbage_image(image_path)
    
    # Output JSON result
    print(json.dumps(result))
    
    # Exit with error code if there was an error
    if "error" in result:
        sys.exit(1)

if __name__ == "__main__":
    main()

