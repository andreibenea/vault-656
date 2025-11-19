SCENES = {
    "c11": {
        "id": "c11",
        "name": "Quarters C-11",
        "description": (
            "You wake up groggy on your bed in Vault 123. The room is dim—only the "
            "emergency floor strips glow faint blue. Your left forearm is bare. "
            "Your Pip-Boy is missing. The door is sealed, its status light glowing yellow."
        ),
        "objects": {
            "bed": {
                "kind": "scenery",
                "description": (
                    "The bed is a mess—twisted sheets, pillow on the floor. It looks like "
                    "someone pulled you out of it rather than waking you."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "locker": {
                "kind": "scenery",
                "description": (
                    "The steel locker is slightly ajar. A dent near the handle suggests "
                    "it was forced open. Inside, your jumpsuit is folded, but your "
                    "belongings box and Pip-Boy cradle are missing."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "floor": {
                "kind": "scenery",
                "description": (
                    "A small plastic syringe cap lies on the floor—standard Medbay issue. "
                    "You don't remember receiving any treatment."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "desk": {
                "kind": "scenery",
                "description": (
                    "A metal desk is bolted to the floor. On top of it sits a dark, unpowered "
                    "terminal and a single Vault-Tec holotape."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "terminal": {
                "kind": "actionable",
                "description": (
                    "The terminal's screen is completely dark. With emergency power only, it "
                    "won't even attempt to boot."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "holotape": {
                "kind": "actionable",
                "description": (
                    "A Vault-Tec holotape with a worn label. Without your Pip-Boy, there's no "
                    "way to read or play whatever's on it."
                ),
                "can_take": True,
                "can_talk": False,
            },
            "vent": {
                "kind": "scenery",
                "description": (
                    "The ventilation grate clicks on and off, cycling air irregularly. "
                    "Something in the system is struggling."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "intercom": {
                "kind": "actionable",
                "description": (
                    "A standard Vault intercom used for communication with Security."
                ),
                "can_take": False,
                "can_talk": True,
                "dialog_id": "intercom_c11",
            },
            "pillow": {
                "kind": "scenery",
                "description": (
                    "You pick up the pillow from the floor. The case is slightly unzipped. "
                    "Inside the pillowcase, you find a tightly folded note. It reads: "
                    "\"You're in danger! Come find me and don't trust anyone!\"\n"
                    "You recognize the hurried scribble — it's your friend Juno."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "door": {
                "kind": "actionable",
                "description": (
                    "A standard sliding Vault door. The status light glows yellow—local lockdown. "
                    "Normally it opens at a touch, but right now it's sealed by an override from outside."
                ),
                "can_take": False,
                "can_talk": False,
            },
        },
        "exits": {"hallway": "hallway_ground"},
        "flags": {"door_locked": True},
    },
    "hallway_ground": {
        "id": "hallway_ground",
        "name": "Ground Floor Hallway",
        "description": (
            "A long, curved hallway lined with numbered doors and flickering wall lamps. "
            "Signs point toward Security, the Overseer's office upstairs, and the main Vault Door."
        ),
        "objects": {
            "signs": {
                "kind": "scenery",
                "description": (
                    "Directional signs point toward Quarters C-11, J-23, Security, the Overseer's office, "
                    "and the Vault Door."
                ),
                "can_take": False,
                "can_talk": False,
            }
        },
        "exits": {
            "c11": "c11",
            "j23": "j23",
            "vault": "vault_door_room",
            "stairs_up": "hallway_upper",
        },
        "flags": {},
    },
    "j23": {
        "id": "j23",
        "name": "Quarters J-23",
        "description": (
            "Juno's quarters are small but organized—tools, notes, and schematics stacked in careful piles. "
            "Her bunk is neatly made, but she's nowhere to be seen."
        ),
        "objects": {
            "bunk": {
                "kind": "scenery",
                "description": "A neatly made bunk with a folded jumpsuit at the foot.",
                "can_take": False,
                "can_talk": False,
            },
            "workbench": {
                "kind": "scenery",
                "description": (
                    "Juno's workbench is cluttered with tools and ventilation schematics for Vault 123."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "note": {
                "kind": "actionable",
                "description": (
                    "A hastily written note from Juno mentioning strange log entries tied to your ID "
                    "and a meeting point near the Overseer's office."
                ),
                "can_take": True,
                "can_talk": False,
            },
        },
        "exits": {"hallway": "hallway_ground"},
        "flags": {},
    },
    "vault_door_room": {
        "id": "vault_door_room",
        "name": "Vault Door Antechamber",
        "description": (
            "You stand before the massive gear-shaped Vault Door. Warning lights blink slowly. "
            "A control podium sits nearby, blank where a Pip-Boy interface should be."
        ),
        "objects": {
            "vault_door": {
                "kind": "actionable",
                "description": (
                    "The colossal Vault Door is sealed shut. Mechanical locks and massive hinges hold it in place."
                ),
                "can_take": False,
                "can_talk": False,
            },
            "control_podium": {
                "kind": "actionable",
                "description": (
                    "A control podium with a recessed Pip-Boy docking port and a small status display."
                ),
                "can_take": False,
                "can_talk": False,
            },
        },
        "exits": {"hallway": "hallway_ground"},
        "flags": {"vault_unlocked": False},
    },
    "hallway_upper": {
        "id": "hallway_upper",
        "name": "Upper Floor Hallway",
        "description": (
            "A quieter upper corridor with reinforced doors. Placards indicate the Security Office "
            "and the Overseer's Office."
        ),
        "objects": {},
        "exits": {
            "stairs_down": "hallway_ground",
            "security_office": "security_office",
            "overseer_office": "overseer_office",
        },
        "flags": {},
    },
    "security_office": {
        "id": "security_office",
        "name": "Security Office",
        "description": (
            "The Security Office is lined with monitors and weapon lockers. Normally it's staffed, "
            "but at times it can be eerily empty."
        ),
        "objects": {
            "consoles": {
                "kind": "scenery",
                "description": "Banks of consoles show camera feeds from across the Vault.",
                "can_take": False,
                "can_talk": False,
            },
            "lockers": {
                "kind": "scenery",
                "description": "Heavy-duty lockers used for storing equipment and personal gear.",
                "can_take": False,
                "can_talk": False,
            },
            "pipboy_cradle": {
                "kind": "actionable",
                "description": (
                    "An empty Pip-Boy cradle with a faint outline where one usually rests."
                ),
                "can_take": False,
                "can_talk": False,
            },
        },
        "exits": {"hallway": "hallway_upper"},
        "flags": {"occupied": True, "pipboy_available": False},
    },
    "overseer_office": {
        "id": "overseer_office",
        "name": "Overseer's Office",
        "description": (
            "The Overseer's Office overlooks parts of the Vault through thick glass. A large desk dominates "
            "the room, with a secure terminal built into its surface."
        ),
        "objects": {
            "desk": {
                "kind": "scenery",
                "description": "A heavy desk piled with reports and access logs.",
                "can_take": False,
                "can_talk": False,
            },
            "overseer_terminal": {
                "kind": "actionable",
                "description": (
                    "A secured Overseer terminal with access to system logs and security alerts."
                ),
                "can_take": False,
                "can_talk": False,
                "dialog_id": "overseer_terminal_menu",
            },
        },
        "exits": {"hallway": "hallway_upper"},
        "flags": {"sector7_alert_raised": False},
    },
}
