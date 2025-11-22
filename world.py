from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from npc import NonPlayerCharacter


class World:
    def __init__(
        self,
        scenes: dict,
        npcs: dict[str, "NonPlayerCharacter"],
        items: dict | None = None,
    ):
        """
        scenes: dict containing all scene data (usually from scenes.py)
        npcs: dict of NPC instances indexed by npc_id
        items: optional dict for item definitions (can be empty or None)
        """
        self.scenes = scenes
        self.npcs = npcs
        self.items = items or {}

    def get_scene(self, scene_id: str) -> dict:
        """Return the scene data for a given scene ID."""
        scene = self.scenes[scene_id]
        return scene

    def get_npc(self, npc_id: str) -> "NonPlayerCharacter":
        """Return an NPC instance by its ID."""
        npc = self.npcs[npc_id]
        return npc

    def move_npc(self, npc_id: str, new_scene_id: str):
        """Update an NPC's current location."""
        npc = self.get_npc(npc_id)
        npc.scene_id = new_scene_id

    def scene_npcs(self, scene_id: str) -> list[str]:
        """
        Return list of NPC IDs currently present in a given scene.
        Useful for 'talk' commands or automatic scene descriptions.
        """
        scene_npcs = []
        for npc in self.npcs:
            if self.npcs[npc].scene_id == scene_id:
                scene_npcs.append(self.npcs[npc])
        return scene_npcs

    def scene_items(self, scene_id: str) -> dict:
        """
        Return list of items currently present in a given scene.
        """
        self.items = self.scenes[scene_id]["objects"]
        return self.items
    
    def remove_item(self, item_id: str):
        """
        Remove an item from the scene.
        """
        # print(f"####DEBUG - items before deletion:\n{self.items}")
        del self.items[item_id]
        # print(f"####DEBUG - items after deletion:\n{self.items}")