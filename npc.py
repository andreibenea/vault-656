from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class NonPlayerCharacter:
    def __init__(
        self, npc_id: str, name: str, scene_id: str, dialog_id: str | None = None
    ):
        """
        npc_id: unique internal ID (e.g. "juno", "overseer")
        name: display name
        scene_id: current scene this NPC is in
        dialog_id: key into your dialog data (e.g. "juno_intro")
        """
        self.npc_id = npc_id
        self.name = name
        self.scene_id = scene_id
        self.dialog_id = dialog_id
    

    def talk(self, game: "Game") -> list[str]:
        """
        Run one step of conversation with this NPC, based on dialog_id and game state.
        Prints NPC reply.
        """
        dialogue = game.dialogue
        options = dialogue["options"]
        for option in options:
            if game.selected_reply == option:
                print(f"{options[option]["npc"]}")
