import re

MEMBER_ID_PATTERN = re.compile(r"([A-Za-z]+)-([0-9]+)")
GRACE_DAYS = 14
FINE_PER_DAY = 2


def parse_member_id(member_id):
    """Return (TYPE, number) for IDs like 'STU-1023', or None if invalid."""
    if not isinstance(member_id, str):
        return None
    match = MEMBER_ID_PATTERN.fullmatch(member_id.strip())
    if match is None:
        return None
    member_type, number = match.groups()
    try:
        return member_type.upper(), int(number)
    except ValueError:  # e.g. absurdly long digit strings
        return None


def total_fine(days_csv):
    """Sum the fines for a CSV of days kept. Invalid entries are skipped."""
    if not isinstance(days_csv, str):
        return 0
    fine = 0
    for part in days_csv.split(','):
        part = part.strip()
        if not part:
            continue
        try:
            d = int(part)
        except ValueError:
            continue
        if d > GRACE_DAYS:
            fine += (d - GRACE_DAYS) * FINE_PER_DAY
    return fine


def shelf_code(title):
    """Return the uppercase initials of the first two words, or None."""
    if not isinstance(title, str):
        return None
    words = title.split()
    if len(words) < 2:
        return None
    return (words[0][0] + words[1][0]).upper()


def main():
    print("==== Running parse_member_id ====")
    user_input = input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    if result is None:
        print("Invalid member ID. Expected format: TYPE-NUMBER (e.g. STU-1023)")
    else:
        print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    if result is None:
        print("Invalid title. Please enter at least two words.")
    else:
        print("Shelf Code:", result)


if __name__ == "__main__":
    main()
