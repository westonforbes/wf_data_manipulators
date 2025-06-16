# Changelog

## 0.0.8 - 2025-05-16
- Data being passed in keep_keys_in_list_dict and remove_keys_in_list_dict was mutable, causing issues with passing as a parameter. modified so the passed data does not get altered.

## 0.0.7 - 2025-05-16
- Added keep_keys_in_list_dict() which is the logical opposite of remove_keys_from_json(), you pass a list of dicts (like seen in Plex API return data) and what you want to keep, it pitches the rest.
- renamed remove_keys_from_json() to delete_keys_in_list_dict().

## 0.0.6 - 2025-05-11
- Cleaned up typo in readme, no code difference.

## 0.0.5 - 2025-05-11
- Added "extract_column_as_list" method.
- Filled out README.md.

## 0.0.4 - 2025-05-11
- Forgot to version setup.py properly.

## 0.0.3 - 2025-05-11
- Trying to get the init right.

## 0.0.2 - 2025-05-11
- Trying to get the init right.

## 0.0.1 - 2025-05-11
- Init