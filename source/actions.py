
# Local project imports
from source import globalvars, map



def use_stairs():
    # check if the player is standing on top of a set of stairs
    list_of_obj = map.map_object_at_coords(globalvars.PLAYER.x, globalvars.PLAYER.y)

    for obj in list_of_obj:
        # check if the object contains a stairs component
        if obj.stairs:
            obj.stairs.use()
            FLOOR_CHANGED = True
            return "Just Changed Floors"

        if obj.portal:
            obj.portal.use()


def move_one_tile(direction):
    if direction == "up":
        dx, dy = 0, -1
    elif direction == "down":
        dx, dy = 0, 1
    elif direction == "left":
        dx, dy = -1, 0
    elif direction == "right":
        dx, dy = 1, 0
    globalvars.PLAYER.creature.move(dx, dy)
    globalvars.FOV_CALCULATE = True


def grab_item():
    objects_at_player = map.map_object_at_coords(globalvars.PLAYER.x, globalvars.PLAYER.y)
    for obj in objects_at_player:
        if obj.item:
            obj.item.pick_up(globalvars.PLAYER)


def drop_item():
    if len(globalvars.PLAYER.container.inventory) > 0:
        globalvars.PLAYER.container.inventory[-1].item.drop(globalvars.PLAYER.x, globalvars.PLAYER.y)
