import random

DATA = [
    (
        "Sesungguhnya bersama kesulitan ada kemudahan.",
        "QS Al-Insyirah 5-6"
    ),
    (
        "Allah tidak membebani seseorang melainkan sesuai dengan kesanggupannya.",
        "QS Al-Baqarah 286"
    ),
    (
        "Janganlah berputus asa dari rahmat Allah.",
        "QS Az-Zumar 53"
    ),
    (
        "Sesungguhnya Allah bersama orang-orang yang sabar.",
        "QS Al-Baqarah 153"
    ),
    (
        "Dan barang siapa bertawakal kepada Allah, niscaya Allah akan mencukupkan keperluannya.",
        "QS At-Talaq 3"
    ),
    (
        "Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia.",
        "HR Bukhari"
    ),
    (
        "Allah itu indah dan menyukai keindahan.",
        "HR Muslim"
    ),
    (
        "Bertakwalah kepada Allah di mana pun kamu berada.",
        "HR Tirmidzi"
    ),
    (
        "Permudahlah dan jangan mempersulit.",
        "HR Bukhari Muslim"
    ),
]


def get():
    quote, ref = random.choice(DATA)

    return quote, ref
