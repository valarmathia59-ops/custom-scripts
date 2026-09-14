"""Generate cryptographically secure random passwords from the command line."""

from __future__ import annotations

import argparse
import secrets
import string


DEFAULT_LENGTH = 16
MIN_LENGTH = 4


def generate_password(length: int, include_symbols: bool = True) -> str:
    """Return a secure password containing uppercase, lowercase, digits, and symbols.

    The password is guaranteed to contain at least one character from each
    selected character group.
    """
    character_groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if include_symbols:
        character_groups.append("!@#$%^&*()-_=+[]{}:,.?")

    if length < len(character_groups):
        raise ValueError(
            f"Password length must be at least {len(character_groups)} "
            "for the selected character options."
        )

    required_characters = [secrets.choice(group) for group in character_groups]
    alphabet = "".join(character_groups)
    remaining_characters = [secrets.choice(alphabet) for _ in range(length - len(required_characters))]
    password_characters = required_characters + remaining_characters
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "-l", "--length", type=int, default=DEFAULT_LENGTH, help=f"Password length (default: {DEFAULT_LENGTH})."
    )
    parser.add_argument(
        "--no-symbols", action="store_true", help="Generate a password without symbols."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    minimum = 3 if args.no_symbols else MIN_LENGTH
    if args.length < minimum:
        raise SystemExit(f"Error: password length must be at least {minimum}.")

    print(generate_password(args.length, include_symbols=not args.no_symbols))


if __name__ == "__main__":
    main()
