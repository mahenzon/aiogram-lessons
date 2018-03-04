import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType

from messages import MESSAGES
from config import BOT_TOKEN, PAYMENTS_PROVIDER_TOKEN, TIME_MACHINE_IMAGE_URL


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)

# Setup prices
PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=4200000)


@dp.message_handler(commands=['terms'])
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms'], reply=False)


@dp.message_handler(commands=['buy'])
async def process_buy_command(message: types.Message):
    if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, MESSAGES['pre_buy_demo_alert'])

    await bot.send_invoice(message.chat.id,
                           title=MESSAGES['tm_title'],
                           description=MESSAGES['tm_description'],
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='rub',
                           photo_url=TIME_MACHINE_IMAGE_URL,
                           photo_height=512,  # !=0/None, иначе изображение не покажется
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[PRICE],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use'
                           )


@dp.pre_checkout_query_handler(func=lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        )
    )


if __name__ == '__main__':
    executor.start_polling(dp, loop=loop)
