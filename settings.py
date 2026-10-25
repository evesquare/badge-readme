import os

START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"

REPOSITORY = os.getenv("INPUT_REPOSITORY")
GH_TOKEN = os.getenv("INPUT_GH_TOKEN")
GH_API_URL = os.getenv("INPUT_GH_API_URL")
COMMIT_MESSAGE = os.getenv("INPUT_COMMIT_MESSAGE")
CREDLY_USER = os.getenv("INPUT_CREDLY_USER")


def _parse_credly_users(raw_users, legacy_user):
    """Parse a comma/whitespace separated user list, keeping the legacy
    single-user setting working.

    Order is preserved and duplicates are removed, because the same
    badge can be visible from more than one account.
    """
    users = []
    for raw in (raw_users or "", legacy_user or ""):
        for name in raw.replace(",", " ").split():
            name = name.strip()
            if name and name not in users:
                users.append(name)
    return users


# CREDLY_USERS accepts several Credly accounts (e.g. a personal account
# and a work account): INPUT_CREDLY_USERS="user1,user2".
# INPUT_CREDLY_USER (single account) is still honoured for compatibility.
CREDLY_USERS = _parse_credly_users(
    os.getenv("INPUT_CREDLY_USERS"),
    CREDLY_USER,
)

try:
    NUMBER_LAST_BADGES = int(os.getenv("INPUT_NUMBER_LAST_BADGES"))
except:
    NUMBER_LAST_BADGES = 0

CREDLY_BASE_URL = "https://www.credly.com"

LIST_REGEX = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
