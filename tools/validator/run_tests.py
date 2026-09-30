import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_file(validator, path):
    try:
        message = load_json(path)
    except (json.JSONDecodeError, OSError) as error:
        return False, [f"JSON/file error: {error}"]

    errors = sorted(
        validator.iter_errors(message),
        key=lambda error: list(error.path)
    )

    return len(errors) == 0, errors


def main():
    validator_dir = Path(__file__).resolve().parent
    project_root = validator_dir.parent.parent

    schema_path = project_root / "specification" / "signal.schema.json"
    examples_dir = project_root / "examples"
    invalid_dir = project_root / "tests" / "invalid"

    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}")
        return 1

    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)

    failures = 0
    tests = 0

    print("FXOTP Test Suite")
    print("================")
    print()

    print("Valid examples must PASS")
    print("------------------------")

    valid_files = sorted(examples_dir.rglob("*.json"))

    if not valid_files:
        print("FAIL: No valid examples found.")
        failures += 1

    for path in valid_files:
        tests += 1
        valid, errors = validate_file(validator, path)
        relative = path.relative_to(project_root)

        if valid:
            print(f"PASS: {relative}")
        else:
            failures += 1
            print(f"FAIL: {relative} should be valid")

            for error in errors:
                location = ".".join(str(item) for item in error.path) or "root"
                print(f"      {location}: {error.message}")

    print()
    print("Invalid fixtures must FAIL")
    print("--------------------------")

    invalid_files = sorted(invalid_dir.rglob("*.json"))

    if not invalid_files:
        print("FAIL: No invalid test fixtures found.")
        failures += 1

    for path in invalid_files:
        tests += 1
        valid, errors = validate_file(validator, path)
        relative = path.relative_to(project_root)

        if not valid:
            print(f"PASS: {relative} was correctly rejected")
        else:
            failures += 1
            print(f"FAIL: {relative} should have been rejected")

    print()
    print("================")

    if failures:
        print(f"TEST SUITE FAILED: {failures} failure(s), {tests} test(s)")
        return 1

    print(f"ALL TESTS PASSED: {tests} test(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
