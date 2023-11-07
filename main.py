def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    fish.x = randint(5, scene.screen_width() - 6)
    fish.y = randint(5, scene.screen_height() - 6)
    info.start_countdown(3)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

fish: Sprite = None
scene.set_background_color(9)
shark = sprites.create(img("""
        .............ccfff..............
            ...........ccddbcf..............
            ..........ccddbbf...............
            ..........fccbbcf...............
            .....fffffccccccff.........ccc..
            ...ffbbbbbbbcbbbbcfff....ccbbc..
            ..fbbbbbbbbcbcbbbbcccff.cdbbc...
            ffbbbbbbffbbcbcbbbcccccfcdbbf...
            fbcbbb11ff1bcbbbbbcccccffbbf....
            fbbb11111111bbbbbcccccccbbcf....
            .fb11133cc11bbbbcccccccccccf....
            ..fccc31c111bbbcccccbdbffbbcf...
            ...fc13c111cbbbfcddddcc..fbbf...
            ....fccc111fbdbbccdcc.....fbbf..
            ........ccccfcdbbcc........fff..
            .............fffff..............
    """),
    SpriteKind.player)
controller.move_sprite(shark)
fish = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . c c c c . . . . 
            . . . . . . c c d d d d c . . . 
            . . . . . c c c c c c d c . . . 
            . . . . c c 4 4 4 4 d c c . . . 
            . . . c 4 d 4 4 4 4 4 1 c . c c 
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
            . f 4 4 4 4 1 c 4 f 4 d f f f f 
            . . f f 4 d 4 4 f f 4 c f c . . 
            . . . . f f 4 4 4 4 c d b c . . 
            . . . . . . f f f f d d d c . . 
            . . . . . . . . . . c c c . . .
    """),
    SpriteKind.food)