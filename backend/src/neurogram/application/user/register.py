from dataclasses import replace

from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.uow import UoW
from neurogram.application.interfaces.gateways.user import UserGateway
from neurogram.application.interfaces.hasher import IPasswordHasher
from neurogram.application.dto.user import CreateUserDTO
from neurogram.domain.entities.user import User
from neurogram.domain.exceptions.user import UserAlreadyExistsError


class RegisterInteractor(Interactor[CreateUserDTO, None]):
    def __init__(
        self,
        user_gateway: UserGateway,
        uow: UoW,
        hash_service: IPasswordHasher,
    ):
        self.user_gateway = user_gateway
        self.hash_service = hash_service
        self.uow = uow


    async def __call__(self, data: CreateUserDTO) -> None:
        user_exist = await self.user_gateway.check_data_unique(
            username=data.username,
            telegram_id=data.telegram_id,
            email=data.email
        )

        if user_exist:
            raise UserAlreadyExistsError
        
        hashed_password = self.hash_service.hash(data.password)
        user_data = replace(data, password=hashed_password)
        await self.user_gateway.add(user_data)
        await self.uow.commit()
        return 