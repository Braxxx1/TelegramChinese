from aiogram.filters import CommandStart
from aiogram import types
from aiogram.utils.markdown import hbold
from loader import dp
from chinese import extract_toponyms, get_info


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    
@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        topon = extract_toponyms(message.text)
        for i in topon:
            await message.answer(get_info(i))
    except TypeError:
        await message.answer('Технические шоколадки!')
    except KeyError:
        await message.answer('Технические шоколадки!')