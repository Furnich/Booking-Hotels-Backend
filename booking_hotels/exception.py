from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль"
)

TokenExpiredException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Время токена истекло"
    )

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токена не существует"
)
IncorrectTokenFormatExcpetion = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена"
)

UserIsNotPresent = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED
)

RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Нет свободных номеров"
)

HaveNoBooking = HTTPException(
    status_code=status.HTTP_204_NO_CONTENT,
    detail="Такой брони не существует"
)

HaveNoHotels = HTTPException(
    status_code=status.HTTP_204_NO_CONTENT,
    detail="Нет свободных отелей или нет отелей с такими данными"
)
