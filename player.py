from npc import NonPlayerCharacter as NPC


class Player(NPC):
    def __init__(self, name: str, start_scene_id: str):
        super().__init__(
            npc_id="player", name=name, scene_id=start_scene_id, dialog_id=None
        )
        self.inventory: list[str] = []
        self.flags: dict[str, bool | str | int] = {}

    def move_to(self, scene_id: str):
        """Update the player's current scene."""
        self.scene_id = scene_id

    def add_item(self, item_id: str, item: dict):
        """Add an item to the player's inventory."""
        self.inventory.append((item_id, item))
        print(f"You pick up the {item_id}.")

    def has_item(self, item_id: str) -> bool:
        """Check if player has a given item."""
        ...

    def remove_item(self, item_id: str):
        """Remove an item from inventory if present."""
        ...
