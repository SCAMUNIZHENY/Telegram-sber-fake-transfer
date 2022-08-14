from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_cancel, kb_client
from scripts import translate
from os import remove


class Price(StatesGroup):
    user_id = State()
    name = State()
    price = State()


async def cmd_start(message: types.Message):
    await message.answer(f"Привет", reply_markup=kb_client)


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=kb_client)


async def cmd_trans(message: types.Message, state: FSMContext):
    await Price.user_id.set()
    await state.update_data(user_id=message.from_user.id)
    await Price.name.set()
    await message.answer('Введите ФИО', reply_markup=kb_cancel)

async def name_step(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Price.price.set()
    await message.answer('Введите сумму', reply_markup=kb_cancel)


async def send(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    user_data = await state.get_data()
    await message.answer_photo(await translate(user_data["user_id"], user_data["name"], user_data["price"]), reply_markup=kb_client)
    remove(f"images/{user_data['user_id']}.jpg")
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_cancel, commands="Отмена", state="*")
    dp.register_message_handler(cmd_cancel, Text(
        equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(cmd_trans, Text(equals='Перевод'), state="*")
    dp.register_message_handler(
        name_step, state=Price.name, content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(
        send, state=Price.price, content_types=types.ContentTypes.TEXT)
