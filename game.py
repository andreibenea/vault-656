import sys
from commands import COMMANDS
from dialogues import DIALOGUES


class Game:
    def __init__(self, world, player):
        """
        world: World instance (holds scenes, NPCs, items)
        player: Player instance
        """
        self.world = world
        self.player = player
        self.current_scene_id = player.scene_id
        self.running = True
        self.in_dialogue = False

    def run(self):
        """Main game loop for the CLI version."""
        print(self.describe_current_scene())
        while self.running:
            raw = input("> ").strip().lower()
            if not raw:
                continue
            if not self.in_dialogue:
                self.handle_command(raw)
            elif self.in_dialogue:
                self.handle_player_response(raw)
    
    def handle_player_response(self, raw_input: str):
        try:
            self.selected_reply = int(raw_input)
        except:
            self.selected_reply = None
        
        if self.selected_reply in self.dialogue["options"]:
            self.in_dialogue = False
            self.dialogue_npc.talk(self)
            self.determine_outcome(self.selected_reply)
        else:
            return print(f"That didn't look right.. try typing in the number corresponding to the answer.")
    
    def handle_command(self, raw_input: str):
        """Parse and route a single line of player input."""
        items = self.world.scene_items(self.current_scene_id)
        npcs = self.world.scene_npcs(self.current_scene_id)
        # print(f"####DEBUG######\n{items.keys()}")
        
        try:
            verb, raw_args = raw_input.split(maxsplit=1)
        except:
            verb, raw_args = raw_input, None
        if verb not in COMMANDS:
            return print("That didn't work. Try to 'look around' to get your bearings!")

        match COMMANDS[verb]["action"]:
            case "exit_game":
                sys.exit()
                return
            case "help":
                return print(
                    """
  _    _ ______ _      _____  
 | |  | |  ____| |    |  __ \\ 
 | |__| | |__  | |    | |__) |
 |  __  |  __| | |    |  ___/ 
 | |  | | |____| |____| |     
 |_|  |_|______|______|_|    

This is a text adventure. You type commands. The game pretends to understand them.

Basic verbs:
  look / look around
  examine <thing>
  use <thing>
  take <item>
  go <exit>
  talk <npc>

When in doubt, try simple two-word commands. The parser is not a mind reader."""
                )
            case "look":
                if not raw_args:
                    return print(
                        f"You take a moment to scan the room.\nThe following items stand out: {", ".join(items)}."
                    )
                args = raw_args.split()
                if "around" in args:
                    return print(
                        f"You take a moment to scan the room.\nThe following items stand out: {", ".join(items)}."
                    )
            case "examine":
                if not raw_args:
                    return print(
                        "You prod at empty space. Nothing happens. Try examining something real."
                    )
                args = raw_args.split()
                for arg in args:
                    if arg not in items:
                        continue
                    return print(f"{items[arg]["description"]}")
            case "use":
                if not raw_args:
                    return print(
                        "You try to use absolutely nothing. Bold strategy. Pick an actual object to use."
                    )
                args = raw_args.split()
                for arg in args:
                    if arg not in items:
                        continue
                    if items[arg]["kind"] == "actionable":
                        if items[arg]["can_talk"]:
                            dialog_id = items[arg]["dialog_id"]
                            self.dialogue = DIALOGUES[dialog_id]
                            self.dialogue_npc = self.world.npcs[self.dialogue["npc_id"]]
                            self.in_dialogue = True
                            print(f"{self.dialogue["intro"]}")
                            i = 1
                            for possible_reply in self.dialogue["options"]:
                                print(f"{i}. {self.dialogue["options"][possible_reply]["player"]}")
                                i += 1
                            return
                        elif items[arg]["can_take"]:
                            return print(
                                "This seems useful. Maybe you should pick it up."
                            )
                        elif items[arg]["is_exit"]:
                            print(f"ITEMS[ARG] is: {items[arg]}")
                            if not self.world.scenes[self.current_scene_id]["flags"]["door_locked"]:
                                return self.change_scene(self.world.scenes[self.current_scene_id]["exits"][arg])
                            else:
                                return print("It's locked!")
            case "take":
                if not raw_args:
                    return print(
                        "You reach out to take… nothing. Impressive technique. Try taking something that exists."
                    )
                args = raw_args.split()
                for arg in args:
                    if arg not in items:
                        continue
                    if items[arg]["can_take"]:
                        self.player.add_item(arg, items[arg])
                        self.world.remove_item(arg)
                        return
                    elif not items[arg]["can_take"]:
                        return print("You can't take that. Nice try, though.")
            case "talk":
                if not raw_args:
                    return print(
                        "You try to strike up a conversation with empty air. It has nothing to say."
                    )
                args = raw_args.split()
                for arg in args:
                    for npc in npcs:
                        if str(arg).title() == str(npc.name) or str(arg) == npc.npc_id:
                            dialog_id = npc.dialog_id
                            self.dialogue = DIALOGUES[dialog_id]
                            self.in_dialogue = True
                            print(f"{self.dialogue["intro"]}")
                return print(f"WE NEED TO TALK")
            case _:
                return print("gotta catchem ALL")
        return print("You don't see anything by that name here.")

    def determine_outcome(self, player_choice: int):
        outcome = self.dialogue["options"][player_choice]["outcome"]
        if outcome == "good":
            self.world.scenes[self.current_scene_id]["flags"]["door_locked"] = False
        elif outcome == "neutral":
            print("That didn't seem to do anything..")
        else:
            print("GAME OVER!")

    def change_scene(self, scene_id: str):
        """Move player to a new scene and handle intro logic."""
        self.current_scene_id = scene_id
        print(self.describe_current_scene())

    def describe_current_scene(self) -> str:
        """Return the current scene description (no printing here)."""
        scene = self.world.get_scene(self.current_scene_id)
        return scene["description"]
