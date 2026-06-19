#!/usr/bin/env python3

from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

# Correct __file__ usage
ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Trace Receipt",
        "schema": ROOT / "schemas" / "trace-receipt.schema.json",
        "example": ROOT / "examples" / "trace-receipt.example.yaml",
    }
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        print(f"[error] {name} validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.absolute_path)
            if not path:
                path = "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {name} example is valid")
    return True

def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        ok = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_valid = all_valid and ok

    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())
