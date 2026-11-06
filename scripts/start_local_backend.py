"""Run the local API with this project's .env taking precedence."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import uvicorn


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env", override=True)
    os.chdir(root / "backend")
    sys.path.insert(0, str(root / "backend"))
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=int(os.environ.get("API_PORT", "8000")),
    )


if __name__ == "__main__":
    main()
