class Game:
    def __init__(self, world, player):
        """
        world: World instance (holds scenes, NPCs, items)
        player: Player instance
        """
        ...

    def run(self):
        """Main game loop for the CLI version."""
        ...

    def handle_command(self, raw_input: str):
        """Parse and route a single line of player input."""
        ...

    def change_scene(self, scene_id: str):
        """Move player to a new scene and handle intro logic."""
        ...

    def describe_current_scene(self) -> str:
        """Return the current scene description (no printing here)."""
        ...
