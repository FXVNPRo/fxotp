import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is not installed.")
    print("Install it with:")
    print("pip install jsonschema")
    sys.exit(1)


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    if len(sys.argv) != 2:
        print("FXOTP Validator")
        print("")
        print("Usage:")
        print("python validate.py <fxotp-message.json>")
        sys.exit(1)

    validator_dir = Path(__file__).resolve().parent
    project_root = validator_dir.parent.parent

    schema_path = project_root / "specification" / "signal.schema.json"
    message_path = Path(sys.argv[1])

    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}")
        sys.exit(1)

    if not message_path.exists():
        print(f"ERROR: Message not found: {message_path}")
        sys.exit(1)

    try:
        schema = load_json(schema_path)
        message = load_json(message_path)
    except json.JSONDecodeError as error:
        print("INVALID JSON")
        print(error)
        sys.exit(1)

    validator = Draft202012Validator(schema)

    errors = sorted(
        validator.iter_errors(message),
        key=lambda error: list(error.path)
    )

    if errors:
        print("INVALID FXOTP MESSAGE")
        print("")

        for error in errors:
            location = ".".join(str(item) for item in error.path)

            if not location:
                location = "root"

            print(f"- {location}: {error.message}")

        sys.exit(1)

    print("VALID FXOTP MESSAGE")
    print("")
    print(f"Protocol : {message.get('protocol')}")
    print(f"Version  : {message.get('version')}")
    print(f"ID       : {message.get('id')}")

    instrument = message.get("instrument", {})
    print(f"Symbol   : {instrument.get('symbol')}")
    print(f"Action   : {message.get('action')}")


if __name__ == "__main__":
    main()
