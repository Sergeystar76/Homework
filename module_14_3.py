from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button11 = KeyboardButton(text='Рассчитать')
button12 = KeyboardButton(text='Информация')
button13 = KeyboardButton(text='Купить')
kb.row(button11, button12)
kb.row(button13)
kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button21 = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
button22 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.row(button21, button22)

kb3 = InlineKeyboardMarkup(resize_keyboard=True)
button31 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button32 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button33 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button34 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.row(button31, button32, button33, button34)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я - бот, помогающий твоему здоровью!', reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'{i}.png', "rb") as img:
            await message.answer(f'Hазвание: Product{i} | Описание: описание {i}| Цена: {i * 100}')
            await message.answer_photo(img)
    await message.answer(f'Выберите продукт для покупки:', reply_markup=kb3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(mes1=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(mes2=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(mes3=message.text)
    data = await state.get_data()
    cal = 10 * int(data['mes1']) + 6.25 * int(data['mes2']) - 5 * int(data['mes3'])
    await message.answer(f'Ваша норма калорий: {cal}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
