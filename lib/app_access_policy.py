import inspect
from rest_access_policy import AccessPolicy
from app_auth.models import AuthAssignment

class AppAccessPolicy(AccessPolicy):
    name = __package__
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"         
        },
    ]

    def is_author(self, request, view, action) -> bool:
        item = view.get_object()
        return request.user == item.owner 

    def is_authorised(self, request, view, action) -> bool:
        perm = self.name.capitalize() + str(action).capitalize()
        item = AuthAssignment.objects.filter(item_name=perm, user_id=request.user.id).first()
        print(item)
        if item:
            return True

        return False