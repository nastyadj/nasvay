from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Address(BaseModel):
    """
    Модель данных для представления адреса.
    Атрибуты:
        street (str): Улица.
        city (str): Город.
        state (str): Штат.
        zip_code (str): Почтовый индекс.
      """
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    """
    Модель данных для представления пользователя.
    Атрибуты
        id (int): Уникальный идентификатор пользователя.
        name (str): Имя пользователя.
        email (EmailStr): Адрес электронной почты пользователя (проверяется на правильный формат).
        age (Optional[int]): Возраст пользователя (не обязательный может быть 'None').
        addresses (List[Address]): Список адресов пользователя
    """
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None
    addresses: List[Address] = []


if __name__ == "__main__":
    address1 = Address(street="123 Main St" , city = "Anywas" , state = "CA" , zip_code = "15472" )
    address2 = Address(street = "456 Ret ST", city = "OtherTown", state = "NU" , zip_code = "57490")
    #Создание экземпляра User
    user = User(
        id=1,
        name="Nikel Roe",
        email="Nikel.Roe@example.com",
        age=21,
        addresses=[address1, address2]
    )
    print("Данные пользователя в формате JSON:")
    # noinspection PyDeprecation
    print(user.json(indent=4))
    print("\nПример работы с данными:")
    print(f"Имя пользователя{user.name}")
    print(f"Адрес пользователя{user.addresses[0].city}")
    print(f"Почтовый индекс пользователя:{user.addresses[0].zip_code}")

    user.age = 21
    new_address(street="789Oak", city="New City", state="NX", zip_code="34387")
    user.addresses.append(new_address)
    print("\nОбновленные данные в формате JSON:")
    # noinspection PyDeprecation
    print(user.json(indent=4))