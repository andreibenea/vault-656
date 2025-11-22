from npc import NonPlayerCharacter as NPC
from game import Game
from player import Player
from world import World
from scenes import SCENES


juno = NPC("juno", "Juno", "j23", "juno_intro")
security_guard_one = NPC("security_guard_one", "Officer Jason", "security_office", "intercom_c11")
overseer = NPC("overseer", "Overseer Hanson", "overseer_office", "overseer")

npcs = {
    "juno": juno,
    "security_guard_one": security_guard_one,
    "overseer": overseer
}

world = World(SCENES, npcs)
player = Player("You", "c11")
game = Game(world, player)

game.run()