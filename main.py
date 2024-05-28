import asyncio
import logging
from datetime import datetime
from keyboards import key_board
from aiogram import Dispatcher, Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db import Student, Messages
from aiogram.filters import CommandStart, Command
bot = Bot('6709079765:AAEf3YVhvxCaBSe5xvNhzwVtzI68gY6e1OQ')
dp = Dispatcher()
router = Router()
class Info(StatesGroup):
    name = State()

@router.message(CommandStart())
async def fast_start(message: Message):
    user_id = str(message.from_user.id)
    array_y = []
    for id_s in Student.select():
        array_y.append(str(id_s.user_id))
    if user_id not in array_y:
        student_id = Student(user_id=user_id)
        student_id.save()
    await message.answer(
        text="Выберите из появившегося кнопки, кому хотите отправить сообщение!",
        reply_markup=key_board(),
    )
@router.message(F.text.in_('Всем'))
async def message_wrt(message: Message, state: FSMContext):
    await message.answer(
        text='Введите сообщение!',
    )
    await state.set_state(Info.name)
@router.message(Info.name)
async def to_db(message: Message, state: FSMContext):
    user_current = Messages(send_message_time=message.text, date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user_current.save()
    for person in Student.select():
        try:
            await bot.send_message(
                person.user_id,
                message.text,
            )
        except:
            await message.answer("Ошибка отправки")
    await message.answer(
        text="Сообщение отправлено успешно!", 
    )
    await state.clear()
async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("The program ended successfully!")