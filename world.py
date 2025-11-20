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
        ...

    def get_npc(self, npc_id: str) -> "NonPlayerCharacter":
        """Return an NPC instance by its ID."""
        ...

    def move_npc(self, npc_id: str, new_scene_id: str):
        """Update an NPC's current location."""
        ...

    def scene_has_npc(self, scene_id: str) -> list[str]:
        """
        Return list of NPC IDs currently present in a given scene.
        Useful for 'talk' commands or automatic scene descriptions.
        """
        ...
