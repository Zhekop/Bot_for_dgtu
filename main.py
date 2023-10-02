from asyncio import run
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import F
from files.vars import dp, bot, now_time, good_morning, good_night
from app.handler_inline_unic import router_inline
from app.handler_inline_bomb import router_bomb
from app.handler_info import router_info
from app.handler_for_artem import artem
from utils.commands import set_commands
'''разница во времени 3 часа'''


async def main():
    dp.include_router(router=router_info)
    dp.include_router(router=router_inline)
    dp.include_router(router=router_bomb)
    dp.callback_query.register(artem, F.data.startswith('artem'))

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    '''один раз во время указанное в (run_date)'''
    # scheduler.add_job(send_message_time, trigger='date', run_date=datetime(2023, 8, 12, 15, 0, 0), kwargs={'bot': bot})

    '''один раз за интервал'''
    # scheduler.add_job(send_message_interval, trigger='interval',  days=1, kwargs={'bot': bot})

    '''каждый день в указанное время'''
    scheduler.add_job(func=good_morning, trigger='cron', hour=7, kwargs={'bot': bot})
    scheduler.add_job(func=good_night, trigger='cron', hour=0, kwargs={'bot': bot})


    scheduler.start()
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print(f'Bot started at {now_time}')
    run(main())