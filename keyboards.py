from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



glist = [InlineKeyboardButton('Фэнетзи', callback_data='фэнтези'), InlineKeyboardButton('История', callback_data='история'),
		InlineKeyboardButton('Криминал', callback_data='криминал'), InlineKeyboardButton('Триллер', callback_data='триллер'),
		InlineKeyboardButton('Фантастика', callback_data='фантастика'), InlineKeyboardButton('Драма', callback_data='драма'),
		InlineKeyboardButton('Комедия', callback_data='комедия')]
ikbg = InlineKeyboardMarkup(row_width=2).add(*glist)


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton('/help'), KeyboardButton('/sel'))
