from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
import os

kb_normal = ReplyKeyboardMarkup(resize_keyboard=True)
button_calories = KeyboardButton(text='Рассчитать')
button_information = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
kb_normal.add(button_calories, button_information, button_buy)

kb_inline = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb_inline.add(button1, button2)

buy_menu = InlineKeyboardMarkup()
buy1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
buy2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
buy3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
buy4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
buy_menu.add(buy1, buy2, buy3, buy4)

api = "7321408181:AAGaGNvPrEGJZO0y9rXwmuiMIDVDlj4lDSo"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_normal)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.answer('Формула: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    all_products = get_all_products()
    directory_in_str = './pictures'
    directory = os.fsencode(directory_in_str)
    for product, picture in zip(all_products, os.fsencode(directory)):
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}', f'{product[0]}')
        filename = os.fsdecode(picture)
        with open(filename, 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text=['Информация'])
async def information(message):
    await message.answer('Something more interesting will happen if you click \'Рассчитать\'.')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = int(data['age']) * 5 + int(data['weight']) * 10 + int(data['height']) * 6.25 + 5
    await message.answer(f'Daily calorie intake: {result}')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
