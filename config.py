from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "14532866"))
API_HASH = getenv("API_HASH", "9c610062589d10304fbc7e87ed75209f")
BOT_TOKEN = getenv("BOT_TOKEN","5219492029:AAH1OUka7h5foE28s6JZrxNx5KXv-Nk4EKY")
BOT_NAME = getenv("BOT_NAME","Kannadiga Music Bot 🚩💛❤️")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQC4SK9TIwl3lYNs2na1tfL6-T45fjEkGmJ5kPjGT2DT3fREkJrHB2RuuxPxjR4LD6PPmdVF3PS5RsH4k_ym5z58wFGexiZKAf8lLcqApx_zDeG_TMGSJWPDvpFLp-R7AGx_JNtKSfoYOS34qUwQs94QDVbBJy8lvqJ-XibuU-lbGg_0fIjF1KT_TfLjSdeKRLWjbMw7T7wVfjcQyBsd-jzXqD3EVLF6B08q02lBITTA7v5uuP2wquQYL5T5ApSCv5Z1-GJTKu-eK9zbjpstXuMdh9NJDM0SlVl7MeOk6NBGWVSp-dqJCQSKpWmr6zjn4slA1fWezb0DIoqbcK7NpsEOAAAAATthn1MA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5127482645").split()))
