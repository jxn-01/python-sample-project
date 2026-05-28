from pathlib import Path

from main import main

if __name__ == "__main__":
    sample_path = Path(__file__).resolve().parent / "data" / "sample_data.csv"
    main([str(sample_path)])
