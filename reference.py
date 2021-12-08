import os
from telegram.ext import Updater

class Ref:
    def token(self):
        token = "5070280174:AAEn7rvSorr71jDZSDL9GaBzt439F-YC5Nw"
        return token
    def port(self):
        PORT = int(os.environ.get('PORT', '8443'))
        return PORT
    def image(self):
        url = 'https://i.ibb.co/Qf2SXCM/Price-List.jpg'
        return url