from newgame2048.init_game import get_new_position

def player_sur_objectif(grid, pos_player,pos_ennemi, pos_objectif):
    i0,j0=pos_player
    grid[i0][j0]=0
    pos_player=pos_objectif
    i1,j1=get_new_position(grid)
    new_abs_player,new_ord_player=pos_player
    value_player=grid[new_abs_player][new_ord_player]
    grid[i1][j1]=2*value_player
    abs_ennemy,ord_ennemy=pos_ennemi
    grid[abs_ennemy][ord_ennemy]=value_player/2
    return grid

def move_player(grid,pos_player,commande):
    old_abs_player,old_ord_player=pos_player
    new_abs_player,new_ord_player=move_pos_player(pos_player,commande)
    grid[new_abs_player][new_ord_player]=grid[old_abs_player][old_ord_player]
    grid[old_abs_player][old_ord_player]=0
    return grid

def move_ennemi(grid,pos_ennemi, pos_objectif, commande):
    old_abs_ennemi, old_ord_ennemi=pos_ennemi
    new_abs_ennemi, new_ord_ennemi=move_pos_ennemi(pos_ennemi, pos_objectif, commande)
    grid[new_abs_ennemi][new_ord_ennemi]=grid[old_abs_ennemi][old_ord_ennemi]
    grid[old_abs_ennemi][old_ord_ennemi]=0
    return grid
