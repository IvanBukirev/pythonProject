from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import *

initiate_db()
products = get_all_products()

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb2 = InlineKeyboardMarkup(
        inline_keyboard=[
                [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
                [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
        ], resize_keyboard=True
)

kb3 = InlineKeyboardMarkup(
        inline_keyboard=[
                [InlineKeyboardButton(text='Продукт1', callback_data='product_buying')],
                [InlineKeyboardButton(text='Продукт2', callback_data='product_buying')],
                [InlineKeyboardButton(text='Продукт3', callback_data='product_buying')],
                [InlineKeyboardButton(text='Продукт4', callback_data='product_buying')]
        ], resize_keyboard=True
)
kb = ReplyKeyboardMarkup(
        keyboard=[
                [KeyboardButton(text='Информация')],
                [KeyboardButton(text='Рассчитать')],
                [KeyboardButton(text='Купить')]
        ], resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (полных лет):')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма каллорий {calories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
            f'Привет, {message.from_user.username}! Я бот помогающий твоему здоровью. Для начала работы наберите Рассчитать')


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer('Это Бот, который поможет тебе рассчитать вашу норму каллорий.')




@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for pr in products:
        await message.answer(f"Название: {pr[1]} | "
                             f"Описание: {pr[2]} | "
                             f"Цена: {pr[3]}")
        with open(f"img{pr[0]}.jpg", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
