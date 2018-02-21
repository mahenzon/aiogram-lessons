from utils import TestStates


help_message = 'Для того, чтобы изменить текущее состояние пользователя, ' \
               f'отправь команду "/setstate x", где x - число от 0 до {len(TestStates.all()) - 1}.\n' \
               'Чтобы сбросить текущее состояние, отправь "/setstate" без аргументов.'

start_message = 'Привет! Это демонстрация работы FSM.\n' + help_message
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_change_success_message = 'Текущее состояние успешно изменено'
state_reset_message = 'Состояние успешно сброшено'
current_state_message = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'invalid_key': invalid_key_message,
    'state_change': state_change_success_message,
    'state_reset': state_reset_message,
    'current_state': current_state_message,
}
