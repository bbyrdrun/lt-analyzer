# LT Analyzer (starter)
Upload a CSV with time, HR, and optional lactate; the app plots your session and estimates LT1 (~2 mmol) and LT2 (~4 mmol).

## Run locally
1. Install Python 3.10+  
2. Clone or download this repo  
3. In a terminal:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   streamlit run app.py
