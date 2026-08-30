
"""
Deterministic validation for Memoria Digital.

This validator checks AI-generated structured records before
they can be incorporated into the digital memorial.

The validator does not generate or modify information.
It only accepts or rejects data according to predefined rules.
"""

from datetime import datetime


REQUIRED_FIELDS = {
    "year",
    "name",
    "date",
    "source",
    "verified"
}


ALLOWED_FIELDS = {
    "year",
    "name",
    "date",
    "source",
    "source_document",
    "verified"
}


def validate_record(record):
    """
    Validate one structured memorial record.

    Returns:
        (True, []) when the record is valid.
        (False, errors) when the record fails validation.
    """

    errors = []

    # 1. Check that the input is an object/dictionary
    if not isinstance(record, dict):
        return False, ["Record must be a JSON object."]

    # 2. Check required fields
    missing = REQUIRED_FIELDS - record.keys()

    if missing:
        errors.append(
            f"Missing required fields: {', '.join(sorted(missing))}"
        )

    # 3. Reject unexpected fields
    unexpected = set(record.keys()) - ALLOWED_FIELDS

    if unexpected:
        errors.append(
            f"Unexpected fields: {', '.join(sorted(unexpected))}"
        )

    # 4. Validate year
    year = record.get("year")

    if not isinstance(year, int) or isinstance(year, bool):
        errors.append("Year must be an integer.")
    elif year < 2003 or year > 2100:
        errors.append("Year must be between 2003 and 2100.")

    # 5. Validate name
    name = record.get("name")

    if not isinstance(name, str):
        errors.append("Name must be a string.")
    elif not name.strip():
        errors.append("Name cannot be empty.")

    # 6. Validate date
    date = record.get("date")

    if not isinstance(date, str):
        errors.append("Date must be a string.")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            errors.append(
                "Date must use ISO format YYYY-MM-DD."
            )

    # 7. Validate source
    source = record.get("source")

    if not isinstance(source, str) or not source.strip():
        errors.append("Source must be a non-empty string.")

    # 8. Validate source document
    source_document = record.get("source_document")

    if source_document is not None and not isinstance(
        source_document, str
    ):
        errors.append(
            "Source document must be a string or null."
        )

    # 9. Validate verification status
    verified = record.get("verified")

    if not isinstance(verified, bool):
        errors.append("Verified must be true or false.")
    elif verified is not True:
        errors.append(
            "Record must be verified before it can enter the memorial."
        )

    # 10. Final decision
    return len(errors) == 0, errors


if __name__ == "__main__":

    valid_example = {
        "year": 2024,
        "name": "Example Name",
        "date": "2024-03-15",
        "source": "Official public source",
        "source_document": None,
        "verified": True
    }

    valid, errors = validate_record(valid_example)

    if valid:
        print("ACCEPT")
        print("Record passed deterministic validation.")
    else:
        print("REJECT")
        for error in errors:
            print(f"- {error}")


    invalid_example = {
        "year": 2024,
        "name": "Example Name",
        "date": "invalid-date",
        "source": "Official public source",
        "source_document": None,
        "verified": False
    }

    valid, errors = validate_record(invalid_example)

    if valid:
        print("ACCEPT")
        print("Record passed deterministic validation.")
    else:
        print("REJECT")
        for error in errors:
            print(f"- {error}")

