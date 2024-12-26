from app.application.interfaces.gateways.chat import ChatGateway
from app.application.interfaces.id_provider import IdProvider
from app.application.interfaces.interactor import Interactor
from app.application.interfaces.uow import UoW
from app.application.dto.chat import DeleteChatDTO
from app.domain.services.access import AccessService


class DeleteChatInteractor(Interactor[DeleteChatDTO, None]):
    def __init__(
        self,
        chat_gateway: ChatGateway,
        uow: UoW,
        access: AccessService,
        id_provider: IdProvider,
    ) -> None:
        self.chat_gateway = chat_gateway
        self.uow = uow
        self.id_provider = id_provider
        self.access = access

    async def __call__(self, data: DeleteChatDTO) -> None:
        chat_id = data.chat_id
        user_id = self.id_provider.get_current_user_id()
        chat_owner_id = await self.chat_gateway.get_chat_owner(chat_id)
        self.access.ensure_can_chat(user_id, chat_owner_id)

        await self.chat_gateway.delete(data.chat_id)
        await self.uow.commit()
        return