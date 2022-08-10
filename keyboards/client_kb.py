from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

but_trans = KeyboardButton('Перевод')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but_trans)

but_cancel = KeyboardButton('Отмена')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(but_cancel)
