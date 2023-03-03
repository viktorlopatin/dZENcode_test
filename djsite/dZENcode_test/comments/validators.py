from django.core.exceptions import ValidationError


def validate_file_type(value):
    ext = value.name.split('.')[-1]
    valid_extensions = ['jpg', 'gif', 'png', 'txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Неверный тип файла. Допустимые типы файлов: jpeg, gif, png, txt')


def validate_file_size(value):
    file_size = value.size
    file_type = value.name.split('.')[-1]
    if file_size > 102400 and file_type == 'txt':
        raise ValidationError("Размер ТХТ файла не может превышать 100кб")
