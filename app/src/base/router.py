from fastapi import APIRouter


class ViewSetRouter(APIRouter):

    def __init__(self,
                 path=None,
                 view_class=None,
                 response_model=None,
                 tags=None
                 ):
        super().__init__()
        view = view_class()
        if hasattr(view, 'list'):
            super().add_api_route(
                response_model=response_model,
                path=f'{path}/',
                endpoint=view.list,
                methods=['GET'],
                tags=tags
            )
        if hasattr(view, 'retrieve'):
            super().add_api_route(
                response_model=response_model,
                path=f'{path}/' + '{id}',
                endpoint=view.retrieve,
                methods=['GET'],
                tags=tags
            )
        if hasattr(view, 'create'):
            super().add_api_route(
                response_model=response_model,
                path=f'{path}/',
                endpoint=view.create,
                methods=['POST'],
                tags=tags
            )
