import logging


from aiogram import Bot, Dispatcher, types, executor
from keyboards import ikbg, kb
from config import TOKEN
from kurs import fantasy, criminal, history, fantastic, thriller, drama, comedy


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def start_command(msg: types.Message):
	await msg.answer(text='Этот телеграм-бот является индивидуальным проектом ученика 10Д, Шарипова Романа.\nДля просмотра функционала введите команду /help.',
					 reply_markup=kb)
	await msg.answer(text='Бот создан для подбора контента.')



@dp.message_handler(commands='help')
async def help_command(msg: types.Message):
	await msg.answer(text="""Данный бот выдает определенный контент (фильм, сериал и мультфильмы) по тегу (жанру).\n
	Для старта подбора введите команду /sel\n
	По всем вопросам писать в телеграм - @rido7 или же на почту drecker3010371@gmail.com""")



@dp.message_handler(commands='sel')
async def help_command(msg: types.Message):
	await msg.answer(text='Выберите жанр', reply_markup=ikbg)


@dp.callback_query_handler()
async def req(callback: types.CallbackQuery):
	await callback.answer('Жанр выбран!')
	if callback.data == 'фэнтези':
		a = fantasy()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'криминал':
		a = criminal()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'фантастика':
		a = fantastic()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'триллер':
		a = thriller()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'история':
		a = history()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'драма':
		a = drama()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)
	if callback.data == 'комедия':
		a = comedy()
		b = f"""Название: {a[1]} ; Рейтинг: {a[2]}; Год выхода: {a[3]}\n{a[-1]}"""
		await callback.message.answer(text=b)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
