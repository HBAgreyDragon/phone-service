import pytest
from app.api.models import PhoneIn, PhoneOut

phones = PhoneIn(
    name='Apple',
    model='Iphone 15',
    max_count='10000000',
    operating='macOs'
)


def test_create_currency(phones: PhoneIn = phones):
    assert dict(phones) == {'name': phones.name,
                            'model': phones.model,
                            'max_count': phones.max_count,
                            'operating': phones.operating
                            }


def test_update_currency_age(phones: PhoneIn = phones):
    phone_upd = PhoneOut(
        name='Apple',
        model='Iphone 15',
        max_count='10000000',
        operating='macOs',
        id=1
    )
    assert dict(phone_upd) == {'name': phones.name,
                                  'model': phones.model,
                                  'max_count': phones.max_count,
                                  'operating': phones.operating,
                                  'id': phone_upd.id
                                  }


def test_update_currency_genre(phones: PhoneIn = phones):
    phone_upd = PhoneOut(
        name='Apple',
        model='Iphone 15',
        max_count='10000000',
        operating='macOs',
        id=1
    )
    assert dict(phone_upd) == {'name': phones.name,
                                  'model': phones.model,
                                  'max_count': phones.max_count,
                                  'operating': phones.operating,
                                  'id': phone_upd.id
                                  }
