from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgCGoAU0uqelpn7Xi_0i_EYxG1FEdyy7WHZnTDCinXsmOkXsHC95SMHRx2pFWmhe0derMfOJiNqT84q3QndRFYzmC5VR-9V0wlVFgxdORq8hmcxIDQ9XUjir5owbVM--M_BZBb1QMTlj23GUOERzCKEbX1zd2Ib4fQSfqD3KpqiOdzLikLQ2rdWr7w_xvqA8F1fqzGSAMV3TQ5wx2YGy4hAVFhu9zZF8IGmnomhk-2uK6pRnYfqIuf16Ewq2U_zDlAcw57jHi4RFW_jRGjkeJ_SCY9LpWqxyOv04dfYe1emowFp594cK4Mt3ewkDFnjaWqg183rWDUWzZFOD_iFeDd1-dmKkBAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5635983147:AAE9wXV2P00UgU-kCOew6TT1ps-tRWdQtcU")
BOT_NAME = getenv("BOT_NAME", "SeCReT MuSiC") 
API_ID = int(getenv("API_ID", "18482353"))
API_HASH = getenv("API_HASH", "9f7840b7015b359a49e142ce42decd71")
BOT_USERNAME = getenv("BOT_USERNAME", "secretmusicrobot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SECRETMAN5/can")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "55"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5531642054").split()))
