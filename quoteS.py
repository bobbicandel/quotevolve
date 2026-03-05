import random

QUOTES = [

{
"text":"Sesungguhnya bersama kesulitan ada kemudahan.",
"source":"QS Al-Insyirah 5-6"
},

{
"text":"Allah tidak membebani seseorang melainkan sesuai kesanggupannya.",
"source":"QS Al-Baqarah 286"
},

{
"text":"Janganlah berputus asa dari rahmat Allah.",
"source":"QS Az-Zumar 53"
},

{
"text":"Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia.",
"source":"HR Bukhari"
},

{
"text":"Allah itu indah dan menyukai keindahan.",
"source":"HR Muslim"
},

{
"text":"Bertakwalah kepada Allah di mana pun kamu berada.",
"source":"HR Tirmidzi"
},

{
"text":"Barangsiapa memudahkan urusan orang lain, Allah akan memudahkan urusannya.",
"source":"HR Muslim"
},

{
"text":"Sesungguhnya Allah bersama orang-orang yang sabar.",
"source":"QS Al-Baqarah 153"
}

]

def get():
    return random.choice(QUOTES)
