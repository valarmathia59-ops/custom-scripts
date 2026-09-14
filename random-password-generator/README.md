# Random Password Generator

A small Python command-line script that creates cryptographically secure random passwords. Passwords include lowercase letters, uppercase letters, digits, and symbols by default.

## Requirements

- Python 3.8 or later

No third-party packages are needed.

## Usage

From this folder, run:

```powershell
python random_password.py
```

This prints a new 16-character password. Choose a different length with `--length` (or `-l`):

```powershell
python random_password.py --length 24
```

To omit symbols:

```powershell
python random_password.py --length 20 --no-symbols
```

The minimum password length is 4 with symbols and 3 without them, so every enabled character group can be represented.

## Security note

The script uses Python's `secrets` module, which is designed for security-sensitive random values. Treat generated passwords as sensitive: avoid sharing them in terminals, screenshots, source control, or chat messages.
